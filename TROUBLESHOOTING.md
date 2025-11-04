# 🔧 QuizMaster Troubleshooting Guide

## Common Issues and Solutions

### 🚫 CSRF Verification Failed (403 Error)

**Problem**: Getting "CSRF verification failed. Request aborted." when submitting forms.

**Causes**:
- Browser preview proxy using different origin
- Missing CSRF tokens in forms
- Incorrect CSRF settings

**Solutions**:
1. **Check CSRF Settings** (Already configured in settings.py):
   ```python
   CSRF_TRUSTED_ORIGINS = [
       'http://127.0.0.1:8000',
       'http://127.0.0.1:57092',  # Browser preview
       'http://localhost:8000',
       'http://localhost:57092',
   ]
   ```

2. **Clear Browser Cache**: 
   - Clear cookies and cache
   - Try in incognito/private mode

3. **Direct Access**: 
   - Try accessing directly at http://127.0.0.1:8000 instead of browser preview

4. **Check Form Templates**: 
   - Ensure all POST forms have `{% csrf_token %}`

### 🔍 Template Syntax Errors

**Problem**: TemplateSyntaxError with complex filter chains.

**Solution**: 
- Use simple `{% if %}` conditions instead of complex filter chains
- Avoid chaining multiple template filters with complex syntax

### 🗄️ Database Issues

**Problem**: Database errors or missing tables.

**Solutions**:
1. **Run Migrations**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

2. **Reset Database** (if needed):
   ```bash
   del db.sqlite3
   python manage.py migrate
   python add_sample_data.py
   ```

### 🔐 Authentication Issues

**Problem**: Login/logout not working properly.

**Solutions**:
1. **Check URL Configuration**: Ensure all auth URLs are properly configured
2. **Clear Sessions**: Clear browser cookies
3. **Check User Creation**: Verify users exist in admin panel

### 🎨 Static Files Not Loading

**Problem**: CSS/JS files not loading.

**Solutions**:
1. **Check Settings**:
   ```python
   STATIC_URL = 'static/'
   ```

2. **Collect Static Files** (for production):
   ```bash
   python manage.py collectstatic
   ```

### 🚀 Server Won't Start

**Problem**: Development server fails to start.

**Solutions**:
1. **Check Port**: Ensure port 8000 is not in use
2. **Check Python Version**: Ensure Python 3.8+ is installed
3. **Install Dependencies**: 
   ```bash
   pip install -r requirements.txt
   ```

## 📞 Getting Help

If you encounter issues not covered here:

1. **Check Django Debug Output**: Look at the detailed error message
2. **Check Browser Console**: Look for JavaScript errors
3. **Check Server Logs**: Review the Django development server output
4. **Test in Different Browser**: Try Chrome, Firefox, or Edge

## ✅ Quick Health Check

Run these commands to verify everything is working:

```bash
# Check Django installation
python -c "import django; print(django.get_version())"

# Check database
python manage.py check

# Run tests (if any)
python manage.py test

# Start server
python manage.py runserver
```

## 🔄 Reset Everything

If all else fails, here's how to reset the project:

```bash
# Stop server (Ctrl+C)
# Delete database
del db.sqlite3

# Run migrations
python manage.py migrate

# Add sample data
python add_sample_data.py

# Create superuser
python manage.py createsuperuser

# Start server
python manage.py runserver
```

---

**Need more help?** Check the Django documentation at https://docs.djangoproject.com/
