from setuptools import setup


setup(
    name='lektor-florian-schulze',
    version='0.1',
    author=u'Florian Schulze',
    author_email='florian.schulze@gmx.net',
    license='MIT',
    install_requires=[
        'python-dateutil'],
    py_modules=['lektor_florian_schulze'],
    entry_points={
        'lektor.plugins': [
            'florian-schulze = lektor_florian_schulze:FlorianSchulzePlugin']})
