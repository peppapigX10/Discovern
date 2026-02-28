define you = Character("Dr. [name]")
define h = Character("Dr. Helper")


label start:
    scene main_room

    $ name = renpy.input("Type your name: ")
    you "Hello, you are a med student at the mental hospital Discovern."

    show you at right
    show patient1 at left 

    

    return
