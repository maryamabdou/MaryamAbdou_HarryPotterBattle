from Wizard import Wizard

class Harry(Wizard):
    w = Wizard()
    spells_Harry = {}
    _healthH = w.health
    _energyH = w.energy

    # getter method to get the properties using an object
    def get_healthH(self):
        return self._healthH

    # setter method to change the value 'healthH' using an object
    def set_healthH(self, healthH):
        self._healthH = healthH

    # getter method to get the properties using an object

    def get_energyH(self):
        return self._energyH

    # setter method to change the value 'energyH' using an object
    def set_energyH(self, energyH):
        self._energyH = energyH

