from os.path import abspath
from os.path import dirname


def make_settings(settings, paths):
    default_paths(settings, paths)
    installed_apps(settings, paths)
    middlewares(settings, paths)
    urlconf(settings, paths)
    templates(settings, paths)
    wsgi(settings, paths)
    auths(settings, paths)
    i18n(settings, paths)
    static(settings, paths)


def default_paths(settings, paths):
    paths['BASE_DIR'] = dirname(dirname(dirname(abspath(__file__))))
    paths.set_path('DATA_DIR', 'BASE_DIR', '../tmpdata')
    paths.set_path('main_static', 'BASE_DIR', 'static')


def session(settings, paths):
    settings['session.type'] = 'file'
    settings['session.key'] = 'needtochangethis'
    settings['session.secret'] = 'needtochangethistoo'
    settings['session.cookie_on_exception'] = True

    paths['session'] = {
        'data_dir': ["%(data)s", 'sessions', 'data'],
        'lock_dir': ["%(data)s", 'sessions', 'lock'],
    }
    settings['session.data_dir'] = '%(paths:session:data_dir)s'
    settings['session.lock_dir'] = '%(paths:session:lock_dir)s'


def installed_apps(settings, paths):
    settings['INSTALLED_APPS'] = [
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',

        'szeol.main',
        'szeol.localauth',
    ]


def middlewares(settings, paths):
    settings['MIDDLEWARE'] = [
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ]


def urlconf(settings, paths):
    settings['ROOT_URLCONF'] = 'szeol.urls'


def templates(settings, paths):
    settings['TEMPLATES'] = [
        {
            'BACKEND': 'django.template.backends.jinja2.Jinja2',
            'DIRS': [],
            'APP_DIRS': True,
            'OPTIONS': {
                # 'context_processors': [
                #     'django.template.context_processors.debug',
                #     'django.template.context_processors.request',
                #     'django.contrib.auth.context_processors.auth',
                #     'django.contrib.messages.context_processors.messages',
                # ],
            },
        },
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


def wsgi(settings, paths):
    settings['WSGI_APPLICATION'] = 'szeol.wsgi.application'


def auths(settings, paths):
    settings['AUTH_PASSWORD_VALIDATORS'] = [
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
    settings['LOGIN_URL '] = 'login'
    settings['LOGIN_REDIRECT_URL'] = 'home'


def i18n(settings, paths):
    settings['LANGUAGE_CODE'] = 'en-us'
    settings['TIME_ZONE'] = 'UTC'
    settings['USE_I18N'] = True
    settings['USE_L10N'] = True
    settings['USE_TZ'] = True


def static(settings, paths):
    settings['STATIC_URL'] = '/static/'
    settings['STATICFILES_DIRS'] = [
        paths['main_static'],
    ]
