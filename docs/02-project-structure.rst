.. _project-structure-label:

=================
Project structure
=================

Everybody tends to have a personal preference for the structure of their project,
and I'm no different. After some trial and tweaking I've come up with a
structure I'm quite happy with.



Setting up the project
======================

First, activate the ``django-foobar`` environment if it's not already active. Next we need to install
Django itself into the new environment.

.. code-block:: none

    ~$ workon django-foobar
    (django-foobar):~$ pip install Django


Creating the working directory
------------------------------

    .. code-block:: none

        (django-foobar):~$ mkdir django-foobar
        (django-foobar):~$ cd django-foobar

    .. note::

        Whenever referring to the "working directory" in this guide, I'm referring to this. In other
        words, the top level directory for the entire project.

Set up the testing environment
------------------------------

    `TDD <https://en.wikipedia.org/wiki/Test-driven_development>`_ is a good practice to follow when
    writing 3rd party Django modules. If you want your library to succeed and people to use and contribute
    to it, you'll need a good test suite! We are going to use the ``django-admin`` command to create a
    testing environment for our module. Inside the project directory enter the following command (make sure
    you include the ``.`` on the end!)

    .. code-block:: none

        (django-foobar):~/django-foobar$ django-admin startproject tests .

    Now, you might be wondering why we are using the ``django-admin startproject`` command to create
    the testing environment, and not the module we are going to develop. That's because we don't want
    to distribute an entire Django project. We only want to distribute the ``django-foobar`` library
    we're going to write, but we want to make sure it can run in an existing Django project. That's what
    we're going to use the ``tests`` project for!


Module source code
------------------

    Next, we need to create a directory containing the source code for our ``django-foobar`` module. Python
    modules uses underscores instead of dashes in their package names, so the python module will be
    called ``django_foobar``. Either create a directory called ``django_foobar`` with an
    ``__init__.py`` file inside it, or just use the ``django-admin`` command to create a new app.

    .. code-block:: none

        (django-foobar):~/django-foobar$ django-admin startapp django_foobar


Documentation
-------------

    Obviously, we need to document our library. This can be done with various tools, but I like to
    use `Sphinx <http://sphinx-doc.org/>`_. That's the very same tool I've used to write this guide,
    so you know how the documentation will look like =)

    .. code-block:: none

        (django-foobar):~/django-foobar$ pip install Sphinx
        ...
        Lots of stuff going on
        ...
        (django-foobar):~/django-foobar$ sphinx-quickstart docs
        Welcome to the Sphinx 1.3.1 quickstart utility.

        Please enter values for the following settings (just press Enter to
        accept a default value, if one is given in brackets).

        Selected root path: docs

        You have two options for placing the build directory for Sphinx output.
        Either, you use a directory "_build" within the root path, or you separate
        "source" and "build" directories within the root path.
        > Separate source and build directories (y/n) [n]:


    Just hit ``<enter>`` for default values and write some sensible values for those which requires
    input (like project name, author, and so on).


Requirements
------------

    The ``requirements.txt`` file contains all the libraries required for *developing* the module.
    Requirements for *installing* the module will be in another file called ``setup.py``. Don't pay any
    attention to that for now, we'll create it later in this guide.

    Create the ``requirements.txt`` file in your project root.

    .. code-block:: none

        (django-foobar):~/django-foobar$ touch requirements.txt


    Open the file in a text editor and add a few dependencies. It's quite common to lock dependency
    versions when developing a library, but it's not strictly required. If no version lock is found,
    ``pip`` will install the most recent version.

    .. code-block:: none

        Django==1.8.4
        Sphinx==1.3.1
        sphinx-rtd-theme==0.1.8

    We'll be adding more to this file as we go along.


README.txt and LICENSE.txt
--------------------------

    Create a README.txt and LICENSE.txt file. The README.txt file should contain a brief description
    of the module, as well as other useful information. In case you decide to upload your project to
    a source hosting service such as Github or Bitbucket, the content of this file will be displayed
    on the front page of your repository.

    The LICENSE.txt file is not so important right now, but if you are going to distribute the source
    code, it is good practice to slap a license on it. There are many licenses to choose from, but I
    tend to choose a fairly liberal license such as the
    `MIT License <http://opensource.org/licenses/MIT>`_ or the
    `Apache v2.0 License <http://www.apache.org/licenses/LICENSE-2.0>`_. There is no single license
    which match every project, so choosing the right one depends a lot on the project type and use case.
    Also, if you work for a company, they might have their own rules and restrictions for licensing
    source code, so make sure to pay attention to that as well ;)

    You don't have to decide now, just leave the LICENSE.txt file there as a reminder.
    Check out `this link <http://opensource.org/licenses/>`_ for a list of popular open source licenses.

    .. code-block:: none

        (django-foobar):~/django-foobar$ touch README.txt LICENSE.txt

Source control
--------------

    This step is optional, but you probably want to add source control to your project. There is
    different source control tools, but I like Git, so let's initialize a git repository in the
    project root.

    .. code-block:: none

        (django-foobar):~/django-foobar$ git init
        Initialized empty Git repository in /path/to/your/project/.git/

    Not all files in your project should go into source control. Add a ``.gitignore`` file in order
    to tell Git which files or directories to ignore.

    .. code-block:: none

        (django-foobar):~/django-foobar$ touch .gitignore

    Open the .gitignore file in your favorite text editor and paste the following lines:

    .. code-block:: none

        __pycache__/
        *.py[cod]

        build/
        dist/
        sdist/
        .eggs/
        *.egg-info/


        # Unit test / coverage reports
        htmlcov/
        .tox/
        .coverage
        .cache
        nosetests.xml
        coverage.xml

        # Translations
        *.mo
        *.pot

        # Django stuff:
        *.log
        *.db

        # Sphinx documentation
        docs/_build/


    You can add stuff to this file as you go along in case there's something we have missed.

    Now is a good time to commit your work!

    .. code-block:: none

        (django-foobar):~/django-foobar$ git commit -a -m "initial commit"

Github
......

If you don't have a `Github <https://github.com/>`_ account, go ahead and create one now!

#. Create an empty repository for your code

    .. image:: _static/new_repository.png

    Fill in some details about your project, but make it public.



There. We now have a pretty good project structure for developing the amazing ``django-foobar`` module.
It should look something like this:

    .. code-block:: none

        ├── LICENSE.txt
        ├── README.rst
        ├── django_foobar
        │   ├── __init__.py
        │   ├── admin.py
        │   ├── migrations
        │   │   └── __init__.py
        │   ├── models.py
        │   ├── tests.py
        │   └── views.py
        ├── docs
        │   ├── Makefile
        │   ├── _build
        │   ├── _static
        │   ├── _templates
        │   ├── conf.py
        │   ├── index.rst
        │   └── make.bat
        ├── manage.py
        ├── requirements.txt
        ├── .gitignore
        └── tests
            ├── __init__.py
            ├── settings.py
            ├── urls.py
            └── wsgi.py


Write some code
===============

Now, this is not a guide for writing Django code, so we'll just write a small testable unit in our
``django_foobar`` module.

Open the ``django_foobar/views.py`` file in the and write in the following code.

    .. code-block:: python

        # -*- coding: utf-8 -*-

        from __future__ import absolute_import, unicode_literals

        from django.http import HttpResponse
        from django.views.generic import View


        class DeepThoughtView(View):

            def get(self, request):
                return HttpResponse(42)




Next, open the ``tests/settings.py`` file and add your module to ``INSTALLED_APPS``

    .. code-block:: python

        INSTALLED_APPS = (
            <snip>

            'django_foobar',
        )


Finally, hook up the view in the ``tests/urls.py`` file.

    .. code-block:: python

        from django_foobar.views import DeepThoughtView

        urlpatterns = [
            <snip>
            url(r'^deepthought/$', view=DeepThoughtView.as_view(), name='django_foobar_deepthought'),
        ]
