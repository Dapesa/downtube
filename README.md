# downtube
A simple .mp3 YouTube downloader for me and my friends.

# Requirements
Obviously you need a virtual environment to run this web app, so follow this steps: 
### Linux:
```
sudo apt-get install python3-pip
sudo pip3 install virtualenv
python3 -m venv venv
source venv/bin/activate
pip install flask pytube
```
### Windows (after installing Python3.10+ and pip3+):
```
python3 -m venv venv
venv/Scripts/activate
pip install flask pytube
```

# Starting the server
Just follow this steps to start the server step-by-step:
1. Clone the repository using git:
```
git clone https://github.com/Dapesa/downtube.git
```
2. Open the repository cloned folder "proj":
```
cd proj
``` 
3. Change flask app to the current app:
* Linux:
```
export FLASK_APP=App.py
```
* Windows:
```
set FLASK_APP=App.py
```
4. Run the server:
```
flask run
```
