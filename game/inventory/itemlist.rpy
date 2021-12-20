
init -2 python:
    class InvItem(store.object):
        def __init__(self, name, image, value, info, id, cost=[]):
            self.name = name 
            self.image = image 
            self.value = int(value) 
            self.info = info 
            self.id = id 
            self.cost = cost 

  
        def see(self):
            if self.id not in seen_items:
                seen_items.append(self.id)

        def pickup(self, amount=1):
            self.see()
            while amount>0:
                inv.append(self.id)
                amount -= 1
     
        def toss(self, amount):
            while amount>0:
                inv.remove(self.id)
                amount -= 1
         
        def buy(self, amount):
            global gold

            self.see()

            gold -= self.value*amount
            while amount>0:
                inv.append(self.id)
                amount -=1

        
        def sell(self, amount):
            global gold

            gold += int(self.value*amount/2)
            self.toss(amount)
        
        def check_price(self):
            if self.value <= gold:
                return True
            return False


    def set_item(self):

        for i in itemlist:
            if self==i[4]: 
                return i

 
    def sortbyname(i):
        thisitem = InvItem(*set_item(i))
        return thisitem.name

    def sortbyprice(i):
        thisitem = InvItem(*set_item(i))
        return thisitem.value






define item_paper = (_("Paper"), "item paper", 3,
    _("The support material of solving questions."), "item_paper")

define item_calculator = (_("Calculator"), "item calculator", 5,
    _("Get help in those math questions!"), "item_calculator")

define item_books = (_("Books"), "item books", 8,
    _("To solve the tricky ones"), "item_books")

define itemlist = [
    
    item_paper,
    item_calculator,
    item_books
    ]

