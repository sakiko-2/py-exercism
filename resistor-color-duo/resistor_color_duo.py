def value(colors):
    color_list = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]

    a, b, *c = colors

    return color_list.index(a) * 10 + color_list.index(b)
