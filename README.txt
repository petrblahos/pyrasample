pyrasample
==========
This is a companion project to a talk delivered during Prague PyVo Event
on the 16th May 2018. You will find the talks in docs/


Getting Started
---------------

- Change directory into your newly created project.

    cd pyrasample

- Create a Python virtual environment.

    python3 -m venv env

- Upgrade packaging tools.

    env/bin/pip install --upgrade pip setuptools

- Install the project in editable mode with its testing requirements.

    env/bin/pip install -e ".[testing]"

- Edit your development.ini. Point the sqlalchemy.url to an existing
  database

- Run your project.

    env/bin/pserve --reload development.ini
