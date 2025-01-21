class Screwdriver:
    def __init__(self, color, len, type, doseRotate, doseTest):
        self, color = color
        self, len = len 
        self, type = type
        self, doseRotate = doseRotate
        self, doseTest = doseTest

    def rotates(self):
        result = f"I am a {self.len} cm {self.color} {self.type} screwdriver"
        if(self.doseRotate):
            print(result + "and I rotate")
        else:
            print(result + "and I don't rotate")

    def testElectricity(self):
        result = f"I am a {self.len} cm {self.color} {self.type} screwdriver"
        if(self.doseTest):
            print(result + "and I test rotate")
        else:
            print(result + "and I don't rotate")
