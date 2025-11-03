print("Jesus is the way and the truth and the life , Amen")
# باسم الثالوث القدوس اميني يا رب بشفاعة ام النور الطاهرة مريم و شفاعة جميع النفوس و شفاعة جميع القديسين و شفتعة جميع الملاءكة و شفاعة جميع التلاميذ و شفاعة جميع الاباء الكهنة و شفاعة جميع الاباء الرهبان و شفاعة جميع الرسل امين
from visitor import visitor

class Menu:
    def __init__(self) :
            pass

  def welcome_menu(self):
      print("welcome to Jesus’s company for reservation of hotels")
      visitor().choose_name()
      print("do you want to reserve an hotel ? ")
      x = input("yes or no :")
      if x.lower() in ["yes", "no"]:
          return x.lower()

  def print_all_information_and_if_continue(self,hotel_name,hotel_stars,numbers_of_nights,numbers_of_members,room_view,numbers_of_meals,type_of_food) :
      stars = "*"
      stars_appear = []
      for i in range(int(hotel_stars)) :
          stars_appear.append(stars)

      x = "".join(stars_appear)

      print(f"""then you choosed :
                  the hotel{hotel_name}

                  with {hotel_stars} {x}

                  with {numbers_of_nights} nights 

                  and you have {numbers_of_members} members and need a room with {numbers_of_members} beds 

                  and you need a view on {room_view}

                  and you need {numbers_of_meals} meals

                  and you need {type_of_food} as a type of food""")

      while True:
           x = input("do you want to continue ? yes or no : ")
           if x.lower() in ["yes" , "no"] :
              if x.lower() == "yes" :
                 return True
              else :
                  return False
           else :
               continue




  def calculation_menu(self,price_of_room_per_night,price_of_food_perday_and_for_one_member,number_of_nights,numbers_of_memebers,function_of_price_of_total_room,function_of_price_of_total_food,Egyptian_or_no) :
         x = ["E.G","Dollar"]
         if Egyptian_or_no == "Egypt" :
             x = x[0]
         else :
              x = x[1]
         print(f"""
          then let calculate 

          the price of room per night is {price_of_room_per_night} 

          the price of food per day and for one member is {price_of_food_perday_and_for_one_member}

          and you will stay{number_of_nights} nights

          and you are {numbers_of_memebers} members 

          then the total price of room is {function_of_price_of_total_room}

          and the total price of food is {function_of_price_of_total_food}""")

         if Egyptian_or_no == "Egypt" :
             print(f"so the total price is {function_of_price_of_total_food + function_of_price_of_total_room} {x}")
             return function_of_price_of_total_food + function_of_price_of_total_room
         else :
              print(f"so the total price is {function_of_price_of_total_food + function_of_price_of_total_room*50} {x}")
              return function_of_price_of_total_food + function_of_price_of_total_room*50