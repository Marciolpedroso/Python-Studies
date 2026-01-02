on = False
channel = 1
volume = 10

def turnOn():
    global on
    on = True

def turnOff():
    global on
    on = False

def increaseVolume():
    global volume
    if on == True and volume < 100:
        volume = +1

def decreaseVolume():
    global volume
    if on == True and volume > 0:
        volume = -1

def nextChannel():
    global channel
    if on == True:
        channel = +1

def previousChannel():
    global channel
    if on == True:
        channel = -1

def setChannel(newChannel):
    global channel
    if on == True and newChannel >= 1:
        channel = newChannel

def status():
    print("TV on? " + str(on))
    print("Channel: " + str(channel))
    print("Volume: " + str(volume))

if __name__ == "__main__":
    status()
    turnOn()
    increaseVolume()
    nextChannel()
    status()