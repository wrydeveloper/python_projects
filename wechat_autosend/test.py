from threading import Timer

def print_a():
    print('a')
    t = Timer(10, print_a)
    t.start()

if __name__ == '__main__':
    print_a()

