Google-Calendar_API

A desktop application build on python runs on terminal uses google calendar API to list and create the events.
It OAuth 2.0 and creates a json file name client_secret.json.
It runs on terminal.

Files:
All modules of the files are held by main.py file which gives calendar_service.
The list_events.py fetches all the upcoming 50 events sort by the upcoming date in an order.
The all_calen.py file shows all the calendars link to a single gmail account.
The create_event.py file creates the event which is ask by the user to give the desired input start & ending date and then it list all events along with the latest event that has been created.

Run:

First create a virtual environment using command "-- python3 -m pip3 install --user virtualenv".
Then after install all the libraries from requirements.txt using command "python3 -m pip3 install -r requirements.txt".
Navigate the terminal directory where you have download this repository.
Then run various .py files according to your need. 
