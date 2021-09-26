#!/bin/bash

echo "starting flask server...."
export FLASK_ENV="developement"
export FLASK_APP="run.py"
flask run

