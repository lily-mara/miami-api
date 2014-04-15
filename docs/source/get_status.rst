get_status\(location\)
======================

When called, this function will return a dictionary containing information
about the given location. For example:

.. code-block:: python

   {
    "is_open": false,
    "time": "00:46",
    "name": "Tower To Go",
    "hours": [
        {
            "open": 1900,
            "is_open": false,
            "close": 2359
        }
    ],
    "id": "tower_to_go"
    }
