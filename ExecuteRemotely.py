class ExecuteRemotely():
	"""
	A wrapper class on the paramiko ssh library
	:input:
	:host=<ip address of the host where command needs to be executed>
	:username=<username with which to login to the remote host>
	:output:
	:<string containing either the command execution error or the output>

	This class does not accept or depend on password but mainly relies on passwordless ssh.
	All error other than
	"""

	def __init__(self,**kwargs):

		if not 'host' in kwargs:
			self.host = "192.168.0.1"
			self.username = "pshah"
		else:
			self.host = kwargs['host']
			self.username = kwargs['username']

		self.file_name =  sys.argv[0]
		self.logger = logging.getLogger(self.file_name)

		# From paramiko documentation
		# "A high-level representation of a session with an SSH server.
		# This class wraps Transport, Channel, and SFTPClient to take care of most aspects of authenticating and opening channels."
		self.client = SSHClient()
		self.client.load_system_host_keys()

		#https://stackoverflow.com/a/41718846
		self.client.set_missing_host_key_policy(AutoAddPolicy())


	def run_command(self,command):
		'''
		A wrapper to the exec_command method
		:input:
		command=<command to be executed on the remote host>
		:output:
		:<string containing either the command execution error or the output>
		'''

		# Placeholder return value
		ret_str = ''

		try:
			self.client.connect(self.host, username=self.username)
      
      # Replacing tilda/~ is very specific to my use case
			stdin, stdout, stderr = self.client.exec_command(command.replace('~', '"'))
			err_str = ''.join(stderr.readlines())
			if err_str:
				ret_str = "Execution error: \n" + err_str
			else:
				ret_str = ''.join(stdout.readlines())

		except paramiko.ssh_exception.AuthenticationException as e:
			self.logger.error("Failed to authenticate user {}@{}".format(self.username,self.host))
			return ret_str
		except paramiko.ssh_exception.BadHostKeyException as e:
			self.logger.error("Failed to authenticate the keys on {} (Check the ~/.SSH/authorized_users file on the server.)".format(self.host))
			return ret_str
		except paramiko.ssh_exception.SSHException as e:
			self.logger.error("Exception in SSH negotiation to {}: {}".format(self.host, e))
			return ret_str
		except socket.error as e:
			self.logger.error("Socket exception while connecting to {}: {}".format(self.host, e))
			return ret_str
		except:
			self.logger.error('Failed to connect to {}: {}'.format(self.host, sys.exc_info()[:2]))
			return ret_str
		else:
			return ret_str
      
if __name__ == "__main__":
  s = ExecuteRemotely()
  # ~(Tilda) is used here to be a placeholder for double inverted commas (")
  print(s.run_command(". /opt/environ.ksh; echo -e ~set heading off; \n set pagesize 0; \n set trimspool on; \n select NAME || ',' || ID || ',' || TO_CHAR(TIME_STAMP, 'yyyy-mm-dd hh24:mi:ss') from LOGIN_TIME where TIME_STAMP >= sysdate - interval '10' minute order by TIME_STAMP asc;~ | sqlplus -s pshah/pshah@dataguard"))
