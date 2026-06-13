#!/bin/bash

tanggal=$(date +%Y%m%d_%H%M)

tar -czvf /backup/backup_$tanggal.tar.gz /home/abdulajiz12/data
