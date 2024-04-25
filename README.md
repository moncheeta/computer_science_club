# Computer Science Club Website
A website for Computer Science Club made during a mini-hackathon.

## setup
To setup the server environment, run ```python -m venv .``` in the root of the project. Then, execute ```. ./bin/activate``` and you should be in the virtual environment. Next, run ```pip install flask schoolopy``` to install all the dependencies. Now, exit using by running ```exit```.

## running
To run the server, you need an API key and its companioning secret. In your browser, go to ```schoology.(PUT DOMAIN HERE).org/api```. There, you can manage your API credentials. Get the key and secret and return.

Now, you can execute ```SCHOOLOGY_API_KEY="PUT KEY HERE" SCHOOLOGY_API_SECRET="PUT SECRET HERE" ./run.sh```.

