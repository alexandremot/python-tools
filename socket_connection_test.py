
import socket

def port_test():
	s = socket.socket()
	address = '127.0.0.1'
	port = 5000  # port number is a number, not string
	try:
		s.connect((address, port)) 
		# originally, it was 
		# except Exception, e: 
		# but this syntax is not supported anymore. 
		print(s)
	except Exception as e: 
		print("something's wrong with %s:%d. Exception is %s" % (address, port, e))
	finally:
		s.close()

if __name__ == "__main__":
    port_test()
