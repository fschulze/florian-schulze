virtualenv = virtualenv

all: bin/stasis

bin/python:
	$(virtualenv) --system-site-packages --clear .
	-clear-setuptools-dependency-links

bin/stasis: bin/python
	bin/pip install docutils
	bin/pip install pyramid_chameleon
	bin/pip install stasis
