#!/bin/bash

# Nama layanan proxy, ganti sesuai dengan layanan proxy yang Anda gunakan
SERVICE="squid"

# Cek status dari layanan
systemctl is-active --quiet $SERVICE
if [ $? -ne 0 ]; then
    echo "$(date): Proxy service is down, restarting..."
    systemctl restart $SERVICE
    echo "$(date): Proxy service restarted."
else
    echo "$(date): Proxy service is running fine."
fi
