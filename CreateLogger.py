#!/usr/local/bin/python3.6

import logging
import logging.handlers
import re

def create_logger(fileName):
	"""
	Returns a logger object. Log level for file is DEBUG (all messages are written), for stream or screen output
	is CRITICAL. Levels: DEBUG < WARNING < ERROR < CRITICAL
	:input:
	:fileName - Name for the logger object. __file__ works best
	:output:
	:Logger object
	"""
	if not fileName:
		return None

	#Creating a logger object with the name of the calling file
	#Need only filename and not the absolute path
	loggerName = re.search('/([^/.]+).py', fileName)[1]		#based on from where the script is called, fileName changes

	logger = logging.getLogger(loggerName)
	logger.setLevel(logging.DEBUG)

	logName = fileName.replace('.py', '.log')

	#Creating a file handler
	fh = logging.handlers.RotatingFileHandler(logName)		#RotatingFileHandler shall append
	fh.setLevel(logging.DEBUG)								#set the log level as debug

	#Creating a stream handler, written to stdout/stderr
	sh = logging.StreamHandler()
	sh.setLevel(logging.CRITICAL)

	#Creating formatters for file and stream handlers
	fileFmt = logging.Formatter(fmt='%(asctime)s,%(threadName)s,%(module)s,line-%(lineno)s,%(levelname)s: %(message)s', datefmt='%Y/%m/%d %H:%M:%S')
	strFmt = logging.Formatter(fmt='%(asctime)s,: %(message)s', datefmt='%H:%M:%S')

	fh.setFormatter(fileFmt)
	sh.setFormatter(strFmt)

	logger.addHandler(fh)
	logger.addHandler(sh)

	return logger

if __name__ == "__main__":
	my_logger = create_logger(__file__)
	my_logger.debug("Test Debug log entry.")
	my_logger.debug("Test Critical log entry.")
