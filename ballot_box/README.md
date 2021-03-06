#Follow My Vote - Ballot Box
This is the website interface for the follow my vote ballot box

##How to run this site:
1. Install Python 2.7 (https://www.python.org/download/releases/2.7/) and pip (https://pip.pypa.io/en/latest/installing.html) if not already installed
2. Change to the root directory which is vote\ballot_box ..
3. Create a new virtual environment: virtualenv env
4. Activate the virtual enviroment: .\env\scripts\activate or bin/activate depening on your os
5. Install Dependencies: pip install -r requirements.txt
6. Start the Development Server: python runserver.py
7. Connect to Site:  http://localhost:5555

Settings can be found in settings.py. You may also need to change the api host address.

###Installation on apache
1.  If modwsgi is not installed on apache follow the directions on this page: https://code.google.com/p/modwsgi/wiki/QuickInstallationGuide
2.  Follow the directions from **How to run this site** above to make sure that the site is installed correctly, and you can run it from the development sever
3.  Configure the ballot-box.wsgi file located in this directory.
    * Change the **activate_this** variable to set the path to the activate_this.py script located in /scripts or /bin of the vitual environment directory
    * Change the **path_to_site** variable to set the path to the site, this should be the same directory in which the .wsgi file is located
4.  Configure Apache:  
    * Follow instructions located on this page: http://flask.pocoo.org/docs/0.10/deploying/mod_wsgi/#configuring-apache
    * Add **WSGIScriptReloading On** to your directory config to allow the server to reload when changes are detected

A restart of apache may be needed.  If you run into problems consult the page: http://flask.pocoo.org/docs/0.10/deploying/mod_wsgi/ for additional help
