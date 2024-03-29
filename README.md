# Feeder Backend

## In a Nutshell

"Feeder" is a webapplication that allows users to post, edit, and delete feeds. The app also offers the ability to post,
edit, and delete comments on the feeds. With Feeder, users can share their thoughts and opinions, receive feedback from
other users, and connect with others. The user interface is user-friendly and easy to navigate.

## Technologies

### Django

"Feeder" was developed using the Django technology. Django is a popular web framework that is widely used for building
high-quality web applications quickly and efficiently. It provides a powerful and secure infrastructure for developing
complex applications, and it is known for its scalability and flexibility. With Django, developers can easily create web
applications with clean and maintainable code, making it a popular choice for building web applications. The use of
Django in the development of "Feeder" ensures that the app is reliable, secure, and easy to maintain.

## Permissions

**Anonym User**

- No Permission

**Default User**

- Can read other feeds
- Can create Feeds
- Can update and delete own Feeds
- Can create Commentaries
- Can update and delete own Commentaries

**Verified User**

- All Default User Permissions
- Can create Feeds + can use more than 200 characters
- Can create Commentaries + can use more than 200 characters

**Moderator**

- All Verified User Permissions
- Can update and delete other Feeds
- Can update and delete other Commentaries
- Can warn verified and default users

**Admin**

- All Moderator Permissions
- Can verify and unverify other users
- Can give and remove moderator role to other users

## Setup

### Pyenv

1. Install Pyenv via Homebrew by running the following command in your terminal: ```brew install pyenv```
2. Once Pyenv is installed, you can install the desired version of Python. For Django 4.1.7, we recommend using Python
   3.11.2 To install this version, run the following command: ```pyenv install 3.11.2```.
   (Warning: It's global, not in a virtual environment. Not recommend).
3. To install virtualenv, you can use the following command if you are using macOS and
   Homebrew: ```brew install pyenv-virtualenv```. This will install pyenv-virtualenv, which is a plugin for pyenv that
   provides support for creating and managing virtual environment.
4. Once Python is installed, you can create a new virtual environment based on Python 3.11.2. To do this, run the
   following command: ```pyenv virtualenv 3.11.2 venv```.
5. Now navigate to your Django project directory and activate the newly created virtual environment. To do this, run the
   following commands: ```cd (Your Path)/django/project``` and ```source (your path)/django/project/venv/bin/activte```.
   This will activate your existing virtual environment.

### Django

1. Make sure you have Pyenv installed with the previous guide. If not, please follow the previous guide on how to
   install Pyenv.
2. Activate your virtual environment by running the following command in your
   terminal: ```source (your path)/django/project/venv/bin/activate```. This will acitvate your virtual environment and
   any packages you install will be specific to this environment.
3. Once your virtual environment is activated, you can use pip to install packages. For example, to install Django, run
   the following command: ```pip install django```. This will install the latest version of Django.
4. Wait for the installation to complete. The installation process should automatically install all necessary
   dependencies.
5. Check that Django was installed correctly by typing the command "django-admin --version" in the command prompt or
   terminal. If Django was installed, the current version of Django should be displayed.
6. You can also install packages from a `requirements.txt` file. This is useful when you need to install multiple
   packages at once. To install the packages listed a `requirements.txt`file, ru the following
   command: ```pip install -r requirements.txt```. This will install all the packages listed in the `requirements.txt`
   file. Note that it's important to do this while your virtual environment is activated. Installing packages globally
   can cause conflicts and make it difficult to manage dependencies.

Congratulations! You have successfully installed Django on your computer in a virtual environment.

### Project

#### Clone using SSH

1. Open your command prompt or terminal.
2. Generate an SSH key by typing the command "ssh-keygen -t rsa" and following the prompts.
3. Log in to your GitHub account and navigate to the project you want to clone.
4. Click on the "Clone or download" button and select "Use SSH" in the top right corner of the pop-up.
5. Copy the SSH URL provided.
6. In the command prompt or terminal, navigate to the directory where you want to clone the project.
7. Type the command ```git clone git@github.com:Kiidle/project.feeder.backend.git``` and press Enter.
8. Wait for the project to be cloned.

#### Clone using HTTPS

1. Open your command prompt or terminal.
2. Log in to your GitHub account and navigate to the project you want to clone.
3. Click on the "Clone or download" button and select "Use HTTPS" in the top right corner of the pop-up.
4. Copy the HTTPS URL provided.
5. In the command prompt or terminal, navigate to the directory where you want to clone the project.
6. Type the command ```git clone https://github.com/Kiidle/project.feeder.backend.git``` and press Enter.
7. Wait for the project to be cloned.

#### Run

1. Open your command prompt or terminal.
2. Navigate to the directory where the cloned project is located using the "cd" command.
3. Once you are in the project's directory, you should see a file called "manage.py". This file is responsible for
   managing the Django project.
4. Type the command ```python manage.py runserver``` and press Enter.
5. Wait for the server to start up.
6. Once the server is up and running, open your web browser and type "http://localhost:8000" in the address bar.
7. If everything was set up correctly, you should see the project.

#### Test

1. Open a terminal window and navigate to the Django project's root directory.
2. Run the following command to execute all the tests in the project: ```python manage.py test -p '*.py'```. This will
   run all the
   tests in the project, including any tests you've written yourself.
3. If you want to run tests for a specific app in your project, you can specify the app's name after the `test`command,
   like this: ```python manage.py test <app_name>```. For example, if you want to run tests for the `feeds` app, you
   would use the following command: ```python manage.py test feeds```.
4. Django provides a range of test runner option that you can use to customize your test execution, such as verbosity
   level and coverage report. To see all available options, run the following command: ```python manage.py help test```
