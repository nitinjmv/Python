### Install virtualenv
`pip install virtualenv`

###  Create virtual env
`virtualenv env`

### Activate virtualenv for powershell
`.\env\Script\activate.ps1`

- If error executing the command, open powershell as admin and run the following command.
`Set-ExecutionPolicy unrestricted`

### Install Flask on venv
`pip install Flask`

### Run the app
`python app.py`

### Access the app 
- `http://127.0.0.1:5000`

### Stop & deactivate the venv
`Ctl+C`

`deactivate`
