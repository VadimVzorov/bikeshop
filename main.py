from bic import Bicycle, BikeShop, Customer
if __name__ == '__main__':

    bike1 = Bicycle('one', 1, 600)
    bike2 = Bicycle('two', 2, 500)
    bike3 = Bicycle('three', 3, 400)
    bike4 = Bicycle('four', 4, 300)
    bike5 = Bicycle('five', 5, 200)
    bike6 = Bicycle('six', 6, 100)

    LightBeam = BikeShop('LightBeam', 0.2, [bike1, bike2, bike3, bike4, bike5, bike6])

    customer1 = Customer('vadim', 400)
    customer2 = Customer('emily', 800)
    customer3 = Customer('nastya', 900)
    customer1.buy(LightBeam)
    customer2.buy(LightBeam)
    customer3.buy(LightBeam)
