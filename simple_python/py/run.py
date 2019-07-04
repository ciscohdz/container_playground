import itertools
import socket

def main():
    list(map(lambda x: print(x, end="-"), list(range(0,4))))
    print("")


if __name__ == "__main__":
    print("Host --> " + socket.gethostname())
    main()
    