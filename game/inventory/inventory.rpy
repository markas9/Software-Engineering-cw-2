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