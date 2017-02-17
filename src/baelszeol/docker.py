from baelfire.dependencies.task import RunBefore

from baelszeol.lib.docker import ContainerTask
from baelszeol.lib.docker import CreateVolume


class PostgresVolume(CreateVolume):
    service_name = 'postgres'
    volume_name = 'psqldb'


class PostgresContainer(ContainerTask):
    service_name = 'postgres'

    def create_dependecies(self):
        super().create_dependecies()
        self.add_dependency(RunBefore(PostgresVolume()))


class Maildump(ContainerTask):
    service_name = 'maildump'


class SentryVolume(CreateVolume):
    service_name = 'sentry'
    volume_name = 'sentrydb'

    def create_dependecies(self):
        super().create_dependecies()
        self.add_dependency(RunBefore(RedisContainer()))

    def build(self):
        super().build()
        self.docker.run('sentry upgrade')


class RedisVolume(CreateVolume):
    service_name = 'redis'
    volume_name = 'redisdb'


class RedisContainer(ContainerTask):
    service_name = 'redis'

    def create_dependecies(self):
        super().create_dependecies()
        self.add_dependency(RunBefore(RedisVolume()))


class SentryContainer(ContainerTask):
    service_name = 'sentry'

    def create_dependecies(self):
        super().create_dependecies()
        self.add_dependency(RunBefore(SentryVolume()))
        self.add_dependency(RunBefore(RedisContainer()))

    def build(self):
        self.docker.run('sentry run cron', True)
        self.docker.run('sentry run worker', True)
        super().build()
