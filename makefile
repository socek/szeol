venv_szeol/bin/python: venv_szeol setup.py
	./venv_szeol/bin/python setup.py develop
	@touch venv_szeol/bin/python

venv_szeol:
	virtualenv3 venv_szeol
