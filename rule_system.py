
maximumBudget = 0

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

def main():
    askQuestions()
    rules()
    test()

def askQuestions():
    global maximumBudget
    answer = input("Kui suure summa oled valmis kulutada kaubale ja transpordile poodi?")
    maximumBudget = int(answer)
    
    
    answer = input("Kui palju inimesi poodi tootele järgi läheb?(nt 1,2,3,4,5)")
    
    answer = input("Mis keelt sa räägid? (inglise, vene, eesti, prantsuse, itaalia, hispaania)")
    
    answer = input("Kas on oluline, et piirkond oleks turvaline? (jah/ei)")
    
    answer = input("Mida soovid osta, kas piim, leib, sai, viin?")
    answer = input("Kui suur valik on poes sinu kaup, kas kauplus, supermarket, hypermarket?")
    answer = input("Kui kiiresti soovid poodi jõuda, 5min, 30min, 1h, 2h?")
    answer = input("Millist transporti soovid kasutada kaubale järgi minemiseks, kas jalgsimatk, yhistransport, eratransport voi auto?")
    answer = input("Kui suure summa oled valmis kulutada kaubale ja transpordile poodi? 5, 10, 25 ,50 ,100")
    answer = input("Kas eelistad, et poes oleks võimalikult vähe rahvast? jah/ei")

    

def rules():
    global productBudget
    if maximumBudget < 5:
        productBudget = 5

def test():
    print(productBudget)

main()