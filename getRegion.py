#! /usr/bin/python3

import requests
r = requests.get("http://169.254.169.254/latest/meta-data/placement/availability-zone")

print list(r.iter_content(chunk_size=1024))[0].decode('ascii')[:-1]

