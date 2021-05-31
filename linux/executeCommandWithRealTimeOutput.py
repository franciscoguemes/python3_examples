#!/usr/bin/python3

# This is first approach to execute a command in a child process and get real time output.
# As you can see in this example there is no call to process.communicate() because it would stop the parent process
# until the child process has finished. Therefore in this example basically I basically bind the child process
# stdout to a pipe and then I read from the pipe the stdout and print it in the parent process.
#
# If you would like to get also the stderr in real time you can not do it with 2 pipes, you will need to use threads.
# To see an example of this, see the next example :-)
#
# See more info at:
#   https://stackoverflow.com/questions/803265/getting-realtime-output-using-subprocess

import subprocess
import sys


def execute(command):
    child_process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
    while child_process.poll() is None:
        out_stdout = child_process.stdout.readline()
        if out_stdout != b'':
            sys.stdout.write(out_stdout.decode(sys.stdout.encoding))
            sys.stdout.flush()


if __name__ == '__main__':
    cmd = "ping -c4 www.franciscoguemes.com"
    execute(cmd)

