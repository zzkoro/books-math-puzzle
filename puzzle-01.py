

def is_sym(src):
    rev = ''.join(reversed(src))
    if rev == src:
        return True
    else:
        return False

def to_num_str(num):
    return str(num)

def to_bin_str(num):
    return bin(num)[2:]

def to_oct_str(num):
    return oct(num)[2:]


if __name__ == "__main__":
    n = 111
    while True:
        if is_sym(to_num_str(n)) and is_sym(to_bin_str(n)) and is_sym(to_oct_str(n)):
            break
        else:
            n = n+2

    
    print('대칭수:', n)
