#Steps to setting up heroku w/ Flask

1. Write the flask app
 * set up `__init__.py` (as defined in `app/__init__.py`)
 * set up the views.py (as defined in `app/views.py`)
 * set up the models.py (as defined in `app/models.py`)
 * set up the manager.py (as defined in `manager.py`)
 * set up the run_server.py (as defined in `run_server.py`)
 * set up the requirements.txt (as defined in `requirements.txt`)

2. Set up the github repo
 * remote setup
 	* set up the remote repository via the + button on github.com
 * in the local (from the root level directory of the repository)
    * `git init`
    * `git add --all`
    * `git commit -m "first commit"`
    * `git remote add origin git@github.com:UserName/repository_name.git`
    * `git push -u origin master`  
* for all future commits:
	* `git add --all` or files to push
	* `git commit -m "what was done since last push"`
	* `git push`

4. Setting up database
	* `createuser -P -s -e -d skills_admin` (when prompted to enter password enter 1234)
	* `createdb skills_db -U skills_admin`
	* python (from top level directory)
		* `from app import db`
		* `db.create_all()`
  	* `python manager.py db init`
  	* `python manager.py db migrate`
  	* `python manager.py db upgrade`