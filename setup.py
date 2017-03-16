#!/usr/bin/env python3
# coding: utf-8

from __future__ import print_function

from setuptools import setup

setup_args = dict(
    name                = 'condamagic',
    py_modules          = ['condamagic'],
    version             = '0.2.0',
    description         = "%condamagic for IPython",
    long_description    = "`%conda install` will run in IPython's env, even if it is not activated.",
    author              = "Min RK",
    author_email        = "benjaminrk@gmail.com",
    url                 = "https://github.com/minrk/condamagic",
    license             = "BSD",
    platforms           = "Linux, Mac OS X",
    keywords            = ['Interactive', 'Interpreter', 'Shell'],
    classifiers         = [
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ],
)

#---------------------------------------------------------------------------
# setup
#---------------------------------------------------------------------------

def main():
    setup(**setup_args)

if __name__ == '__main__':
    main()
