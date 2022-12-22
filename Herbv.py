class Herb:
        def __init__ (self,herb_name:str,herb_code:str,herb_treasures:dict):
             self.herb_name = herb_name
             self.herb_code = herb_code
             self.herb_treasures = herb_treasures
    
banny = Herb("texas","765490",{"strength":7,"agility":5})
print(banny.herb_name)
print(banny.herb_code)
print(banny.herb_treasures)  
    