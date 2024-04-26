# Computer Science Club Website
A website for Computer Science Club made during a mini-hackathon.

## setup
### environment
To setup the server environment, run `python -m venv .` in the root of the project. Then, execute `. ./bin/activate` and you should be in the virtual environment. Next, run `pip install flask schoolopy jsonpickle cachecontrol google-auth google_auth_oauthlib` to install all the dependencies. Now, `exit`.

### schoology
In ```config.py```, change ```DOMAIN``` to the URL of the Schoology instance. In addition, change ```GROUP_ID``` to the ID of the Schoology group. This can be found by visiting the Schoology website and by navigating to the Schoology group. The group's ID should be right after the ```/group/...``` subdirectory of the domain. To get a Schoolopy API key and secret, goto `schoology.(PUT DOMAIN HERE).org/api`. There, you can manage your API credentials. Get the key and the secret.

### google
To setup Google OAuth2, go [here](https://developers.google.com/identity/oauth2/web/guides/get-google-api-clientid) and follow the instructions. Copy the json into a file called `google_auth.json` in the root of the project. In `config.py`, change `REDIRECT_URL` to the URL you used when you set up the Google project. Make sure that the redirect URL is added as one of the "Authorized redirect URIs."

## running
Now, you can execute `SCHOOLOGY_API_KEY="PUT KEY HERE" SCHOOLOGY_API_SECRET="PUT SECRET HERE" ./run.sh`.

