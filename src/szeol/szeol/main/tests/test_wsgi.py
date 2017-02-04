from szeol.wsgi import application


# just a sanity check
def test_wsgi():
    assert application
