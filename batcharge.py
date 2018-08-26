#!/usr/bin/env python3
# coding=UTF-8

import re
import subprocess
import sys

commands = {'Linux': 'acpi', 'Darwin': 'pmset -g batt'}

def format_output(batt_percent, battery_number):
  color_green = '%{[32m%}'
  color_yellow = '%{[1;33m%}'
  color_red = '%{[31m%}'
  num_only = re.match(r'\d{2,3}', batt_percent).group()
  color_option = int(num_only)/10
  color_out = (
    color_green if color_option > 6
    else color_yellow if color_option > 4
    else color_red
  )

  return color_out + ' ['+str(battery_number) +':' + num_only +' ♥] '


system_type = subprocess.getoutput('uname')
battery_info = subprocess.getoutput(commands[system_type])


pattern = re.compile(r'\d{2,3}%', re.I)
batteries = pattern.finditer(battery_info)
battery_life = ''
battery_number = 0

for battery in batteries:
  battery_life += format_output(battery.group(), battery_number)
  battery_number += 1

sys.stdout.write(battery_life)
