from datetime import datetime, timedelta
from main import get_calendar_service
from list_events import main_list


def main():
   # Creates an event based on user input.
   service = get_calendar_service()

   # User input date for event
   print("Start (first enter the month then date sperated by a space): ", end ="")
   a,b = input().split()
   start = datetime(2021,int(a),int(b))
   print("End (first enter the month then date sperated by a space): ", end ="")
   a,b = input().split()
   end = datetime(2021,int(a),int(b))
   start = start.isoformat()
   end = end.isoformat()
  
   #Creating event which will store on primary calendar.
   event_result = service.events().insert(calendarId='primary',
       body={
           "summary": input("Event Name: "),
           "description": input("Event Description: "),
           "start": {"dateTime": start, "timeZone": 'Asia/Kolkata'},
           "end": {"dateTime": end, "timeZone": 'Asia/Kolkata'},
       }
   ).execute()
   
   #Event created succesfully 
   print("created event")
   print("id: ", event_result['id'])
   print("Description: ", event_result['summary'])
   print("starts at: ", event_result['start']['dateTime'])
   print("ends at: ", event_result['end']['dateTime'])

if __name__ == '__main__':
   main()
   
# Calling list_event to list all events
main_list()

