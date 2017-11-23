#! /bin/bash
LINELEN=150
while true; do clear; printf "\n\n"; python assets/getTimeLeft.py end_date.data | figlet -f assets/shefjam.flf -w $LINELEN; sleep 0.25; done

#while true; do clear; python assets/getTimeLeft.py end_date.data | figlet -c -f assets/modular.flf; sleep 0.25; done
#center(){ l="$(cat -)"; s=$(echo -e "$l"| wc -L); echo "$l" | while read l;do j=$(((s-${#l})/2));echo "$(while ((--j>0)); do printf " ";done;)$l";done;};

