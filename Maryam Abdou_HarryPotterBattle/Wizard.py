class Wizard:
    health = 100
    energy = 500
    CommonSpell = {}

    # open the spells file and put each spell in its dictionary
    def readingText(self, CommonSpell, spells_Harry, spells_Voldemort):
        with open("spells.txt") as f:
            for line in f:
                (kind, spell, power) = line.split()
                if kind == 'A':
                    CommonSpell[spell] = int(power)
                elif kind == 'H':
                    spells_Harry[spell] = int(power)
                elif kind == 'V':
                    spells_Voldemort[spell] = int(power)

        # concatenate the common spells to the wizards spells
        spells_Harry.update(CommonSpell)
        spells_Voldemort.update(CommonSpell)

    # take input of spells from each wizard and return the power of the spells
    def input(self, spells_Harry, spells_Voldemort):
        HarrySpell, VoldemortSpell = input().split()
        power_HarrySpell = spells_Harry.get(HarrySpell, "Not Spell")
        power_VoldemortSpell = spells_Voldemort.get(VoldemortSpell, "Not Spell")
        return power_HarrySpell, power_VoldemortSpell





