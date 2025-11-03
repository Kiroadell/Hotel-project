print("Jesus is the way and the truth and the life , Amen")
# باسم الثالوث القدوس اميني يا رب بشفاعة ام النور الطاهرة مريم و شفاعة جميع النفوس و شفاعة جميع القديسين و شفتعة جميع الملاءكة و شفاعة جميع التلاميذ و شفاعة جميع الاباء الكهنة و شفاعة جميع الاباء الرهبان و شفاعة جميع الرسل امين
import random
from outiles import Location
from outiles import Food


class visitor:
    def __init__(self):
        self.name = ""
        self.phone_number = ""
        self.budget = self.get_budget()
        self.numbers_of_membres = 0
        self.numbers_of_night = 0
        self.location = ""

  def get_budget(self) :
    while True :
        # generate a numeric budget (int)
        budget = random.randint(100, 10000)
        self.budget = int(budget)
        return self.budget
        

  def choose_name(self):#done
    while True:
        name = input("what's your name  : ")
        if name.isalpha():
            self.name = name
            break
        else:
            print(
                "please i haven't heard your name , can you tell me it again  "
            )
            continue


  def get_phone_number(self)   : 
    while True:
        print("Jesus is the way and the truth and the life , Amen")
        # باسم الثالوث القدوس اميني يا رب بشفاعة ام النور الطاهرة مريم و شفاعة جميع النفوس و شفاعة جميع القديسين و شفتعة جميع الملاءكة و شفاعة جميع التلاميذ و شفاعة جميع الاباء الكهنة و شفاعة جميع الاباء الرهبان و شفاعة جميع الرسل امين
        import random
        from outiles import Location
        from outiles import Food


        class visitor:
          def __init__(self):
            self.name = ""
            self.phone_number = ""
            self.budget = self.get_budget()
            self.numbers_of_membres = 0
            self.numbers_of_night = 0
            self.location = ""

          def get_budget(self):
            # generate a numeric budget (int)
            budget = random.randint(100, 10000)
            self.budget = int(budget)
            return self.budget

          def choose_name(self):  # done
            while True:
              name = input("what's your name  : ")
              if name.isalpha():
                self.name = name
                break
              else:
                print("please i haven't heard your name , can you tell me it again  ")

          def get_phone_number(self):
            while True:
              phone_number = input("enter your phone number :")
              if len(phone_number) == 12 and phone_number[0] == '0' and phone_number[1] == '1':
                self.phone_number = phone_number
                break
              else:
                print("enter your phone number again")

          def get_numbers_of_members(self):  # done
            while True:
              numbers_of_members = input("enter the number of membres :")
              try:
                n = int(numbers_of_members)
              except ValueError:
                print("please enter a valid number")
                continue
              if n > 0:
                self.numbers_of_membres = n
                return n
              print("enter the number of members again ")

          def numbers_of_nights(self):  # done
            while True:
              try:
                numbers_of_nights = int(input("how many nights you want to stay :"))
              except ValueError:
                print("please enter a valid number")
                continue
              if numbers_of_nights > 0:
                self.numbers_of_night = numbers_of_nights
                return numbers_of_nights
              else:
                print("again")

          def choose_location(self):  # done
            while True:
              location = input("enter where you want to reserve: ")
              self.location = location
              return location.capitalize()

          def how_many_stars(self):  # done
            while True:
              try:
                visitor_desir_stars = int(input("you need a hotel with how many stars :"))
              except ValueError:
                print("please enter a valid number")
                continue
              if visitor_desir_stars > 5:
                print("please again")
                continue
              else:
                return visitor_desir_stars

          def view_desir(self, desir):
            # return the desired view key (e.g. 'sea')
            return desir

          def how_many_meals(self):
            while True:
              x = input("now about food how many meals you want to eat ? (1-3) ")
              try:
                xi = int(x)
              except ValueError:
                continue
              if xi in [1, 2, 3]:
                return xi
              else:
                continue

          def what_food(self):
            for i in range(len(Food)):
              print(f"{i+1} - {Food[i]}")
            while True:
              x = input("what do you want? (enter name or number)")
              # allow numeric selection
              if x.isdigit():
                idx = int(x) - 1
                if 0 <= idx < len(Food):
                  return Food[idx]
              if x in Food:
                return x
              else:
                print("not availble ")
                continue

          def will_buy(self, total_price):
            print(f"i will buy and pay the total price which is {total_price}")

          def do_not_have_money(self, total_price):
            print(f"i only have {self.budget} and i can not pay ")

          def want_toamount(self, total_price):
            print(f"then i will buy {total_price%2}")


