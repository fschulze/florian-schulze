mr.developer 1.3 - Fewer surprises
##################################
:date: 2009-11-15 16:20
:author: Fschulze42
:category: Development, Plone

The last releases of `mr.developer`_ (1.2 and 1.3) reduce the amount of
surprises.

The packages from auto-checkout are now automatically added and removed
from the list of development packages when you switch buildout
configurations. Before you had to run ``develop reset`` and rerun
buildout for that to work. If you have an existing checkout, you may
want to reset it, so that this change is picked up.

The last used buildout configuration is now read directly. That means if
you change source declarations in your buildout configuration, then you
don't have to rerun buildout anymore for mr.developer to pick up those
changes. You still have to run buildout after changing the develop
status of a package, but that's the same as with a plain buildout
without mr.developer.

.. _mr.developer: http://pypi.python.org/pypi/mr.developer
