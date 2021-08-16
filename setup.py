from setuptools import setup

setup(
   name='Time Machine - Mail',
   version='0.1.0',
   author='Cristian Figueroa',
   author_email='cristianrfr@gmail.com',
   package_dir={'': 'src'},
   packages=['timemachine', 'timemachine.mail'],
   scripts=['src/timemachine/mail/main.py'],
   description='Time Machine For Storing IMAP State',
   long_description=open('README.md').read(),
   install_requires=[
       "pyyaml",
       "pytz",
   ],
)
