class Shop():
    
    def __init__(self, product_price, transport_price, 
                 transport_time, parking, parking_charge, service_language, wheelchair_accessibility, crowd):
        self.product_price = product_price
        self.transport_price = transport_price
        self.transport_time = transport_time
        self.parking = parking
        self.parking_charge = parking_charge
        self.service_language = service_language
        self.wheelchair_accessibility = wheelchair_accessibility
        self.crowd = crowd
        
class Inputs():
    
    def __init__(self, maximumBudget, preferredTransport, expectedArrival, preferredSelectionSize, product, area,language, maximumPeople, handicaped,popularity):
        self.maximumBudget = maximumBudget
        self.preferredTransport = preferredTransport
        self.expectedArrival = expectedArrival
        self.preferredSelectionSize = preferredSelectionSize
        self.product = product
        self.area = area
        self.language = language
        self.inputs.maximumPeople = inputs.maximumPeople
        self.handicaped = handicaped
        self.popularity = popularity
        
class Outputs():
    
    def __init__(self):
        self.productBudget = None
        self.best_transport = None
        self.transport_budget = None
        self.best_transport_time = None
        self.parking_wish = None
        self.parking_can_pay = None
        self.language = None
        self.wheelchair_or_pram = None
        self.best_crowd = None
        self.best_selection_size = None

def main():
    inputs = askQuestions()
    outputs = rules(inputs)
    test(outputs)

def askQuestions():

    answer = input("Kui suure summa oled valmis  kulutada kaubale ja transpordile poodi?")
    inputs.maximumBudget = int(answer)

    answer = input("Kui palju inimesi poodi tootele järgi läheb?(nt 1,2,3,4,5)")
    
    answer = input("Mis  keelt sa räägid? (inglise, vene, eesti, prantsuse, itaalia, hispaania)")
    
    answer = input("Kas on oluline, et piirkond oleks turvaline? (jah/ei)")
    



    answer = input("Mida soovid osta, kas piim, leib, sai, viin?")
    product = answer     
    answer = input("Kui suure summa oled valmis kulutada kaubale ja transpordile poodi?")
    inputs.maximumBudget = int(answer)
    answer = input("Kui suur valik on poes sinu kaup, kas kauplus, supermarket, hypermarket?")
    preferredSelectionSize = answer
    answer = input("Kui kiiresti soovid poodi jõuda, 5min, 30min, 1h, 2h?")
    inputs.expectedArrival = answer
    answer = input("Millist transporti soovid kasutada kaubale järgi minemiseks, kas jalgsimatk, yhistransport, eratransport voi auto?")

    answer = input("Kui suure summa oled valmis  kulutada kaubale ja transpordile poodi? 5, 10, 25 ,50 ,100")

    preferredTransport = answer
    answer = input("Kui palju inimesi poodi tootele järgi läheb?")
    inputs.maximumPeople = int(answer)
    answer = input("Mis keelt sa räägid? (inglise, vene, eesti, prantsuse, itaalia, hispaania)")
    language = answer
    answer = input("Kas on oluline, et piirkond oleks turvaline? (jah/ei)")
    area = answer
    answer = input("Kas lähed ratastooli, vankri, mõlemaga või ilma?(vanker, ratastool, molemad, ei)")
    inputs.handicaped = answer

    answer = input("Kas eelistad, et poes oleks võimalikult vähe rahvast? jah/ei")
    popularity = answer
    inputs = Inputs(inputs.maximumBudget, preferredTransport, inputs.expectedArrival, preferredSelectionSize, product,area, language,inputs.maximumPeople, inputs.handicaped, popularity)
    return inputs

def rules(inputs):
    outputs = Outputs()
    if inputs.inputs.maximumBudget < 5:
        outputs.productBudget = 5

#jalksi

    if (inputs.maximumBudget >= 0 and inputs.maximumBudget <=10 and inputs.expectedArrival == "5min"
        and inputs.handicaped == "ei" and inputs.maximumPeople <= 2 and inputs.preferredTransport == "jalgsimatk"):
        outputs.bestTransport = "jalksimatk"

  
    if (inputs.maximumBudget >= 0 and inputs.maximumBudget <= 5 and inputs.expectedArrival == "30min" and inputs.handicaped == "ei" and inputs.maximumPeople <= 5 and inputs.preferredTransport == "jalgsimatk"):
       outputs.bestTransport = "jalksimatk"
  
    if (inputs.maximumBudget >= 0 and inputs.maximumBudget <= 5 and inputs.expectedArrival == "1h" 
      and inputs.handicaped == "ei" and inputs.maximumPeople <= 5 and inputs.preferredTransport == "jalgsimatk"):
          outputs.bestTransport = "jalksimatk"

    if (inputs.maximumBudget >= 0 and inputs.maximumBudget <= 5 and inputs.expectedArrival == "2h" 
        and inputs.handicaped == "ei" and inputs.maximumPeople <= 5 and inputs.preferredTransport ==  "jalgsimatk"):
          outputs.bestTransport = "jalksimatk"

    if (inputs.maximumBudget >= 0 and inputs.maximumBudget <= 5 and inputs.handicaped ==  "ei"
        and inputs.expectedArrival == "2h" and inputs.maximumPeople <= 5 and inputs.preferredTransport == "yhistransport"):
          outputs.bestTransport = "jalksimatk"
  
    if (inputs.maximumBudget >= 0 and inputs.maximumBudget <=10 and inputs.expectedArrival == "1h"
        and inputs.handicaped == "ei" and inputs.maximumPeople <= 4 and inputs.preferredTransport ==  "eratransport"):
          outputs.bestTransport = "jalksimatk"
  
  
        #takso
    if (inputs.maximumBudget >= 50 and inputs.maximumBudget <=100 and inputs.expectedArrival == "30min"
      and inputs.handicaped == "ei" and inputs.maximumPeople <= 4 and inputs.preferredTransport == "eratransport"):
          outputs.bestTransport = "eratransport"
  
    if (inputs.maximumBudget >= 50 and inputs.maximumBudget <=100 and inputs.expectedArrival == "5min"
      and inputs.handicaped == "ei" and inputs.maximumPeople <= 4 and inputs.preferredTransport == "eratransport"):
          outputs.bestTransport = "eratransport"

    if (inputs.maximumBudget >= 50 and inputs.maximumBudget <=100 and inputs.expectedArrival == "30min" 
      and inputs.handicaped == "jah" and inputs.maximumPeople <= 4 and inputs.preferredTransport == "eratransport"):
          outputs.bestTransport = "eratransport"
  
    if (inputs.maximumBudget >= 50 and inputs.maximumBudget <=100 and inputs.expectedArrival == "5min" 
      and inputs.handicaped == "jah" and inputs.maximumPeople <= 4 and inputs.preferredTransport == "eratransport"):
          outputs.bestTransport = "eratransport"



   #yhistransport
    if (inputs.maximumBudget >= 10 and inputs.maximumBudget <= 49 and inputs.expectedArrival == "30min" and inputs.handicaped == "ei"
        and inputs.maximumPeople <= 5 and inputs.preferredTransport == "yhistransport"):
           outputs.bestTransport = "yhistransport"
    if (inputs.maximumBudget >= 10 and inputs.maximumBudget <= 49 and inputs.expectedArrival == "30min" and inputs.handicaped == "jah"
        and inputs.maximumPeople <= 5 and inputs.preferredTransport == "yhistransport"):
           outputs.bestTransport = "yhistransport"
    if (inputs.maximumBudget >= 10 and inputs.maximumBudget <= 49 and inputs.expectedArrival == "1h" and inputs.handicaped == "ei"
         and inputs.maximumPeople <= 5 and inputs.preferredTransport == "yhistransport"):
            outputs.bestTransport = "yhistransport"
    if (inputs.maximumBudget >= 10 and inputs.maximumBudget <= 49 and inputs.expectedArrival == "1h" and inputs.handicaped == "jah"
        and inputs.maximumPeople <= 5 and inputs.preferredTransport == "yhistransport"):
           outputs.bestTransport = "yhistransport"
    if (inputs.maximumBudget >= 10 and inputs.maximumBudget <= 49 and inputs.expectedArrival == "2h" and inputs.handicaped == "jah"
        and inputs.maximumPeople <= 5 and inputs.preferredTransport == "yhistransport"):
          outputs.bestTransport = "yhistransport"
    if (inputs.maximumBudget >= 10 and inputs.maximumBudget <= 49 and inputs.expectedArrival == "2h" and inputs.handicaped == "ei"
        and inputs.maximumPeople <= 5 and inputs.preferredTransport == "yhistransport"):
          outputs.bestTransport = "yhistransport"
          
 #enda auto
 
    if (inputs.maximumBudget >= 0 and inputs.maximumBudget <= 100 and inputs.expectedArrival == "5min" 
        and inputs.handicaped == "ei" and inputs.maximumPeople <= 5 and inputs.preferredTransport == "auto"):
    		 outputs.bestTransport = "auto"
 
    if (inputs.maximumBudget >= 0 and inputs.maximumBudget <= 100 and inputs.expectedArrival == "5min"
        and inputs.handicaped == "jah" and inputs.maximumPeople <= 5 and inputs.preferredTransport == "auto"):
            outputs.bestTransport = "auto"
 
    if (inputs.maximumBudget >= 0 and inputs.maximumBudget <= 100 and inputs.expectedArrival == "30min"
        and inputs.handicaped == "ei" and inputs.maximumPeople <= 5 and inputs.preferredTransport == "auto"):
        outputs.bestTransport = "auto"


    if (inputs.maximumBudget >= 0 and inputs.maximumBudget <= 100 and inputs.expectedArrival == "30min" 
        and inputs.handicaped == "jah" and inputs.maximumPeople <= 5 and inputs.preferredTransport == "auto"):
        outputs.bestTransport = "auto"
 
    if (inputs.maximumBudget >= 0 and inputs.maximumBudget <= 100 and inputs.expectedArrival == "1h" 
        and inputs.handicaped == "ei" and inputs.maximumPeople <= 5 and inputs.preferredTransport == "auto"):
        outputs.bestTransport = "auto"

    if(inputs.maximumBudget >= 0 and inputs.maximumBudget <= 100 and inputs.expectedArrival == "1h" and 
        inputs.handicaped == "jah" and inputs.maximumPeople <= 5 and inputs.preferredTransport == "auto"):
        outputs.bestTransport = "auto"

    if (inputs.maximumBudget >= 0 and inputs.maximumBudget <= 100 and inputs.expectedArrival == "2h" 
        and inputs.handicaped == "ei" and inputs.maximumPeople <= 5 and inputs.preferredTransport == "auto"):
        outputs.bestTransport = "auto"

 
    if (inputs.maximumBudget >= 0 and inputs.maximumBudget <= 100 and inputs.expectedArrival == "2h" 
        and inputs.handicaped == "jah" and inputs.maximumPeople <= 5 and inputs.preferredTransport == "auto"):
        outputs.bestTransport = "auto"


    return outputs

def test(outputs):
    print(outputs.productBudget)
    
def createShops():
    rimi = Shop({'piim': 10, 'leib': 7, 'sai': 5, 'viin': 10}, 0, 60, True, True, ["eesti", "vene"], False, "hypermarket")
    felixiKaubad = Shop({'piim': 3, 'leib': 5, 'sai': 6, 'viin': 30}, 10, 15, False, False, ["eesti"], True, "kauplus")
    Selver = Shop({'piim': 6, 'leib': 4, 'sai': 7, 'viin': 15}, 10, 15, False, False, ["eesti, hispaania , vene, prantsuse, itaalia"], True, "supermarket")
    Prisma = Shop({'piim': 2, 'leib': 6, 'sai': 8, 'viin': 17}, 10, 15, False, False, ["eesti, inglise, vene, hispaania"], True, "supermarket")
    Kaubakeskus = Shop({'piim': 12, 'leib': 3, 'sai': 4, 'viin': 8}, 10, 15, False, False, ["eesti"], True, "kauplus")
    Ica = Shop({'piim': 9, 'leib': 9, 'sai': 4, 'viin': 25}, 0, 60, True, True, ["eesti", "vene, inglise, prantsuse"], False, "hypermarket")
main()

