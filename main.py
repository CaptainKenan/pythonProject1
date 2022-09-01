import tkinter as tk


def addtocart(label, price):
    label.config(text=int(label['text']) + price)


root = tk.Tk()
root.title("Restoran")
root.geometry("800x500")
bg = tk.PhotoImage(file="restoran (2) (1).png")
table = tk.PhotoImage(file="table100x100.png")
menuimage = tk.PhotoImage(file="menu.png")
shopbg = tk.PhotoImage(file="magazine.png")
skladbg = tk.PhotoImage(file="skladphoto.png")
btncheck = tk.Button(root, text="Check")
btncheck.place(x="140", y="170")
bglabel = tk.Label(root, image=bg)
bglabel.place(x=0, y=0)
labelbalance = tk.Label(root, text=100000,
                        foreground="black")
labelbalance.place(x="750", y="50")


def all_plus(label,labelfrommainmenu, labeladd):
    label.config(text=float(label['text']) + float(labeladd['text']))
    labeladd.config(text=0)
    labelfrommainmenu.config(text=0)


def burger(label, labelfrommainmenu, price):
    stock1["Bread"] -= 2
    stock1["Meat"] -= 0.6
    stock1["Pickle"] -= 4
    stock1["Tomato"] -= 1
    stock1["Cheese"] -= 1
    label.config(text=round(float(label['text']) + float(price), 2))
    labelfrommainmenu.config(text=round(float(labelfrommainmenu['text']) + float(price), 2))


def Pizza(label, labelfrommainmenu, price):
    stock1["Tomato"] -= 3
    stock1["Cheese"] -= 6
    stock1["Olive"] -= 10
    label.config(text=round(float(label['text']) + float(price), 2))
    labelfrommainmenu.config(text=round(float(labelfrommainmenu['text']) + float(price), 2))


def bread(label, labelfrommainmenu, price):
    stock1["Bread"] -= 2
    label.config(text=round(float(label['text']) + float(price), 2))
    labelfrommainmenu.config(text=round(float(labelfrommainmenu['text']) + float(price), 2))


def cheese_sticks(label, labelfrommainmenu, price):
    stock1["Cheese"] -= 5
    stock1["Bread"] -= 4
    label.config(text=round(float(label['text']) + float(price), 2))
    labelfrommainmenu.config(text=round(float(labelfrommainmenu['text']) + float(price), 2))


def Qutab(label, labelfrommainmenu, price):
    stock1["Meat"] -= 10
    label.config(text=round(float(label['text']) + float(price), 2))
    labelfrommainmenu.config(text=round(float(labelfrommainmenu['text']) + float(price), 2))

def Kabab(label, labelfrommainmenu, price):
    stock1["Meat"] -= 6
    stock1["Bread"] -= 2
    stock1["Onion"] -= 7
    label.config(text=round(float(label['text']) + float(price), 2))
    labelfrommainmenu.config(text=round(float(labelfrommainmenu['text']) + float(price), 2))


def Steik(label, labelfrommainmenu, price):
    stock1["Meat"] -= 6
    stock1["Bread"] -= 2
    stock1["Onion"] -= 5
    label.config(text=round(float(label['text']) + float(price), 2))
    labelfrommainmenu.config(text=round(float(labelfrommainmenu['text']) + float(price), 2))


def Dolma(label, labelfrommainmenu, price):
    stock1["Leaf"] -= 30
    stock1["Bread"] -= 2
    label.config(text=round(float(label['text']) + float(price), 2))
    labelfrommainmenu.config(text=round(float(labelfrommainmenu['text']) + float(price), 2))


def Capital_Salad(label, labelfrommainmenu, price):
    stock1["Bread"] -= 2
    stock1["Green"] -= 6
    stock1["Tomato"] -= 1
    stock1["Cucumber"] -= 1
    label.config(text=round(float(label['text']) + float(price), 2))
    labelfrommainmenu.config(text=round(float(labelfrommainmenu['text']) + float(price), 2))


def Sezar_Salad(label, labelfrommainmenu, price):
    stock1["Bread"] -= 5
    stock1["Tomato"] -= 2
    stock1["Meat"] -= 2
    label.config(text=round(float(label['text']) + float(price), 2))
    labelfrommainmenu.config(text=round(float(labelfrommainmenu['text']) + float(price), 2))


# stock1 = {"Bread": 60}
# stock2 = {"Onion": 44}
# stock3 = {"Green": 51}
# stock4 = {"Meat": 56}
# stock5 = {"Tomato": 32}
# stock6 = {"Potato": 12}
# stock7 = {"Pickle": 63}
# stock8 = {"Cucumber": 43}
# stock9 = {"Leaf": 47}
# stock10 = {"Olive": 66}
# stock11 = {"Cheese": 32}

stock1 = {"Bread": 60, "Onion": 44, "Green": 51, "Meat": 56, "Tomato": 32, "Potato": 12, "Pickle": 63, "Cucumber": 43,
          "Leaf": 47, "Olive": 66, "Cheese": 32, "Mushrooms": 67}


def stock():
    stock = tk.Toplevel(root)
    stock.title("Stock")
    stock.geometry("700x400")
    labelstockbg = tk.Label(stock, image=skladbg)
    labelstockbg.place(x="0", y="0")
    labelstock1 = tk.Label(stock, text=f"Bread: {stock1['Bread']}",
                           font=1000000000000000)
    labelstock1.place(x="20", y="50")
    labelstock2 = tk.Label(stock, text=f"Onion: {stock1['Onion']}",
                           font=1000000000000000)
    labelstock2.place(x="20", y="100")
    labelstock3 = tk.Label(stock, text=f"Green: {stock1['Meat']}",
                           font=1000000000000000)
    labelstock3.place(x="20", y="150")
    labelstock4 = tk.Label(stock, text=f"Tomato: {stock1['Tomato']}",
                           font=1000000000000000)
    labelstock4.place(x="20", y="200")
    labelstock5 = tk.Label(stock, text=f"Potato: {stock1['Potato']}",
                           font=1000000000000000)
    labelstock5.place(x="20", y="250")
    labelstock6 = tk.Label(stock, text=f"Pickle: {stock1['Pickle']}",
                           font=1000000000000000)
    labelstock6.place(x="200", y="50")
    labelstock7 = tk.Label(stock, text=f"Cucumber: {stock1['Cucumber']}",
                           font=1000000000000000)
    labelstock7.place(x="200", y="100")
    labelstock8 = tk.Label(stock, text=f"Leaf: {stock1['Leaf']}",
                           font=1000000000000000)
    labelstock8.place(x="200", y="150")
    labelstock9 = tk.Label(stock, text=f"Olive: {stock1['Olive']}",
                           font=1000000000000000)
    labelstock9.place(x="200", y="200")
    labelstock10 = tk.Label(stock, text=f"Cheese: {stock1['Cheese']}",
                            font=1000000000000000)
    labelstock10.place(x="200", y="250")
    labelstock11 = tk.Label(stock, text=f"Mushrooms: {stock1['Mushrooms']}",
                            font=1000000000000000)
    labelstock11.place(x="350", y="250")


btnstock = tk.Button(root, text="Stock",
                     command=stock)
btnstock.place(x="20", y="50")


# def addtocheck(label, price):
# label.config(text=int(label['text']) + price)

def menu(label):
    menu = tk.Toplevel(root)
    menu.title("MENU")
    menu.geometry("400x600")
    labelmenu = tk.Label(menu, image=menuimage)
    labelmenu.place(x=0, y=0)
    buttoncheck = tk.Button(menu, text="Check",
                            command=lambda: all_plus(labelbalance, label,labelcheck))
    buttoncheck.place(x="50", y="40")
    labelcheck = tk.Label(menu, text=0)
    labelcheck.place(x="50", y="10")
    labelburger = tk.Label(menu, text="Burgers",
                           width="15",
                           height="1")
    labelburger.place(x="60", y="230")
    btnmenu1 = tk.Button(menu, text="2.20$",
                         width="5",
                         height="1",
                         command=lambda: burger(labelcheck, label, 2.20))
    btnmenu1.place(x="350", y="230")
    labelpizza = tk.Label(menu, text="Pizza",
                          width="15",
                          height="1")
    labelpizza.place(x="60", y="260")
    btnmenu2 = tk.Button(menu, text="12.50$",
                         width="5",
                         height="1",
                         command=lambda: Pizza(labelcheck, label, 12.50))
    btnmenu2.place(x="350", y="260")
    labelbread = tk.Label(menu, text="Bread",
                          width="15",
                          height="1")
    labelbread.place(x="60", y="290")
    btnmenu3 = tk.Button(menu, text="1$",
                         width="5",
                         height="1",
                         command=lambda: bread(labelcheck, label, 1))
    btnmenu3.place(x="350", y="290")
    labelCheeseSticks = tk.Label(menu, text="Cheese Sticks",
                                 width="39",
                                 height="1")
    labelCheeseSticks.place(x="60", y="364")
    btnmenu4 = tk.Button(menu, text="4$",
                         width="5",
                         height="1",
                         command=lambda: cheese_sticks(labelcheck, label,4))
    btnmenu4.place(x="350", y="360")
    labelQutab = tk.Label(menu, text="Qutab",
                          width="24",
                          height="1")
    labelQutab.place(x="60", y="395")
    btnmenu5 = tk.Button(menu, text="0.3$",
                         width="5",
                         height="1",
                         command=lambda: Qutab(labelcheck, label, 0.3))
    btnmenu5.place(x="350", y="395")
    labelKebab = tk.Label(menu, text="Kabab",
                          width="17",
                          height="1")
    labelKebab.place(x="60", y="430")
    btnmenu6 = tk.Button(menu, text="17$",
                         width="5",
                         height="1",
                         command=lambda: Kabab(labelcheck, label, 17))
    btnmenu6.place(x="350", y="430")
    labelSteik = tk.Label(menu, text="Steik",
                          width="17",
                          height="1")
    labelSteik.place(x="60", y="460")
    btnmenu7 = tk.Button(menu, text="21$",
                         width="5",
                         height="1",
                         command=lambda: Steik(labelcheck, label, 21))
    btnmenu7.place(x="350", y="460")
    labelDolma = tk.Label(menu, text="Dolma",
                          width="17",
                          height="1")
    labelDolma.place(x="60", y="550")
    btnmenu8 = tk.Button(menu, text="13$",
                         width="5",
                         height="1",
                         command=lambda: Dolma(labelcheck, label, 13))
    btnmenu8.place(x="350", y="550")
    labelSalad = tk.Label(menu, text="Capital Salad",
                          width="20",
                          height="1")
    labelSalad.place(x="60", y="520")
    btnmenu9 = tk.Button(menu, text="0.7$",
                         width="5",
                         height="1",
                         command=lambda: Capital_Salad(labelcheck, label, 0.7))
    btnmenu9.place(x="350", y="520")
    labelSezar = tk.Label(menu, text="Sezar Salad",
                          width="17",
                          height="1")
    labelSezar.place(x="60", y="580")
    btnmenu10 = tk.Button(menu, text="0.7$",
                          width="5",
                          height="1",
                          command=lambda: Sezar_Salad(labelcheck, label,0.7))
    btnmenu10.place(x="350", y="580")


def store():
    def addtocart(label, labels, label11, labelobject, price):
        label.config(text=round(float(label['text']) + float(price), 2))
        labelobject.config(text=int(labelobject['text']) + 1)
        label11.config(text=round(float(label11['text']) - float(price), 2))
        labels.config(text=int(labels['text']) - price)

    storeWindow = tk.Toplevel(root)
    storeWindow.title("store Window")
    storeWindow.geometry("700x600")
    labelshopfoto = tk.Label(storeWindow, image=shopbg)
    labelshopfoto.place(x="0", y="0")

    labels = tk.Label(storeWindow,
                      text=labelbalance['text'],
                      padx="10",
                      pady="10",
                      font=" 50",
                      height="1",
                      width="10")
    labels.place(x=50, y=50)
    Meat_button = tk.Button(storeWindow, text="Meat:17AZN",
                            height="2",
                            width="13",
                            command=lambda: addtocart(labeladd, labelbalance, labels, labelMeat, 17))
    Meat_button.place(x=350, y=200)
    Green_button = tk.Button(storeWindow, text="Green:20coin",
                             height="2",
                             width="13",
                             command=lambda: addtocart(labeladd, labelbalance, labels, labelGreen, 0.20))
    Green_button.place(x=350, y=280)
    Tomato_button = tk.Button(storeWindow, text="Tomato:1.99AZN",
                              height="2",
                              width="13",
                              command=lambda: addtocart(labeladd, labelbalance, labels, labelTomato, 1.99))
    Tomato_button.place(x=350, y=350)
    Potato_button = tk.Button(storeWindow, text="Potato:1.55AZN",
                              height="2",
                              width="13",
                              command=lambda: addtocart(labeladd, labelbalance, labels, labelPotato, 1.55))
    Potato_button.place(x=600, y=250)
    Onion_button = tk.Button(storeWindow, text="Onion:80coin",
                             height="2",
                             width="13",
                             command=lambda: addtocart(labeladd, labelbalance, labels, labelOnion, 0.80))
    Onion_button.place(x=150, y=150)
    Bread_button = tk.Button(storeWindow, text="Bread:60coin",
                             height="2",
                             width="13",
                             command=lambda: addtocart(labeladd, labelbalance, labels, labelBread, 0.60))
    Bread_button.place(x=200, y=250)
    labelTomato = tk.Label(storeWindow,
                           text="0",
                           padx="10",
                           pady="10",
                           font=" 50",
                           height="1",
                           width="10")
    labelTomato.place(x=50, y=400)
    labelOnion = tk.Label(storeWindow,
                          text="0",
                          padx="10",
                          pady="10",
                          font=" 50",
                          height="1",
                          width="10")
    labelOnion.place(x=150, y=400)
    labelMeat = tk.Label(storeWindow,
                         text="0",
                         padx="10",
                         pady="10",
                         font=" 50",
                         height="1",
                         width="10")
    labelMeat.place(x=250, y=400)
    labelGreen = tk.Label(storeWindow,
                          text="0",
                          padx="10",
                          pady="10",
                          font=" 50",
                          height="1",
                          width="10")
    labelGreen.place(x=350, y=400)
    labelPotato = tk.Label(storeWindow,
                           text="0",
                           padx="10",
                           pady="10",
                           font=" 50",
                           height="1",
                           width="10")
    labelPotato.place(x=450, y=400)
    labelBread = tk.Label(storeWindow,
                          text="0",
                          padx="10",
                          pady="10",
                          font=" 50",
                          height="1",
                          width="10")
    labelBread.place(x=550, y=400)
    labeladd = tk.Label(storeWindow,
                        text="0",
                        padx="10",
                        pady="10",
                        font=" 50",
                        height="1",
                        width="10")
    labeladd.place(x=50, y=300)


btnstore = tk.Button(root, text="Store",
                     command=store)
btnstore.place(x="20", y="90")

btn1 = tk.Button(root, image=table,
                 width="100",
                 height="100",
                 command= lambda: menu(labelTable1))
btn1.place(x="50", y="150")
btn2 = tk.Button(root, image=table,
                 width="100",
                 height="100",
                 command=lambda: menu(labelTable2))
btn2.place(x="250", y="150")
btn3 = tk.Button(root, image=table,
                 width="100",
                 height="100",
                 command=lambda: menu(labelTable3))
btn3.place(x="450", y="150")
btn4 = tk.Button(root, image=table,
                 width="100",
                 height="100",
                 command=lambda: menu(labelTable4))
btn4.place(x="650", y="150")
btn5 = tk.Button(root, image=table,
                 width="100",
                 height="100",
                 command=lambda: menu(labelTable5))
btn5.place(x="50", y="300")
btn6 = tk.Button(root, image=table,
                 width="100",
                 height="100",
                 command=lambda: menu(labelTable6))
btn6.place(x="250", y="300")
btn7 = tk.Button(root, image=table,
                 width="100",
                 height="100",
                 command=lambda: menu(labelTable7))
btn7.place(x="450", y="300")
btn8 = tk.Button(root, image=table,
                 width="100",
                 height="100",
                 command=lambda: menu(labelTable8))
btn8.place(x="650", y="300")
labelname = tk.Label(root, text="EHDI KAFE",
                     font="200")
labelname.place(x="350", y="20")

labelTable1 = tk.Label(root, text="0",
                       font="100000")
labelTable1.place(x="50", y="250")
labelTable2 = tk.Label(root, text="0",
                       font="100")
labelTable2.place(x="250", y="250")
labelTable3 = tk.Label(root, text="0",
                       font="100")
labelTable3.place(x="450", y="250")
labelTable4 = tk.Label(root, text="0",
                       font="100")
labelTable4.place(x="650", y="250")
labelTable5 = tk.Label(root, text="0",
                       font="100")
labelTable5.place(x="50", y="400")
labelTable6 = tk.Label(root, text="0",
                       font="100")
labelTable6.place(x="250", y="400")
labelTable7 = tk.Label(root, text="0",
                       font="100")
labelTable7.place(x="450", y="400")
labelTable8 = tk.Label(root, text="0",
                       font="100")
labelTable8.place(x="650", y="400")

root.mainloop()
