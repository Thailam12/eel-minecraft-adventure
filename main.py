import eel
eel.init("web")
@eel.expose
def a():
    return 0

eel.start("index.html")