# downtube
A ridiculous .mp3 YouTube downloader.

![alt text](https://github.com/Dapesa/downtube/blob/7151bb64a8e7b108ede96189474da3aa0c9c871b/Screenshot%202023-02-22%20at%2001-41-44%20DownTube%20by%20Dapesa%20(DevDuck).png)

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
venv\Scripts\activate
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
