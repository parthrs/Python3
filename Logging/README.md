# Logging

1.  CreateLogger.py - A module wrapping the python logging module to write all messages to a .log file and additionally also print critical messages to the stdout.
2.  ExecuteRemotely.py - A class wrapping the python paramiko library, specifically the exec_command method to execute commands remotely. Uses the create logger module to return a logger object and write to it.
