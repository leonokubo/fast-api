# Test FAST API

- PRE
```sh
pyenv shell 3.9.7
eval "$(pyenv init --path)"
pip install pipenvpyen  
```
<br>

- VENV 3.9
```
python -m venv .venv
```

- RUN
```
- uvicorn main:app --reload
```
<br>

-- TREE
```tree
├── app
│   ├── __init__.py
│   ├── main.py
│   ├── dependencies.py
│   └── routers
│   │   ├── __init__.py
│   │   ├── items.py
│   │   └── users.py
│   └── internal
│       ├── __init__.py
│       └── admin.py
```
