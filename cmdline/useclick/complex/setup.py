from setuptools import setup

setup(
    name = "Hello",
    version = '1.0',
    py_modules=['hello'],
    install_requires = [
        'click',
    ],
    entry_points='''
        [console_scripts]
        hello=hello:cli
    '''
)