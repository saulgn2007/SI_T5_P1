import keyboard

def tecla(event):
    print(event.name)
    with open("registro.txt", "a") as f:
        f.write(event.name)
        f.write("\n")

keyboard.on_press(tecla)
keyboard.wait()
