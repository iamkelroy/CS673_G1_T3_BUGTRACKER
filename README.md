# CS673_G1_T3_BUGTRACKER
Group 1, Team 3: Bug tracker repository for the CS 673 Spring 2015.

## Installation

### 1. Requirements
You will find the *requirements.txt* file has the currently required installation files. We have included the files needed for testing as well. 
To install directly:

`$ pip install -r requirements.txt`

### 2. Tweaks

#### local.py
The file `issue_tracker/settings/local.py` contains a common schema for local development. Please be aware that changing this file affects all developers.

#### Initialize the database
First set the database engine (PostgreSQL, MySQL, etc..) in your settings file `issue_tracker/settings/local.py`.  Initialize the database:

`python2.7 ./manage.py migrate`

### Ready? Go!

`python2.7 ./manage.py runserver`
