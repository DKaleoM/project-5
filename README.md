# Brevets Time Calculator (MongoDB edition)
## Author Info
Author: Kaleo

Contact: kaleom@uoregon.edu

## Description
This project hosts a webpage server for a brevets time calculator
It is based on the one at https://rusa.org/octime_acp.html
The interactive frontend is made using JQuery
The backend is made using the Flask python library, and runs in docker
The actual calculation is in a separate file, and is unit tested
A Makefile is provided with the tasks "run", "logs", and "test"

New in MongoDB edition:
The calculator comes with submit and display buttons! 
Data is saved when submitting, and can be fetched later with display.
This is achieved via a second docker container running MongoDB


## Sources used:

For python documentation references: python docs

https://docs.python.org/

For flask documentation reference: the flask documentation
I also found documentation for the libraries flask ships with here,
including the one with the data structure for requests. 

https://flask.palletsprojects.com/en/3.0.x/

For misc python stuff: w3schools 

https://www.w3schools.com/howto/howto_js_redirect_webpage.asp

For docker compose: docker docs

https://docs.docker.com/compose/gettingstarted/
