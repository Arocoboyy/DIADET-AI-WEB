import time
import eel

eel.init('page')
@eel.expose
def timeFun():
    curr_time=time.strftime("%H:%M:%S")
    return curr_time

eel.start('index.html')