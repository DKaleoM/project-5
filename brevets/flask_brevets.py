"""
Replacement for RUSA ACP brevet time calculator
(see https://rusa.org/octime_acp.html)

"""

import flask
from flask import request
import arrow  # Replacement for datetime, based on moment.js
import acp_times  # Brevet time calculations
import config

import source_gen_tests  #testing code source generation
from source_gen_tests import create_tests_py

import logging

###
# Globals
###
app = flask.Flask(__name__)
CONFIG = config.configuration()

###
# Pages
###


@app.route("/")
@app.route("/index")
def index():
    app.logger.debug("Main page entry")
    return flask.render_template('calc.html')


@app.errorhandler(404)
def page_not_found(error):
    app.logger.debug("Page not found")
    return flask.render_template('404.html'), 404


###############
#
#Source generation using Jinja
#
###############

#disabled for now
#todo: make it export to a connected folder in docker
#instead of as an endpoint on the server
"""


@app.route("/source_gen_tests")
def source_gen_tests():
    with open("generated_tests.py","w") as f:
        contents = create_tests_py()
        f.write(contents)
    
    return flask.send_file("generated_tests.py") 

"""

###############
#
# AJAX request handlers
#   These return JSON, rather than rendering pages.
#
###############
@app.route("/_calc_times")
def _calc_times():
    """
    Calculates open/close times from miles, using rules
    described at https://rusa.org/octime_alg.html.
    Expects one URL-encoded argument, the number of miles.
    """
    app.logger.debug("Got a JSON request")
    km = request.args.get('km', 1600, type=float)
    brevet_dist = request.args.get('brevet_dist', 1600, type=int)
    time_str = request.args.get('start_time',type=str)
    
    app.logger.debug("km={}".format(km))
    app.logger.debug("brevet_dist={}".format(brevet_dist))
    app.logger.debug("time_str={}".format(time_str))
    app.logger.debug("request.args: {}".format(request.args))

    start_time = arrow.get(time_str,"YYYY-MM-DDTHH:mm")

    app.logger.debug("start_time={}".format(start_time.format('YYYY-MM-DDTHH:mm')))
    
    # FIXME!
    # Right now, only the current time is passed as the start time
    # and control distance is fixed to 200
    # You should get these from the webpage!
    
    open_time = acp_times.open_time(km, brevet_dist, start_time).format('YYYY-MM-DDTHH:mm')
    
    close_time = acp_times.close_time(km, brevet_dist, start_time).format('YYYY-MM-DDTHH:mm')
    
    result = {"open": open_time, "close": close_time}

    app.logger.debug("results={}".format(result))
    
    return flask.jsonify(result=result)


#############

app.debug = CONFIG.DEBUG
if app.debug:
    app.logger.setLevel(logging.DEBUG)

if __name__ == "__main__":
    print("Opening for global access on port {}".format(CONFIG.PORT))
    app.run(port=CONFIG.PORT, host="0.0.0.0")
