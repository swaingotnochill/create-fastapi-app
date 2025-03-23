freeze:
	uv pip freeze > requirements-lock.txt

install:
	uv pip install -e .

uninstall:
	uv pip uninstall create-fastapi-app 

test:
	create-fastapi-app demo-app
