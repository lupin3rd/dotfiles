#!/usr/bin/bash
# set -e ensures that the script exits immediately with an error if any of the following commands exit with an error.
set -e

urxvt -e udisksctl unlock -b /dev/sdb6

# Make sure it exists. This is probably unnecessary if the previous command exited without error.
max_loops=50
i=0
while [[ ! -e /dev/dm-0 ]]
do
  sleep 0.1
  i=$((i+1))
  [[ $i -gt $max_loops ]] && exit 1
done

udisksctl mount -b /dev/dm-0
