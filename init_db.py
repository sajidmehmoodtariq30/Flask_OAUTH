#!/usr/bin/env python3
"""
Database initialization script for Flask Auth App
"""

import os
import sys
from pathlib import Path

# Add the project directory to the Python path
project_dir = Path(__file__).parent
sys.path.insert(0, str(project_dir))

from app import app, db, User
from dotenv import load_dotenv

def init_db():
    """Initialize the database with tables"""
    load_dotenv()
    
    print("🗄️  Initializing database...")
    
    with app.app_context():
        # Create all tables
        db.create_all()
        print("✅ Database tables created successfully")
        
        # Check if any users exist
        user_count = User.query.count()
        print(f"📊 Current user count: {user_count}")
        
        if user_count == 0:
            create_admin = input("Create an admin user? (y/N): ").lower().strip()
            if create_admin == 'y':
                create_admin_user()

def create_admin_user():
    """Create an admin user"""
    print("\n👤 Creating admin user...")
    
    username = input("Admin username: ").strip()
    if not username:
        print("❌ Username cannot be empty")
        return
    
    email = input("Admin email: ").strip()
    if not email:
        print("❌ Email cannot be empty")
        return
    
    first_name = input("First name (optional): ").strip()
    last_name = input("Last name (optional): ").strip()
    
    password = input("Admin password: ").strip()
    if len(password) < 6:
        print("❌ Password must be at least 6 characters")
        return
    
    # Check if user already exists
    existing_user = User.query.filter(
        (User.username == username) | (User.email == email)
    ).first()
    
    if existing_user:
        print("❌ User with this username or email already exists")
        return
    
    # Create admin user
    admin_user = User(
        username=username,
        email=email,
        first_name=first_name if first_name else None,
        last_name=last_name if last_name else None
    )
    admin_user.set_password(password)
    
    db.session.add(admin_user)
    db.session.commit()
    
    print(f"✅ Admin user '{username}' created successfully!")

def reset_db():
    """Reset the database (WARNING: This will delete all data!)"""
    confirm = input("⚠️  This will delete ALL data! Are you sure? Type 'yes' to confirm: ")
    if confirm.lower() != 'yes':
        print("❌ Database reset cancelled")
        return
    
    print("🗑️  Resetting database...")
    
    with app.app_context():
        db.drop_all()
        db.create_all()
        print("✅ Database reset successfully")

def main():
    """Main function"""
    if len(sys.argv) > 1:
        if sys.argv[1] == 'reset':
            reset_db()
        elif sys.argv[1] == 'admin':
            with app.app_context():
                create_admin_user()
        else:
            print("Usage: python init_db.py [reset|admin]")
            print("  reset - Reset the database (deletes all data)")
            print("  admin - Create an admin user")
    else:
        init_db()

if __name__ == "__main__":
    main()
