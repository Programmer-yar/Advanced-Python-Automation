def convert(R, G, B):
    colors = list((R/255, G/255, B/255))
    print(tuple(colors))


convert(0, 112, 192)