class myplexer:
   def route(self, arg):
      def inner(func):
         user_input = input("enter Input: ")
         if user_input == arg:
            print(func())
      return inner

