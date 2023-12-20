from .base import *

ALLOWED_HOSTS = []

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = "6gu4+z=qz8zr7w+y2hyqibm*@rqf3q8tj^gfk&-ns1*1er7^%6"


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}