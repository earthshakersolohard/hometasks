from time import sleep

class TrafficLight:
    __color = 'Red'

    def running(self, count, red_time, yellow_time, green_time):
        while count > 0:
            self.__color = 'Red'
            print(f'\033[31m{self.__color}')
            for i in range(1, red_time + 1):
                sleep(1)
                print(f'\033[31m{i} сек')

            self.__color = 'Yellow'
            print(f'\033[33m{self.__color}')
            for i in range(1, yellow_time + 1):
                sleep(1)
                print(f'\033[33m{i} сек')

            self.__color = 'Green'
            print(f'\033[32m{self.__color}')
            for i in range(1, green_time + 1):
                sleep(1)
                print(f'\033[32m{i} сек')

            count -= 1

t = TrafficLight()
t.running(3,7,2,7)
