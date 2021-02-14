
import socket


def port_test():
    s = socket.socket()
    address = '18.231.152.211'
    port = 5000  # port number is a number, not string
    try:
        s.connect((address, port))
        print(s)
    except Exception as e:
        print("something's wrong with %s:%d.")
        print("Exception is %s" % (address, port, e))
    finally:
        s.close()


if __name__ == "__main__":
    port_test()
