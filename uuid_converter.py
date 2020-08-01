
import sys
import uuid


class NULL_NAMESPACE:
    bytes = b''


def my_func():
    if (len(sys.argv)) == 1:
        print('\n >>> please, run again like this:')
        print('\n\t python uuid_converter.py <string>')
        exit()
    else:
        new_uuid = str(uuid.uuid3(NULL_NAMESPACE, sys.argv[1]))
        print('\n' + new_uuid)


if __name__ == '__main__':
    my_func()
