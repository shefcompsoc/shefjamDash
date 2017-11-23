from datetime import datetime, date, time, timedelta
import sys

if len(sys.argv) == 1 or sys.argv[1] == "-h" or sys.argv[1] == "--help":
  print("Returns the time until an event given in a text file, the name of which sould be given as the first parameter and should contain a date in the format XX/XX/XX XX:XX:XX")
  exit()

end = ""
with open(sys.argv[1], "r") as f:
  end = f.readline()

if end == "":
  print("Error calculating time")
  exit()

end = datetime.strptime(end.strip(), "%d/%m/%y %H:%M:%S")
now = datetime.now()
spacing = "  "
if end<now :
  print(spacing+"00:00:00")
else:
  diff = end-now
  print(spacing+'%02.0d:%02.0d:%02.0d' % (diff.total_seconds()//3600, (diff.total_seconds()//60)%60, diff.total_seconds()%60))

