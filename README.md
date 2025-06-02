Project

To run this project, stay in the p4/ directory and use the flask run command. The file that is run is run.py. It simply imports the app object from the flask_app/ package. The reason we have this new structure is to avoid the problem of circular imports in Python projects.

In __init__.py, apps are now created by calling the create_app() function.

All of the view functions are in routes.py. The database models are in models.py, and the MovieClient class is now in client.py. The current_time() function you used in the last project is now in utils.py, and it's been imported into routes.py for your convenience. Forms are still in forms.py.

We create the db, login_manager, and movie_client objects and initialize them using the init_app() function of these extensions.

Then we register the users and movies blueprints and set a global 404 error handler function.

The configuration is loaded from config.py. Although we don't have many configuration values for this project, this kind of pattern is the best practice for when your apps might get more complicated and have lots of configuration values.

Make sure to set the secret key in config.py!!!
