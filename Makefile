# Makefile for the hello-github-demo project

# Install dependencies
install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

# Run tests
test:
	PYTHONPATH=. pytest

# Run tests with coverage
coverage:
	PYTHONPATH=. pytest --cov=src

# Lint the code
lint:
	pylint src/

# Build Docker image
build:
	docker build -t hello-github-demo .

# Run Docker container
docker-run:
	docker run -it -p 8081:8080 hello-github-demo

# Run the main application
run:
	python src/greet.py

# Clean up temporary files
clean:
	find . -type f -name '*.pyc' -delete
	find . -type d -name '__pycache__' -delete
	rm -rf .pytest_cache