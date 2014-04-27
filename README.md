Miami API
=========

This is (going to be) a simple RESTful API written in Python that provides
information about Miami University.

Currently, there are only a few useful functions.

```python
from miami_api import *

#returns the hours for `location` on current weekday
get_status(location)

#returns list containing all currently open dining locations and their hours
get_open()

#returns hours for all dining locations open today
get_today_hours()

#returns information on the given student
get_person_info(name)

```

documentation is hosted on [ReadTheDocs](http://miami-api.rtfd.org)
