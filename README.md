# CP1895FlaskProject
For CP1895 I am creating a website to display a collection of albums I have been listening to. To do this, I will be developing the backend code in python - making use of Flask.

Below you will find instructions on how to install and run the app. These instructions are for MACOSX users as that is the OS I used while developing the app. 
These instructions may differ slightly for other operating systems.


<h2>INSTALLATION/HOW TO USE:</h2>
<h3>Step 1:</h3> 
Download all of the files in my project repository into your own folder (listed below).

<ul>
  <li>static folder</li>
  <li>templates folder</li>
  <li>application.py</li>
  <li>albums.db</li>
 </ul>

Open the project folder in your preferred IDE. I used PyCharm on MACOSX - it will automatically open your project in a venv (virtual environment). 
In this case, the virtual environment is also already activated. 

<h3>Step 2:</h3> 
In the IDE terminal, ensure you are in the project directory and install flask using the following commands:

<pre>
<code>
  (venv) user@example % cd project_folder_path_here
  
  (venv) user@example project_folder_path_example % pip install flask
</code>
</pre>

You will also need to install flask sessions by entering:

<pre>
<code>
  (venv) project_path_example % pip install Flask-Session
</code>
</pre>

<h3>Step 3:</h3> 
Once everything is installed, it is time export the environment as development and export and application file in flask like so:

<pre>
<code>
(venv) project_path_example % export FLASK_ENV=development

(venv) project_path_example % export FLASK_APP=file_path_for_project_folder/venv/application.py
</code>
</pre>

<h3>Step 4</h3> 
Now it is time to run the app. Simply type the follow command in terminal

<pre>
<code>
(venv) project_path_example % flask run
</code>
</pre>

The app will begin the run and a link will appear in the terminal. Just click the link to take you to the homepage for my web app.

<h2>Site Functionality</h2>
View my top album's of the moment by navigating using the navbar. Login with your username to create and edit your own list.
