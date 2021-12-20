image bg shop = Solid("#ffbedb")
image bg lab = Solid("#c3beff")
image beta= im.Scale("rooms/beta.jpg", 1920,1080)
image inventory= im.Scale("rooms/inventory.jpg", 1920,1080)
image buy= im.Scale("rooms/beta.jpg", 1920,1080)
# python:
#     gold = 20 #starting amount
#     inv = []
#     seen_items = []
#     market = []

# $ market = [ "item_paper", "item_calculator", "item_books" ]
    
# ## INVENTORY SETUP
# $ InvItem(*item_books).pickup(3)
# $ InvItem(*item_paper).pickup(2)
# $ InvItem(*item_calculator).pickup(1)
label test_menu:
    scene beta
    menu:
        "Inventory ":
            jump inventory 
        "Buy Items":
            jump market_buy
        "Sell Items":
            jump market_sell
        "Go Back to Game":
            jump begin
       

##ITEMS
label inventory:
    scene bg shop
    call screen inventory(inv) 
    jump  test_menu

label market_buy:
    scene bg shop
    call screen shop(market)
    jump test_menu

label market_sell:
    scene bg shop
    call screen inventory(inv, selling=True)
    jump test_menu