#!/usr/bin/env python3
"""
Development script for Flask Auth App
Run this script to start the development server with the proper environment setup.
"""

import os
import subprocess
import sys
from pathlib import Path

def main():
    """Main function to run the Flask application"""
    
    # Get the project directory
    project_dir = Path(__file__).parent
    
    # Change to project directory
    os.chdir(project_dir)
    
    # Check if .env file exists
    env_file = project_dir / '.env'
    if not env_file.exists():
        print("⚠️  Warning: .env file not found!")
        print("Creating a basic .env file for development...")
        
        # Create basic .env file
        with open(env_file, 'w') as f:
            f.write("""# Flask Configuration
SECRET_KEY=dev-secret-key-change-this-in-production
FLASK_ENV=development
FLASK_DEBUG=True

# Database Configuration
DATABASE_URL=sqlite:///users.db

# Security Settings
SESSION_COOKIE_SECURE=False
SESSION_COOKIE_HTTPONLY=True
SESSION_COOKIE_SAMESITE=Lax
""")
        print("✅ Created basic .env file")
    
    # Check if virtual environment is activated
    if not hasattr(sys, 'real_prefix') and not (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
        print("⚠️  Warning: Virtual environment not detected!")
        print("It's recommended to run this in a virtual environment.")
        print("To create one: python -m venv venv")
        print("To activate: venv\\Scripts\\activate (Windows) or source venv/bin/activate (Unix)")
        print()
    
    # Install requirements if needed
    try:
        import flask
        import flask_sqlalchemy
        import flask_wtf
        import bcrypt
        from dotenv import load_dotenv
        print("✅ All required packages are installed")
    except ImportError as e:
        print(f"❌ Missing package: {e}")
        print("Installing requirements...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
            print("✅ Requirements installed successfully")
        except subprocess.CalledProcessError:
            print("❌ Failed to install requirements")
            return 1
    
    print("🚀 Starting Flask Auth App...")
    print("📱 Access the app at: http://localhost:5000")
    print("🛑 Press Ctrl+C to stop the server")
    print("-" * 50)
    
    # Run the Flask application
    try:
        from app import app
        app.run(host='0.0.0.0', port=5000, debug=True)
    except KeyboardInterrupt:
        print("\n👋 Flask Auth App stopped")
        return 0
    except Exception as e:
        print(f"❌ Error starting the application: {e}")
        return 1

if __name__ == "__main__":
    sys.exit(main())
