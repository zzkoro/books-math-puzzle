import re

def calc():
    lst = [ 0 for _ in range(100)]

    for n in range(1,100):
        for idx in range(n, 100, n+1):
            if lst[idx] == 0:
                lst[idx] = 1
            else:
                lst[idx] = 0

    back_card = list()

    card_num = 1
    for card_status in lst:  # 1: 앞면, 0: 뒷면이 위인 상태
        if card_status == 0:
            back_card.append(card_num)
        card_num += 1

    print("back_card:{}".format(back_card))

if __name__ == "__main__":
   calc()
