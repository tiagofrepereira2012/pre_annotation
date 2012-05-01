Example buildout environment
============================

This simple example demonstrates how to wrap Bob-based scripts on buildout
environments. This may be useful for homework assignments, tests or as a way to
distribute code to reproduce your publication.

Installation
------------

.. note::

  To follow these instructions locally you will need a local copy of this
  package. Start by cloning this project with something like::

    $ git clone --depth=1 https://github.com/idiap/bob.project.example.git
    $ cd bob.project.example
    $ rm -rf .git # you don't need the git directories...

  Alternatively, you can use the github tarball API to download the package::

    $ wget --no-check-certificate https://github.com/idiap/bob.project.example/tarball/master -O- | tar xz 
    $ mv idiap-bob.project* bob.project.example

Installation of the toolkit uses the `buildout <http://www.buildout.org/>`_
build environment. You don't need to understand its inner workings to use this
package. Here is a recipe to get you started (shell commands are marked with a
``$`` signal)::
  
  $ python bootstrap.py
  $ ./bin/buildout

These 2 commands should download and install all non-installed dependencies and
get you a fully operational test and development environment.

.. note::

  The python shell used in the first line of the previous command set
  determines the python interpreter that will be used for all scripts developed
  inside this package. Because this package makes use of `Bob
  <http://idiap.github.com/bob>`_, you must make sure that the ``bootstrap.py``
  script is called with the **same** interpreter used to build Bob, or
  unexpected problems might occur.

  If Bob is installed by the administrator of your system, it is safe to
  consider it uses the default python interpreter. In this case, the above 3
  command lines should work as expected.

Usage
-----

Please refer to the documentation inside the ``doc`` directory of this package
for further instructions on the functionality available inside this package.

Reference
---------

Include your `bibtex` reference to make it easy for others to cite your work
correctly:

  @ARTICLE{joedoe-2012,
    author = {Joe Doe},
    title = {An Example Buildout Package},
     booktitle = {This is Just a Bob Package},
     year = {2012},
  }
