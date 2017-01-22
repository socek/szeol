from baelfire.dependencies import PidIsNotRunning
from baelfire.task import SubprocessTask


class Maildump(SubprocessTask):

    def phase_settings(self):
        super().phase_settings()
        self.paths.set_path('pid:maildump', 'tasks', 'maildump.pid')

    def create_dependecies(self):
        self.add_dependency(PidIsNotRunning(pid_file_name='pid:maildump'))

    def build(self):
        self.popen(
            ['maildump -p %(pid:maildump)s' % self.paths],
        )
