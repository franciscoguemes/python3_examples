#!/usr/bin/python3

# In this example I got real time output from the child process in the stdout and stderr. To achive this
# I use threads since I am streaming two pipes at the same time.
#
# See more info at:
#   https://kevinmccarthy.org/2016/07/25/streaming-subprocess-stdin-and-stdout-with-asyncio-in-python/
#   https://stackoverflow.com/questions/18421757/live-output-from-subprocess-command
#   https://stackoverflow.com/questions/803265/getting-realtime-output-using-subprocess
#   https://docs.python.org/3/library/asyncio-subprocess.html

import asyncio


async def _read_stream(stream, cb):
    while True:
        line = await stream.readline()
        if line:
            cb(line)
        else:
            break


async def _stream_subprocess(cmd, stdout_cb, stderr_cb):
    process = await asyncio.create_subprocess_exec(*cmd,
            stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)

    await asyncio.wait([
        _read_stream(process.stdout, stdout_cb),
        _read_stream(process.stderr, stderr_cb)
    ])
    return await process.wait()


def execute(cmd, stdout_cb, stderr_cb):
    loop = asyncio.get_event_loop()
    rc = loop.run_until_complete(
        _stream_subprocess(
            cmd,
            stdout_cb,
            stderr_cb,
    ))
    loop.close()
    return rc


if __name__ == '__main__':
    cmd = "ping -c10 www.franciscoguemes.com && sleep 1 && echo this would be an error! 1>&2 "
    print(execute(
        ["bash", "-c", cmd],
        lambda x: print("STDOUT: %s" % x),
        lambda x: print("STDERR: %s" % x),
        ))
    # print(execute(
    #     ["bash", "-c", "echo hello world! && echo stdout && sleep 1 && echo stderr 1>&2 && sleep 1 && echo done"],
    #     lambda x: print("STDOUT: %s" % x),
    #     lambda x: print("STDERR: %s" % x),
    # ))