get_today_hours\(\)
===================

When called, this will return a list of dictionaries containing information
about every dining hall that is open at any time today.

For example:

.. code-block:: python

   [
    {
        "is_open": false,
        "time": "00:42",
        "name": "Erickson Hall",
        "hours": [
            {
                "open": 1100,
                "is_open": false,
                "close": 1400
            },
            {
                "open": 1700,
                "is_open": false,
                "close": 1900
            }
        ],
        "id": "erickson"
    },
    {
        "is_open": false,
        "time": "00:42",
        "name": "Alexander Hall",
        "hours": [
            {
                "open": 1100,
                "is_open": false,
                "close": 1400
            },
            {
                "open": 1700,
                "is_open": false,
                "close": 1900
            }
        ],
        "id": "alexander"
    },

   ...

   ]
