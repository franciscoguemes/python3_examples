#!/usr/bin/python3

# This example shows how to execute a command (i.e. an application) that will run in a separate child
# process. This separate child process is detached from the parent process on which this program is being
# executed, therefore the child process will continue running once this programme has finished.
#
# This example starts the module http.server from the command in Linux.
#   The example runs the http server in a separate process and prints in the command line
#   the instructions to stop the child process.
# Once the programme finishes the http.server is expected to continue running in background.

import subprocess

DEFAULT_PORT = 8000


def execute(command):
    web_server_process = subprocess.Popen(command,
                                          stdin=None,
                                          stdout=None,
                                          stderr=None,
                                          close_fds=True)
    print(f"In order to stop child process where http.server is being executed type: kill -9 {web_server_process.pid}")


if __name__ == '__main__':
    cmd = ['python3', '-m', 'http.server', str(DEFAULT_PORT)]
    execute(cmd)
