import sys


from bael.project.develop import Develop
from baelfire.dependencies import AlwaysRebuild
from baelfire.dependencies import RunBefore
from baelfire.error import CommandAborted
from baelfire.error import CommandError

from .django import BaseManagePy
from baelszeol.django import MigrateSql
from baelszeol.docker import Maildump
from baelszeol.docker import SentryContainer


class BaseDjangoServerTask(BaseManagePy):

    def create_dependecies(self):
        self.add_dependency(RunBefore(Develop()))
        self.add_dependency(AlwaysRebuild())


class Runserver(BaseDjangoServerTask):

    def create_dependecies(self):
        super().create_dependecies()
        self.add_dependency(RunBefore(MigrateSql()))
        self.add_dependency(RunBefore(Maildump()))
        self.add_dependency(RunBefore(SentryContainer()))

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


class Coverage(BaseDjangoServerTask):

    def build(self):
        cmd = " --cov szeol " + " ".join('"%s"' % x.strip().replace('"', r'\"')
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


class Shell(BaseDjangoServerTask):

    def create_dependecies(self):
        super().create_dependecies()
        self.add_dependency(RunBefore(MigrateSql()))

    def build(self):
        try:
            self.manage('shell')
        except (CommandAborted, CommandError):
            pass
