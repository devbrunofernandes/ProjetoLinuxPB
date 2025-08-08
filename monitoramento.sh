#!/bin/bash
IP_DO_SERVIDOR=$(ip addr show dev enp0s3 | grep "inet " | awk '{print $2}' | cut -d/ -f1)
python3 /var/script/monitoramento.py $IP_DO_SERVIDOR