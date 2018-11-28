# Python2 Flask Example Application (S2i Exclusive Build Process)

# Intro
TODO

# License
TODO

# Project Structure
-------
```sh
.
├── Dockerfile
├── README.md
├── config.py
├── exampleapp.py
├── requirements.txt
├── static
│   ├── adx_dodiis.png
│   ├── adx_logo_invert_xs.png
│   ├── adx_logo_nofill.png
│   ├── adx_logo_xs.png
│   ├── bootstrap.min.css
│   ├── dodiis_demo.jpg
│   ├── icon-application-containers.png
│   ├── icon-common-control-provider.png
│   ├── icon-data-storage.png
│   ├── tweets.txt
│   └── tweets_clean.txt
├── templates
│   ├── 404.html
│   ├── base.html
│   ├── base2.html
│   ├── demo.html
│   ├── dodiis.html
│   ├── dodiis2.html
│   └── index.html
└── wsgi.py
```

# Required Files
```
Dockerfile
```
Typically a Dockerfile is used to build a Docker container image. By utilizing the S2i buld process, we are actually going to not use the `Dockerfile`. We are including it in this repo for local testing.

```
exampleapp.py
```
The main python file to run the sample application. This is where the Flask runtime server object is instantiated and routes are defined. Running `python exampleapp.py` will run the webapplication using the `development webserver` 
which is `not` intended for production use cases. To use Flask in more production-focused applications, use a third-party webserver such as [](Gunicorn) or Nginx. Here's a link that explains [why](https://ironboundsoftware.com/blog/2016/06/27/faster-flask-need-gunicorn/).

```
wsgi.py
```
WSGI specifies the rules which needs to be implemented by the Web Application side and the Web Server side so that they can interact with each other. This is what tells the `gunicorn` webserver what it should be serving up. 
Override `gunicorn` specific variables here.

```
requirements.txt
```
The `requirements.txt` acts as the manifest of all external python dependencies your application needs to function. Libraries will be downloaded and installed using the `pip` python dependency manager during the S2i build process.

```
config.py
```
The `config.py` file acts as an external configuration file for the `gunicorn` webserver. NOTE: You will need to set an environment variable (APP_CONFIG) in your s2i artifact injector pod (<app_name>-s2i-runtime-artifact-injector) 
to the full filepath of the file. (example: /opt/app-root/config.py, /opt/app-root is the default location that s2i will inject your source code into the compiled Docker image.)

```
.gitignore
```
This is a manifest of wildcarded file-types that are to be ignored by the Git SCM.

```
templates & static
```
The `templates` and `static` folders are where Flask-specific files live. If you need to learn more about Flask, see [](Here)
