.. _working-environment-label:

===================
Working environment
===================

When working on a new project it will probably have different requirements than your previous projects.

Some reasons might include:
    #. Required libraries probably differs
    #. Same libraries, but different or incompatible versions
    #. You shouldn't pollute your system with libraries only required for a single
       project.
    #. It's easy to fix in case you screw up something

There are many solutions to this, the most popular includes:
    #. virtualenv
    #. pyenv
    #. Vagrant

Each of these have their own strength and weaknesses, but I usually goes for ``virtualenv`` with a wrapper
library called ``virtualenvwrapper``. I think it works quite good, so I'm going to use it in this
guide as well.


Installing virtualenv and virtualenvwrapper
-------------------------------------------

Virtualenv creates a new python "distribution" in its own directory. All required python libraries will
be installed in this directory as well, instead of in the operating systems python environment.

Installing is easy. First you need ``pip`` installed. The ``pip`` command is available in most
recent python installs by default. We'll install the ``virtualenv`` and ``virtualenvwrapper`` libraries in
our system environment, because it need to have access to the system installed python distribution in order
to make copies of it.

    .. code-block:: none

        ~$ sudo pip install virtualenvwrapper

The above command will install both ``virtualenv`` and the ``virtualenvwrapper`` which gives us an easy
cli for managing our virtual environments.

The ``virtualenvwrapper`` uses an environment variable called ``WORKON_HOME``, which defaults to
``~/.virtualenvs``. All the virtual environments created are placed in this directory. You can of course
override the ``WORKON_HOME`` variable if you choose to, but I think it's a good place to store my
virtual environments.


Creating a virtual environment for the project
----------------------------------------------

We are now ready to create a new and shiny environment for our project. The following statement is probably
quite opinionated, but it's my guide, so here it comes ;)

**All new python projects should be written using the most recent Python version (3.4 at the time of writing)!**

Of course, there are exceptions to this rule, but I believe that it is better to write in the most recent
version, and use the ``six`` compatibility layer to add backward support.

That being said, go a head and install Python 3 (the most recent version) if you don't have it installed.


    .. code-block:: none

        (Skip this step if you already have Python3 installed)
        ~$ sudo apt-get install python3


Let's create a new virtual environment called ``django-foobar`` for our project.

    .. code-block:: none

        ~$ mkvirtualenv -p `which python3` django-foobar
        Running virtualenv with interpreter /usr/local/bin/python3
        <snip>
        Installing setuptools, pip...done.
        (django-foobar)~$

You'll see the currently active environment in your prompt. In order to deactivate the environment,
simply enter the command ``deactivate``, and to activate it again you would type in
``workon django-foobar``.

While the virtual environment is active, all packages you install will be installed in the
``$WORKON_HOME/django-foobar/lib/python3.4/site-packages/``, the python interpreter will be
``$WORKON_HOME/django-foobar/bin/python`` and so on. So when you execute the ``python`` command,
it will be the one in your active environment, not your system python.

Good stuff!
