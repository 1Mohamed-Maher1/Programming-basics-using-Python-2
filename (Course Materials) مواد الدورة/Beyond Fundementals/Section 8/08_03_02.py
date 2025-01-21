from screwdriver import Screwdriver

slottedScrewdriver = Screwdriver("Black", 10, "Slotted", False, True)
slottedScrewdriver.rotates()
slottedScrewdriver.testsElectricity()

triWingScrewdriver = Screwdriver("Yellow", 15, "Tri_wing", True, False)
triWingScrewdriver.rotates()
triWingScrewdriver.testsElectricity()

philipsScrewdriver = Screwdriver("Red", 36, "Philips", True, False)
philipsScrewdriver.rotates()
philipsScrewdriver.testsElectricity()