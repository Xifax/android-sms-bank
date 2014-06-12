Android SMS bank web frontend
-----------------------------

## About directory structure:

        smsbank
        |= fabfile    <-- Fabric runtime files
        |= requirements    <-- Python virtualenv requirements
        |
        |= references
        |   |= conf    <-- Server related configuration files
        |   \= docs    <-- Docs about the project
        |
        |= etc    <-- Mostly front-end files.
        |   |= test    <--  Javascript unit tests.
        |   |= app    <-- Project-wise static files. Contains styles, scripts,
        images, fonts sub-directories
        |   |= templates    <-- Project-wise Django templates
        |   \= uploads    <-- User-uploaded content (`MEDIA_ROOT`)
        |
        \= smsbank
            |= spec    <-- Environment-specific Django settings and WSGI applications
            |= my    <-- Custom project information. See below for details
            |= common    <-- A special app which injects project-wise functionalities. See below for details
            |= apps    <-- Apps created by you (Run `django-admin.py startapp <your_app_name>` here)
            \= utils    <-- Utilities modules written by you

## Details of some directories:

    smsbank/smsbank/my/

Should contain secret keys, local settings and so on.
These files are for soft-linking in other places.


    smsbank/smsbank/common/

This directory holds a special Django app which injects project-wise
functionalities written by you.

Common usage:

* Management commands
* Template tags
* Templates for overriding other apps (such as the `admin` app)
* Static contents for overriding other apps (such as the `admin` app)
* Contributed translations (via a python file which contains strings to be translated, e.g. trans.py)
* Project wise unit tests

Put this app in the first element of INSTALLED_APPS so that it takes priority
for processing, like this:

```python
INSTALLED_APPS = (
    'smsbank.common',  # <-- Put it here to override `admin` app's template and static files
    'django.contrib.admin',
    'django.contrib.auth',
    ...
)
```
