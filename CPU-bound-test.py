import concurrent.futures
from hashlib import md5
from random import choice

count = 0
list_ = [0, 1, 2, 3, 4]


def get_coin(i):
    while True:
        s = "".join([choice("0123456789") for i in range(50)])
        h = md5(s.encode('utf8')).hexdigest()

        if h.endswith("00000"):
            return s, h


def main():
    with concurrent.futures.ProcessPoolExecutor(max_workers=100) as executor:
        for res in zip(list_, executor.map(get_coin, list_)):
            print(res)


if __name__ == '__main__':
    main()
