# Variables
PYTHON=python3
PIP=pip3
FLASK_APP=app.py
FLASK_ENV=development
HTML_DIR=templates
JS_DIR=static/js

# Target
.PHONY: all
all: install run
    
# Dependencies
.PHONY: install
install:
    $(PIP) install flask openai requests

.PHONY: run
run:
	FLASK_APP=$(FLASK_APP) \
	FLASK_ENV=$(FLASK_ENV) \
	flask run

.PHONY: dev-install
dev-install: install
	$(PIP) install --user pytest flake8 black
	npm install --global terser

# Clean packages and cached files
.PHONY: clean
clean:
	$(PIP) uninstall -y flask openai requests pytest flake8 black
	find . -type f -name '*.pyc' -delete
	find . -type d -name '__pycache__' -delete

# HTML files
.PHONY: minify-html 
minify-html:
	find $(HTML_DIR) -type f -name '*.html' -exec html-minifier --collapse-whitespace --remove-comments --minify-css true --minify-js true -o {} {} \;

# Javascript files (using terser)
.PHONY: minify-js
minify-js:
	find $(JS_DIR) -type f -name '*.js' -exec npx terser {} -o {} --compress --mangle \;