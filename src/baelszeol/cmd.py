import logging

from bael.project.core import ProjectCore

from .tasks import Manage
from .tasks import Runserver
from .tasks import Shell
from .tasks import Tests


class ReProjectCore(ProjectCore):

    def before_dependencies(self):
        super().before_dependencies()
        self.paths.set_path('exe:pytest', 'virtualenv:bin', 'py.test')


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
