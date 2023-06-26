import subprocess
import shlex
# init command


cmd = "arecord -Dac108 -f S32_LE -r 48000 -c 4 -d 2"
cmd = shlex.split(cmd)

# excute ffmpeg command
pipe = subprocess.Popen(cmd,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.STDOUT,
                    # bufsize=1000
                    )


# print(pipe.stderr)
print(type(pipe.stdout))
print(len(pipe.stdout))
