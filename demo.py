from flask import Flask, request

# Starting of project
app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Welcome to the Flask App!</h1>" \
    "<Button onclick=\"location.href='/about'\">Go to About</Button>" \
    "<Button onclick=\"location.href='/contact'\">Go to Contact</Button>"

@app.route('/about')
def about():
    return "<h1>About Page</h1><p>This is a simple Flask application.</p>" \
    "<Button onclick=\"location.href='/contact'\">Contact Us</Button>" \
    "<Button onclick=\"location.href='/'\">Go to Home</Button>"

@app.route('/contact')
def contact():
    return "<h1>Contact Page</h1><p>Feel free to reach out!</p>" \
    "<Button onclick=\"location.href='/'\">Go to Home</Button>"

@app.route('/submit', methods=['GET','POST'])
def submit():
    if request.method == 'POST':
        # Here you would handle form submission
        return "<h1>Form Submitted!</h1>" \
               "<Button onclick=\"location.href='/'\">Go to Home</Button>"
    return "<h1>Submit Form</h1>" \
           "<form method='POST'>" \
           "<input type='text' name='data' placeholder='Enter some data'>" \
           "<input type='submit' value='Submit'>" \
           "</form>" \
           "<Button onclick=\"location.href='/'\">Go to Home</Button>"