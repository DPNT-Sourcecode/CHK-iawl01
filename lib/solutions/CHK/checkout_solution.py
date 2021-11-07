

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):  
    
    class SKU_database:
        def __init__(self, cost, offer_available, offer_quantity, offer_cost):
            self.cost = cost
            self.offer_available = offer_available
            self.offer_quantity = offer_quantity
            self.offer_cost = offer_cost
            
        def get_total_price(self, quantity):
            if (offer_available):
                return quantity * self.cost
            else:
                return quantity * self.cost
            
    
    sku_database = {"A" : SKU_database(50, False, 0, 0),
                    "B" : SKU_database(30, False, 0, 0),
                    "C" : SKU_database(20, False, 0, 0),
                    "D" : SKU_database(15, False, 0, 0)
                    }
    
    total = 0
    #Get all unique items in the list
    unique_items = set(skus)
    
    
    for item in unique_items:

        #Count number of instances of an item being checked out
        item_quantity = skus.count(item)
        
        try:
            total += sku_database[item].get_total_price(item_quantity)
            
        except KeyError as e:
            # Return -1 on key error
            return -1
    
    return total







