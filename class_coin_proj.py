import random
class Coin:
     def __init__(self,rare=False,clean=True, heads=True,**kwargs):
         self.is_rare=rare
         self.is_clean= clean
         self.heads = heads

         if self.is_rare:
             self.value=self.origal_value*1.25
         else:
             self.value=self.origal_value
         if self.is_clean:
             self.colour=self.clean_colour
         else:
             self.colour=self.rusty_colour
     def rust(self):
          self.colour=self.rusty_colour
     def clean(self):
          self.colour= self.clean_colour

     def __del__(self):
          prin("Coin Spent")

     def flip(self):
          heads_options=[True,False]
          choice =random.choicr(heads_options)
          self.heads=choice

class Pound(Coin):
     def __init__(self):
          data = {
               "original_value": 1.00,
               "clean_colour": "gold",
               "rusty_colour": "greenish",
               "num_edges": 1,
               "diameter": 22.5,
               "thickness": 3.15,
               "mass": 9.5
               
               }
          super().__init__(**data)
         
coin1=Pound()
coin1.flip()
             

        

           
