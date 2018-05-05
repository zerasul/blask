from setuptools import setup, find_packages
from os import path
from m2r import convert


currdir = path.abspath(path.dirname(__file__))
with open(path.join(currdir, 'README.md')) as f:
    long_desc = f.read()
long_rst_desc = convert(long_desc)
setup(
    name='Blask',
    version='0.1.0b8',
    packages=find_packages(exclude=['tests']),
    url='https://getblask.com',
    license='GPL 3.0',
    author='zerasul',
    author_email='zerasul@gmail.com',
    description='A simple Blog engine using Flask and Markdown.',
    classifiers=[
       'Development Status :: 4 - Beta',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content :: News/Diary',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    long_description=long_rst_desc,
    python_requires='>=3',
    install_requires=[
          'flask',
          'markdown',
          'markdown-full-yaml-metadata',
          'Pygments',
          'm2r'
    ],
    test_require=[
        'pytest',
        'pytest-cov'
    ]
)
