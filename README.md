# Info
Web interface for the [ledypi](https://github.com/nicofirst1/ledypi), please refer to the latter.

To install the necessary dependencies use:

```pip install -r requirements.txt```

## Usage

Run on the default port (8000) with:
```python3 manage.py start```

You'll find the webpage on [localhost](http://127.0.0.1:8000)

### Custom ports
You can also specify an ip and a port with:

```python3 manage.py start IP:PORT```


to pass any addition arguments set them as environmental variables before running:
 
```export var_name="My value"```

 
# todo
- fix readme []
- fix double call in get_form_values []
- fix compatibility with controller []
- fix android app []
- []