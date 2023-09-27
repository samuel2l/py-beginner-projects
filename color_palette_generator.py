import numpy as np
from PIL import Image, ImageOps
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        img_file = request.files['file']
        color_code = request.form['color_code']
        colors = give_most_hex(img_file.stream, color_code)
        return render_template('color_gen.html',
                               colors_list=colors,
                               code=color_code)
    return render_template('color_gen.html')


def rgb_to_hex(rgb):
    return '%02x%02x%02x' % rgb


def give_most_hex(path, code):
    img = Image.open(path).convert('RGB')
    size = img.size
    if size[0] >= 400 or size[1] >= 400:
        img = ImageOps.scale(image=img, factor=0.2)
    elif size[0] >= 600 or size[1] >= 600:
        img = ImageOps.scale(image=img, factor=0.4)
    elif size[0] >= 800 or size[1] >= 800:
        img = ImageOps.scale(image=img, factor=0.5)
    elif size[0] >= 1200 or size[1] >= 1200:
        img = ImageOps.scale(image=img, factor=0.6)
    img = ImageOps.posterize(img, 2)
    image_array = np.array(img)


    unique_colors = {}
    for column in image_array:
        for rgb in column:
            t_rgb = tuple(rgb)
            if t_rgb not in unique_colors:
                unique_colors[t_rgb] = 0
            if t_rgb in unique_colors:
                unique_colors[t_rgb] += 1

    #sort it but we want top 10 so since it is in asc we reverse it to get desc
    sorted_unique_colors = sorted(
        unique_colors.items(), key=lambda x: x[1],
        reverse=True)
#unique_colors dictionary. Each item is represented as a tuple where the first element is the RGB color (the key), and the second element is the count of occurrences (the value).

#key=lambda x: x[1]: This is a lambda function that specifies the sorting key. In this case, it's sorting based on the second element of each tuple, which is the count of occurrences (the value). x[1] extracts the value from each tuple.
    converted_dict = dict(sorted_unique_colors)
    # print(converted_dict)


    values = list(converted_dict.keys())
    main_colors = values[0:3]

    # code to convert rgb to hex
    if code == 'hex':
        hex_list = []
        for color in main_colors:
            hex = rgb_to_hex(color)
            hex_list.append(hex)
        return hex_list
    else:
        return main_colors






if __name__ == '__main__':
    app.run(debug=True)