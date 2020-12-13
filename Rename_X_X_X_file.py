import os



def rename_X_X_X_file(path, filename_replace):
    pass  # FIXME

def is_prime(number):
    for element in range(2, number):
        if number % element == 0:
            return False
    return True

def print_next_prime(number):
    index = number
    while True:
        index += 1
        if is_prime(index):
            print(index)

if __name__ == '__main__':
    filename_replace = ["40", "02"]
    path = '../imagevideo/'
    rename_X_X_X_file(path, filename_replace)
