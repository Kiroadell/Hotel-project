print("Jesus is the way and the truth and the life , Amen")
# باسم الثالوث القدوس اميني يا رب بشفاعة ام النور الطاهرة مريم و شفاعة جميع النفوس و شفاعة جميع القديسين و شفتعة جميع الملاءكة و شفاعة جميع التلاميذ و شفاعة جميع الاباء الكهنة و شفاعة جميع الاباء الرهبان و شفاعة جميع الرسل امين
from hotel import Hotel
import random

class room:
   def __init__(self):
    #je que veux prendre le nombre que le visiteur va l’entre puis je vais verifier si il est disponible ou non et l’attribuer a la chambre
    self.number_room = None  # Will be set by choose_number_room
    self.nights_avalible = 0  # done
    self.beds = 0  # == numbers of members of visitor
    self.tv_or_not = random.choice([True, False])
    self.view = "" #random from view’s list



   def choose_number_room(self,hotel : Hotel) :
       while True :
           number = random.choice(hotel.rooms)
           self.number_room = number
           return number
