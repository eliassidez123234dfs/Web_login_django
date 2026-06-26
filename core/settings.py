from pathlib import Path
import os
import environ

# ===========================================================================
# 1. CONFIGURACIÓN BASE Y ENTORNO
# ===========================================================================

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Inicializar django-environ
env = environ.Env()

# Leer el archivo .env (debe estar en la raíz del proyecto)
environ.Env.read_env(BASE_DIR / '.env')

# ===========================================================================
# 2. SEGURIDAD: CLAVES Y MODO DEBUG
# ===========================================================================

# SECURITY WARNING: keep the secret key used in production secret!
# La clave secreta se lee desde el archivo .env
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG debe ser False en producción. Se lee desde .env (por defecto False)
DEBUG = env.bool('DEBUG', default=False)

# SECURITY WARNING: define los hosts permitidos (ej: 'localhost, .dominio.com')
# Se lee como lista desde .env
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')

# ===========================================================================
# 3. APLICACIONES INSTALADAS
# ===========================================================================

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

PROJECT_APPS = [
    # 'bootstrap5',   # <-- Eliminado para evitar incompatibilidad con Django 6.0
    'users',          # Tu aplicación de usuarios
    'products',       # Catálogo y gestión de productos
    'contact',        # Formulario y bandeja de contacto
]

INSTALLED_APPS = DJANGO_APPS + PROJECT_APPS

# ===========================================================================
# 4. MIDDLEWARE (orden crítico para seguridad)
# ===========================================================================

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',   # Obligatorio para seguridad
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ===========================================================================
# 5. CONFIGURACIÓN DE SEGURIDAD AVANZADA (HTTPS, HSTS, COOKIES)
# ===========================================================================

# --- Redirección forzada a HTTPS (en producción) ---
# Si DEBUG=False, todas las peticiones HTTP se redirigen a HTTPS
SECURE_SSL_REDIRECT = not DEBUG  # Solo activo en producción

# --- Cookies seguras ---
# Las cookies de sesión y CSRF solo se enviarán por HTTPS
SESSION_COOKIE_SECURE = not DEBUG
CSRF_COOKIE_SECURE = not DEBUG

# --- HSTS (HTTP Strict Transport Security) ---
# Obliga a los navegadores a usar siempre HTTPS durante el tiempo indicado (en segundos)
# 31536000 segundos = 1 año (esta es una recomendacion)
SECURE_HSTS_SECONDS = 31536000 if not DEBUG else 0
# Incluir subdominios en la política HSTS
SECURE_HSTS_INCLUDE_SUBDOMAINS = not DEBUG
# Permite que el sitio sea incluido en la lista de precarga de HSTS de los navegadores
SECURE_HSTS_PRELOAD = not DEBUG

# --- Prevención de clickjacking ---
# Deniega que el sitio sea mostrado dentro de un iframe (evita ataques UI redress)
X_FRAME_OPTIONS = 'DENY'

# --- Prevención de sniffing de MIME types ---
# Los navegadores no intentarán adivinar el tipo MIME de los recursos
SECURE_CONTENT_TYPE_NOSNIFF = True

# --- Protección contra XSS (cross-site scripting) ---
# Los navegadores activan su filtro XSS para bloquear ataques
SECURE_BROWSER_XSS_FILTER = True

# --- Política de seguridad de contenido (CSP) - OPCIONAL ---
# Si quieres añadir CSP, descomenta y configura según tus necesidades
# CSP_DEFAULT_SRC = ("'self'",)
# CSP_SCRIPT_SRC = ("'self'", "https://cdn.jsdelivr.net")
# CSP_STYLE_SRC = ("'self'", "https://cdn.jsdelivr.net")
# INSTALLED_APPS += ('csp',)
# MIDDLEWARE.insert(0, 'csp.middleware.CSPMiddleware')

# ===========================================================================
# 6. CONFIGURACIÓN DE CSRF
# ===========================================================================

# Orígenes que pueden enviar peticiones POST con token CSRF (ej: frontend en otro dominio)
# Se lee desde .env como lista
CSRF_TRUSTED_ORIGINS = env.list('CSRF_TRUSTED_ORIGINS', default=[])

# ===========================================================================
# 7. ENRUTAMIENTO Y TEMPLATES
# ===========================================================================

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # <-- Añadimos la carpeta global de templates
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'

# ===========================================================================
# 8. BASE DE DATOS (SQLite para desarrollo)
# ===========================================================================

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# ===========================================================================
# 9. VALIDACIÓN DE CONTRASEÑAS (seguridad de usuarios)
# ===========================================================================

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

# ===========================================================================
# 10. INTERNACIONALIZACIÓN
# ===========================================================================

LANGUAGE_CODE = 'es-es'   # Cambiado a español
TIME_ZONE = 'America/Bogota'  # Ajusta según tu zona horaria
USE_I18N = True
USE_TZ = True

# ===========================================================================
# 11. ARCHIVOS ESTÁTICOS Y MEDIA
# ===========================================================================

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static',   # Carpeta global para CSS, JS, imágenes
]
STATIC_ROOT = BASE_DIR / 'staticfiles'   # Para recoger archivos en producción (collectstatic)

# Archivos subidos por usuarios (imágenes de productos, etc.)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# ===========================================================================
# 12. CONFIGURACIÓN DE LOGGING (OPCIONAL, pero recomendado)
# ===========================================================================

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'WARNING',
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False,
        },
    },
}

# ===========================================================================
# 13. CONFIGURACIÓN ADICIONAL PARA EL ENTORNO DE PRODUCCIÓN
# ===========================================================================

if not DEBUG:
    # En producción, se recomienda usar una base de datos más robusta (PostgreSQL)
    # Puedes descomentar y configurar:
    # DATABASES['default'] = env.db('DATABASE_URL')

    # Configuración de correo para producción (SMTP)
    # Define EMAIL_HOST, EMAIL_PORT, EMAIL_HOST_USER, EMAIL_HOST_PASSWORD en .env
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = env('EMAIL_HOST', default='')
    EMAIL_PORT = env.int('EMAIL_PORT', default=587)
    EMAIL_USE_TLS = env.bool('EMAIL_USE_TLS', default=True)
    EMAIL_HOST_USER = env('EMAIL_HOST_USER', default='')
    EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD', default='')

    # Cabeceras de seguridad adicionales
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# ===========================================================================
# 14. CONFIGURACIÓN DE CORREO PARA EL FORMULARIO DE CONTACTO
# ===========================================================================

# Backend de correo (por defecto imprime en consola para desarrollo)
if DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Dirección desde la que se envían los correos
DEFAULT_FROM_EMAIL = 'noreply@red.com'

# Dirección que recibe las notificaciones del formulario de contacto
CONTACT_EMAIL = env('CONTACT_EMAIL', default='admin@red.com')