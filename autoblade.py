import subprocess
import time
import sys

fname=input("file: ")
splits=input("splits: ")
try:
    #write duration cmd: getting duration from probing the metadata of an mp4, and filtering with regex
    dur_cmd = "ffprobe -i "+fname+" -show_entries format=duration -v quiet |grep duration| sed 's/.*=//'"
    #run duration cmd and set communicate() to string
    duration=str(subprocess.Popen(dur_cmd, shell=True, stdout=subprocess.PIPE, universal_newlines=True).communicate()[0])
    #get desired length from total duration (convert to float) and number of splits (also float for consistency
    length=float(duration)/float(splits)
    #use time to convert seconds to timecode format
    timecode=time.strftime('%H:%M:%S', time.gmtime(length))

    #split video, copy first section, repeat for given timecode
    spl_cmd = 'ffmpeg -i '+fname+ ' -c copy -map 0 -segment_time '+timecode+'  -f segment -reset_timestamps 1 output%03d.mp4'
    subprocess.Popen(spl_cmd.split())
except:
    #a really bad exception handler :(
    print("Exception!: filename should be string // splits should be int")
