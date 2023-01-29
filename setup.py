# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

long_desc = open('README.rst').read()

requires = ['Sphinx>=5.0']

setup(
    name='sphinxcontrib-codeblock-callouts',
    version='1.0.0',
    url='https://github.com/tk0miya/sphinxcontrib-codeblock-callouts',
    license='BSD',
    author='Takeshi KOMIYA',
    author_email='i.tkomiya@gmail.com',
    description='Sphinx extension to allow to mark "callouts" for code-blocks up',
    long_description=long_desc,
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Framework :: Sphinx :: Extension',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Documentation',
        'Topic :: Documentation :: Sphinx',
    ],
    platforms='any',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires,
    namespace_packages=['sphinxcontrib'],
)
