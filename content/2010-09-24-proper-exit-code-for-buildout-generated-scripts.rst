Proper exit code for buildout generated scripts
###############################################
:date: 2010-09-24 16:30
:author: Fschulze42
:category: Development

I recently ran into the issue that our Hudson installation didn't report
test failures. After digging for a bit, I discovered, that scripts
installed by zc.recipe.egg don't return the exit code for some cases.
There is a bugreport at
`https://bugs.launchpad.net/zc.buildout/+bug/164629`_. In our case the
generated coverage script depended on this and because the sys.exit was
missing, the test failures were masked.

The following is a way to fix this in your buildouts now until it's
fixed in zc.buildout::

    [buildout]
    extensions = buildout.extensionscripts
    extension-scripts =
        ${buildout:directory}/src/buildout-utils.py:patchScriptGeneration

The ``patchScriptGeneration`` function in ``src/buildout-utils.py``
looks like this::

    def patchScriptGeneration(buildout):
        from zc.buildout import easy_install
        if not 'sys.exit(' in easy_install.script_template:
            easy_install.script_template = easy_install.script_template.replace(
                "%(module_name)s.%(attrs)s(%(arguments)s)",
                "sys.exit(%(module_name)s.%(attrs)s(%(arguments)s))")

.. _`https://bugs.launchpad.net/zc.buildout/+bug/164629`: https://bugs.launchpad.net/zc.buildout/+bug/164629
