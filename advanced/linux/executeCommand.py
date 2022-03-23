#!/usr/bin/python3

# Example on how to execute the 'ls -l .' command in Linux.
#
# TODO: Make the output to be as the original in LINUX.

import subprocess

process = subprocess.Popen(['ls', '-l', '.'],
                         stdout=subprocess.PIPE,
                         stderr=subprocess.STDOUT)
#This call to communicate() is a blocking call, this means that the parent process will be stoped until the child process finish its work.
stdout, stderr = process.communicate()
print(stdout)
print(stderr)
