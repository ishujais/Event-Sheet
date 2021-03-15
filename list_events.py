import datetime
from main import get_calendar_service

def main_list():
   service = get_calendar_service()
   # Call the Calendar API

   now = datetime.datetime.utcnow().isoformat() + 'Z'
   # 'Z' indicates UTC time
 
   print('Getting list of events')
   # Reads the 50 upcoming events & list them according to their appearing date.
   events_result = service.events().list(
       calendarId='primary', timeMin=now,
       maxResults=50, singleEvents=True,
       orderBy='startTime').execute()
   events = events_result.get('items', [])

   if not events:
       print('No upcoming events found.')
   for event in events:
       start = event['start'].get('dateTime', event['start'].get('date'))
       try:
        print(start, event['summary'])
       except:
           continue
    
if __name__ == '__main__':
   main_list()
