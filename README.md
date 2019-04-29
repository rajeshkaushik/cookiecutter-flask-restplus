Flask RestPlus microservice template
# cookiecutter-flask-restplus

Cookiecutter template for flask restplus microservice including swagger docs, namespaces, test setup and more
## Introduction
This cookie cutter is a very simple boilerplate for starting a REST api using Flask-RestPlus

Features
* Standardise the best practices across python projects
* Quick start of new project
* Organised project structure
* Health-check endpoint
* Test setup
* Test coverage
* Sonar-cube integration details
* Git hooks
* Deployment files:   Docekrfile, wigs.py, gunicorn_config.py
* Pipenv for stable releases

Config option available for
* Basic APIKEY authorization
* New-relic integration
* Custom error response format
{% if cookiecutter.slackclient == 'y' %}
* slack integration for error logs
{% endif %}
* Swagger docs

## Usage details

## Environment variables

Docker service needs these env vars in file .env (not committed to git)

    FLASK_ENV=production
    APIKEY={uuid}

## Deploying on Docker


### Application container

    docker build -t {{cookiecutter.app_name}}:1 .
    docker run --name {{cookiecutter.app_name}} --env-file .env -d -p 8350:8350 {{cookiecutter.app_name}}:1


## open docs in browser using link
    http://localhost:8350/{{cookiecutter.app_name}}/v1/doc/

## login to docker container and run tests
    docker exec -it {{cookiecutter.app_name}} bash
    python -m pytest {{cookiecutter.app_name}}/

# check test case coverage
    coverage run -m pytest && coverage report --omit='*lib/*.py,*test_*.py' && coverage xml -i

# create type_info files to generate type hints for mypy

eg.
```
pyannotate --type-info type_info/TestActivity.json -v {{cookiecutter.app_name}} -w
```


## running on your system without docker

# Install pipenv on your system
    https://github.com/pypa/pipenv


## Install packages including dev

    pipenv install --dev

### If error installing pycurl

```
PYCURL_SSL_LIBRARY=openssl LDFLAGS="-L/usr/local/opt/openssl/lib" CPPFLAGS="-I/usr/local/opt/openssl/include" pip install --no-cache-dir pycurl
```

## Run all test cases

    pytest .

## Run development server

    python run.py

## open docs in browser using link

    http://localhost:5000/{{cookiecutter.app_name}}/v1/doc/


##### run this script to install git-hooks

```
./tools/git/install_hooks.sh
```

##### New-relic integration
    check wsgi.py file

## SonarQube commands for enabling Sonar quality gate on Jenkins

```
coverage run -m pytest && coverage report --omit='*lib/*.py,*test_*.py' && coverage xml -i
/opt/sonar/bin/sonar-runner -Dsonar.host.url=http://10.20.4.242:9000 -Dsonar.projectKey=guestpass-qa -Dsonar.projectName=guestpass-qa -Dsonar.sources=. -Dsonar.exclusions=.venv/**,env/**,.env/**,**/*.pyc,**/__pycache__/**,**/tests/**,scripts/deployment_test_build.py -Dsonar.python.coverage.reportPath=coverage.xml
```


## SonarQube setup on local  (Linux)

Install java

Go to [SonarQube website](https://www.sonarqube.org/downloads/) and download SonarQube Community Edition 7.2.1

Unzip the downloaded file (sonarqube-7.2.1.zip)

Go to **sonarqube-7.2.1/conf** and set the **wrapper.java.command** property to java path in **wrapper.conf**
```
wrapper.java.command=/java/path/
```

Now got inside sonarqube-7.2.1/bin/$OS where $OS is your operating system

Start  SonarQube server
```
$ ./sonar.sh start
```
Open a browser and go to http://localhost:9000/. It will display Sonar homepage

Download [SonarQube Scanner](https://docs.sonarqube.org/display/SCAN/Analyzing+with+SonarQube+Scanner) and unzip it

Add $SONAR_SCANNER_PATH/bin to your path.

Navigate to the project folder where the "sonar-project.properties" file is located

To use SonarQube, run

```
$ sonar-scanner
```

#### Deployment comments
