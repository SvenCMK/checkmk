#!/usr/bin/env python3

import argparse
import platform

#####  some variables #####
server = "" # let this empty to use systems hostname
site = ""
protocol = "https" # change to http if your update server doesn't provide SSL

os = str.lower(platform.system()) # set windows or linux
if len(server) < 1:
    server = str.lower(platform.node())

parser=argparse.ArgumentParser(description="This script is to register your host to checkmk.")
parser.add_argument('server', metavar='s', type=str, help='Address of the Checkmk site in the format "<server>" or "<server>:<port>"')

print("os: "+os)
print("server: "+ server)
args = parser.parse_args()
print(args)


def register_tls():
    pass
def register_updater():
    pass


