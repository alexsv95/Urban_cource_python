import threading
import time

class Knight(threading.Thread):
    def __init__(self, name: str, power: int):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power

    def run(self):
        enemys = 100
        day = 0
        print(f'{self.name}, на нас напали')
        while enemys:
            enemys -= self.power
            day += 1
            time.sleep(1)
            print(f'{self.name} сражается {day} день(дня), осталось {enemys} врагов')
        print(f'{self.name} одержал победу спустя {day} дней(дня)')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()
first_knight.join()
print('Все битвы закончились')