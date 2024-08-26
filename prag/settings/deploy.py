from .base import *

env = environ.Env(
    #set casting, default value
    DEBUG = (bool,False)
)



#reading .env file
environ.Env.read_env(
    env_file= os.path.join(BASE_DIR, '.env')
)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret! 배포 시 노출 X
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*'] #모든 사용자 사용 가능

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "django",
        "USER": "django",
        "PASSWORD": "password1234",
        "HOST": "mariadb",
        "PORT": "3306",
    }
}