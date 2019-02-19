READ ME:

*This project probably took almost 2 hours

*First time using subprocesses, so please comment on any best practices

*ffmpeg is great and makes sense, but subprocesses is another beast


Purpose:

	Divide a mp4 video file into 'n'  equal duration segments


Dependencies:

	ffmpeg (system), ffprobe (system), python3 (system), subprocesses (python3), time(python3)


Use:

	$python3 autoblade.py

	-->enter file name

	-->enter number of splits


Output:

	output00$.mp4 *n



Thoughts:
	
	Wow! Who knew passing outputs from a subprocess to string would be so convoluted?

	I first considered using the ffmpy python library instead of subprocesses, but the set-up format was not conductive

	to a multistep task. So I used subprocesses to essentially automate a process the user can do on their own.

	If I wasn't self-imposing a time-limit, I would figure out the ffmpy formatting and check for dependencies in the
	
	script. This way the user is worrying about less.

	Also stackoverflow is amazing and there are some great contributors out there.



To-do:

	Implement using ffmpy
	
	Check for dependencies

	Auto-Install dependencies
	
	Give option for custom filenames



Curiosities:

	Managing subprocesses
	
	Passing data between subprocesses without storing python variable

	Modularity of subprocess commands
