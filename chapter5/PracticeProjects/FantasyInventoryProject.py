def display_inventory(inventory):
    print("Inventory")
    item_total = 0
    for i, v in inventory.items():
        print(str(v) + ' ' + i)
        item_total += v
    print("total number of items is :{item_total}".format(item_total =item_total))


inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
display_inventory(inventory)
