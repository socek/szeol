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
    paths['cwd'] = dirname(dirname(paths['BASE_DIR']))
    paths.set_path('DATA_DIR', 'BASE_DIR', '../tmpdata')
    paths.set_path('main_static', 'BASE_DIR', 'static')


def installed_apps(settings, paths):
    settings['INSTALLED_APPS'] = [
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',

        'raven.contrib.django.raven_compat',

        'szeol.main',
        'szeol.menu',
        'szeol.localauth',
        'szeol.dashboard',
        'szeol.products',
        'szeol.contacts',
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
    settings['LOGIN_URL '] = '/accounts/login'
    settings['LOGIN_REDIRECT_URL'] = 'dashboard_home'
    settings['LOGOUT_REDIRECT_URL'] = '/'


def i18n(settings, paths):
    paths.set_path('locale', 'BASE_DIR', '../../locale')
    settings['LANGUAGE_CODE'] = 'pl-pl'
    settings['TIME_ZONE'] = 'UTC'
    settings['USE_I18N'] = True
    settings['USE_L10N'] = True
    settings['USE_TZ'] = True
    settings['LOCALE_PATHS'] = (paths['locale'],)


def static(settings, paths):
    settings['STATIC_URL'] = '/static/'
    settings['STATICFILES_DIRS'] = [
        paths['main_static'],
    ]
