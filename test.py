import subprocess

# init command
cmd = "arecord -Dac108 -f S32_LE -r 48000 -c 4 -d 2"

# excute ffmpeg command
pipe = subprocess.run(cmd,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    shell=True
                    )


# print(pipe.stderr)
print(type(pipe.stdout))
print(len(pipe.stdout))
