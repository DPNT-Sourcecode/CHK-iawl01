

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):  
    sku_database = {"A" : 50,
                    "B" : 30,
                    "C" : 20,
                    "D" : 15
                    }
    
    total = 0
    #Get all unique items in the list
    unique_items = set(skus)
    
    
    for item in unique_items:

        item_quantity = skus.count(item)
        
        try:
            total += sku_database[item]
            
        except KeyError as e:
            # Return -1 on key error
            return -1
    
    return total





