# Python / Flask with Modularization
- in order to set up a modularized flask application we need to take some steps.

- first we need to build a file system for all of our files.

## The Folder Structure

```txt
-- Project folder
    - flask_app
        - config
            - mysqlconnection.py
        - controllers
            - user_controller.py
        - models
            - user.py
        - static
            - css
                - style.css
            - images
            - js
                - script.js
        - templates
            - index.html
        - __init__.py
    - Pipfile
    - Pipfile.lock
    - server.py
```

## The files

- second to last we have the `__init__` file [Here](./boilerplate/__init__.py).
- first we have `mysqlconnection.py` found [Here](./boilerplate/mysqlconnections.py).
- then we have a Model file [Here](./boilerplate/user.py)
- next we have the controllers check out an example [Here](./boilerplate/user_controller.py)
- you are well versed at html, css, and javascript so no example of that
- finally we have the `server.py` file [Here](./boilerplate/server.py)
