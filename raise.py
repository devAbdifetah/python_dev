def colorize(text,color):
     if type(text) is not str:
          raise TypeError("value must be instance of str")
     print(f"printed {text} in {color}")

colorize('hi','red')     

