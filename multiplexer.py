class myplexer:
   def run(self):
       user_input = input("enter Input: ")
       return user_input

   def route(self, arg):
       def inner(func):
           if arg == self.run():
               print(func())
       return inner
