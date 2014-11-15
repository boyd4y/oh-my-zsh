#!/usr/bin/env python
# coding=UTF-8

# cp this file to ~/bin/
import math, subprocess

p = subprocess.Popen(["ioreg", "-rc", "AppleSmartBattery"], stdout=subprocess.PIPE)
output = p.communicate()[0]

o_max = [l for l in output.splitlines() if 'MaxCapacity' in l][0]
o_cur = [l for l in output.splitlines() if 'CurrentCapacity' in l][0]

b_max = float(o_max.rpartition('=')[-1].strip())
b_cur = float(o_cur.rpartition('=')[-1].strip())

charge = b_cur / b_max
charge_threshold = int(math.ceil(100 * charge))

# Output
import sys

out =  str(charge_threshold) + '%%'

color_yellow='\033[93m'
color_green='\033[32m'
color_red = '\033[31m'
color_reset = '\033[0m'

color_out = (
    color_green if charge_threshold > 60
    else color_yellow if charge_threshold > 40
    else color_red
)

out = color_out + out + color_reset
sys.stdout.write(out)

