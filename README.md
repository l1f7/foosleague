# Lift Project Starter

This is the starter repo for new Lift Django projects.

PROJECT NAME
=============
Description goes here

- Strategy: people go here
- Back End: people go here
- Front End: people go here
- Design: people go here


Install
=========
This is where you write how to get a new laptop to run this project.

```
make setup venv=foosleague && workon foosleague && make install
```

Deploy
========
IP: 12.345.67.890

Domain: leagueoffoos.com

This is where you describe how the project is deployed in production.

- Clear liftoff/liftoff/templates/robots.txt file
- Make sure ALLOWED_HOSTS is set in the settings
- Change SECRET_KEY


Development
===========

### LOCAL MEDIA DURING DEVELOPMENT - BitTorrent Sync

1. Create Media Folder (if necessary)
2. Install BitTorrent Sync (http://www.bittorrent.com/sync)
3. Add Folder to Sync
  - Secret Key: <generate secret key>
  - Select media folder to sync.


Account Info
==========
TODO: Write account credentials for all accounts associated with this project(ex. Stripe, Mailchip, etc.)

###Example Account
- username: lift
- password: liftpassword

Yoman
======
- liftoff
- liftoff/liftoff
- liftoff/pytest.ini
  DJANG_SETTINGS_MODULE=liftoff.settings.test
- liftoff/liftoff/manage.py
  os.environ.setdefault("DJANGO_SETTINGS_MODULE", "liftoff.settings.production")
- liftoff/liftoff/wsgi.py
  os.environ.setdefault("DJANGO_SETTINGS_MODULE", "liftoff.settings.production")
- liftoff/liftoff/liftoff/settings/base.py
  ALLOWED_HOSTS = ['.example.com',]


Notes
======
TODO: Write any additional notes you have for this project
