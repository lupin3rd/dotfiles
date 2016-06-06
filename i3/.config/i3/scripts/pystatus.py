# -*- coding: utf-8 -*-

import subprocess

from i3pystatus import Status
from i3pystatus.mail import imap

status = Status(standalone=True)


status.register("pulseaudio",
    format="♪ {volume_bar}",
    multi_colors=True,
    color_unmuted='#00ff00',
    vertical_bar_width=2,
    bar_type='vertical')

status.register("clock",
    format="%a %d %b %I:%M:%S",)

# Shows the average load of the last minute and the last 5 minutes
# (the default value for format is used)
status.register("load")

# Shows your CPU temperature, if you have a Intel CPU
status.register("temp",
    format="{temp:.0f}°C",)

# The battery monitor has many formatting options, see README for details
# This would look like this:
# Discharging 6h:51m
status.register("battery",
    format="{status} {remaining:%E%hh:%Mm}",
    alert=True,
    alert_percentage=5,
    status={
        "DIS":  "Discharging",
        "CHR":  "Charging",
        "FULL": "Bat full",
    },)

# Shows the address and up/down state of eth0. If it is up the address is shown in
# green (the default value of color_up) and the CIDR-address is shown
# (i.e. 10.10.10.42/24).
# If it's down just the interface name (eth0) will be displayed in red
# (defaults of format_down and color_down)
#
# Note: the network module requires PyPI package netifaces
status.register("network",
    interface="wlan0",
    format_up="{v4cidr}",)

status.register("mem_bar",
  multi_colors=True
  )

# Shows disk usage of /
# Format:
# 42/128G [86G]
status.register("disk",
    path="/",
    format="HD: {percentage_used}%",)

status.register('cpu_usage_bar',
  cpu='usage_cpu0',
  format='{usage_bar_cpu0}',
  bar_type='vertical'
  )

status.register('cpu_usage_bar',
  cpu='usage_cpu1',
  format='{usage_bar_cpu1}',
  bar_type='vertical')

status.run()
