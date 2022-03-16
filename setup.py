import atexit

import pip
from setuptools import setup
from setuptools.command.install import install

pre_deps = [
]

post_deps = [
]

def _pre_install():
    for dep in pre_deps:
        pip.main(['install', '-I', dep, '--upgrade'])

def _post_install():
    for dep in post_deps:
        pip.main(['install', '-I', dep, '--upgrade'])

class Install(install):
    def __init__(self, *args, **kwargs):
        _pre_install()
        super(Install, self).__init__(*args, **kwargs)
        atexit.register(_post_install)

setup(
    name='referral_program_api',
    version='0.0.1',
    description='Referral Program API',
    author='Miftakhul A',
    author_email='',
    url='',
    install_requires=[
        'psycopg2-binary==2.9.1',
        'sqlalchemy==1.4.20',
        'alembic==1.6.5',
        'marshmallow==3.9.1',
        'requests==2.25.0',
        'pycryptodome==3.10.1',
        'gunicorn==20.1.0',
        'flask==2.0.1',
        'pyjwt==1.7.1',
        'alchemy-mock==0.4.3',
        'faker==8.16.0'
    ],
    cmdclass={'install': Install}
)
