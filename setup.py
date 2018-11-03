from setuptools import setup, find_packages
from pathlib import Path

currdir = Path(__file__).resolve().parents[0]
file_to_open = 'README.md'
with open(currdir / file_to_open) as f:
    long_desc = f.read()
#long_rst_desc = convert(long_desc)

setup(
    name='Blask',
    version='0.1.1b1',
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
    entry_points='''
        [console_scripts]
        blaskcli=Blask.blaskcli:blaskcli
    ''',
    long_description=long_desc,
    long_description_content_type='text/markdown',
    python_requires='>=3',
    install_requires=[
          'flask',
          'markdown',
          'Pygments',
          'click'
    ],
    test_requires=[
        'pytest',
        'pytest-cov'
    ]
)
