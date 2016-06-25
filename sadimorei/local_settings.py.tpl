# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 't0p_s3cr3t!!'

DEBUG = True or False

ALLOWED_HOSTS = []

DATABASES = {
    'default':
        {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': u'db_name',
            'HOST': u'127.0.0.1',
            'USER': u'db_user',
            'PASSWORD': u'db_password',
            'TEST': {
                'CHARSET': "utf8",
                'COLLATION': "utf8_general_ci",
            },
        }
}
