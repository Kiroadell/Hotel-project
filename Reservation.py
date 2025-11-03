print("Jesus is the way and the truth and the life , Amen")
# باسم الثالوث القدوس اميني يا رب بشفاعة ام النور الطاهرة مريم و شفاعة جميع النفوس و شفاعة جميع القديسين و شفتعة جميع الملاءكة و شفاعة جميع التلاميذ و شفاعة جميع الاباء الكهنة و شفاعة جميع الاباء الرهبان و شفاعة جميع الرسل امين
import random
from hotel import Hotel  # Fixed import case
from room import room
from visitor import visitor
from Menu import Menu
from outiles import View  # Removed unused random_number import


class reservation:
    def __init__(self):
        self.menu1 = Menu()
        self.visitor1 = visitor()
        hotel1 = Hotel()
        hotel2 = Hotel()
        hotel3 = Hotel()
        hotel4 = Hotel()
        hotel5 = Hotel()
        hotel6 = Hotel()
        hotel1.get_name_of_hotel()
        hotel2.get_name_of_hotel()
        hotel3.get_name_of_hotel()
        hotel4.get_name_of_hotel()
        hotel5.get_name_of_hotel()
        hotel6.get_name_of_hotel()
        self.room1 = room()
        self.hotels = [hotel1, hotel2, hotel3, hotel4, hotel5, hotel6]
        # choose a hotel for this reservation (random)
        self.hotel_used = random.choice(self.hotels)

    def reservation_procedure(self):
        # 1 take location and display hotels
        desir = self.menu1.welcome_menu()
        if desir == "yes":
            self.visitor1.choose_location()
            for i in range(6):
                if i == 0:
                    print(f"you have these hotels in {self.visitor1.location} :")
                print(self.hotels[i].name)

            # 2 take stars and check if he want to reserve in it or not
            stars = self.visitor1.how_many_stars()
            self.hotel_used.stars = stars
            print(f"the hotel named {self.hotel_used.name} has {stars} stars")
            continue_to_reserve_after_stars = input("do you want to reserve in it ? yes or no :")
            if continue_to_reserve_after_stars.lower() == "yes":

                # 3 take numbers of night and check not more than 14
                while True:
                    numbers_of_night = self.visitor1.numbers_of_nights()
                    if numbers_of_night not in range(2, 15):
                        print("you cant reserve more than 14 nights and less than 2")
                        continue
                    else:
                        print(f"so you need a room for {numbers_of_night} nights")
                        self.room1.nights_avalible = numbers_of_night
                        break

                # 4 take numbers members and assign it to room beds
                while True:
                    numbers_of_members = self.visitor1.get_numbers_of_members()
                    # assign beds in room according to members
                    self.room1.beds = numbers_of_members
                    print(f"so you need a room with {self.room1.beds} beds for {numbers_of_members} members")
                    break

                # 5 take view desir
                while True:
                    x = input("do you want a view ? yes or no : ")
                    if x.lower() == "yes":
                        for i in range(len(View)):
                            print(f"{i+1} - {View[i]}")
                        y = input("what do you need? (enter name or number): ")
                        if y.isdigit():
                            idx = int(y) - 1
                            if 0 <= idx < len(View):
                                self.room1.view = View[idx]
                        elif y in View:
                            self.room1.view = y
                        else:
                            # default to first view if unrecognized
                            self.room1.view = View[0]
                        print(f"view selected: {self.room1.view}")
                        break
                    else:
                        # no view desired
                        self.room1.view = None
                        break

                # 6 Food
                x = self.visitor1.how_many_meals()
                print(f"you choosed {x} meals")
                self.hotel_used.numbers_of_meals = x

                # 7 what food do you want
                x = self.visitor1.what_food()
                print(f"you choosed {x}")
                self.hotel_used.food_type = x

                # 8 print all information and if continue
                # compute totals first
                price_per_night = self.hotel_used.price_per_night
                food_price_per_day = self.hotel_used.food_price_per_day
                number_of_nights = self.room1.nights_avalible
                numbers_of_members = self.visitor1.numbers_of_membres
                total_room_price = self.hotel_used.price_oftotal_reservation_of_room(number_of_nights, numbers_of_members)
                total_food_price = self.hotel_used.food_price(self.hotel_used.numbers_of_meals, number_of_nights)
                
                # Show info and ask to proceed
                proceed = self.menu1.print_all_information_and_if_continue(
                    self.hotel_used.name,
                    self.hotel_used.stars,
                    self.room1.nights_avalible,
                    self.room1.beds,
                    self.room1.view or "no view",  # Handle None view
                    self.hotel_used.numbers_of_meals,
                    self.hotel_used.food_type,
                )
                
                if proceed:
                    total_price = self.menu1.calculation_menu(
                        price_per_night,
                        food_price_per_day,
                        number_of_nights,
                        numbers_of_members,
                        total_room_price,
                        total_food_price,
                        "Egypt" if self.hotel_used.location == "Egypt" else "Other"  # Fix currency logic
                    )

                    # 9 check budget
                    if self.visitor1.budget >= total_price:
                    self.visitor1.will_buy(total_price)
                    print("thanks for visting us ")
                else:
                    self.visitor1.do_not_have_money(total_price)
                    want_to_amount = input("do you want to amount ? yes or no : ")
                    if want_to_amount.lower() == "yes":
                        self.visitor1.want_toamount(total_price)
                        print("thanks for visiting us enjoy your time")
                    else:
                        print("thanks for visiting us ")