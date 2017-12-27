from setuptools import setup

setup(
    name='day of code',
    description='Day of code katas.',
    package_dir={'': 'katas'},
    author='Darren Haynes',
    author_email='darrenhaynes@zoho.com',
    py_modules=[],
    install_requires=[],
    extras_require={
        'testing': ['pytest', 'pytest-cov', 'pytest-watch', 'tox'],
        'development': ['ipython']
    },
    entry_points={
        'console_scripts': {
        }
    }
)
