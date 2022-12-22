class Block:
        def __init__ (self,block_name:str,block_code:str,block_height:dict):
             self.herb_name = block_name
             self.herb_code = block_code
             self.herb_treasures =block_height
    
banny = Block("texas","765490",{"strength":7,"agility":5})
print(banny.herb_name)
print(banny.herb_code)
print(banny.herb_treasures)  
    