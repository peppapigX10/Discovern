define you = Character("Dr. [name]")

label start:
    scene main_room

    $ name = renpy.input("Type your name: ")
    you "Hello, you are a psychologist at the hospital Discovern."

    show you at right
    

    return
