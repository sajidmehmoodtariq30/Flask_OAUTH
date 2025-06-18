# Flask Authentication App

A modern, secure Flask authentication system with beautiful UI/UX design and comprehensive user management features.

## 🚀 Features

### Core Authentication

- **Secure User Registration** with email validation
- **Login/Logout System** with session management
- **Password Hashing** using bcrypt for security
- **Form Validation** with real-time feedback
- **Profile Management** with editable user information

### Modern UI/UX

- **Responsive Design** that works on all devices
- **Beautiful Gradient Backgrounds** with smooth animations
- **Modern Typography** using Inter font family
- **Interactive Elements** with hover effects and transitions
- **Flash Messages** with auto-dismissal and manual close
- **Password Visibility Toggle** for better UX
- **Loading States** for form submissions
- **Client-side Validation** with JavaScript

### Security Features

- **Environment Variables** for sensitive configuration
- **Secure Session Management** with configurable cookies
- **Input Sanitization** and validation
- **CSRF Protection** with Flask-WTF
- **SQL Injection Prevention** with SQLAlchemy ORM

### Enhanced Functionality

- **User Profiles** with avatar initials
- **Profile Editing** with validation
- **User Activity Tracking** (last login, join date)
- **Account Status Management**
- **Extended User Model** with first/last names

## 📁 Project Structure

``` bash
Flask_OAUTH/
├── app.py                 # Main Flask application
├── .env                   # Environment variables (not in git)
├── .gitignore            # Git ignore file
├── requirements.txt      # Python dependencies
├── README.md            # This file
├── static/
│   ├── css/
│   │   └── style.css    # Modern CSS styles
│   ├── js/
│   │   └── app.js       # JavaScript functionality
│   └── favicon.ico      # Site favicon
├── templates/
│   ├── base.html        # Base template
│   ├── index.html       # Home page
│   ├── login.html       # Login page
│   ├── signup.html      # Registration page
│   ├── profile.html     # User profile page
│   └── edit_profile.html # Profile editing page
└── instance/
    └── users.db         # SQLite database
```

## 🛠️ Installation & Setup

### 1. Clone the Repository

```bash
git clone <repository-url>
cd Flask_OAUTH
```

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Environment Configuration

Create a `.env` file in the project root:

```env
# Flask Configuration
SECRET_KEY=your-very-long-secret-key-here-change-this-in-production
FLASK_ENV=development
FLASK_DEBUG=True

# Database Configuration
DATABASE_URL=sqlite:///users.db

# Security Settings
SESSION_COOKIE_SECURE=False
SESSION_COOKIE_HTTPONLY=True
SESSION_COOKIE_SAMESITE=Lax

# Email Configuration (for future features)
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USE_TLS=True
MAIL_USERNAME=your-email@gmail.com
MAIL_PASSWORD=your-app-password

# OAuth Configuration (for future integration)
GOOGLE_CLIENT_ID=your-google-client-id
GOOGLE_CLIENT_SECRET=your-google-client-secret
```

### 5. Run the Application

```bash
python app.py
```

The application will be available at `http://localhost:5000`

## 🎨 UI/UX Features

### Design System

- **Color Palette**: Modern gradient design with primary colors
- **Typography**: Inter font family for clean, readable text
- **Spacing**: Consistent spacing using CSS custom properties
- **Shadows**: Layered shadows for depth and elevation
- **Border Radius**: Rounded corners for modern appearance

### Interactive Elements

- **Buttons**: Gradient backgrounds with hover effects
- **Forms**: Floating labels and validation feedback
- **Cards**: Elevated cards with subtle shadows
- **Animations**: Smooth transitions and micro-interactions

### Responsive Design

- **Mobile-First**: Optimized for mobile devices
- **Tablet Support**: Adapted layouts for medium screens
- **Desktop**: Full-featured desktop experience
- **Accessibility**: Proper contrast ratios and keyboard navigation

## 🔧 Technical Details

### Backend Architecture

- **Flask**: Lightweight web framework
- **SQLAlchemy**: ORM for database operations
- **Flask-WTF**: Form handling and CSRF protection
- **Bcrypt**: Password hashing and verification
- **Python-dotenv**: Environment variable management

### Frontend Architecture

- **Vanilla JavaScript**: No framework dependencies
- **CSS Grid & Flexbox**: Modern layout techniques
- **CSS Custom Properties**: Consistent theming
- **Progressive Enhancement**: Works without JavaScript

### Database Schema

```sql
Users Table:
- id (Primary Key)
- username (Unique)
- email (Unique)
- password_hash
- first_name
- last_name
- created_at
- last_login
- is_active
```

## 🔐 Security Considerations

### Authentication Security

- **Password Hashing**: Bcrypt with salt rounds
- **Session Management**: Secure session cookies
- **CSRF Protection**: Token-based protection
- **Input Validation**: Server and client-side validation

### Data Protection

- **Environment Variables**: Sensitive data not in code
- **SQL Injection Prevention**: Parameterized queries
- **XSS Prevention**: Template escaping enabled
- **Secure Headers**: Configurable security headers

## 🚀 Deployment

### Environment Variables for Production

```env
SECRET_KEY=your-production-secret-key-very-long-and-random
FLASK_ENV=production
FLASK_DEBUG=False
DATABASE_URL=your-production-database-url
SESSION_COOKIE_SECURE=True
```

### Production Checklist

- [ ] Generate strong SECRET_KEY
- [ ] Set FLASK_DEBUG=False
- [ ] Use production database
- [ ] Enable HTTPS
- [ ] Configure proper CORS
- [ ] Set up monitoring
- [ ] Configure logging

## 📱 Browser Support

- **Chrome**: Latest 2 versions
- **Firefox**: Latest 2 versions
- **Safari**: Latest 2 versions
- **Edge**: Latest 2 versions
- **Mobile**: iOS Safari, Chrome Mobile

## 🔮 Future Enhancements

### Planned Features

- **OAuth Integration**: Google, GitHub, Facebook login
- **Email Verification**: Account activation via email
- **Password Reset**: Secure password recovery
- **Two-Factor Authentication**: TOTP-based 2FA
- **User Roles**: Admin, user, moderator roles
- **API Endpoints**: RESTful API for mobile apps
- **Dark Mode**: Toggle between light and dark themes
- **Audit Logging**: Track user actions and changes

### Technical Improvements

- **Rate Limiting**: Prevent brute force attacks
- **Caching**: Redis for session storage
- **Background Tasks**: Celery for async operations
- **Database Migrations**: Alembic for schema changes
- **Testing**: Comprehensive test suite
- **CI/CD**: Automated testing and deployment

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 📞 Support

For questions or issues, please open an issue on GitHub or contact the development team.

## 🙏 Acknowledgments

- Flask community for the excellent framework
- Bootstrap team for design inspiration
- Modern web development practices and patterns

---

**Built with ❤️ using Flask, SQLAlchemy, and modern web technologies**