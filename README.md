# PyCli

A simple and easy-to-use Python3 API client using the native python http library

<br />
<br />


## Requirements
---

### Python
```
Python3 is needed to run this project locally
pip is needed to import this project
```

<br />
<br />

## Importing
---

### Installing
```
pip install git+https://github.com/jake-young-dev/PyCli.git#egg=PyCli
```

### Usage
```
from PyCli.client import get, post

status, body = get(https://www.google.com) 

Port can be supplied as second argument if needed.

status, body = get('http://localhost/, 3000)
```