#!/bin/bash
python -c "from pyfiglet import Figlet; print(Figlet(font=\"assets/shefjam.flf\", width=150).renderText(\"ShefJam V:  Powerless\"))"
echo "Tweet us with #shefjamV!"

# Just stop the prompt from coming back up...
# Could use sleep, but this keeps it open indefinitely
# Even if there is that annoying little input box.
read -p "" q
