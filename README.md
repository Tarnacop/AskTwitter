# AskTwitter

## Background
This application was built alongside my Project ATAA team-mates (Alexandru Rosu, Alexandru Blinda and Tudor Suruceanu) for the BrumHack 5.0 (https://www.brumhack.co.uk) hackathon.

## What it does
The user inputs an entity (e.g. a person, a concept etc.) and the system gathers and outpus some interesting information about the subject from Twitter. 
### Features:
- computing an overall percent of "positivity" based on Twitter opinions around the inputted entity
- collecting the most used adjectives as regards the subject matter chosen 

### The future
A bunch of TODOs:
- collect information about a specific Twitter user
- display beautiful and useful visualisation of these statistics (e.g. graphs and charts)

## How it does it
The overall "positivity" percent is computed by gathering a number of tweets on the subject and analysing them via Google's NLP API in order to determing whether the tweets were positive or damning ones. It then takes the average value got for each tweet and returns it.
Both the adjectives and the tweets are gathered using the Twitter API.

## Some design/architecture thoughts
We've chosen the App-API architecture for this application with a Python (Flask) API holding the functionality and a client written in AngularJS and bootstrap which is served by a minimal Node.js webserver.

### Possible improvements
Perhaps we could've done better with using the same technology (i.e. either Node or Flask) both for the API and the webserver, in order to maintain consistency.

## How to use
The API is the first one to be started, and one can navigate to the `api` directory and run the command:
`python api.py` after having installed the required dependencies.

Then one can navigate to `app` and start the webserver:
`node server.js`

After that, use a browser to navigate to `http://localhost:<chosen_port>` where *chosen_port* is the port configured inside the file `server.js`.

### Small note about usage
As our API key has expired all functionality will not be available and an user-friendly error message will be displayed instead.
