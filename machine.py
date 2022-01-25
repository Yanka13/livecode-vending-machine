from enum import Enum


class Rack():
    def __init__(self,code, name, price):
        self.code = code
        self.name = name
        self.price = price
        self.quantity = 0


class Coin(Enum):
    NICKEL = 5
    DIME = 10
    QUARTIER = 25
    DOLLAR = 100


class Machine():
    def __init__(self, racks, coins_count=10):
        self.racks = dict((rack.code, rack) for rack in racks)
        self.coins = dict((coin, coins_count) for coin in Coin)
        self.amount = 0


    def refill(self, code, quantity):
        self.racks[code].quantity += quantity


    def insert(self, coin):
        self.coins[coin] += 1
        self.amount += coin.value

    def give_change_back(self, change):
        if change == 0:
                  return True
        else:
            for coin in reversed(Coin):
                if self.coins[coin] > 0:
                    count = change // coin.value
                    change = change % coin.value
                    self.coins[coin] -= count

    def press(self, code):
        rack = self.racks[code]

        #check if there is enough stock
        if rack.quantity >= 1:

            #check if user has put enough money
            if self.amount  >= rack.price:
                rack.quantity -= 1

                change = self.amount - rack.price
                self.give_change_back(change)
                self.amount -= rack.price
                return True
            else:
                #TODO Give feedback to user explaining he has not enough money
                return False

        else:
            # TODO GIVE feedback to user saying that stocks are empty
            return False


if __name__ == "__main__":
    racks = [Rack("A", "", 100), Rack("C", "", 85)]
    racks = dict((rack.code, rack) for rack in racks)
    print(racks)

    for coin in Coin:
        print(coin, coin.value)
