
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
        self.productBudget = 0

def main():
    inputs = askQuestions()
    outputs = rules(inputs)
    test(outputs)

def askQuestions():
    answer = input("Kui suure summa oled valmis kulutada kaubale ja transpordile poodi?")
    maximumBudget = int(answer)
    
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