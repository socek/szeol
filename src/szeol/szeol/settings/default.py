def make_settings(settings, paths):
    database(settings, paths)
    hosts(settings, paths)
    env(settings, paths)
    vue(settings, paths)


def database(settings, paths):
    paths.set_path('sqlite_db', 'DATA_DIR', 'sqlite3.db')
    settings['DATABASES'] = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': '%(paths:sqlite_db)s',
        }
    }


def hosts(settings, paths):
    settings['ALLOWED_HOSTS'] = []


def env(settings, paths):
    settings['SECRET_KEY'] = 'po*sdjb$inb22#zj%%=n)8v7pc!%--%&wah3eqmgvopcc6a#*^o-'
    settings['DEBUG'] = True


def vue(settings, paths):
    settings['VUE_URL'] = 'https://cdnjs.cloudflare.com/ajax/libs/vue/2.2.4/vue.min.js'
