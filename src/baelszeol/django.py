from os import fwalk
from os.path import getmtime
from os.path import join

from bael.project.virtualenv import BaseVirtualenv
from baelfire.dependencies import Dependency


class UrlsChanged(Dependency):

    def __init__(self, src_name, destination_name):
        super().__init__()
        self.src_name = src_name
        self.destination_name = destination_name

    @property
    def src(self):
        return self.paths[self.src_name]

    @property
    def destination(self):
        return self.paths[self.destination_name]

    def should_build(self):
        try:
            destination_time = getmtime(self.destination)
        except FileNotFoundError:
            return True
        for root, dirs, files, rootfd in fwalk(self.src):
            if 'urls.py' in files:
                urls_path = join(root, 'urls.py')
                if destination_time < getmtime(urls_path):
                    return True
        return False


class BaseManagePy(BaseVirtualenv):

    def manage(self, cmd, *args, **kwargs):
        cmd = 'manage.py ' + cmd
        return self.python(
            cmd,
            cwd=self.paths['package']['main'],
            *args,
            **kwargs
        )

    def pytest(self, command='', *args, **kwargs):
        kwargs['shell'] = True
        kwargs['cwd'] = self.paths['package']['main']
        command = self.paths['exe:pytest'] + ' ' + command
        return self.popen([command], *args, **kwargs)
