Example buildout environment
============================

This simple example demonstrates how to wrap Bob-based scripts on buildout
environments. This may be useful for homework assignments, tests or as a way to
distribute code to reproduce your publication. In summary, if you need to give
out code to others, we recommend you do it following this template so your code
can be tested, documented and run in an orderly fashion.

Installation
------------

.. note::

  To follow these instructions locally you will need a local copy of this
  package. Start by cloning this project with something like (shell commands 
  are marked with a ``$`` sign)::

    $ git clone --depth=1 https://github.com/idiap/bob.project.example.git
    $ cd bob.project.example
    $ rm -rf .git # you don't need the git directories...

  Alternatively, you can use the github tarball API to download the package::

    $ wget --no-check-certificate https://github.com/idiap/bob.project.example/tarball/master -O- | tar xz 
    $ mv idiap-bob.project* bob.project.example

Installation of the toolkit uses the `buildout <http://www.buildout.org/>`_
build environment. You don't need to understand its inner workings to use this
package. Here is a recipe to get you started::
  
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

Documentation
-------------

To write documentation, use the `Sphinx Document Generator
<http://sphinx.pocoo.org/>`_. A template has been setup for you under the
``docs`` directory. Get familiar with Sphinx and then unleash the writer in
you.

Once you have edited both ``docs/conf.py`` and ``docs/index.rst`` you can run
the document generator executing ``./bin/sphinx``. The system is setup to
generate output at the ``built-docs`` directory. 

For more details and tweaking hints checkout the manual for
`collective.recipe.sphinxbuilder
<http://pypi.python.org/pypi/collective.recipe.sphinxbuilder/>`_.

Unit Tests
----------

Writing unit tests is an important asset on code that needs to run in different
platforms and a great way to make sure all is OK. We have setup a template for
tests under ``example/test.py``. Tests are setup in `buildout`` using the
recipe `pbp.recipe.noserunner
<http://pypi.python.org/pypi/pbp.recipe.noserunner/>`_. A script called
``./bin/tests.py`` will be created which can run anything that resembles a test
on the example package.

Reference
---------

Include your `bibtex` reference to make it easy for others to cite your work
correctly::

  @ARTICLE{joedoe-2012,
    author = {Joe Doe},
    title = {An Example Buildout Package},
     booktitle = {This is Just a Bob Package},
     year = {2012},
  }
