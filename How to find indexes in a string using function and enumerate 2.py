def func():
    x = "AAATAAAAAATAAA"
    for index, item in enumerate(x):
        if item == "T":
            print(index,"is index of ", item)
func()
