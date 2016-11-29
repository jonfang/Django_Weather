*python3.4+ required, django 1.9.5+ required 
sudo apt-get install python3-pip
sudo pip3 install Django==1.9.5
virtualenv to check software dependency

#1:install virtualenv for the virtual environment
$pip install virtualenv
$cd project_dir
$virtualenv venv / $virtualenv -p /usr/bin/python3.x venv (for setting python as default)
$source venv/bin/activate #for actiavting the environment
$deactivate #to deactivate the environment

#2install django framework
$pip install django==1.9.x
$python -c "import django; print(django.get_version())" #check django installed

#3 install pyowm library for weather API-*need to register with OpenWeatherMap to get the weather entries
$pip install pyowm**** last letter is ***m***


Reference: https://docs.mongodb.com/getting-started/shell/import-data/

#4 install MongoDB and transfer data into the DB
$sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv EA312927
$echo "deb http://repo.mongodb.org/apt/ubuntu trusty/mongodb-org/3.2 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.2.list
$sudo apt-get update
$sudo apt-get install -y mongodb-org
*If running into file extension error, go to /etc/apt/sources.list.d/ and rename weird extension files, e.g. ending with lis

#5MongoDB python driver 
$pip install pymongo

#PYOWM library
pip install does not have the unit test code, so need to download it natively from git hub to check out the testing codes



#Django structure
$main skeleton html pages in template directory
$customization style css/javascript in static directory
$view.py for rendoring pages



Reference:
weather animation source: https://codepen.io/joshbader/pen/EjXgqr


#Project workflow
0.Activate virtualenvf
1.Get weather data from from openweathermap usig main/weather class from core directory===> run python main.py
2.Dump the generated weather data as json format into output file===>python main.py > output.json, with convert_to_json function ran
3.Drop the json data into the Mongo database===>
mongoimport --db test --collection sample_weather --drop --file output.json
4.Set up Django Website 
5.For the website, retrieve and search against Mongo DB server

Idea(Python code) ===> Backend(MongoDB) ===> Frontend(Django framework server)

