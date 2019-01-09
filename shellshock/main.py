from shellshock.parse import convert_source
import sys

if __name__ == '__main__':
    print(convert_source(sys.argv[1], include_source=True))
