Getting Started
===============

When you first download the repo, there are four python files included:

.. code-block:: none

   test.py
   miami_api.py
   server.py
   html_functions.py

- ``test.py`` simply informs you if you have the required modules installed.
  When run, this will either give instructions on how to install the Tornado
  web framework, or inform the user that the requirement is already met.

- ``miami_api.py`` holds the functions that are used for the API calls by the
  web server. This can also be used by itself as an API independent of the
  server. This file will not do anything if run.

- ``server.py`` holds the logic for the web server that hosts the RESTful API
  and the dynamic homepage. When run, this will not show any output, and will
  just begin hosting a server on port ``5000``.

- ``html_functions.py`` holds some functions that make the HTML templates
  cleaner. Tried to keep as much logic as possible out of them. This file will
  not do anything if run.


API Calls:
^^^^^^^^^^

There are three main API calls that this provides:

.. toctree::
   :maxdepth: 2

   get_open
   get_today_hours
   get_status
