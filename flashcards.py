# Quick Flash Cards - Sam H. 2019

import webbrowser
import os
from jinja2 import Environment, FileSystemLoader
root = os.path.dirname(os.path.abspath(__file__))

data={}

# open flashcard data
card_data_file = open(root + "\\cards_data.txt", "r")
card_data = card_data_file.readlines()

# extract answer / question, skip first line as this contains the title.
for item in card_data[2:]:
    question = item.split(":")[0]
    answer = item.split(":")[1]
    data[question]=answer
print(data)

# set card title (first element in data, actual card data begins at third element)
title = card_data[0].split(":")[1]

# author is second element
author = card_data[1].split(":")[1]

# settings
use_gradient = True
card_color_front_gradient = ["#ffffff", "#e0e0e0"]
card_color_back_gradient = ["#e0e0e0", "#ffffff"]
card_color_front = "#fff"
card_color_back = "#d5e7f7"
card_text_color = "#000000"

# card template
templates_dir = os.path.join(root, 'templates')
env = Environment( loader = FileSystemLoader(templates_dir) )
template = env.get_template('template.html')
 
# card output html file
filename = os.path.join(root, 'html', 'flashcards.html')
with open(filename, 'w') as fh:
    fh.write(template.render(
        card_color_front = card_color_front,
        card_color_back = card_color_back,
        questions = data,
        title=title,
        use_gradient=use_gradient,
        card_color_front_gradient=card_color_front_gradient,
        card_color_back_gradient=card_color_back_gradient,
        card_text_color=card_text_color,
        author=author
    ))

# open browser after card generation
webbrowser.open(filename)