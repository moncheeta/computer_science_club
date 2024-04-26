# computer_science_club

A website for Computer Science Club. It was made during a mini-hackathon.

## setup

To setup the server environment, run `python -m venv .` in the root of the project. Then, execute `. ./bin/activate` and you should be in the virtual environment. Next, run `pip install flask schoolopy` to install all the dependencies. Now, exit using by running `exit`.

To setup Google OAuth2, goto [get google api clientid](https://developers.google.com/identity/oauth2/web/guides/get-google-api-clientid) and follow the instructions. Copy the json file into `google_auth.json` in the root of the project. In the `config.py` file in the directory of the project, change `REDIRECT_URL` to the url you used when you set up the google project.

## running

To run the server, you need an API key and its companioning secret. In your browser, go to `schoology.(PUT DOMAIN HERE).org/api`. There, you can manage your API credentials. Get the key and secret and return.

Now, you can execute `SCHOOLOGY_API_KEY="PUT KEY HERE" SCHOOLOGY_API_SECRET="PUT SECRET HERE" ./run.sh`.
