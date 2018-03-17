class Shop():
    
    def __init__(self, shopName, productPrice, transportPrice, transportTime, parking, parkingCharge, serviceLanguage, wheelchairAccessibility, shopType):
        self.name = shopName
        self.productPrice = productPrice
        self.transportPrice = transportPrice
        self.transportTime = transportTime
        self.parking = parking
        self.parkingCharge = parkingCharge
        self.serviceLanguage = serviceLanguage
        self.wheelchairAccessibility = wheelchairAccessibility
        self.shopType = shopType
        
class Inputs():
    
    def __init__(self, maximumBudget, preferredTransport, expectedArrival, preferredSelectionSize, 
                 product, area, language, maximumPeople, handicapped, fearsCrowd):
        self.maximumBudget = maximumBudget
        self.preferredTransport = preferredTransport
        self.expectedArrival = expectedArrival
        self.preferredSelectionSize = preferredSelectionSize
        self.product = product
        self.area = area
        self.language = language
        self.maximumPeople = maximumPeople
        self.handicapped = handicapped
        self.fearsCrowd = fearsCrowd
        
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
        self.bestShopType = None
    
    # for testing
    def getAllOutputs(self):
        return [self.product, self.productBudget, self.transportBudget, self.bestTransportTime, 
                self.parkingWish, self.parkingCanPay, self.language, self.wheelchairOrPram, self.bestShopType]

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
    answer = input("Kui suurt kaubavalikut sa soovid (suur/keskmine/pole oluline?)")
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
    handicapped = answer
    answer = input("Kas on oluline, et poes oleks võimalikult vähe rahvast? jah/ei")
    fearsCrowd = answer
    inputs = Inputs(maximumBudget, preferredTransport, expectedArrival, preferredSelectionSize, product, area, language, maximumPeople, handicapped, fearsCrowd)
    return inputs

def rules(inputs):
    outputs = Outputs()

    #productBudget

    if inputs.maximumBudget <= 5:
        outputs.productBudget = 5

    if inputs.maximumBudget > 5:
        outputs.productBudget = 100
    
    #transportBudget

    if inputs.maximumBudget < 5:
        outputs.transportBudget = 0
        

    #bestTransportTime 
    
    #parkingCanPay 
    if (inputs.preferredTransport == "auto"):
        outputs.parkingwish = "yes"
        if(outputs.parkingwish == "yes" and inputs.maximumBudget >= 15):
            outputs.parkingCanPay ="yes"
        else:
            outputs.parkingCanPay ="no"
            
    if (inputs.preferredTransport == "yhistransport" or inputs.preferredTransport == "eraauto" or inputs.preferredTransport == "jalgsi"):
        outputs.parkingwish = "no"
    
    #language
    outputs.language = inputs.language

    # (vanker, ratastool, molemad, ei)")
    #wheelchairOrPram
    if inputs.handicapped == "vanker" or inputs.handicapped == "ratastool" or inputs.handicapped == "molemad":
        outputs.parkingwish = True
        outputs.wheelchairOrPram = True
    else:
        outputs.wheelchairOrPram = False
        

    #bestShopType
    if inputs.fearsCrowd == "ei" and  inputs.preferredSelectionSize == "suur":
        outputs.bestShopType = "hypermarket"
    elif inputs.fearsCrowd == "ei" and  inputs.preferredSelectionSize == "keskmine":
        outputs.bestShopType = "supermarket"
    elif inputs.fearsCrowd == "ei" and  inputs.preferredSelectionSize == "pole oluline":
        outputs.bestShopType = "kauplus"
    elif inputs.fearsCrowd == "jah" and  inputs.preferredSelectionSize == "suur":
        outputs.bestShopType = "supermarket"
    elif inputs.fearsCrowd == "jah" and  inputs.preferredSelectionSize == "keskmine":
        outputs.bestShopType = "kauplus"
    elif inputs.fearsCrowd == "jah" and  inputs.preferredSelectionSize == "pole oluline":
        outputs.bestShopType = "kauplus"

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
    
    # for testing
    outs = outputs.getAllOutputs()
    for output in outs:
        print (output)
        
    for shop in shops:
        shopPoints = 0
        if shop.productPrice[outputs.product] < outputs.productBudget:
            shopPoints += 10
            print(shop.name, "good price")
        if shop.parking and outputs.parkingWish:
            shopPoints += 5
            print(shop.name, "parking")
        if not shop.parkingCharge and outputs.parkingWish and not outputs.parkingCanPay:
            shopPoints += 5
            print(shop.name, "free parking")
        if shop.wheelchairAccessibility and outputs.wheelchairOrPram:
            shopPoints += 5
            print(shop.name, "wheelchair")
        if shop.shopType == outputs.bestShopType:
            shopPoints +=  5
            print(shop.name, "best type")
        shopsPoints.append({shop.name: shopPoints})
    return shopsPoints

def printResults(shopsPoints):
    for shopPoints in shopsPoints:
        for name, points in shopPoints.items():
            print(name, points)

main()




