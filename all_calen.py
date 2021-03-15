from main import get_calendar_service

def main():
   service = get_calendar_service()
   # Calling Google_Calendar API
   print('Getting list of calendars')
   calendars_result = service.calendarList().list().execute()

   # List all the calendars added to the gmail account.

   calendars = calendars_result.get('items', [])

   if not calendars:
       print('No calendars found.')
   for calendar in calendars:
       summary = calendar['summary']
       id = calendar['id']
       primary = "Primary" if calendar.get('primary') else " "
       print("%s\t%s\t%s" % (summary, id, primary))

if __name__ == '__main__':
   main()
