#!/bin/zsh

export FLASK_APP=app.py
pipenv run flask run --host='0.0.0.0'

#
# Vue CLI v4.1.1
# ┌─────────────────────────────────────────┐
# │                                         │
# │   New version available 4.1.1 → 4.4.6   │
# │    Run npm i -g @vue/cli to update!     │
# │                                         │
# └─────────────────────────────────────────┘
# 
# ? Please pick a preset: Manually select features
# ? Check the features needed for your project: Babel, Router, Linter
# ? Use history mode for router? (Requires proper server setup for index fallback in production) Yes
# ? Pick a linter / formatter config: Airbnb
# ? Pick additional lint features: (Press <space> to select, <a> to toggle all, <i> to invert selection)Lint on save
# ? Where do you prefer placing config for Babel, ESLint, etc.? In package.json
# ? Save this as a preset for future projects? (y/N) N
#

#
# to run vue app 
# $ cd client
# $ npm run serve
#

