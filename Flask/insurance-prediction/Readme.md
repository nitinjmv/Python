### Run as docker 
`docker build -t insurance .`
- Flask runs at default port 5000

`docker run --rm -d -p 5000:5000 insurance`

---

### Install virtualenv
`pip install virtualenv`

###  Create virtual env
`virtualenv env`

### Activate virtualenv for powershell
`.\env\Script\activate.ps1`

- If error executing the command, open powershell as admin and run the following command.
`Set-ExecutionPolicy unrestricted`

### Install Flask on venv
`pip install -r requirements.txt`


### Run the model to generate .pkl
`python model.py`

### Run the app
`python app.py`

### Access the app 
- `http://127.0.0.1:5000`

### Stop & deactivate the venv
`Ctl+C`

`deactivate`
