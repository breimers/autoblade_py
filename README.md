READ ME:

*This project probably took almost 2 hours

*First time using subprocesses, so please comment on any best practices

*ffmpeg is great and makes sense, but subprocesses is another beast


Purpose:

	Divide a mp4 video file into 'n'  equal duration segments


Dependencies:

	ffmpeg (system), python3 (system), subprocesses (python3), time(python3)


Use:

	$python3 autoblade.py

	-->enter file name

	-->enter number of splits


Output:

	output00$.mp4 *n
