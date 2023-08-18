# import solara
#
# # Declare reactive variables at the top level. Components using these variables
# # will be re-executed when their values change.
# sentence = solara.reactive("Solara makes our team more productive.")
# word_limit = solara.reactive(10)
#
#
# @solara.component
# def Page():
#     # Calculate word_count within the component to ensure re-execution when reactive variables change.
#     word_count = len(sentence.value.split())
#
#     solara.SliderInt("Word limit", value=word_limit, min=2, max=20)
#     solara.InputText(label="Your sentence", value=sentence, continuous_update=True)
#
#     # Display messages based on the current word count and word limit.
#     if word_count >= int(word_limit.value):
#         solara.Error(f"With {word_count} words, you passed the word limit of {word_limit.value}.")
#     elif word_count >= int(0.8 * word_limit.value):
#         solara.Warning(f"With {word_count} words, you are close to the word limit of {word_limit.value}.")
#     else:
#         solara.Success("Great short writing!")
#
# # The following line is required only when running the code in a Jupyter notebook:
# # Page()

from flask import Flask
import solara.server.flask
from flask import Flask, render_template_string

from sol import Page

app = Flask(__name__)
app.register_blueprint(solara.server.flask.blueprint, url_prefix="/solara/")

@app.route("/")
def hello_world():
    return render_template_string("""
    <p>Hello, World!</p>
    <iframe src="/solara/Page" width="100%" height="600px"></iframe>
    """)
