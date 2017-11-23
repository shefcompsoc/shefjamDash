import sys
import os
from pyfiglet import Figlet
from time import sleep
from datetime import time, datetime

if len(sys.argv) < 3 or sys.argv[1] == "-h" or sys.argv[1] == "--help":
  print("Reads the file given as the first argument that consists of scores and names in the format \"score - name\\n\" and displays them sorted by score")
  print("Score is taken as a time in minutes and seconds (with decimal points) in the format MM:SS, or just a number.")
  print("The second argument should be the game name")
  print("The third argument is whether the scores should be `ascending` or `decending`");
  exit()

while True:
  #print("\n " + sys.argv[2] + " Leader Board\n")

  output = ""
  f = Figlet()
  output += f.renderText("Leader Board")

  scores = []
  with open(sys.argv[1], "r") as f:
    scores = f.readlines();

  if len(scores) < 1:
    continue

  scoreType = "number"
  if ":" in scores[0]:
    scoreType = "time"


  for i in xrange(len(scores)):
    data = scores[i].split("-")
    if(scoreType == "time"):
      # Have to convert to a stupid datetime to make it work then strip out the time part
      scores[i] = (datetime.strptime("1/1/17 0:" + data[0].strip(), "%d/%m/%y %H:%M:%S.%f").time(), data[1].strip())
    else:
      scores[i] = (float(data[0].strip()), data[1].strip())

  setReverse = True
  if sys.argv[3] == "ascending":
    setReverse = False

  scores = sorted(scores, key=lambda x: x[0], reverse=setReverse)

  if scoreType == "time":
    for s in scores:
      eqName = (s[1]+"          ")[:10]
      output += "\n  " + eqName + " - " + '%02.0d:%02.0d.%s'%(s[0].minute, s[0].second, str(s[0].microsecond)[:3])

  if scoreType == "number":
    for s in scores:
      eqName = (s[1]+"          ")[:10]
      output += "\n  " + eqName + " - " + str(s[0])
  
  os.system("clear")
  print output
  sleep(10)

