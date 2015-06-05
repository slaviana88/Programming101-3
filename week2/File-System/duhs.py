import sys
import os


path = sys.argv[1]


def bytes_to_gb(b):
    return b / (10 ** -9)


def get_size(path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(path):
        for f in filenames:
            if os.path.exists(f):
                total_size += os.path.getsize(os.path.join(dirpath, f))

    return bytes_to_gb(total_size)

print(get_size(path))
