#! /usr/bin/env python

import os
import urllib
import cgi
import subprocess
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--file", "-f", type=str, required=True)
args = parser.parse_args()
filename = args.file

fname = filename.split(".")[0]
extension = filename.split(".")[1:]

if "testResult" in fname:
    print filename
    watch_instance = 'python watch_testResults.py {0}'.format(filename)
    subprocess.call(watch_instance, shell=True)

if "instanceHealth" in fname:
    print filename
    watch_instance = 'python watch_instance.py {0}'.format(filename)
    subprocess.call(watch_instance, shell=True)

print "The html file is served from templates/"
