import sys
import os
from time import sleep
from datetime import datetime, date, time, timedelta
from pyfiglet import Figlet

if len(sys.argv) < 3 or sys.argv[1] == "-h" or sys.argv[1] == "--help":
  print("Reads the file given as the first argument and lists the next [second argument] events coming up")
  print("NOTE: The events must be in time order.")
  exit()

while True:
  output = ""
  now = datetime.now()
  f = Figlet()
  output += f.renderText("Upcoming Events")
  #print("\nUpcoming Events:\n")

  events = []
  with open(sys.argv[1], "r") as f:
    events = f.readlines();

  if len(events) < 1:
    continue

  # Get the size of the pane
  rows, columns = os.popen('stty size', 'r').read().split()

  eventsShown = 0
  eventsMax = int(sys.argv[2])
  for i in xrange(len(events)):
    data = events[i].split("-")
    data[0] = data[0].strip()
    data[1] = data[1].strip()
    # Have to convert to a stupid datetime to make it work then strip out the time part
    eventTime = datetime.strptime(data[0], "%d/%m/%y %H:%M")
    if eventTime > now and eventsShown < eventsMax:
      suffix = "th"
      if eventTime.day == 11 or eventTime.day == 12 or eventTime.day == 13:# Ignore these stupid numbers that don't follow the pattern.
        suffix = "th"
      else:
        ending = eventTime.day%10 #Get the ending character
        if ending == 1:
          suffix = "st"
        elif ending == 2:
          suffix = "nd"
        elif ending == 3:
          suffix = "rd"
      eventTimestamp = eventTime.strftime("%d"+suffix+" @ %H:%M")
      endDashes = ''.join(['-' for i in xrange(int(rows)-len(eventTimestamp)-4)])
      output += "\n-- " + eventTimestamp + " " + endDashes
      output += "\n\n " + data[1]
      output += "\n"
  
  os.system("clear")
  print output
  sleep(60)
