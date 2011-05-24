# -*- coding: utf-8 -*-

import sys
import unittest
from distutils.core import setup, Command

class TestCommand(Command):
    user_options = []
    
    def initialize_options(self):
        pass
    
    def finalize_options(self):
        pass
    
    def run(self):
        tests = unittest.TestLoader().discover('mutpy/test', '*_test.py', '.')
        text_runner = unittest.TextTestRunner()
        text_runner.run(tests)
        
if sys.hexversion < 0x3020000:
    print('Mutpy requires Python 3.2 or newer!')
    sys.exit()

setup(name='MutPy',
      version='0.1',
      description='Mutation testing tool for Python 3.x source code.',
      author='Konrad Hałas',
      author_email='hakonrad@gmail.com',
      url='https://bitbucket.org/khalas/mutpy/',
      packages=['mutpy'],
      scripts=['bin/mutpy'],
      cmdclass={'test': TestCommand},
      classifiers=['Programming Language :: Python :: 3.2',
                   'Environment :: Console',
                   'Intended Audience :: Developers',
                   'Topic :: Software Development :: Testing']
     )