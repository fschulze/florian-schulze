A buildout to tame the snake pit
################################
:date: 2008-12-14 16:16
:author: Fschulze42
:category: Development, Plone
:tags: buildout, Plone, python

After reading `philiKON's post about building Python 2.5 with readline
on Mac OS X Leopard`_ and getting my new MacBook Pro, I decided to
create a buildout which does all the hard work and is reproducible when
I managed to mess up the Python installation.

If you know how to run a buildout and don't want to know any of the
details, then just fetch it
from \ `http://svn.plone.org/svn/collective/buildout/python-macosx/`_.
It will build `Python`_ 2.4, 2.5, 2.6 and 3.0. For the 2.x Python's it
will also create a `virtualenv`_ and install `zc.buildout`_ and `PIL`_
into it. A script called ``'install-links'`` will be created, which will
link the main scripts and binaries into ``/opt/local/bin`` when run.

The biggest issue I ran into while creating the buildout was getting the
readline library properly picked up by the configuration part of the
Python build. The only way I got it working, was to use a common
installation prefix for readline and Python.

The buildout does several things:

-  It builds Python 2.4-2.6 and Python 3.0 with readline support
-  It creates virtualenv's for the 2.x Python's
-  It installs zc.buildout and PIL into those virtualenv's (You should
   make sure that any dependencies for PIL are already installed, on
   Leopard with just XCode, you need to install the jpeg library. I use
   `MacPorts`_ for that, with the following command:
   ``sudo port install jpeg``.)
-  It creates a script which links the main scripts and binaries into
   ``/opt/local/bin``

You can easily customize the destination of the links by using a custom
cfg file which extends the main buildout.cfg one like this::

    [buildout]
    extends = buildout.cfg

    [install-links]
    prefix = /opt/local

The ``/bin`` will be appended by default.

.. _philiKON's post about building Python 2.5 with readline on Mac OS X Leopard: http://philikon.wordpress.com/2008/10/31/readline-and-python-25-on-os-x/
.. _`http://svn.plone.org/svn/collective/buildout/python-macosx/`: http://svn.plone.org/svn/collective/buildout/python-macosx/
.. _Python: http://www.python.org
.. _virtualenv: http://pypi.python.org/pypi/virtualenv
.. _zc.buildout: http://pypi.python.org/pypi/zc.buildout
.. _PIL: http://www.pythonware.com/products/pil/
.. _MacPorts: http://www.macports.org/
