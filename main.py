import solara


color = solara.reactive("red")


@solara.component
def Page():
    solara.Select(label="Color", values=["red", "green", "blue", "orange"], value=color)
    solara.Markdown("## Hello World", style={"color": color.value})


