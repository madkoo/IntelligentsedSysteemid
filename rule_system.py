class Shop():
    
    def __init__(self, shopName, productPrice, transportPrice, transportTime, parking, 
                 parkingCharge, serviceLanguage, wheelchairAccessibility, shopType, area):
        self.name = shopName
        self.productPrice = productPrice
        self.transportPrice = transportPrice
        self.transportTime = transportTime
        self.parking = parking
        self.parkingCharge = parkingCharge
        self.serviceLanguage = serviceLanguage
        self.wheelchairAccessibility = wheelchairAccessibility
        self.shopType = shopType
        self.area = area
        
class Inputs():
    
    def __init__(self, maximumBudget, preferredTransport, expectedArrival, preferredSelectionSize, 
                 product, safetyImportant, language, numberOfPeople, handicapped, fearsCrowd):
        self.maximumBudget = maximumBudget
        self.preferredTransport = preferredTransport
        self.expectedArrival = expectedArrival
        self.preferredSelectionSize = preferredSelectionSize
        self.product = product
        self.safetyImportant = safetyImportant
        self.language = language
        self.numberOfPeople = numberOfPeople
        self.handicapped = handicapped
        self.fearsCrowd = fearsCrowd
        
class Outputs():
    
    def __init__(self):
        self.product = None
        self.productBudget = None
        self.bestTransport = None
        self.transportBudget = None
        self.bestTransportTime = None
        self.parkingWish = None
        self.parkingCanPay = None
        self.language = None
        self.wheelchairOrPram = None
        self.bestShopType = None
        self.bestArea = None

def testInputs():
    maximumBudget = 30
    preferredTransport = "yhistransport"
    expectedArrival = "30min"
    preferredSelectionSize = "suur"
    product = "piim"
    safetyImportant = "jah"
    language = "inglise"
    numberOfPeople = 2
    handicapped = "vanker"
    fearsCrowd = "jah"
    
    inputs = Inputs(maximumBudget, preferredTransport, expectedArrival, preferredSelectionSize, 
                    product, safetyImportant, language, numberOfPeople, handicapped, fearsCrowd)
    return inputs

def main():
    inputs = askQuestions() #testInputs() ei viitsi küsimustele vastata kogu aeg
    outputs = rules(inputs)
    shops = createShops()
    shopsPoints = getShopsPoints(outputs, shops)
    printResults(shopsPoints)

def askQuestions():
    answer = ""
    while answer not in ["piim", "leib", "sai", "viin"]:
        answer = input("Mida soovid osta, kas piim, leib, sai, viin?")
    product = answer
    answer = ""
    while not answer.isdigit():
        answer = input("Kui suure summa oled valmis kulutada kaubale ja transpordile poodi?")
    maximumBudget = int(answer)
    answer = ""
    while answer not in ["suur", "keskmine", "pole oluline"]:
        answer = input("Kui suurt kaubavalikut sa soovid (suur/keskmine/pole oluline?)")
    preferredSelectionSize = answer
    answer = ""
    while answer not in ["5min", "30min", "1h", "2h"]:
        answer = input("Kui kiiresti soovid poodi jõuda, 5min, 30min, 1h, 2h?")
    expectedArrival = answer
    answer = ""
    while answer not in ["jalgsimatk", "yhistransport", "eratransport", "auto"]:
        answer = input("Millist transporti soovid kasutada kaubale järgi minemiseks, kas jalgsimatk, yhistransport, eratransport voi auto?")
    preferredTransport = answer
    answer = ""
    while not answer.isdigit():
        answer = input("Kui palju inimesi poodi tootele järgi läheb?")
    numberOfPeople = int(answer)
    answer = ""
    while answer not in ["inglise", "vene", "eesti", "prantsuse", "itaalia", "hispaania"]:
        answer = input("Mis keelt sa räägid? (inglise, vene, eesti, prantsuse, itaalia, hispaania)")
    language = answer
    answer = ""
    while answer not in ["jah", "ei"]:
        answer = input("Kas on oluline, et piirkond oleks turvaline? (jah/ei)")
    safetyImportant = answer
    answer = ""
    while answer not in ["ratastool", "vanker", "molemad", "ei"]:
        answer = input("Kas lähed ratastooli, vankri, mõlemaga või ilma?(vanker, ratastool, molemad, ei)")
    handicapped = answer
    answer = ""
    while answer not in ["jah", "ei"]:
        answer = input("Kas on oluline, et poes oleks võimalikult vähe rahvast? jah/ei")
    fearsCrowd = answer
    
    inputs = Inputs(maximumBudget, preferredTransport, expectedArrival, preferredSelectionSize, 
                    product, safetyImportant, language, numberOfPeople, handicapped, fearsCrowd)
    return inputs

def rules(inputs):
    outputs = Outputs()

    #bestTransport
    
    #tahab jalgsi
    if (inputs.preferredTransport == "jalgsimatk" and inputs.expectedArrival == "5min" and inputs.maximumBudget >= 10
        and (inputs.handicapped == "ei" or inputs.handicapped == "vanker")):
        outputs.bestTransport = "yhistransport"
    
    elif inputs.preferredTransport == "jalgsimatk":
        outputs.bestTransport = "jalgsimatk"

    # tahab taksoga
    elif (inputs.preferredTransport == "eratransport" and inputs.maximumBudget >= 50 and inputs.numberOfPeople <= 4
        and inputs.handicapped == "ei"):
        outputs.bestTransport = "eratransport"

    elif inputs.preferredTransport ==  "eratransport" and 10 <= inputs.maximumBudget < 50:
        outputs.bestTransport = "yhistransport"
          
    elif inputs.preferredTransport ==  "eratransport" and inputs.maximumBudget < 10:
        outputs.bestTransport = "jalgsimatk"
        
    elif inputs.preferredTransport == "eratransport" and inputs.handicapped == "vanker":
        outputs.bestTransport = "yhistransport"
        
    elif inputs.preferredTransport == "eratransport" and (inputs.handicapped == "ratastool" or inputs.handicapped == "molemad"):
        outputs.bestTransport = "jalgsi"
    
    elif inputs.preferredTransport == "eratransport" and inputs.numberOfPeople > 4:
        outputs.bestTransport = "yhistransport"

    #yhistransport
    elif (inputs.preferredTransport == "yhistransport" and inputs.maximumBudget >= 10
        and (inputs.handicapped == "ei" or inputs.handicapped == "vanker")):
        outputs.bestTransport = "yhistransport"
        
    elif inputs.preferredTransport == "yhistransport" and inputs.maximumBudget < 10:
        outputs.bestTransport = "jalgsimatk"
        
    elif inputs.preferredTransport == "yhistransport" and inputs.handicapped != "ei":
        outputs.bestTransport = "jalgsimatk"
              
    #enda auto
    elif inputs.preferredTransport == "auto" and inputs.numberOfPeople <= 5:
        outputs.bestTransport = "auto"
        
    elif (inputs.preferredTransport == "auto" and inputs.maximumBudget >= 50 
        and inputs.numberOfPeople <= 4 and inputs.handicapped == "ei"):
        outputs.bestTransport = "auto"
        
    elif (inputs.preferredTransport == "auto" and inputs.maximumBudget >= 30 
        and inputs.numberOfPeople <= 4 and inputs.handicapped == "jah"):
        outputs.bestTransport = "auto"
        
    elif (inputs.preferredTransport == "auto" and inputs.maximumBudget >= 20 
        and inputs.numberOfPeople <= 2 and inputs.handicapped == "ei"):
        outputs.bestTransport = "auto"
             
    elif (inputs.preferredTransport == "auto" and inputs.numberOfPeople > 5 and inputs.maximumBudget >= 50 
        and inputs.numberOfPeople <= 4 and inputs.handicapped == "ei"):
        outputs.bestTransport = "eratransport"
        
    elif (inputs.preferredTransport == "auto" and inputs.numberOfPeople > 5 and inputs.maximumBudget >= 10 
        and inputs.numberOfPeople <= 4 and (inputs.handicapped == "ei" or inputs.handicapped == "vanker")):
        outputs.bestTransport = "eratransport"
    else:
        outputs.bestTransport = "jalgsimatk"

    #transportBudget
    if outputs.bestTransport == "jalgsimatk":
        outputs.transportBudget = 0
    elif outputs.bestTransport == "auto" and inputs.maximumBudget > 10:
        outputs.transportBudget = 5
    elif outputs.bestTransport == "yhistransport":
        if inputs.numberOfPeople == 1 and inputs.maximumBudget >= 10:
            outputs.transportBudget = 5
        elif inputs.numberOfPeople > 3 and inputs.maximumBudget > 25:
            outputs.transportBudget = 20
        elif inputs.maximumBudget > 15:
            outputs.transportBudget = 10
        else:
            outputs.transportBudget = 0
    elif outputs.bestTransport == "eratransport":
        outputs.transportBudget = 50
    else:
        outputs.transportBudget = 0
    
    #bestTransportTime
    if inputs.expectedArrival == "5min":
        outputs.bestTransportTime = 5
    elif inputs.expectedArrival == "30min":
        outputs.bestTransportTime = 30
    elif inputs.expectedArrival == "1h":
        outputs.bestTransportTime = 60
    elif inputs.expectedArrival == "2h":
        outputs.bestTransportTime = 120
    
    #productBudget

    outputs.productBudget = inputs.maximumBudget - outputs.transportBudget
    
    #parkingWish
    #parkingCanPay 
    if (inputs.preferredTransport == "auto"):
        outputs.parkingWish = "yes"
        if(outputs.parkingWish == "yes" and inputs.maximumBudget >= 15):
            outputs.parkingCanPay ="yes"
        else:
            outputs.parkingCanPay ="no"
            
    if (inputs.preferredTransport == "yhistransport" or inputs.preferredTransport == "eratransport"
        or inputs.preferredTransport == "jalgsi"):
        outputs.parkingWish = "no"
    
    #language
    outputs.language = inputs.language

    # (vanker, ratastool, molemad, ei)")
    #wheelchairOrPram
    if inputs.handicapped == "vanker" or inputs.handicapped == "ratastool" or inputs.handicapped == "molemad":
        outputs.wheelchairOrPram = True
    else:
        outputs.wheelchairOrPram = False
        
    #area
    if(inputs.safetyImportant == "jah" and inputs.fearsCrowd == "ei"):
        outputs.bestArea = "rahvarohke"
    elif(inputs.safetyImportant == "jah" and inputs.fearsCrowd == "jah"):
        outputs.bestArea = "keskmine"
    elif(inputs.safetyImportant == "ei" and inputs.fearsCrowd == "jah"):
        outputs.bestArea = "rahulik"
    elif(inputs.safetyImportant == "ei" and inputs.fearsCrowd == "ei" and inputs.preferredSelectionSize == "pole oluline"):
        outputs.bestArea = "rahulik"
    elif(inputs.safetyImportant == "ei" and inputs.fearsCrowd == "ei" and inputs.preferredSelectionSize == "suur"):
        outputs.bestArea = "rahvarohke"
    else: 
        outputs.bestArea = "keskmine"
        
        
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


    
    
    return outputs
    
def createShops():
    rimi = Shop("Rimi", {'piim': 10, 'leib': 7, 'sai': 5, 'viin': 10},
                {'jalgsimatk': 0, 'yhistransport': 10, 'eratransport': 50, 'auto': 0}, 
                {'jalgsimatk': 30, 'yhistransport': 10, 'eratransport': 8, 'auto': 5}, 
                True, True, ["eesti", "vene"], False, "hypermarket","rahvarohke")
    felixiKaubad = Shop("Felixi kaubad", {'piim': 3, 'leib': 5, 'sai': 6, 'viin': 30}, 
                {'jalgsimatk': 0, 'yhistransport': 5, 'eratransport': 20, 'auto': 0}, 
                {'jalgsimatk': 10, 'yhistransport': 5, 'eratransport': 4, 'auto': 2}, 
                False, False, ["eesti"], True, "kauplus","rahulik")
    selver = Shop("Selver", {'piim': 6, 'leib': 4, 'sai': 7, 'viin': 15}, 
                {'jalgsimatk': 0, 'yhistransport': 15, 'eratransport': 60, 'auto': 0}, 
                {'jalgsimatk': 40, 'yhistransport': 15, 'eratransport': 10, 'auto': 7}, 
                False, False, ["eesti, hispaania , vene, prantsuse, itaalia"], True, "supermarket","rahvarohke")
    prisma = Shop("Prisma", {'piim': 2, 'leib': 6, 'sai': 8, 'viin': 17}, 
                {'jalgsimatk': 0, 'yhistransport': 10, 'eratransport': 60, 'auto': 0}, 
                {'jalgsimatk': 20, 'yhistransport': 8, 'eratransport': 6, 'auto': 4}, 
                False, False, ["eesti, inglise, vene, hispaania"], True, "supermarket","rahvarohke")
    kaubakeskus = Shop("Kaubakeskus", {'piim': 12, 'leib': 3, 'sai': 4, 'viin': 8}, 
                {'jalgsimatk': 0, 'yhistransport': 15, 'eratransport': 80, 'auto': 0}, 
                {'jalgsimatk': 100, 'yhistransport': 30, 'eratransport': 20, 'auto': 10}, 
                False, False, ["eesti"], True, "kauplus","keskmine")
    ica = Shop("Ica", {'piim': 9, 'leib': 9, 'sai': 4, 'viin': 25}, 
               {'jalgsimatk': 0, 'yhistransport': 8, 'eratransport': 50, 'auto': 0}, 
               {'jalgsimatk': 60, 'yhistransport': 20, 'eratransport': 15, 'auto': 8}, 
               True, True, ["eesti", "vene, inglise, prantsuse"], False, "hypermarket","keskmine")
    grossiToidukaubad = Shop("Grossi Toidukaubad", {'piim': 5, 'leib': 4, 'sai': 2, 'viin': 7}, 
               {'jalgsimatk': 2, 'yhistransport': 15, 'eratransport': 45, 'auto': 3}, 
               {'jalgsimatk': 20, 'yhistransport': 15, 'eratransport': 12, 'auto': 6}, 
               False, True, ["eesti", "vene"], True, "kauplus","rahulik")
    
    shops = [rimi, felixiKaubad, selver, prisma, kaubakeskus, ica, grossiToidukaubad]
    return shops

def getShopsPoints(outputs, shops):
    shopsPoints = []
    for shop in shops:
        shopPoints = 0
        if shop.productPrice[outputs.product] < outputs.productBudget:
            shopPoints += 10
        if shop.transportPrice[outputs.bestTransport] < outputs.transportBudget:
            shopPoints += 10
        if shop.transportTime[outputs.bestTransport] < outputs.bestTransportTime:
            shopPoints += 5
        if shop.parking and outputs.parkingWish:
            shopPoints += 5
        if not shop.parkingCharge and outputs.parkingWish and not outputs.parkingCanPay:
            shopPoints += 5
        if outputs.language in shop.serviceLanguage:
            shopPoints += 5
        if shop.wheelchairAccessibility and outputs.wheelchairOrPram:
            shopPoints += 5
        if shop.shopType == outputs.bestShopType:
            shopPoints +=  5
        if shop.area == outputs.bestArea:
            shopPoints +=  5
        shopsPoints.append({"name":shop.name, "points": shopPoints})
    return shopsPoints

def printResults(shopsPointsDict):
    sortedShops = sorted(shopsPointsDict, key=lambda k: k['points'], reverse=True) 
    for rank, shop in enumerate(sortedShops):
        print(shop['name'] + ":", shop['points'], "punkti")
        if rank > 1:
            break;

main()




