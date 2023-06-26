import subprocess
import shlex
# init command


cmd = 'arecord -Dac108 -f S32_LE -r 48000 -c 4 -d 10'
cmd = shlex.split(cmd)

# excute ffmpeg command
pipe = subprocess.Popen(cmd,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.STDOUT,
                    # bufsize=1000
                    )


# header
s = pipe.stdout.read(124)

size = 768000
count = 0

s = bytes(0)

while True:
    frame = pipe.stdout.read(size)
    if len(frame) == 0:
        break
    else:
        count += 1

print(frame)
print(count * size)
print((count * size) / 7680000)