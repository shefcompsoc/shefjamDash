import sys
from time import sleep
from pyfiglet import Figlet
from datetime import datetime, date, time, timedelta

end = sys.argv[1]
end = datetime.strptime(end.strip(), "%d/%m/%y %H:%M:%S")

f = Figlet(font="assets/shefjam.flf", width=100)

while True:
    now = datetime.now()

    if end < now:
        diff = "00:00:00"
    else:
        diff = end - now
        diff = '%02.0d:%02.0d:%02.0d' % (diff.total_seconds() // 3600, (diff.total_seconds() // 60) % 60, diff.total_seconds() % 60)

    # clear screen
    sys.stderr.write("\x1b[2J\x1b[H")

    # print figlet
    print(f.renderText(diff))

    # wait for next second
    sleep(1)
