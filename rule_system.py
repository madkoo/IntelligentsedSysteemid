
productBudget = 0

class Shop():
    
    def __init__(self, product_price, transport, transport_price, 
                 transport_time, parking, parking_charge, service_language, wheelchair_accessibility, crowd):
        self.product_price = product_price
        self.transport = product_price
        self.transport_price = transport_price
        self.transport_time = transport_time
        self.parking = parking
        self.parking_charge = parking_charge
        self.service_language = service_language
        self.wheelchair_accessibility = wheelchair_accessibility
        self.crowd = crowd
        
class Inputs():
    
    def __init__(self, maximumBudget):
        self.maximumBudget = maximumBudget
        
class Outputs():
    
    def __init__(self):
        self.productBudget = None
        self.best_transport = None
        self.transport_budget = None
        self.best_transport_time = None
        self.parking_w== h = None
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
    maximumBudget = int(answer)

    answer = input("Kui palju inimesi poodi tootele järgi läheb?(nt 1,2,3,4,5)")
    
    answer = input("Mis  keelt sa räägid? (inglise, vene, eesti, prantsuse, itaalia, hispaania)")
    
    answer = input("Kas on oluline, et piirkond oleks turvaline? (jah/ei)")
    
    answer = input("Mida soovid osta, kas piim, leib, sai, viin?")
    answer = input("Kui suur valik on poes sinu kaup, kas kauplus, supermarket, hypermarket?")
    answer = input("Kui kiiresti soovid poodi jõuda, 5min, 30min, 1h, 2h?")
    answer = input("Millist transporti soovid kasutada kaubale järgi minemiseks, kas jalgsimatk, yhistransport, eratransport voi auto?")
    answer = input("Kui suure summa oled valmis  kulutada kaubale ja transpordile poodi? 5, 10, 25 ,50 ,100")
    answer = input("Kas eelistad, et poes oleks võimalikult vähe rahvast? jah/ei")

    inputs = Inputs(maximumBudget)
    return inputs

def rules(inputs):
    outputs = Outputs()
    if inputs.maximumBudget < 5:
        outputs.productBudget = 5
        
    return outputs

def test(outputs):
    print(outputs.productBudget)

main()



#
#  if maximum-budget == 5:
    
#		
# if maximum-budget >= 0 & maximum-budget <=10:
#        
#   if maximum-budget >= 10 & maximum-budget <=20:
#        
#       jalksi

#   if maximum-budget >= 0 & maximum-budget <=10 & expected-arrival ==  "5min" & 
#      handicaped ==  ei & maximum-people <= 2 & preferred-transport ==  jalgsimatk:

#  
#   if maximum-budget >= 0 & maximum-budget <=5 & expected-arrival ==  30min 
#     & handicaped ==  ei & maximum-people <= 5 & preferred-transport ==  jalgsimatk:
#       
#  
#   if maximum-budget >= 0 & maximum-budget <=5 & expected-arrival ==  1h 
#   & handicaped ==  ei & maximum-people <= 5 & preferred-transport ==  jalgsimatk:
#      
#  
#   if maximum-budget >= 0 & maximum-budget <=5 & expected-arrival ==  2h 
#      & handicaped ==  ei & maximum-people <= 5 & preferred-transport ==  jalgsimatk:

#
#   if maximum-budget >= 0 & maximum-budget <=5 & handicaped ==  ei
 #     & maximum-people <= 5 & preferred-transport ==  yh== transport:

#  
#   if maximum-budget >= 0 & maximum-budget <=10 & expected-arrival ==  1h
#     & handicaped ==  ei & maximum-people <= 4 & preferred-transport ==  eratransport:
#       
#  
#  
#        #takso
#   if maximum-budget >= 50 & maximum-budget <=100 & expected-arrival ==  30min
#      & handicaped ==  ei & maximum-people <= 4 & preferred-transport ==  eratransport:
    
#  
#   if maximum-budget >= 50 & maximum-budget <=100 & expected-arrival ==  5min
#      & handicaped ==  ei & maximum-people <= 4 & preferred-transport ==  eratransport:
#        
#
#   if maximum-budget >= 50 & maximum-budget <=100 & expected-arrival ==  30min 
#      & handicaped ==  jah & maximum-people <= 4 & preferred-transport ==  eratransport:
#        
#  
#   if maximum-budget >= 50 & maximum-budget <=100 & expected-arrival ==  5min 
#      & handicaped ==  jah & maximum-people <= 4 & preferred-transport ==  eratransport:
#        
#
#

#   yhistransport
#   if maximum-budget >= 10 & maximum-budget <= 49 & expected-arrival ==  30min handicaped ==  ei
#       & maximum-people <= 5 & preferred-transport ==  yh== transport:
#        
#   if maximum-budget >= 10 & maximum-budget <= 49 & expected-arrival ==  30min handicaped ==  jah
#       & maximum-people <= 5 & preferred-transport ==  yh== transport:
#        
#   if maximum-budget >= 10 & maximum-budget <= 49 & expected-arrival ==  1h handicaped ==  ei
 #       & maximum-people <= 5 & preferred-transport ==  yh== transport:

#   if maximum-budget >= 10 & maximum-budget <= 49 & expected-arrival ==  1h handicaped ==  jah
#       & maximum-people <= 5 & preferred-transport ==  yh== transport

#   if maximum-budget >= 10 & maximum-budget <= 49 & expected-arrival ==  2h handicaped ==  jah
#        & maximum-people <= 5 & preferred-transport ==  yh== transport:
#       
#   if maximum-budget >= 10 & maximum-budget <= 49 & expected-arrival ==  2h handicaped ==  ei
#       & maximum-people <= 5 & preferred-transport ==  yh== transport:



