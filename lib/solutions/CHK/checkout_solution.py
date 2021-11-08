

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
                    "F" : SKU_database(10, False, {},  True,  3, "F"),
                    "G" : SKU_database(20, False, {},  False, 0, 0),
                    "H" : SKU_database(10, True,  {10:80, 5: 45},  False, 0, 0),
                    "I" : SKU_database(35, False, {},  False, 0, 0),
                    "J" : SKU_database(60, False, {},  False, 0, 0),
                    "K" : SKU_database(70, True,  {2: 120},  False, 0, 0),
                    "L" : SKU_database(90, False, {},  False, 0, 0),
                    "M" : SKU_database(15, False, {},  False, 0, 0),
                    "N" : SKU_database(40, False, {},  True, 3, "M"),
                    "O" : SKU_database(10, False, {},  False, 0, 0),
                    "P" : SKU_database(50, True,  {5: 200},  False, 0, 0),
                    "Q" : SKU_database(30, True,  {3: 80},  False, 0, 0),
                    "R" : SKU_database(50, False, {},  True, 3, "Q"),
                    "S" : SKU_database(20, False, {},  False, 0, 0),
                    "T" : SKU_database(20, False, {},  False, 0, 0),
                    "U" : SKU_database(40, False, {},  True, 4, "U"),
                    "V" : SKU_database(50, True,  {3: 130, 2:90},  False, 0, 0),
                    "W" : SKU_database(20, False, {},  False, 0, 0),
                    "X" : SKU_database(17, False, {},  False, 0, 0),
                    "Y" : SKU_database(20, False, {},  False, 0, 0),
                    "Z" : SKU_database(21, False, {},  False, 0, 0)
                  
                    }
    
    
    #SKU, group_quantity, group_price
    #SKUs in order of price. Inelegant solution for the future, needs revision
    group_discount_database = [["ZSTYX", 3, 45]]
    
    
    total = 0
    #Get all unique items in the list
    unique_items = set(skus)
    

    #System design isn't ideal for group discounts, will have to resolve those first
    for group in group_discount_database:
        available_group_items = ""
        
        for discount_group_item in group[0]:
            available_group_items += skus.count(discount_group_item) * discount_group_item 
            
        #Get amount of times that the discount can be applied
        total += (len(available_group_items) // group[1]) * group[2]
        
        #Select the most expensive items to be removed first as part of any offer
        print(available_group_items, total)
            
        
    
    
    
    #Check for offers involving multiple items, as this might modify quantities
    available_free_items = ""
    
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





