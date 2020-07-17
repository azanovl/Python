import time
def pause(sec):
    for _ in range(sec):
        print("* ", end="")
        time.sleep(1)

class Trafficllight:
    __color = None
    def running(self):
        print("\r\033[31m {}".format("RED"), end="")
        pause(7)
        print("\r\033[33m {}".format("YELLOW"), end="")
        pause(2)
        print("\r\033[32m {}".format("GREEN"), end="")
        pause(7)
        print("\r\033[33m {}".format("YELLOW"), end="")
        pause(2)
        print("\r\033[31m {}".format("RED"), end="")
        pause(7)

a = Trafficllight()
a.running()
