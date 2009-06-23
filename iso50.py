#!/usr/bin/env python 
import urllib
import urllib2 
import sys 
import re
import subprocess

file_path = ""
base_url = "http://blog.iso50.com/page/"

#global rem_file

def dlProgress( count, blockSize, totalSize):
	percent = int(count*blockSize*100/totalSize)
	#sys.stdout.write("\r" + rem_file + "...%d%%" % percent)
	sys.stdout.write( "\r" + "...%d%%" % percent)
	sys.stdout.flush()

def fFileExists(filePath):
	try: 
		st = os.stat(filePath) 
	except OSError: 
		# TODO: should check that Errno is 2 
		return False 
	return True

def download(url, filePath):
	failedDownload = False
	try:
		#rem_file = f
		urllib.urlretrieve(url, filePath, reporthook=dlProgress)
		print
	except:
		print "exception: n  %s, n  %s, n  %s n  when downloading %s" % (sys.exc_info()[0], sys.exc_info()[1], sys.exc_info()[2], url)
		failedDownload = True
	# remove potentially only partially downloaded file
	if failedDownload and fFileExists(filePath):
		removeRetryCount = 0
		while removeRetryCount < 3:
			time.sleep(1) # try to sleep to make the time for the file not be used anymore
			try:
				os.remove(filePath)
				break
			except:
				print "exception: n  %s, n  %s, n  %s n  when trying to remove file %s" % (sys.exc_info()[0], sys.exc_info()[1], sys.exc_info()[2], filePath)
				removeRetryCount += 1

def main():
	for i in range(1, 2): 
		page_url = "%s%d" % (base_url, i) 
		for line in  urllib2.urlopen(page_url):
			files = re.findall("soundFile=.*\.mp3", line)
			for f in files:
				f = urllib2.unquote(f.lstrip("soundFile="))
				print "Downloading %s" % (f)
				#subprocess.call(["wget", "-nc", f]) 
				#urllib.urlretrieve( f, download_dir)
#				download(f, file_path)



if __name__=="__main__":
	main()

