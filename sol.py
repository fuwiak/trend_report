import solara


@solara.component
def ClickButton():
    clicks, set_clicks = solara.use_state(0)

    def my_click_hander():
        set_clicks(clicks + 1)

    solara.Button(label=f"Clicked: {clicks}", on_click=my_click_hander)
    solara.Button(label=f"Reset", on_click=lambda: set_clicks(0))

Page = ClickButton
