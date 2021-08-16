from setuptools import setup, find_packages

setup(
    name='Time Machine - Mail',
    version='0.1.0',
    author='Cristian Figueroa',
    author_email='cristianrfr@gmail.com',
    package_dir={'': 'src'},
    include_package_data=True,
    packages=find_packages(where="src"),
    scripts=['scripts/backup.py', 'scripts/query_server.py'],
    description='Time Machine For Storing IMAP State',
    long_description=open('README.md').read(),
    install_requires=[
       "pyyaml",
       "pytz",
    ],
    classifiers=[
        "Programming Language :: Python :: 3.9"
    ]
)
