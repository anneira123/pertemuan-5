class Ticket:
    def __init__(self, number):
        self.number = number
    def __add__(self, other):
        return self.number + other.number
    
ticket1 = Ticket(1)
ticket2 = Ticket(2)

print ("total penjualan tiket:", ticket1 + ticket2)