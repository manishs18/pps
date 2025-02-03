'''
Problem Statement

Royal Orchid is a florist. They want to be alerted when stock of a flower goes below a particular level. 
The flowers are identified using name, price per kg and stock available (in kgs).
Write a Python program to implement the above requirement

Details of Flower class are given below:

Class name: Flower

Attributes                      flower_name
(Private)                       price_per_kg 
                                stock_available

                         
                         
Methods                         __init__()                                  Create and initialize all instance variables to None
(public)
                                validate_flower()                            Return true, if flower name is valid. Else, return false (Refer table for valid flower names)

                                validate_stock(required_quantity            Accept the quantity required. Return true, if stock ) is available.
                                                                            Else return false.

                                sell_flower(required_quantity)              Accept the quantity required.
                                                                            Validate flower name and stock.
                                                                            If both are valid, update stock available based on the quantity required

                                check_level()                               Check if available stock is below the order level 
                                                                            If so, return true. Else, retum false (Refer table for order level of each flower)

                                setter methods                              Include setter methods for all instance variables to set its values

                                getter methods                              Include getter methods for all instance variables to get its values



                                
Flower Name          Level(in Kgs)

orchid               15
rose                 25
jasmine              40

Note: Perform case insensitive string comparison mpanson

Reprecent few flowers, witialize instance variables using setter methods, Invoke appropriate methods and test your program.
'''


class Flower: 
     
    __flower={"orchid":20,"rose":30,"jasmine":50} 
     
    def __init__(self): 
        self.__flower_name=None 
        self.__price_per_kg=None 
        self.__stock_available=None 
         
    def set_flower_name(self,fn): 
        self.__flower_name = fn.lower() 
         
    def set___price_per_kg(self,ppk): 
        self.__price_per_kg = ppk 
         
    def set___stock_available(self): 
        if self.__flower_name in Flower.__flower.keys(): 
            self.__stock_available=Flower.__flower[self.__flower_name] 
            print(self.__stock_available)
         
         
    def get_flower_name(self): 
        return self.__flower_name 
     
    def get__price_per_kg(self): 
        return self.__price_per_kg 
     
    def get__stock_available(self): 
        return self.__stock_available 
     
     
    def validate_flower(self):       
         
        if self.__flower_name in Flower.__flower.keys(): 
            return True 
        else: 
            return False 
         
    def validate_stock(self,rqd_qty): 
         
        if rqd_qty <= self.__stock_available: 
            return True 
        else: 
            return False 
         
    def sell_flower(self,rqd_qty): 
         
        if self.validate_flower() and self.validate_stock(rqd_qty): 
            Flower.__flower[self.__flower_name] -= rqd_qty 
            return True 
          
        else: 
            return False  
         
    def check_level(self): 
         
        if Flower.__flower["orchid"] <= 15 or Flower.__flower["rose"] <= 40 or Flower.__flower["jasmine"]<=40: 
            return True  
        else: 
            return False


f1 = Flower()
f1.set_flower_name('orchid')
f1.set___price_per_kg(99)
f1.set___stock_available()
print(f1.get_flower_name(),f1.get__price_per_kg(),f1.get__stock_available(),f1.sell_flower(30))
if f1.check_level():
    print("Need to update the stock... ")

else:
    print("No need to the update stock..")

