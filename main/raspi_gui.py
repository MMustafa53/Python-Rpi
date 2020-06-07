from guizero import App, Text, TextBox, PushButton, Slider, Combo, CheckBox, ButtonGroup, info


def deger():
    def highlight():
        text_box.bg = "lightblue"

    def lowlight():
        text_box.bg = "white"

    app = App()
    text_box = TextBox(app)

    # When the mouse enters the TextBox
    text_box.when_mouse_enters = highlight
    # When the mouse leaves the TextBox
    text_box.when_mouse_leaves = lowlight

    def do_this():
        print(text_box.value)

    text_box.when_key_pressed = do_this

    app.display()


def deger_yaz():
    def highlight():
        text_box.bg = "lightblue"

    def lowlight():
        text_box.bg = "white"

    app = App()
    text_box = TextBox(app)

    # When the mouse enters the TextBox
    text_box.when_mouse_enters = highlight
    # When the mouse leaves the TextBox
    text_box.when_mouse_leaves = lowlight

    def do_this():
        print(text_box.value)

    text_box.when_key_pressed = do_this

    app.display()


def change_text_size(slider_value):
    welcome_message.size = slider_value


def do_booking():
    print(book_seats.value)
    info("Booking", "Thank you for booking")


# app = App(title="Hello world", layout="grid")
app = App(title="Hello world")
# welcome_message = Text(app, text="Welcome to my app")
# my_name = TextBox(app)
update_text = PushButton(app, command=deger, text='Değer nedir')
# text_size = Slider(app, command=change_text_size, start=10, end=80)
# my_cat = Picture(app, image="cat.gif")


# film_choice = Combo(app, command=deger_yaz, options=["Star Wars", "Frozen", "Lion King"], grid=[1, 0], align="left")
# print(film_choice.value)
# vip_seat = CheckBox(app, command=deger_yaz, text="VIP seat?", grid=[1, 1], align="left", enabled=True)
# print(vip_seat.value)
# film_description = Text(app, text="Which film?", grid=[0, 0], align="left")
# row_choice = ButtonGroup(app, command=deger_yaz, options=[["Front", "Front"], ["Middle", "Middle"], ["Back", "Back"]],
#                          selected="Middle", horizontal=True, grid=[1, 2], align="left")
# print(row_choice.value)
#
# book_seats = PushButton(app, command=do_booking, text="Book seat", grid=[1, 3], align="left")
# print(book_seats.value)

app.display()
