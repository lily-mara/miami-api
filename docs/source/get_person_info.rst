get_person_info\(name\)
============

Returns information about the given person. Currently quite limited and slow,
as it parses html from Miami's quite slow directory lookup page.

.. code-block:: python

    >>> from miami_api import *
    >>> get_person_info('Sally Student')
    {
        'name': 'Student, Sally M.',
        'id': 'studentsm',
        'email': 'studentsm@miamioh.edu'
    }
