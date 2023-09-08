#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    arg_len = len(argv) - 1
    if arg_len == 0:
        print("{:d} arguments.".format(arg_len))
    else:
        comment = "{:d} argument:".format(arg_len) if arg_len == 1 else "{:d} arguments:".format(arg_len)
        print(comment)
        count = 0
        for arg in argv:
            if count != 0:
                print("{:d}: {}".format(count, arg))
            count += 1
