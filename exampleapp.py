from flask import Flask, render_template, redirect, url_for, request, session, flash, g, abort
from functools import wraps
import datetime


application = Flask(__name__)

# Default simple route
@application.route('/', methods=['GET', 'POST']) #this is called a decorator
def home():
    return "boom"

# Custom 404 page
@application.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Start the server with the 'run()' method
if __name__ == '__main__':
    application.run(host="0.0.0.0",debug=True)

