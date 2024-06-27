import colorgram

# Extract 6 colors from an image.
colors = colorgram.extract('B:\\Python\\Day-18\\Project\\asset.jpg', 10)
list_of_colors = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    color = (r, g, b)
    list_of_colors.append(color)