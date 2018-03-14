
maximumBudget = 0

productBudget = 0

class Shop():
    
    def __init__(self, product_price, transport, transport_price, 
                 transport_time, parking, parking_charge, service_language, wheelchair_accessibility, crowd):
        self.product_price
        self.transport
        self.transport_price
        self.transport_time
        self.parking
        self.parking_charge
        self.service_language
        self.wheelchair_accessibility
        self.crowd

def main():
    askQuestions()
    rules()
    test()

def askQuestions():
    global maximumBudget
    answer = input("Kui suure summa oled valmis kulutada kaubale ja transpordile poodi?")
    maximumBudget = int(answer)

def rules():
    global productBudget
    if maximumBudget < 5:
        productBudget = 5

def test():
    print(productBudget)

main()