"""
Django settings for myproject project.

Generated by 'django-admin startproject' using Django 4.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import platform
import os
from myproject.redirect_middleware import LoginRequiredMiddleware
from myproject.middleware import AutoLogoutMiddleware

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-a^-!si_9u(5noyi=)l%uno@o!0kn95cba#2ajn)2lwdmi^^%e&'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


ALLOWED_HOSTS = ['*', 'fertppm.pythonanywhere.com']

CRISPY_TEMPLATE_PACK = 'bootstrap4'

# Application definition

INSTALLED_APPS = [
    'admin_interface',
    'flat_responsive', # only if django version < 2.0
    'flat', # only if django version < 1.9
    'colorfield',
    'admin_menu',
    'axes',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myapp',
    'crispy_forms',
    'crispy_bootstrap4',
    # 'calculation',
    'widget_tweaks'
]

X_FRAME_OPTIONS='SAMEORIGIN' # only if django version >= 3.0

MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Static file handling
    'django.middleware.security.SecurityMiddleware',  # Security-related headers
    'django.contrib.sessions.middleware.SessionMiddleware',  # Session management
    'django.middleware.common.CommonMiddleware',  # Common processing (e.g., URL handling)
    'django.middleware.csrf.CsrfViewMiddleware',  # CSRF protection
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # User authentication
    'myproject.redirect_middleware.LoginRequiredMiddleware',  # Your custom middleware (Authentication-related?)
    'axes.middleware.AxesMiddleware',  # IP blocking for suspicious login attempts
    'myproject.middleware.AutoLogoutMiddleware',  # Automatic logout after inactivity
    'django.contrib.messages.middleware.MessageMiddleware',  # Message handling
    'django.middleware.clickjacking.XFrameOptionsMiddleware',  # Clickjacking protection
]

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'axes.backends.AxesStandaloneBackend',  # Use the new name
    # ...
]


# Configure the automatic logout time after inactivity (in seconds)
AUTO_LOGOUT_TIME = 300  # 5 minutes (adjust the value as needed)

# Configure Django Axes to track user activity for auto-logout
AXES_KEEP_RECORD = True
AXES_LOCK_OUT_AT_FAILURE = False


ROOT_URLCONF = 'myproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'myapp.context_processors.include_login_form'

            ],
        },
    },
]

WSGI_APPLICATION = 'myproject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

if platform.system() == 'Windows':
    DATABASES = {
        'default': {
            # 'ENGINE': 'django.db.backends.mysql',
            # 'NAME': 'fertppm$fertdatabase',
            # 'USER': 'fertppm',
            # 'PASSWORD': 'Sulu5542',
            # 'HOST': 'fertppm.mysql.pythonanywhere-services.com',
            # 'PORT': '3306',

            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',

            # 'ENGINE': 'django.db.backends.postgresql',
            # 'NAME': 'postgres',
            # 'USER': 'masteruser',
            # 'PASSWORD': 'Sulu5542',
            # 'HOST': 'fertigation-project.cf7k6d2wcc3q.us-west-2.rds.amazonaws.com',
            # 'PORT': '5432',
        }
    }
elif platform.system() == 'Linux':
        DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'fertppm$fertdatabase',
            'USER': 'fertppm',
            'PASSWORD': 'Sulu5542',
            'HOST': 'fertppm.mysql.pythonanywhere-services.com',
            'PORT': '3306',

            # 'ENGINE': 'django.db.backends.sqlite3',
            # 'NAME': BASE_DIR / 'db.sqlite3',

            # 'ENGINE': 'django.db.backends.postgresql',
            # 'NAME': 'postgres',
            # 'USER': 'masteruser',
            # 'PASSWORD': 'Sulu5542',
            # 'HOST': 'fertigation-project.cf7k6d2wcc3q.us-west-2.rds.amazonaws.com',
            # 'PORT': '5432',
        }
    }


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = '/mystaticfiles/'
STATIC_ROOT = BASE_DIR / 'productionfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# STATICFILES_DIRS = [
#     BASE_DIR / 'mystaticfiles',
# ]

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "mystaticfiles"),
]

WHITENOISE_MANIFEST_STRICT = False

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


"""DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
"""

# LOGIN_REDIRECT_URL = 'dasboard'
# LOGOUT_REDIRECT_URL = 'login'

LOGIN_URL = '/login/'


SECURE_SSL_REDIRECT=False
SESSION_COOKIE_SECURE=False
CSRF_COOKIE_SECURE=False

# ADMIN_LOGO = 'FERTPPM.jpeg'
MENU_WEIGHT = {
    'World': 20,
    'Auth': 4,
    'Sample': 5
}

ADMIN_STYLE = {
    'primary-color': '#164B36',
    'secondary-color': 'green',
    'tertiary-color': '#51B48E',
    'body-color': 'white',
    'backgound-color': 'black',
}

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')