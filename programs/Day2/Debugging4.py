item_list = {"1":"Burger", "2":"Hotdog", "3":"Bun", "4":"Ketchup", "5":"Cheese"}
n = 0

while n < 5:
    for i in item_list:
        print(item_list[i])
        n=n+1

print(item_list["5"])