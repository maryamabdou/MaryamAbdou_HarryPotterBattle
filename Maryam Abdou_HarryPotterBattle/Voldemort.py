from Wizard import Wizard

class Voldemort(Wizard):
    w = Wizard()
    spells_Voldemort = {}
    _healthV = w.health
    _energyV = w.energy

    # getter method to get the properties using an object
    def get_healthV(self):
        return self._healthV

    # setter method to change the value 'healthV' using an object
    def set_healthV(self, healthV):
        self._healthV = healthV

    # getter method to get the properties using an object

    def get_energyV(self):
        return self._energyV

    # setter method to change the value 'energyV' using an object
    def set_energyV(self, energyV):
        self._energyV = energyV

