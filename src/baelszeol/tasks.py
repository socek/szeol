import sys


from bael.project.develop import Develop
from baelfire.dependencies import AlwaysRebuild
from baelfire.dependencies import RunBefore
from baelfire.error import CommandAborted
from baelfire.error import CommandError

from .django import BaseManagePy


class BaseDjangoServerTask(BaseManagePy):

    def create_dependecies(self):
        self.add_dependency(RunBefore(Develop()))
        self.add_dependency(AlwaysRebuild())


class Runserver(BaseDjangoServerTask):

    def build(self):
        try:
            self.manage('runserver')
        except (CommandAborted, CommandError):
            pass


class Tests(BaseDjangoServerTask):

    def build(self):
        cmd = " ".join('"%s"' % x.strip().replace('"', r'\"')
                       for x in sys.argv[1:])
        try:
            self.pytest(cmd)
        except (CommandAborted, CommandError):
            pass


class Manage(BaseDjangoServerTask):

    def manage(self, cmd, *args, **kwargs):
        kwargs['shell'] = True
        kwargs['cwd'] = self.paths['package']['main']
        cmd = 'manage.py ' + cmd
        return self.python(
            cmd,
            *args,
            **kwargs
        )

    def build(self):
        cmd = " ".join('"%s"' % x.strip().replace('"', r'\"')
                       for x in sys.argv[1:])
        try:
            self.manage(cmd)
        except (CommandAborted, CommandError):
            pass


class Coverage(BaseDjangoServerTask):

    def build(self):
        try:
            self.pytest(
                (
                    '--junitxml=/home/socek/projects/rejoiner/test-reports/django.xml'
                    ' --cov=app --cov=debug --cov-config=.coveragerc --cov-report=html'
                ),
                shell=True
            )
            print('')
            print('')
            print('')
        except (CommandAborted, CommandError):
            pass


class Shell(BaseDjangoServerTask):

    def build(self):
        try:
            self.manage('shell')
        except (CommandAborted, CommandError):
            pass
