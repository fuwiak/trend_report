# import solara
#
#
# color = solara.reactive("red")
#
#
# @solara.component
# def Page():
#     solara.Select(label="Color", values=["red", "green", "blue", "orange"], value=color)
#     solara.Markdown("## Hello World", style={"color": color.value})
#
#
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
  return "Hello World!"
