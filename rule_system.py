class Shop():
    
    def __init__(self, shopName, productPrice, transportPrice, transportTime, parking, parkingCharge, serviceLanguage, wheelchairAccessibility, crowd):
        self.name = shopName
        self.productPrice = productPrice
        self.transportPrice = transportPrice
        self.transportTime = transportTime
        self.parking = parking
        self.parkingCharge = parkingCharge
        self.serviceLanguage = serviceLanguage
        self.wheelchairAccessibility = wheelchairAccessibility
        self.crowd = crowd
        
class Inputs():
    
    def __init__(self, maximumBudget, preferredTransport, expectedArrival, preferredSelectionSize, product, area, language, maximumPeople, handicaped, popularity):
        self.maximumBudget = maximumBudget
        self.preferredTransport = preferredTransport
        self.expectedArrival = expectedArrival
        self.preferredSelectionSize = preferredSelectionSize
        self.product = product
        self.area = area
        self.language = language
        self.maximumPeople = maximumPeople
        self.handicaped = handicaped
        self.popularity = popularity
        
class Outputs():
    
    def __init__(self):
        self.product = None
        self.productBudget = None
        self.transportBudget = None
        self.bestTransportTime = None
        self.parkingWish = None
        self.parkingCanPay = None
        self.language = None
        self.wheelchairOrPram = None
        self.bestCrowd = None
        self.bestSelectionSize = None

def main():
    inputs = askQuestions()
    outputs = rules(inputs)
    #test(outputs)
    shops = createShops()
    shopsPoints = getShopsPoints(outputs, shops)
    printResults(shopsPoints)

def askQuestions():
    answer = input("Mida soovid osta, kas piim, leib, sai, viin?")
    product = answer     
    answer = input("Kui suure summa oled valmis kulutada kaubale ja transpordile poodi?")
    maximumBudget = int(answer)
    answer = input("Kui suur valik on poes sinu kaup, kas kauplus, supermarket, hypermarket?")
    preferredSelectionSize = answer
    answer = input("Kui kiiresti soovid poodi jõuda, 5min, 30min, 1h, 2h?")
    expectedArrival = answer
    answer = input("Millist transporti soovid kasutada kaubale järgi minemiseks, kas jalgsimatk, yhistransport, eratransport voi auto?")
    preferredTransport = answer
    answer = input("Kui palju inimesi poodi tootele järgi läheb?")
    maximumPeople = int(answer)
    answer = input("Mis keelt sa räägid? (inglise, vene, eesti, prantsuse, itaalia, hispaania)")
    language = answer
    answer = input("Kas on oluline, et piirkond oleks turvaline? (jah/ei)")
    area = answer
    answer = input("Kas lähed ratastooli, vankri, mõlemaga või ilma?(vanker, ratastool, molemad, ei)")
    handicaped = answer
    answer = input("Kas eelistad, et poes oleks võimalikult vähe rahvast? jah/ei")
    popularity = answer
    inputs = Inputs(maximumBudget, preferredTransport, expectedArrival, preferredSelectionSize, product, area, language, maximumPeople, handicaped, popularity)
    return inputs

def rules(inputs):
    outputs = Outputs()
    if inputs.maximumBudget < 5:
        outputs.productBudget = 5

    #productBudget
    if(inputs.maximumBudget >=40):
        outputs.productBudget = 15
    
    #transportBudget
    
    #bestTransportTime 
    
    #parkingCanPay 
    if (inputs.preferredTransport == "auto"):
        parkingwish = "yes"
        if(parkingwish == "yes" and inputs.maximumBudget >= 15):
            outputs.parkingCanPay ="yes"
        else:
            outputs.parkingCanPay ="no"
            
    if (inputs.preferredTransport == "yhistransport" or inputs.preferredTransport == "eraauto" or inputs.preferredTransport == "jalgsi"):
        parkingwish = "no"
    
    #language
    
    #wheelchairOrPram
    
    #bestCrowd 
    
    #bestSelectionSize 

    #transport time


    #transport price

    #product

    outputs.product = inputs.product


    #maximum budget


    return outputs

def test(outputs):
    print(outputs.productBudget)
    
def createShops():
    rimi = Shop("Rimi", {'piim': 10, 'leib': 7, 'sai': 5, 'viin': 10}, 0, 60, True, True, ["eesti", "vene"], False, "hypermarket")
    felixiKaubad = Shop("Felixi kaubad", {'piim': 3, 'leib': 5, 'sai': 6, 'viin': 30}, 10, 15, False, False, ["eesti"], True, "kauplus")
    selver = Shop("Selver", {'piim': 6, 'leib': 4, 'sai': 7, 'viin': 15}, 10, 15, False, False, ["eesti, hispaania , vene, prantsuse, itaalia"], True, "supermarket")
    prisma = Shop("Prisma", {'piim': 2, 'leib': 6, 'sai': 8, 'viin': 17}, 10, 15, False, False, ["eesti, inglise, vene, hispaania"], True, "supermarket")
    kaubakeskus = Shop("Kaubakeskus", {'piim': 12, 'leib': 3, 'sai': 4, 'viin': 8}, 10, 15, False, False, ["eesti"], True, "kauplus")
    ica = Shop("Ica", {'piim': 9, 'leib': 9, 'sai': 4, 'viin': 25}, 0, 60, True, True, ["eesti", "vene, inglise, prantsuse"], False, "hypermarket")
    
    shops = [rimi, felixiKaubad, selver, prisma, kaubakeskus, ica]
    return shops

def getShopsPoints(outputs, shops):
    shopsPoints = []
    
    for shop in shops:
        shopPoints = 0
        if shop.productPrice[outputs.product] < outputs.productBudget:
            shopPoints += 10
        shopsPoints.append({shop.name: shopPoints})
    return shopsPoints

def printResults(shopsPoints):
    for shopPoints in shopsPoints:
        for name, points in shopPoints.items():
            print(name, points)

main()




