class counter:
    def reset(self, initValue):
        self.count = initValue

    def increment(self):
        self.count += 1

    def get(self):
        return self.count
    
a = counter()
a.reset(0)
print(a.get())

b = counter()
b.reset(100)
b.increment()
print(b.get())