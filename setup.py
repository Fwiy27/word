from setuptools import setup, find_packages

setup(
    name = 'word',
    version = '1.0.5',
    description = "Fun Word Finder",
    long_description = open('README.md').read(),
    author = 'Landon Migawa',
    author_email = 'landonmigawa27@gmail.com',
    maintainer = 'Landon Migawa',
    maintainer_email = 'landonmigawa27@gmail.com',
    packages = find_packages(include = ['word']),
    package_data={'word': ['*.txt']},
    python_requires = ">=3.7"
)
