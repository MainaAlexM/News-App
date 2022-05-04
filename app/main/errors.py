from flask import render_template
from . import main

@main.app_errorhandler(404)
def myError(error):
    '''
    Function to handle the 404 error - file not found

    Args:
        error
    '''
    return render_template('myError.html'),404
    