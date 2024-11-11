import threading, random, time

class Bank:
    lock = threading.Lock()

    def __init__(self):
        self.balance = 0

    def deposit(self):
        for i in range(100):
            random_deposit = random.randint(50, 500)
            self.balance += random_deposit
            print(f'Пополнение: {random_deposit}. Баланс: {self.balance}')
            time.sleep(0.001)
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()


    def take(self):
        for i in range(100):
            random_take = random.randint(50, 500)
            print(f'Запрос на {random_take}')
            if random_take <= self.balance:
                self.balance -= random_take
                print(f'Снятие: {random_take}. Баланс: {self.balance}')
            else:
                self.lock.acquire()
                print(f'Запрос на {random_take} отклонён, недостаточно средства')


bk = Bank()
th1 = threading.Thread(target=Bank.deposit, args=(bk, ))
th2 = threading.Thread(target=Bank.take, args=(bk, ))
th1.start()
th2.start()
th1.join()
th2.join()
print(f'Итоговый баланс: {bk.balance}')
