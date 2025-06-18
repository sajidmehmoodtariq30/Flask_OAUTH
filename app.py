from flask import Flask, request, redirect, url_for, session, Response, render_template, flash
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length, EqualTo
import bcrypt
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'your-secret-key-change-this-in-production')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///users.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Security settings
app.config['SESSION_COOKIE_SECURE'] = os.getenv('SESSION_COOKIE_SECURE', 'False').lower() == 'true'
app.config['SESSION_COOKIE_HTTPONLY'] = os.getenv('SESSION_COOKIE_HTTPONLY', 'True').lower() == 'true'
app.config['SESSION_COOKIE_SAMESITE'] = os.getenv('SESSION_COOKIE_SAMESITE', 'Lax')

db = SQLAlchemy(app)

# User Model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    first_name = db.Column(db.String(50), nullable=True)
    last_name = db.Column(db.String(50), nullable=True)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    last_login = db.Column(db.DateTime, nullable=True)
    is_active = db.Column(db.Boolean, default=True)

    def set_password(self, password):
        self.password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    
    def check_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password_hash.encode('utf-8'))
    
    def get_full_name(self):
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        return self.username
    
    def get_initials(self):
        if self.first_name and self.last_name:
            return f"{self.first_name[0]}{self.last_name[0]}".upper()
        return self.username[0].upper()

# Forms
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()], render_kw={"placeholder": "Enter your username"})
    password = PasswordField('Password', validators=[DataRequired()], render_kw={"placeholder": "Enter your password"})
    submit = SubmitField('Login')

class SignupForm(FlaskForm):
    first_name = StringField('First Name', validators=[Length(max=50)], render_kw={"placeholder": "Enter your first name"})
    last_name = StringField('Last Name', validators=[Length(max=50)], render_kw={"placeholder": "Enter your last name"})
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Choose a username"})
    email = StringField('Email', validators=[DataRequired(), Email()], render_kw={"placeholder": "Enter your email address"})
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)], render_kw={"placeholder": "Create a password"})
    confirm_password = PasswordField('Confirm Password', 
                                   validators=[DataRequired(), EqualTo('password')], render_kw={"placeholder": "Confirm your password"})
    submit = SubmitField('Sign Up')

class ProfileForm(FlaskForm):
    first_name = StringField('First Name', validators=[Length(max=50)], render_kw={"placeholder": "Enter your first name"})
    last_name = StringField('Last Name', validators=[Length(max=50)], render_kw={"placeholder": "Enter your last name"})
    email = StringField('Email', validators=[DataRequired(), Email()], render_kw={"placeholder": "Enter your email address"})
    submit = SubmitField('Update Profile')

# Routes
@app.route('/')
def index():
    if 'user_id' in session:
        user = User.query.get(session['user_id'])
        return render_template('index.html', user=user)
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'user_id' in session:
        return redirect(url_for('index'))
    
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data) and user.is_active:
            session['user_id'] = user.id
            user.last_login = db.func.current_timestamp()
            db.session.commit()
            flash(f'Welcome back, {user.get_full_name()}!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Invalid username or password', 'danger')
    
    return render_template('login.html', form=form)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if 'user_id' in session:
        return redirect(url_for('index'))
    
    form = SignupForm()
    if form.validate_on_submit():
        # Check if username or email already exists
        existing_user = User.query.filter(
            (User.username == form.username.data) | 
            (User.email == form.email.data)
        ).first()
        
        if existing_user:
            if existing_user.username == form.username.data:
                flash('Username already exists. Please choose a different one.', 'danger')
            if existing_user.email == form.email.data:
                flash('Email already registered. Please use a different email.', 'danger')
        else:
            # Create new user
            user = User(
                username=form.username.data, 
                email=form.email.data,
                first_name=form.first_name.data,
                last_name=form.last_name.data
            )
            user.set_password(form.password.data)
            db.session.add(user)
            db.session.commit()
            flash('Account created successfully! Please log in.', 'success')
            return redirect(url_for('login'))
    
    return render_template('signup.html', form=form)

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    flash('You have been logged out', 'info')
    return redirect(url_for('index'))

@app.route('/profile')
def profile():
    if 'user_id' not in session:
        flash('Please log in to view your profile', 'warning')
        return redirect(url_for('login'))
    
    user = User.query.get(session['user_id'])
    return render_template('profile.html', user=user)

@app.route('/profile/edit', methods=['GET', 'POST'])
def edit_profile():
    if 'user_id' not in session:
        flash('Please log in to edit your profile', 'warning')
        return redirect(url_for('login'))
    
    user = User.query.get(session['user_id'])
    form = ProfileForm(obj=user)
    
    if form.validate_on_submit():
        # Check if email already exists for another user
        existing_user = User.query.filter(
            User.email == form.email.data,
            User.id != user.id
        ).first()
        
        if existing_user:
            flash('Email already in use by another account', 'danger')
        else:
            user.first_name = form.first_name.data
            user.last_name = form.last_name.data
            user.email = form.email.data
            db.session.commit()
            flash('Profile updated successfully!', 'success')
            return redirect(url_for('profile'))
    
    return render_template('edit_profile.html', form=form, user=user)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    
    # Get port from environment variable (useful for deployment)
    port = int(os.getenv('PORT', 5000))
    debug = os.getenv('FLASK_DEBUG', 'True').lower() == 'true'
    
    app.run(host='0.0.0.0', port=port, debug=debug)
