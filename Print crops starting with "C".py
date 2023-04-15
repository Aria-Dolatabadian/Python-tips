Crop = "Wheat Barley Rice Soybean Corn Canola"
lst = list(filter(
        lambda x:"c"==x[0].lower(),
        Crop.split(" ")
))

print(*lst, sep="\n")
