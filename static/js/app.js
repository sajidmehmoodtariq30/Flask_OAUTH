// Modern JavaScript for Flask Auth App
class FlaskAuthApp {
    constructor() {
        this.init();
    }

    init() {
        this.setupFormValidation();
        this.setupPasswordToggle();
        this.setupAnimations();
        this.setupAlertDismissal();
        this.setupFormSubmission();
        this.setupThemeToggle();
    }

    // Form Validation
    setupFormValidation() {
        const forms = document.querySelectorAll('form');
        forms.forEach(form => {
            const inputs = form.querySelectorAll('input[required]');
            inputs.forEach(input => {
                input.addEventListener('blur', () => this.validateField(input));
                input.addEventListener('input', () => this.clearFieldError(input));
            });

            form.addEventListener('submit', (e) => {
                if (!this.validateForm(form)) {
                    e.preventDefault();
                }
            });
        });
    }

    validateField(field) {
        const value = field.value.trim();
        const fieldName = field.name;
        let isValid = true;
        let errorMessage = '';

        // Clear previous errors
        this.clearFieldError(field);

        // Required field validation
        if (!value) {
            isValid = false;
            errorMessage = `${this.capitalizeFirst(fieldName)} is required`;
        }

        // Email validation
        if (fieldName === 'email' && value) {
            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            if (!emailRegex.test(value)) {
                isValid = false;
                errorMessage = 'Please enter a valid email address';
            }
        }

        // Password validation
        if (fieldName === 'password' && value) {
            if (value.length < 6) {
                isValid = false;
                errorMessage = 'Password must be at least 6 characters long';
            }
        }

        // Confirm password validation
        if (fieldName === 'confirm_password' && value) {
            const passwordField = document.querySelector('input[name="password"]');
            if (passwordField && value !== passwordField.value) {
                isValid = false;
                errorMessage = 'Passwords do not match';
            }
        }

        // Username validation
        if (fieldName === 'username' && value) {
            if (value.length < 4) {
                isValid = false;
                errorMessage = 'Username must be at least 4 characters long';
            }
        }

        if (!isValid) {
            this.showFieldError(field, errorMessage);
        } else {
            this.showFieldSuccess(field);
        }

        return isValid;
    }

    validateForm(form) {
        const inputs = form.querySelectorAll('input[required]');
        let isFormValid = true;

        inputs.forEach(input => {
            if (!this.validateField(input)) {
                isFormValid = false;
            }
        });

        return isFormValid;
    }

    showFieldError(field, message) {
        field.classList.add('error');
        field.classList.remove('success');
        
        let errorElement = field.parentNode.querySelector('.form-error');
        if (!errorElement) {
            errorElement = document.createElement('div');
            errorElement.classList.add('form-error');
            field.parentNode.appendChild(errorElement);
        }
        errorElement.textContent = message;
    }

    showFieldSuccess(field) {
        field.classList.add('success');
        field.classList.remove('error');
        this.clearFieldError(field);
    }

    clearFieldError(field) {
        field.classList.remove('error');
        const errorElement = field.parentNode.querySelector('.form-error');
        if (errorElement) {
            errorElement.remove();
        }
    }

    // Password Toggle Functionality
    setupPasswordToggle() {
        const passwordFields = document.querySelectorAll('input[type="password"]');
        passwordFields.forEach(field => {
            const wrapper = document.createElement('div');
            wrapper.style.position = 'relative';
            field.parentNode.insertBefore(wrapper, field);
            wrapper.appendChild(field);

            const toggleBtn = document.createElement('button');
            toggleBtn.type = 'button';
            toggleBtn.innerHTML = '👁️';
            toggleBtn.style.cssText = `
                position: absolute;
                right: 10px;
                top: 50%;
                transform: translateY(-50%);
                background: none;
                border: none;
                cursor: pointer;
                font-size: 16px;
                opacity: 0.7;
                transition: opacity 0.3s ease;
            `;
            toggleBtn.addEventListener('click', () => this.togglePassword(field, toggleBtn));
            wrapper.appendChild(toggleBtn);

            toggleBtn.addEventListener('mouseenter', () => {
                toggleBtn.style.opacity = '1';
            });
            toggleBtn.addEventListener('mouseleave', () => {
                toggleBtn.style.opacity = '0.7';
            });
        });
    }

    togglePassword(field, button) {
        if (field.type === 'password') {
            field.type = 'text';
            button.innerHTML = '🙈';
        } else {
            field.type = 'password';
            button.innerHTML = '👁️';
        }
    }

    // Animations
    setupAnimations() {
        // Intersection Observer for scroll animations
        if ('IntersectionObserver' in window) {
            const observer = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        entry.target.style.animationDelay = '0.1s';
                        entry.target.classList.add('animate-in');
                    }
                });
            });

            const animatedElements = document.querySelectorAll('.user-card, .btn, .alert');
            animatedElements.forEach(el => observer.observe(el));
        }

        // Add hover effects to buttons
        const buttons = document.querySelectorAll('.btn');
        buttons.forEach(btn => {
            btn.addEventListener('mouseenter', () => {
                btn.style.transform = 'translateY(-2px)';
            });
            btn.addEventListener('mouseleave', () => {
                btn.style.transform = 'translateY(0)';
            });
        });
    }

    // Alert Dismissal
    setupAlertDismissal() {
        const alerts = document.querySelectorAll('.alert');
        alerts.forEach(alert => {
            // Auto-dismiss success and info alerts after 5 seconds
            if (alert.classList.contains('alert-success') || alert.classList.contains('alert-info')) {
                setTimeout(() => {
                    this.dismissAlert(alert);
                }, 5000);
            }

            // Add dismiss button
            const dismissBtn = document.createElement('button');
            dismissBtn.innerHTML = '×';
            dismissBtn.style.cssText = `
                position: absolute;
                right: 10px;
                top: 10px;
                background: none;
                border: none;
                font-size: 20px;
                cursor: pointer;
                opacity: 0.7;
                transition: opacity 0.3s ease;
            `;
            dismissBtn.addEventListener('click', () => this.dismissAlert(alert));
            
            alert.style.position = 'relative';
            alert.appendChild(dismissBtn);
        });
    }

    dismissAlert(alert) {
        alert.style.opacity = '0';
        alert.style.transform = 'translateX(100%)';
        setTimeout(() => {
            alert.remove();
        }, 300);
    }

    // Form Submission with Loading States
    setupFormSubmission() {
        const forms = document.querySelectorAll('form');
        forms.forEach(form => {
            form.addEventListener('submit', (e) => {
                const submitBtn = form.querySelector('button[type="submit"], input[type="submit"]');
                if (submitBtn && this.validateForm(form)) {
                    this.showLoadingState(submitBtn);
                }
            });
        });
    }

    showLoadingState(button) {
        button.classList.add('loading');
        button.disabled = true;
        
        // Re-enable button after 10 seconds as fallback
        setTimeout(() => {
            this.hideLoadingState(button);
        }, 10000);
    }

    hideLoadingState(button) {
        button.classList.remove('loading');
        button.disabled = false;
    }

    // Theme Toggle (for future use)
    setupThemeToggle() {
        // Check for saved theme preference or default to 'light'
        const currentTheme = localStorage.getItem('theme') || 'light';
        document.documentElement.setAttribute('data-theme', currentTheme);

        // Create theme toggle button (if needed in future)
        this.createThemeToggle();
    }

    createThemeToggle() {
        const themeToggle = document.createElement('button');
        themeToggle.innerHTML = '🌙';
        themeToggle.style.cssText = `
            position: fixed;
            top: 20px;
            right: 20px;
            background: rgba(255, 255, 255, 0.9);
            border: none;
            border-radius: 50%;
            width: 40px;
            height: 40px;
            cursor: pointer;
            font-size: 16px;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
            transition: all 0.3s ease;
            z-index: 1000;
        `;

        themeToggle.addEventListener('click', () => {
            this.toggleTheme();
            themeToggle.innerHTML = document.documentElement.getAttribute('data-theme') === 'dark' ? '☀️' : '🌙';
        });

        document.body.appendChild(themeToggle);
    }

    toggleTheme() {
        const currentTheme = document.documentElement.getAttribute('data-theme');
        const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
        
        document.documentElement.setAttribute('data-theme', newTheme);
        localStorage.setItem('theme', newTheme);
    }

    // Utility Functions
    capitalizeFirst(string) {
        return string.charAt(0).toUpperCase() + string.slice(1);
    }

    // Show notification
    showNotification(message, type = 'info') {
        const notification = document.createElement('div');
        notification.className = `alert alert-${type}`;
        notification.textContent = message;
        notification.style.cssText = `
            position: fixed;
            top: 20px;
            right: 20px;
            z-index: 1000;
            max-width: 300px;
            animation: slideInRight 0.3s ease-out;
        `;

        document.body.appendChild(notification);

        // Auto-dismiss after 3 seconds
        setTimeout(() => {
            this.dismissAlert(notification);
        }, 3000);
    }

    // Copy to clipboard functionality
    copyToClipboard(text) {
        if (navigator.clipboard) {
            navigator.clipboard.writeText(text).then(() => {
                this.showNotification('Copied to clipboard!', 'success');
            });
        } else {
            // Fallback for older browsers
            const textArea = document.createElement('textarea');
            textArea.value = text;
            document.body.appendChild(textArea);
            textArea.select();
            document.execCommand('copy');
            document.body.removeChild(textArea);
            this.showNotification('Copied to clipboard!', 'success');
        }
    }
}

// Initialize the app when the DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    new FlaskAuthApp();
});

// Add some CSS animations via JavaScript
const style = document.createElement('style');
style.textContent = `
    @keyframes slideInRight {
        from {
            opacity: 0;
            transform: translateX(100%);
        }
        to {
            opacity: 1;
            transform: translateX(0);
        }
    }

    .animate-in {
        animation: fadeInUp 0.6s ease-out forwards;
    }

    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }

    .btn:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15) !important;
    }

    .btn:active {
        transform: translateY(0) !important;
    }

    .form-control:focus {
        transform: scale(1.02);
    }
`;
document.head.appendChild(style);
