from .factory import SettingsFactory

factory = SettingsFactory()
factory.populate_for('uwsgi', globals())
