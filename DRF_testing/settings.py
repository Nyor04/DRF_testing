"""
Django settings for DRF_testing project.

Generated by 'django-admin startproject' using Django 5.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
from os import getenv
from dotenv import load_dotenv


load_dotenv()
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = getenv('DJANGO_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'drf_spectacular',
    'django_extensions',
    'app_patient',
    'app_doctor',
    'app_appointment',
    'docs',
   
]




MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'DRF_testing.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'DRF_testing.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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

#rest_framework config dict.
# REST_FRAMEWORK = {
#     # Use Django's standard `django.contrib.auth` permissions,
#     # or allow read-only access for unauthenticated users.
#     '
# }




# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    # YOUR SETTINGS
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
     ],
}

SPECTACULAR_SETTINGS = {
    'TITLE': 'Dr. Appointment API',
    'DESCRIPTION': 'API para gestionar citas con doctores de un hospital X, creada para practicar con django Rest Framework',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
    'TAGS': [
        {
            'name': 'Patients',
            'description': 'Endpoints for managing Patients in the system.',
        },
        {
            'name': 'Admin - Patients',
            'description': 'Administrative actions for Patients management.',
        },
        {
            'name': 'Appointment',
            'description': 'Endpoints for managing Appointments in the system.',
        },
        {
            'name': 'Admin - Appointment',
            'description': 'Administrative actions for Appointments management.',
        },
        {
            'name': 'AppointmentNotes',
            'description': 'Endpoints for managing Appointment Notes in the system.',
        },
        {
            'name': 'Admin - AppointmentNotes',
            'description': 'Administrative actions for Appointment Notes management.',
        },
        {
            'name': 'Doctors',
            'description': 'Endpoints for managing Doctors in the system.',
        },
        {
            'name': 'Admin - Doctors',
            'description': 'Administrative actions for Doctors management.',
        },
        {
            'name': 'MedicalNotes',
            'description': 'Endpoints for managing Medical Notes in the system.',
        },
        {
            'name': 'Admin - MedicalNotes',
            'description': 'Administrative actions for Medical Notes management.',
        },
        {
            'name': 'Department',
            'description': 'Endpoints for managing Departments in the system.',
        },
        {
            'name': 'Admin - Department',
            'description': 'Administrative actions for Departments management.',
        },
        {
            'name': 'DoctorAvailability',
            'description': 'Endpoints for managing Doctors Availabilities in the system.',
        },
        {
            'name': 'Admin - DoctorAvailability',
            'description': 'Administrative actions for Doctors Availabilities management.',
        },
        {
            'name': 'Insurance',
            'description': 'Endpoints for managing Insurance in the system.',
        },
        {
            'name': 'MedicalRecords',
            'description': 'Endpoints for managing Medica Records in the system.',
        },
        
        
        
    ],
}