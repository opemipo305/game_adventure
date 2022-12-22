class Bread:
        def __init__ (self,bread_name:str,bread_code:str,bread_treasures:dict):
             self.bread_name = bread_name
             self.bread_code = bread_code
             self.bread_treasures =bread_treasures
    
banny = Bread("texas","765490",{"strength":7,"agility":5})
print(banny.bread_name)
print(banny.bread_code)
print(banny.bread_treasures)  
    