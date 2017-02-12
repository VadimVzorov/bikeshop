import random

class Bicycle(object):
    def __init__(self, model, weight, cost):
        self.model = model
        self.wight = weight
        self.cost = cost

class BikeShop(object):
    def __init__(self, name, margin, invent=[], price_list={}, account=0, profit=0, net_profit=0):
        self.name = name
        self.invent = invent
        self.margin = margin
        self.price_list = self.create_pricelist()
        self.account = account
        self.profit = profit
        self.net_profit = net_profit

    def create_pricelist(self):
        price_list = {}
        for bike in self.invent:
            price = bike.cost * (1 + self.margin)
            price_list[bike] = price
        return price_list

    def sell(self, bike):
        self.invent.remove(bike)
        print(self.name, 'has these bikes left:')
        for x in self.invent:
            print(x.model)
        print('\n')
        self.account += self.price_list[bike]
        self.net_profit += self.price_list[bike] - bike.cost
        print('Total net profit of', self.name, 'is $', self.net_profit)
        self.price_list.pop(bike)

    def get_profit(self):
        pass
        #calculate total profit from the information about the deal

class Customer(object):
    def __init__(self, name, money=0, bikes_owned=[]):
        self.name = name
        self.money = money
        self.bikes_owned = bikes_owned

    def identify_bikes(self, bike_shop):
        potential_bikes=[]
        print(bike_shop.name + ' currently have:')
        for x in bike_shop.invent:
            print(x.model)
        print('\n')
        print(self.name + ' can afford:')
        for x in bike_shop.price_list:
            if bike_shop.price_list[x] <= self.money:
                potential_bikes.append(x)
                print(x.model)
        print('\n')
        return potential_bikes

    def buy(self, bike_shop):
        choice = random.choice(self.identify_bikes(bike_shop))
        print(self.name + ' chooses bike ' + choice.model)
        print('\n')
        self.money -= bike_shop.price_list[choice]
        print(self.name, 'has $', self.money, 'left', '\n')
        self.bikes_owned.append(choice)
        bike_shop.sell(choice)


        #check if already owns the bike
        #make a purchase
        # choice = input('Choose your bike: ')
        # if calc_price(choice) <= sel:
        #     pass
        #subtract purchase from funds
