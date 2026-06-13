#!/bin/bash

used=$(df / | awk 'NR==2 {print $5}' | sed 's/%//')

free=$((100-used))

echo "Space HDD anda tinggal $free%"
