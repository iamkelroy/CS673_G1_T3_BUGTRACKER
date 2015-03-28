# CS673_G1_T3_BUGTRACKER
Group 1, Team 3: Issue tracker repository for the CS 673 Spring 2015.

## Installation

### 1. Download
Now, you need the *CS673_G1_T3_BUGTRACKER* project files in your workspace:

    $ cd /path/to/your/workspace
    $ git clone git@github.com:iamkelroy/CS673_G1_T3_BUGTRACKER.git head1 && cd head1

### 2. Requirements
You will find the *requirements.txt* file has the currently required installation files. We have included the files needed for testing as well. 
To install directly:

`$ pip install -r requirements.txt`

### 3. Local changes and getting started

#### local.py
The file `issue_tracker/settings/local.py` contains a common schema for local development. Please be aware that changing this file affects all developers.

#### Initialize the database
First set the database engine (PostgreSQL, MySQL, etc..) in your settings file `issue_tracker/settings/local.py`.  For windows users, please initialize the database in a directory you can write to.  Initialize the database:

`python2.7 ./manage.py migrate`

#### Populate the db with test data.
This command will populate dummy users, a test user and 1000 dummy issues.
The superuser account username: 'test', password: 'testpw'

`python2.7 manage.py populate_demo_data`

### Ready? Go!

`python2.7 ./manage.py runserver`

