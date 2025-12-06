from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

# ========= SEGURIDAD =========
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY")
DEBUG = False
ALLOWED_HOSTS = ["*"]

# ========= APPS =========
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "clinica",
]

# ========= MIDDLEWARE =========
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# ========= STATIC FILES =========
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

# ========= DATABASE (RAILWAY POSTGRES) =========
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("PGDATABASE"),
        "USER": os.environ.get("PGUSER"),
        "PASSWORD": os.environ.get("PGPASSWORD"),
        "HOST": os.environ.get("PGHOST"),
        "PORT": os.environ.get("PGPORT"),
    }
}

# ========= STATIC FILES (WHITENOISE) =========
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
