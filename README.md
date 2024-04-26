# Computer Science Club Website
A website for Computer Science Club made during a mini-hackathon.

## setup

To setup the server environment, run `python -m venv .` in the root of the project. Then, execute `. ./bin/activate` and you should be in the virtual environment. Next, run `pip install flask schoolopy jsonpickle cachecontrol google-auth google_auth_oauthlib` to install all the dependencies. Now, exit using by running `exit`.

To get a Schoolopy API key and secret, goto `schoology.(PUT DOMAIN HERE).org/api`. There, you can manage your API credentials. Get the key and the secret.

To setup Google OAuth2, go [here](https://developers.google.com/identity/oauth2/web/guides/get-google-api-clientid) and follow the instructions. Copy the json into a file called `google_auth.json` in the root of the project. In the `config.py` file in the directory of the project, change `REDIRECT_URL` to the url you used when you set up the google project.

## running
Now, you can execute `SCHOOLOGY_API_KEY="PUT KEY HERE" SCHOOLOGY_API_SECRET="PUT SECRET HERE" ./run.sh`.

