import urllib.request
import urllib.error
import re
import sys
import time
import os
import pipes

def video_to_audio(fileName):
	try:
		file, file_extension = os.path.splitext(fileName)
		file = pipes.quote(file)
		video_to_wav = 'ffmpeg -i ' + file + file_extension + ' ' + file + '.wav'
		final_audio = 'lame '+ file + '.wav' + ' ' + file + '.mp3'
		os.system(video_to_wav)
		os.system(final_audio)
		print("sucessfully converted ", fileName, " into audio!")
	except OSError as err:
		print(err.reason)
		exit(1)

def main():
	if len(sys.argv) <1 or len(sys.argv) > 2:
		print('command usage: python3 video_to_audio.py FileName')
		exit(1)
	else:
		filePath = sys.argv[1]  # check if the specified file exists or not
		try:
			if os.path.exists(filePath):
				print("file found!")
		except OSError as err:
			print(err.reason)
			exit(1)
		video_to_audio(filePath)  # convert video to audio
		time.sleep(1)

if __name__ == '__main__':
	main()
