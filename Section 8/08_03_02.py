from screwdriver import Screwdriver

slottedScrewdriver = Screwdriver("black", 10, "Slotted", False, True)
slottedScrewdriver .rotates()
slottedScrewdriver .testElectricity()

Tri_wingScrewdriver = Screwdriver("Yellow", 15, "Tri_wing", True, False)
Tri_wingScrewdriver .rotates()
Tri_wingScrewdriver .testElectricity()

PhilipsScrewdriver =Screwdriver("Red", 36, "Philips", True, False)
PhilipsScrewdriver .rotates()
PhilipsScrewdriver .testElectricity()
