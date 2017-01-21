from morfdict import Factory


class SettingsFactory(object):
    ENDPOINTS = {
        'uwsgi': [('app', True), ('default', True), ('local', False)],
    }

    def __init__(self):
        self.module = 'szeol'
        self.settings = {}
        self.paths = {}

    def get_for(self, endpoint):
        files = self.ENDPOINTS[endpoint]
        return self._generate_settings(files)

    def _generate_settings(self, files=None):
        files = files or []
        factory = Factory(self.module)
        settings, paths = factory.make_settings(
            settings=self.settings,
            paths=self.paths,
            additional_modules=files,
        )
        settings['paths'] = paths
        return settings, paths

factory = SettingsFactory()
for _settings in factory.get_for('uwsgi'):
    for name, value in _settings.items():
        locals()[name] = value
