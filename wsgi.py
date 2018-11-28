import os
import logging
from logging.handlers import RotatingFileHandler
from OpenSSL import SSL
from mooit import application

if __name__ == "__main__":
    context = SSL.Context(SSL.SSLv23_METHOD)
    certfile = '/secret/cert/python-tls.crt' # This is where our certs are stored using OpenShift secrets. 
    keyfile = '/secret/cert/python-tls.key'
    if not os.path.exists('/secret/cert'):
        certfile = './python-tls.crt'
        keyfile = './python-tls.key'
    application.run(host="0.0.0.0",port=8443,ssl_context=(certfile,keyfile))
