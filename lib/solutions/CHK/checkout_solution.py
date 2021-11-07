

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):  
    
    class SKU_database:
        def __init__(self, cost, offer_available, offers, 
                     multi_offer_available, multi_offer_quantity, multi_offer_free):
            self.cost = cost
            self.offer_available = offer_available
            self.offers = offers
            self.multi_offer_available = multi_offer_available
            self.multi_offer_quantity = multi_offer_quantity
            self.multi_offer_free = multi_offer_free
            
            
            
        def get_total_price(self, quantity):
            
            if (self.offer_available):
                
                #Cycle through multiple offers, largest quantity first
                offer_quantities = self.offers.keys()
                cost_total = 0
                remaining_quantity = quantity
                
                #All instances where offer can be applied
                for offer in offer_quantities:                         
                    offer_quantity = (remaining_quantity // offer)
                    cost_total += offer_quantity * self.offers[offer]
                    remaining_quantity -= (offer_quantity * offer) 
                    
                #Any remainder where offers can't be applied
                cost_total += remaining_quantity * self.cost

                return cost_total
            
            else:
                return quantity * self.cost
            
            
            
        def get_multiple_item_promotion(self, quantity):
            
            if(self.multi_offer_available):
                #All possible free items available with offer
                total_free = quantity // self.multi_offer_quantity           
                return self.multi_offer_free * total_free
            
            else :
                return ""
            
            
            
    
    sku_database = {"A" : SKU_database(50, True, {5: 200, 3: 130}, False, 0, 0),
                    "B" : SKU_database(30, True, {2: 45},  False, 0, 0),
                    "C" : SKU_database(20, False, {},  False, 0, 0),
                    "D" : SKU_database(15, False, {},  False, 0, 0),
                    "E" : SKU_database(40, False, {},  True,  2, "B"),
                    "F" : SKU_database(10, False, {},  True,  3, "F")
                    }
    
    total = 0
    #Get all unique items in the list
    unique_items = set(skus)
    
    
    available_free_items = ""
    
    #Check for offers involving multiple items first, as this might modify quantities
    for item in unique_items:
        #Count number of instances of an item being checked out
        item_quantity = skus.count(item)
        try:
            available_free_items += sku_database[item].get_multiple_item_promotion(item_quantity)
            
        except KeyError as e:
            # Return -1 on key error
            return -1
   
    
   
    
    #Checkout each item by quantity
    for item in unique_items:

        #Count number of instances of an item being checked out
        item_quantity = skus.count(item)
        item_free = available_free_items.count(item)
        
        #Subtract available free items, but don't go negative
        item_quantity = max(0, item_quantity - item_free)
        
        try:
            total += sku_database[item].get_total_price(item_quantity)
            
        except KeyError as e:
            # Return -1 on key error
            return -1
    
    return total


