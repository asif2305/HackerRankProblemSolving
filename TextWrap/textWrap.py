import textwrap

from pip._vendor.distlib.compat import raw_input


def wrap(string, data):
    str=""
    for d in range(0,len(string),max_width):
        str+=string[d:d+max_width] +"\n"

    return str


if __name__ == '__main__':
    string, max_width = raw_input(), int(raw_input())
    result = wrap(string, max_width)
    print(result)