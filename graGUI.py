import random
import time

class stock(object):
    NumOfStocks = 0
    stocksList = []

    def __init__(self, name, price):
        self.boost = random.randint(-5, 5)
        self.name = name
        self.price = price
        self.oldPrice = price
        self.growth = self.growth
        stock.NumOfStocks += 1
        self.pricehistory = []
        self.__class__.stocksList.append(self)

    def growth(self):
        return round((self.price / self.oldPrice - 1) * 100, 2)

    def boost(self):
        if self.price < 50: self.boost += random.randint(0, 2)
        if self.price > 2000: self.boost += random.randint(-2, 0)
        if self.boost > 10: self.boost = 10
        if self.boost < -10: self.boost = -10
        self.boost += random.randint(-1, 1)
        return self.boost

    def change(self):
        self.pricehistory.append(self.price)
        sum = 0
        for i in range(100):
            x = random.randint(-100, 100)
            sum += x
        self.oldPrice = self.price
        boost = stock.boost(self)
        if self.price <= 1:
            self.price = random.randint(1, 10)
        self.price = round(self.price + self.price * sum / 10000 + boost, 2)
        self.price = round(self.price, 2)
        return self.price

    def tickX(self, liczba_tickow):
        for i in range(liczba_tickow):
            self.change()
        return self.price

    @classmethod
    def getNumOfStocks(cls):
        print('actual number of stocks: ', cls.NumOfStocks)
        return cls.NumOfStocks

    @classmethod
    def displayStocks(cls):
        print('------------')
        for x in cls.stocksList:
            print('Name: ', x.name, '\n', 'Price: ', x.price, '\n', 'Growth: ', x.growth(), '%', '\n', 'Boost: ', x.boost)
        print('-----------')
        return stock.stocksList

    def boostToHsv(self,boost):
        return (boost+10) * 5

class player:

    colors = False

    def __init__(self, StartMoney, Stock1Ilosc=0, Stock2Ilosc=0, Stock3Ilosc=0):
        self.money = StartMoney
        self.stock1 = Stock1Ilosc
        self.stock2 = Stock2Ilosc
        self.stock3 = Stock3Ilosc

    def buyStock(self, stock, ilosc):
        if stock == '1' or stock == x1.name:
            if x1.price * ilosc <= p1.money:
                self.money -= round(x1.price * ilosc, 2)
                self.money = round(self.money, 2)
                self.stock1 += 1 * ilosc
            else:
                print("you can't afford that")


        if stock == '2' or stock == x2.name:
            if x2.price * ilosc <= p1.money:
                self.money -= round(x2.price * ilosc, 2)
                self.money = round(self.money, 2)
                self.stock2 += 1 * ilosc
            else:
                print("you can't afford that")


        if stock == '3' or stock == x3.name:
            if x3.price * ilosc <= p1.money:
                self.money -= round(x3.price * ilosc, 2)
                self.money = round(self.money, 2)
                self.stock3 += 1 * ilosc
            else:
                print("you can't afford that")


    def sellStock(self, stock, ilosc):
        if stock == '1' or stock == x1.name:
            if ilosc <= self.stock1:
                self.stock1 -= ilosc
                self.money += x1.price * ilosc
                self.money = round(self.money)
            else:
                    print('You dont have enough', x1.name)

        if stock == '2' or stock == x2.name:
            if ilosc <= self.stock2:
                self.stock2 -= ilosc
                self.money += x2.price * ilosc
                self.money = round(self.money)
            else:
                print('You dont have enough', x2.name)

        if stock == '3' or stock == x3.name:
            if ilosc <= self.stock3:
                self.stock3 -= ilosc
                self.money += x3.price * ilosc
                self.money = round(self.money)
            else:
                print('You dont have enough', x3.name)

    def displayInventory(self):
        inv = {'Money :': self.money,
               x1.name: self.stock1,
               x2.name: self.stock2,
               x3.name: self.stock3}
        for k in inv.keys():
            print(k, ':', inv[k])
        return inv

x1 = stock('Stock 1',500)
x2 =stock('Stock 2', 500)
x3 = stock('Stock 3',500)

p1 = player(1000)


from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.properties import  ObjectProperty, ListProperty
from kivy.graphics import Color, Rectangle
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from kivy.clock import Clock

#kv = Builder.load_file("my.kv")

class MainWindow(Screen):

    clock_interval = 5


    def __init__(self, **kwargs):
        super(MainWindow, self).__init__(**kwargs)
        # save a reference to the event
        self.clock = Clock.schedule_interval(self.btn, self.clock_interval)


        
    money = ObjectProperty(None)

    stock1 = ObjectProperty(p1.stock1)
    stock2 = ObjectProperty(p1.stock2)
    stock3 = ObjectProperty(p1.stock3)

    stock1_name = ObjectProperty(None)
    stock2_name = ObjectProperty(None)
    stock3_name = ObjectProperty(None)

    name1 = ObjectProperty(None)
    price1 = ObjectProperty(None)
    growth1 = ObjectProperty(None)

    name2 = ObjectProperty(None)
    price2 = ObjectProperty(None)
    growth2 = ObjectProperty(None)

    name3 = ObjectProperty(None)
    price3 = ObjectProperty(None)
    growth3 = ObjectProperty(None)

    def buy1(self):
        p1.buyStock(x1.name, 1)
        self.ids.stock1_posiadane.text = str(p1.stock1)
        self.ids.money.text = str(p1.money)

    def sell1(self):
        p1.sellStock(x1.name, 1)
        self.ids.stock1_posiadane.text = str(p1.stock1)
        self.money.text = str(p1.money)

    def buy2(self):
        p1.buyStock(x2.name, 1)
        self.ids.stock2_posiadane.text = str(p1.stock2)
        self.money.text = str(p1.money)

    def sell2(self):
        p1.sellStock(x2.name, 1)
        self.ids.stock2_posiadane.text = str(p1.stock2)
        self.money.text = str(p1.money)

    def buy3(self):
        p1.buyStock(x3.name, 1)
        self.ids.stock3_posiadane.text = str(p1.stock3)
        self.money.text = str(p1.money)

    def sell3(self):
        p1.sellStock(x3.name, 1)
        self.ids.stock3_posiadane.text = str(p1.stock3)
        self.money.text = str(p1.money)


    def btn(self, *args):
        print(self.clock_interval, 'second clock')
        if p1.colors:
            self.ids.stock1.hue = stock.boostToHsv(x1, x1.boost) / 255
            self.ids.stock2.hue = stock.boostToHsv(x2, x2.boost) / 255
            self.ids.stock3.hue = stock.boostToHsv(x3, x3.boost) / 255

        self.ids.stock1_name.text = str(x1.name)
        self.ids.stock2_name.text = str(x2.name)
        self.ids.stock3_name.text = str(x3.name)

        x1.change()
        x2.change()
        x3.change()

        self.money.text = str(p1.money)

        self.name1.text = x1.name
        self.price1.text = str(x1.price)
        self.growth1.text = str(x1.growth())

        self.name2.text = x2.name
        self.price2.text = str(x2.price)
        self.growth2.text = str(x2.growth())

        self.name3.text = x3.name
        self.price3.text = str(x3.price)
        self.growth3.text = str(x3.growth())

        stock.displayStocks()




class SecondWindow(Screen):

    item1_price = ObjectProperty(None)
    item2_price = ObjectProperty(None)
    shop1 = False
    money = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(SecondWindow, self).__init__()
        # Photo can be reference by running the photo function once:
        Clock.schedule_once(self.photo)




    def reduce_clock_interval(self):
        main_window = App.get_running_app().root.get_screen('main')
        MainWindow.clock_interval -= 1
        main_window.clock.cancel()
        main_window.clock = Clock.schedule_interval(main_window.btn, MainWindow.clock_interval)


    def photo(self, dt):
        # Replace the given image source value:
        self.ids.imageView1.source = 'shop_1.jpg'
        self.ids.imageView2.source = 'shop_2.jpg'



    def shop_buy_1(self):
        shop1_price = 500
        if SecondWindow.shop1 == False:
            if p1.money >= shop1_price:

                SecondWindow.shop1 = True
                p1.colors = True
                p1.money -= shop1_price
                p1.money = round(p1.money,2)
                self.ids.item1_price.text = str(shop1_price)
            else: print("You dont have nough money")
        else: print("Item already bought")

    def shop_buy_2(self):
        shop2_price = 500

        if p1.money >= shop2_price:
            SecondWindow.reduce_clock_interval(SecondWindow)
            p1.money -= shop2_price
            p1.money = round(p1.money, 2)
            self.ids.item2_price.text = str(shop2_price)

        else:
            print("You dont have nough money")










class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("my.kv")




class MyApp(App):
    def build(self):
        return kv




if __name__ == '__main__':
    MyApp().run()