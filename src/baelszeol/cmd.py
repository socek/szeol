import logging

from bael.project.core import ProjectCore

from .tasks import Manage
from .tasks import Runserver
from .tasks import Shell
from .tasks import Tests
from .tasks import Coverage


class ReProjectCore(ProjectCore):

    def before_dependencies(self):
        super().before_dependencies()
        self.paths.set_path('exe:pytest', 'virtualenv:bin', 'py.test')
        self.paths.set_path('docker', 'cwd', 'docker')
        self.paths.set_path('psqldb', 'docker', 'psqldb')
        self.paths.set_path('sentrydb', 'docker', 'sentrydb')
        self.paths.set_path('redisdb', 'docker', 'redisdb')
        self.paths['locale'] = ['%(cwd)s', 'locale', 'pl', 'LC_MESSAGES']
        self.paths.set_path('gettext_pl_po', 'locale', 'django.po')
        self.paths.set_path('gettext_pl_mo', 'locale', 'django.mo')


def run_task(cls):
    format = ' * %(levelname)s %(name)s: %(message)s *'
    logging.basicConfig(level=logging.INFO, format=format)

    task = cls(ReProjectCore())
    task.run()
    task.save_report()


def runserver():
    run_task(Runserver)


def shell():
    run_task(Shell)


def manage():
    run_task(Manage)


def tests():
    run_task(Tests)


def coverage():
    run_task(Coverage)
