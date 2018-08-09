from setuptools import find_packages
import distutils.command.build
from distutils.core import setup
import install_tools

DESC = 'An extension of py-aiger providing advanced tool support, including SAT and QBF solvers.'

# we need to redefine the build command to
# be able to download and compile solvers
class build(distutils.command.build.build):
    '''
    custom build class to enable compilation of CADET. Adapted from python-sat
    '''
    def run(self):
        # download and compile cadet
        install_tools.install(
            'cadet',
            'https://github.com/MarkusRabe/cadet/archive/v2.5.tar.gz')
        
        # now, do standard build
        distutils.command.build.build.run(self)

setup(
    name='py-aiger-analysis',
    version='0.1',
    description=DESC,
    url='http://github.com/mvcisback/py-aiger-analysis',
    author='Marcell Vazquez-Chanlatte',
    author_email='marcell.vc@eecs.berkeley.edu',
    license='MIT',
    install_requires=[
        'py-aiger',
        'py-aiger-bv',
        'funcy',
        'dd',
        'python-sat',
    ],
    cmdclass={'build': build},
    packages=find_packages(),
)
