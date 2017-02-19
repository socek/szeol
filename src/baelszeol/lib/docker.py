from subprocess import PIPE
from subprocess import Popen

from baelfire.dependencies import Dependency
from baelfire.dependencies.file import FileDoesNotExists
from baelfire.task import Task


class ContainerIsNotRunning(Dependency):

    def __init__(self, service_name):
        super().__init__()
        self.service_name = service_name

    def should_build(self):
        return not DockerComposeCtlWrapper(self.service_name).is_active()


class DockerComposeCtlWrapper(object):
    prefix = 'szeol'
    _cache = dict()

    def __init__(self, service_name, cwd=None):
        self.service_name = service_name
        self.container_name = '{0}_{1}'.format(
            self.prefix,
            service_name)
        self.cwd = cwd

    def is_active(self):
        if 'ps' not in self._cache:
            spp = Popen(
                ['docker ps'],
                shell=True,
                stdout=PIPE,
                stderr=PIPE,
            )
            self._cache['ps'] = spp.stdout.read().strip()
        return bytes(self.container_name, 'utf8') in self._cache['ps']

    def start(self):
        spp = Popen(
            ['docker-compose up -d ' + self.service_name],
            shell=True,
            stdout=PIPE,
            stderr=PIPE,
            cwd=self.cwd,
        )
        if spp.wait() != 0:
            raise RuntimeError(spp.stderr.read())

    def run(self, cmd, detach=False):
        cmd = 'docker-compose run {0} {1} {2}'.format(
            '-d' if detach else '',
            self.service_name,
            cmd)
        spp = Popen(
            [cmd],
            shell=True,
            cwd=self.cwd,
        )
        if spp.wait() != 0:
            raise RuntimeError('Command return error')

    def create_volume(self, name):
        spp = Popen(
            ['docker volume create --name={0}'.format(name)],
            shell=True,
            stdout=PIPE,
            stderr=PIPE,
            cwd=self.cwd,
        )
        if spp.wait() != 0:
            raise RuntimeError(spp.stderr.read())


class DockerTask(Task):

    @property
    def docker(self):
        if not getattr(self, '_docker', None):
            self._docker = DockerComposeCtlWrapper(
                self.service_name,
                self.paths['docker'])
        return self._docker


class ContainerTask(DockerTask):

    def create_dependecies(self):
        self.add_dependency(ContainerIsNotRunning(self.service_name))

    def build(self):
        self.docker.start()


class CreateVolume(DockerTask):
    volume_name = None

    def create_dependecies(self):
        self.add_dependency(FileDoesNotExists(self.volume_name))

    def build(self):
        self.docker.create_volume(self.volume_name)
