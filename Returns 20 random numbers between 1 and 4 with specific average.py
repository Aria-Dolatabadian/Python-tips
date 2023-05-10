from random import randint


def show_ave(user_ave, count: int, range_num: int):
    i = [range_num for _ in range(20) ]

    if sum(i) / count <= user_ave:
        return "user average is greater then average of all numbers"

    while True:
        temp_numbers = []
        for _ in range(count):
            temp_numbers.append(randint(1, range_num))

        if sum(temp_numbers) / count == user_ave:
            return temp_numbers


print(show_ave(2.15, 20, 4))
