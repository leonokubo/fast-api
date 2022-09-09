# Test FAST API

- Pre
```sh
pyenv shell 3.9.7
eval "$(pyenv init --path)"
pip install pipenvpyen  
```
<br>

- Venv 3.9
```
python -m venv .venv
```

- Run
```
- uvicorn main:app --reload
```
<br>

-- Tree
```tree
├── main.py          # "main" module, e.g. import app.main
├── app                  # "app" is a Python package
│   ├── __init__.py      # this file makes "app" a "Python package"
│   ├── dependencies.py  # "dependencies" module, e.g. import app.dependencies
│   └── routers          # "routers" is a "Python subpackage"
│   │   ├── __init__.py  # makes "routers" a "Python subpackage"
│   │   ├── items.py     # "items" submodule, e.g. import app.routers.items
│   └── internal         # "internal" is a "Python subpackage"
│       ├── __init__.py  # makes "internal" a "Python subpackage"
│       └── admin.py     # "admin" submodule, e.g. import app.internal.admin
```
