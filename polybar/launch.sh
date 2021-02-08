#!/usr/bin/bash

killall -q polybar
while pgrep -u $UID -x polybar >/dev/null; do sleep 1; done
polybar bspwm 2>&1 | tee -a /tmp/polybar1.log & disown
