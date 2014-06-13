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
        |   |= app    <-- Project-wise static files.
        images
        |   |= templates    <-- Project-wise Django templates.
        |   \= uploads    <-- User-uploaded content (`MEDIA_ROOT`)
        |
        \= smsbank
            |= spec    <-- Environment-specific settings, WSGI applications
            |= my    <-- Custom project information.
            |= common    <-- Project-wise functionalities.
            details
            |= apps    <-- Additional web modules.
            \= utils    <-- Additional utilities.

## Details of some directories:

    smsbank/smsbank/my/

Should contain secret keys, local settings and so on.
These files are for soft-linking in `smsbank/spec`.
