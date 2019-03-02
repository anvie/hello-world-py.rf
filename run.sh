#!/usr/bin/env bash
echo "Starting $name$ server..."
export FLASK_APP=$name_snake_case$.py
flask run
