import subprocess
import time
import sys

fname=input("file: ")
splits=input("splits: ")
try:
    dur_cmd = "ffprobe -i "+fname+" -show_entries format=duration -v quiet |grep duration| sed 's/.*=//'"
    duration=str(subprocess.Popen(dur_cmd, shell=True, stdout=subprocess.PIPE, universal_newlines=True).communicate()[0])
    length=float(duration)/float(splits)

    timecode=time.strftime('%H:%M:%S', time.gmtime(length))


    spl_cmd = 'ffmpeg -i '+fname+ ' -c copy -map 0 -segment_time '+timecode+'  -f segment -reset_timestamps 1 output%03d.mp4'
    subprocess.Popen(spl_cmd.split())
except:
    print("Exception!: filename should be string // splits should be int")
