from queue import Queue
from random import randint
from threading import Thread
import time


class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None


class Guest(Thread):
    def __init__(self, name):
        Thread.__init__(self)
        self.name = name

    def run(self):
        time.sleep(randint(3,10))


class Cafe:

    def __init__(self, *args):
        self.queue = Queue()
        self.tables = args

    def guest_arrival(self, *guest):
        for g in guest:
            for t in self.tables:
                if t.guest is None:
                    t.guest = g
                    g.start()
                    print(f'{g.name} сел(-а) за стол номер {t.number}')
                    break
            else:
                self.queue.put(g)
                print(f'{g.name} в очереди')
                print('В очереди гостей',self.queue.qsize())


    def discuss_guest(self):
        i = 0
        t_guest = self.tables[i].guest
        while not self.queue.empty() or t_guest:
            if not t_guest.is_alive():
                print(f'{t_guest.name} покушал(-а) и ушел(-а)')
                print(f'Стол номер {self.tables[i].number} свободен')
                t_guest = None
            if not self.queue.empty() and t_guest is None:
                t_guest = self.queue.get()
                print(f'{t_guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {self.tables[i].number}')
                print('В очереди гостей', self.queue.qsize())
            i += 1
            if i == len(self.tables):
                i = 0



tables = [Table(number) for number in range(1, 6)]
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
guests = [Guest(name) for name in guests_names]
cafe = Cafe(*tables)
print(cafe.tables)
cafe.guest_arrival(*guests)
cafe.discuss_guest()