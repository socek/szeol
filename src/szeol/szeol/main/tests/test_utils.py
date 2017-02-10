from freezegun import freeze_time
from datetime import datetime

from szeol.main.utils import default_now


def test_default_now():
    now = datetime.utcnow()
    with freeze_time(now):
        assert default_now() == now
