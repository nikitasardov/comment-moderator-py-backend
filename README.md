## How to install this project
#### 1. Install python3 and pip3
`$ apt-get install python3 python3-pip`

#### 2. Clone this project
`$ git clone https://github.com/nikitasardov/comment-moderator-py-backend.git`

#### 3. Install requirements from pip3
`$ pip3 install -r <project_folder>/requirements.txt`

## How to run the app

#### 1. Run the app
`$ python3 app.py`
* data.json will be created after start if it wasn't there already. It's a dump of default data and then it is updated after any changes. When you run the app next time, previously modified data will be loaded from data.json
* if you want to leave the app running and close the terminal run this `$ nohup python3 app.py &`
* to save logs run this `$ nohup python3 app.py > app.log`
* read logs like this `$ tailf app.log`

#### 2. Check from browser
http://localhost:4567/api/articles/ should give you json with all available data
