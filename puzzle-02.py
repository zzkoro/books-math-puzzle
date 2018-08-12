import re

def calc():
    #op = ["+", "-", "*", "/", ""]
    op = ["*", ""]
    for n in range(1000, 10000):
        s_n = str(n)
        for i in range(len(op)):
            for j in range(len(op)):
                for k in range(len(op)):
                    val = s_n[3] + op[i] + s_n[2] + op[j] + s_n[1] + op[k] + s_n[0]
                    #val = s_n[0] + op[i] + s_n[1] + op[j] + s_n[2] + op[k] + s_n[3]
                    if len(val) > 4:
                        l_val = re.split(r'(\+|-|\*|/)', val)
                        for idx in range(len(l_val)):
                            if l_val[idx][0] == '0':
                                l_val[idx] = str(int(l_val[idx]))
                        try:
                            if n == eval(''.join(l_val)):
                                print("{} = {}".format(val, n))
                        except ZeroDivisionError:
                            pass


if __name__ == "__main__":
   calc()
