import threading

class FizzBuzz(object):
    def __init__(self, n):
        self.n = n
        self.curr = 1
        self.lock = threading.Lock()
        self.cond = threading.Condition(self.lock)

    def fizz(self, printFizz):
        while True:
            with self.cond:
                while self.curr <= self.n and (self.curr % 3 != 0 or self.curr % 5 == 0):
                    self.cond.wait()

                if self.curr > self.n:
                    self.cond.notify_all()
                    return

                printFizz()
                self.curr += 1
                self.cond.notify_all()

    def buzz(self, printBuzz):
        while True:
            with self.cond:
                while self.curr <= self.n and (self.curr % 5 != 0 or self.curr % 3 == 0):
                    self.cond.wait()

                if self.curr > self.n:
                    self.cond.notify_all()
                    return

                printBuzz()
                self.curr += 1
                self.cond.notify_all()

    def fizzbuzz(self, printFizzBuzz):
        while True:
            with self.cond:
                while self.curr <= self.n and (self.curr % 5 != 0 or self.curr % 3 != 0):
                    self.cond.wait()

                if self.curr > self.n:
                    self.cond.notify_all()
                    return

                printFizzBuzz()
                self.curr += 1
                self.cond.notify_all()

    def number(self, printNumber):
        while True:
            with self.cond:
                while self.curr <= self.n and (self.curr % 3 == 0 or self.curr % 5 == 0):
                    self.cond.wait()

                if self.curr > self.n:
                    self.cond.notify_all()
                    return

                printNumber(self.curr)
                self.curr += 1
                self.cond.notify_all()