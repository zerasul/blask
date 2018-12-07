from setuptools import setup, find_packages
from pathlib import Path

info_file = Path(__file__).resolve().parents[0] / 'README.md'
with info_file.open() as f:
    long_desc = f.read()

setup(
    name='Blask',
    version='0.1.1b6',
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
        'pytest-cov',
        'pylint'
    ]
)
