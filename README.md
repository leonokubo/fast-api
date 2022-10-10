# Test FAST API

```
    Service Short URL (MVP)
```

- DOC
```
    http://127.0.0.1:8080/docs
```

- Pre
```sh
pyenv shell 3.9.7
eval "$(pyenv init --path)"
docker-compose up -d
```
<br>

- Venv 3.9
```
python -m venv .venv
. .venv/bin/activate
```

- Create base
- ```
make create_base.py  
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
	├── application
	│   └── __init__.py
	├── dependencies.py
	├── domain
	│   ├── entity
	│   │   ├── __init__.py
	│   │   └── short_url.py
	│   └── __init__.py
	├── handler
	│   ├── __init__.py
	│   └── short_url
	│       └── __init__.py
	├── infra
	│   ├── cache
	│   │   ├── fastapi_cache.py
	│   │   └── __init__.py
	│   ├── config
	│   │   └── __init__.py
	│   ├── __init__.py
	│   └── repository
	│       ├── __init__.py
	│       └── short_url.py
	├── __init__.py
	└── router
		├── __init__.py
		└── short_url.py
```
