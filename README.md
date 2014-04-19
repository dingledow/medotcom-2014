# Django Heroku Skeleton

This is a minimal Django skeleton project that is set up for local
development and ready to deploy to [Heroku][1].


## Setting up for local development.

Download/fork/clone this repo to your local machine and then cd into
the root of the repository.

Create the virtualenv and install the requirements &ndash;

    virtualenv venv
    . ./venv/bin/activate
    pip install -r requirements.txt


Set up the local project &ndash;

    python app/manage.py syncdb --settings=app.settings.local
    python app/manage.py collectstatic --settings=app.settings.local
    
You can now runserver &ndash;

    python app/manage.py runserver --settings=app.settings.local

Once it's up and running, you can carve the project to your needs. The
static assets are in `srv/assets` and you can use a one liner shell
command to sync the assets to static as you develop ( _remember to
activate your virtualenv `./venv/bin/activate`_ ) &ndash;
    
    while true; do python app/manage.py collectstatic --noinput --settings=app.settings.local; sleep 1; done

## Deploying to Heroku

Make sure you've done the following three things

* have a [Heroku][1] account
* have the [Heroku toolbelt][0] installed
* have auth'd against Heroku using `heroku login` command.

Create the app

    heroku apps:create sensible-app-name --region eu   --buildpack git://github.com/heroku/heroku-buildpack-python.git

Just double check that it's likely to run on Heroku by using the
foreman command &ndash;

    foreman start

If all is good, do your first deploy to Heroku &ndash;

    git push heroku master
    
Set up a variable to point to your settings (_examples uses `base` but you may create your own `production` settings_)

    heroku config:set DJANGO_SETTINGS_MODULE=app.settings.base

Now scale up the worker to one &ndash;

    heroku ps:scale web=1

If you check your deploy once it's completed it may fail if you try to
do anything that hits the database, so sync the database.

    heroku run python app/manage.py syncdb

Finally, set the `SECRET_KEY` to something other than what is in the
settings.

    heroku config:set SECRET_KEY=YOUR-SECRET-KEY-GOES-HERE

All done, enjoy.

[0]: https://toolbelt.heroku.com/
[1]: https://heroku.com/
