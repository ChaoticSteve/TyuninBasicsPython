class TrafficLight:
    def __init__(self, colour='red'):
        self.__colour = colour

    def switch(self):
        import time
        if self.__colour == 'red':
            self.__colour = 'yellow'
            time.sleep(7)
        elif self.__colour == 'yellow':
            self.__colour = 'green'
            time.sleep(2)
        elif self.__colour == 'green':
            self.__colour = 'red'
            time.sleep(5)

    def running(self):
        for _ in range(3):
            print(self.__colour)
            self.switch()



trafficlight = TrafficLight()
trafficlight.running()
