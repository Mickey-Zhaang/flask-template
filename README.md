# flask-template

Author : Mickey Zhang  
Purpose : Entreprenurial SWE @ Colby College -- CS422  

## Initial Setup

1) After git cloning or downloading the zip file, open the file in your Code Editor
2) I did something silly and pushed my .env file out... NEVER DO THAT! But you can help me fix it by locating the .gitignore and find the environments section. Add .env into this section, doesn't matter where so long as it is in this gitignore file then Git will ignore it on push (hence the name). This is an important lesson as .env should hold all of your app's secrets i.e. api keys, secret key, etc... and you don't want anyone random on github to see them!  
   ![image](https://github.com/user-attachments/assets/2f5a998a-b497-45b6-8de9-1fb160a08eef)
3) Now open the terminal and run `python -m venv venv` to create a virtual environment (venv) called venv  
4) Activate it with `source venv/Scripts/activate` on Windows or `source venv/bins/activate` on Mac, and you should see a (venv) above your terminal  
5) Once your venv is set up and running, run `pip install -r requirements.txt` which recursively downloads everything in requirements.txt like python, pytest, flask etc...
6) Now you are ready to explore the Flask App
   * Start navigating around --  
   * run `python app.py` and follow the local host url to view a local version of the app
   * run `python tests/run_tests.py` to get a look at tests
