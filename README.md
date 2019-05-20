# WebAndAPI Test App
## Pre-requisites
We need to install the following tools as part of the pre-requisites to be able to run this example.
### Tech.
* [Python3] -- Python is a programming language that lets you work more quickly and integrate your systems more effectively.
    * Check the python version in this way, i.e
        ```ssh 
        $ python3.x -V
        Python 3.7.0
        ```  
* [Pip] -- pip is a package management system used to install and manage software packages written in Python.
    * Check the pip version in this way, i.e 
        ```ssh 
        $ pip --version
        pip 18.1 from /Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/pip (python 3.7)
        ```     
### Install [VirtualEnv].
For more deep information about VirtualEnv, click on the link above. But basically the idea with a virtual environment is to have an isolated environment where you can run your project with some specific tools versions. It allows to have more than one environment in a single local machine.

```ssh
pip install virtualenv
```

### Creating a workspace.
Lets create a new folder to start working and creating our local working environment.
#### Unix
```sh
$ mkdir ~/demo_workspace            ## create a new folder in your favourite path
$ cd ~/demo_workspace               ## move to the new workspace
$ virtualenv -p python3.7 demo  ## Create a new virtualenv
$ cd api_demo                       ## go into the virtualenv folder
$ source bin/activate               ## active the virtualenv
```
#### Windows
```sh
$ create a folder to use as workspace   ## create a new folder in your favourite path
$ cd <workspace folder>                 ## move to the new workspace
$ virtualenv demo                       ## Create a new virtualenv (by default we are using python 3.7 since is the one we installed before)
$ cd demo                               ## go into the virtualenv folder
$ Scripts\activate                      ## active the virtualenv
```
### Clone this project
In this step we are going to clone the code from this repository.
```ssh
$ git clone https://github.com/ovalerio280788/BehaveWebAndAPI.git
```

At this point we will have something like this in the virtualenv directory:
```ssh
BehaveWebAndAPI/  Include/  Lib/  LICENSE.txt  Scripts/  tcl/
```

### Install libraries to be able to run this demo project.
Here we will use pip to install all the required libraries into the active virtual environment.
In this case we have a [requirements.txt] file, that contain all the libraries needed to run this demo project.
```ssh
$ cd BehaveWebAndAPI/               ## Move into the repository folder.
$ pip install -r requirements.txt   ## To install libs into this file.
$ pip freeze                        ## to see the installed libs.
```

### Running the API application.
Into the repository directory, execute the following command to generate the migrations for this demo proyect.
```ssh
$ cd web
$ python manage.py migrate                   ## build the database
$ python manage createsuperuser              ## Create a new user ovalerio/admin123 is used on tests
$ python manage.py runserver 0.0.0.0:9000    ## Run the local server
```
Now you can go to your favorite browser and open this url http://127.0.0.1:9000/ 

### References
* https://www.python.org/downloads/
* https://behave.readthedocs.io/en/latest/ 
* http://docs.python-requests.org/en/master/user/quickstart/ 
* http://allure.qatools.ru/


[Python3]: <https://www.python.org/downloads/>
[PIP]: <https://pip.pypa.io/en/stable/installing/>
[VIRTUALENV]: <https://virtualenv.pypa.io/en/latest/>
[BEHAVE]: <https://behave.readthedocs.io/en/latest/>
[REQUESTS]: <http://docs.python-requests.org/en/master/user/quickstart/>
[requirements.txt]: <https://github.com/ovalerio280788/api_django_behave_requests/blob/master/requirements.txt>
