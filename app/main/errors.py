from flask import render_template
from.import main


@main.errorhandler(404)
def not_found(error):
    '''
    Function to render the 404 error pagge
    '''

    return render_template('404.html'), 404