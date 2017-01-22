from subprocess import PIPE
from subprocess import Popen

from baelfire.dependencies import Dependency
from baelfire.task import Task


class IsNotRunning(Dependency):

    def __init__(self, daemon_name):
        super().__init__()
        self.daemon_name = daemon_name

    def should_build(self):
        return not SystemCtlWrapper(self.daemon_name).is_active()


class SystemCtlWrapper(object):

    def __init__(self, name):
        self.name = name

    def is_active(self):
        spp = Popen(
            ['systemctl is-active ' + self.name],
            shell=True,
            stdout=PIPE,
            stderr=PIPE,
        )
        return spp.stdout.read().strip() == b'active'

    def start(self):
        spp = Popen(
            ['sudo systemctl start ' + self.name],
            shell=True,
            stdout=PIPE,
            stderr=PIPE,
        )
        if spp.wait() != 0:
            raise RuntimeError(spp.stderr.read())


class DaemonTask(Task):

    def create_dependecies(self):
        self.add_dependency(IsNotRunning(self.daemon_name))

    def build(self):
        SystemCtlWrapper(self.daemon_name).start()
