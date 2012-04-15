from setuptools import setup, find_packages

setup(

    # This is the basic information about your project. Feel free to modify all
    # this before releasing code publicly.
    name='bob.project.example',
    version='0.1',
    description='Example for using Bob inside a buildout project',
    url='http://github.com/idiap/bob.project.example',
    license='LICENSE.txt',
    author='Andre Anjos',
    author_email='andre.anjos@idiap.ch',

    # If you have a better, long description of your package, place it on the
    # 'doc' directory and then hook it here, uncommenting the following line
    #long_description=open('doc/long-description.rst').read(),

    # This line is required for any distutils based packaging.
    packages=find_packages(),

    # This line defines which packages should be installed when you "install"
    # this package. When using "buildout", this refers to "local" installation
    # of the package. So, don't worry. You won't need adminstrative privileges
    # when using buildout.
    #
    # Anyhow, you need to put here the "required" material you will want to run
    # against. Buildout will not bother about python packages that are already
    # installed. It will locally install those python modules which are missing.
    install_requires=[
        #"bob",      # base signal proc./machine learning library

        # here are some more examples you could include:

        #"argparse", # better option parsing
        #"ipython",  # better prompt than the stock python
        #"ipdb",     # better debugging support with syntax highlighting
    ],

    # This entry defines which scripts you will have inside the 'bin' directory
    # once you install the package (or run 'bin/buildout'). The order of each
    # entry under 'console_scripts' is like this:
    #   script-name-at-bin-directory = module.at.your.library:function
    #
    # The module.at.your.library is the python file within your library.
    #
    # In this example we will create a single program that will print the
    # version of bob.
    entry_points={
      'console_scripts': [
        'test.py = example.test:main',
        ],
      },

)
