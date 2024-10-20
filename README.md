# 🤓 Kanopi-Assignment

A Django/React application that generates a swatch of five random colours

## 👓 Overview

This application takes in data under the JSON structure where a member has the data of their name, ID, and home city, which then logs the ID and subsequently sends it to our API, which then sums the ID down to a single digit and picks the associated word, sends it back which we then log the result.


## 🔨 API Setup

Firstly, make sure pipenv is installed since it is the virtual environment we are using, then after entering our virtual environment install requirements as usual
```
pip install -r requirements.txt
```
Make sure you run migrations (there are migrations for the purposes of the stage 2 answer) and run the server.

## 🔨 Frontend Setup

Make sure Meteor is installed, we used the Meteor framework with React just to get everything set up quickly.

Then run
```
meteor npm install
```
so that all our required packages are installed, then we can run our frontend with
```
meteor npm run start
```

That's it! Pretty easy stuff.

## 🧠 Stage 2 Answer

So when considering alternate colour spaces, I made it as straightforward as possible on the backend side by turning the possible space of colours to be randomised as data. Every colour type is defined as an abstract model for the purposes of extensibility, so as long as a colour space only uses 3 values, like BRGB in this case, we only need to add BRGB as a type via post request and define the maximum values that BRGB colours can be. Where a bit more work is required is if a colour space doesn't use either red, green, or blue/hue, saturation, lightness, in which case we only need to add the new properties as choices in the model, and that's it. On the frontend, adding support for more colour spaces basically just means adding a new dynamic string for the style for css to support. I'm not super versed on colour spaces myself, and BRGB seems to be a made up colour space because I can't google it, but for the purposes of the frontend, if a colour space can be converted to RGB mathematically then that's where we can put the conversion to RGB pretty simply via our API call.

## 🤔 What I didn't do

The main thing I didn't do is implement testing, which would take me more time than the allotment probably allows, but I'd absolutely put in unit testing for putting colour spaces in the database.
