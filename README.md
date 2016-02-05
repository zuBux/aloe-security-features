# aloe-security-features
This repo contains a number of security-related BDD features for [Aloe](https://github.com/aloetesting/aloe) using [Selenium](http://docs.seleniumhq.org/).

# Notes
Some Scenarios (like testing for HttpOnly and Secure flags) will work without any modification, just change the URL variable in `steps.py`. Others, like the Session Fixation scenario, will require a new implementation of some steps (e.g `user_login` and `user_logout`).
