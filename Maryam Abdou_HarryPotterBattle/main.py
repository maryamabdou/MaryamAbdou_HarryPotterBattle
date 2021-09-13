from Harry import Harry
from Voldemort import Voldemort
from Wizard import Wizard

if __name__ == '__main__':
    i = 0
    j = 0
    w = Wizard()
    h = Harry()
    v = Voldemort()

    # open the spells file and put each spell in its dictionary
    w.readingText(w.CommonSpell, h.spells_Harry, v.spells_Voldemort)

    # stop the game when the health of one of the wizards is zero or less
    while (h.get_healthH() > 0) and (v.get_healthV() > 0):
        # take input of the two spells
        print('Enter the two spells (harry then voldemort):')
        power_HarrySpell, power_VoldemortSpell = w.input(h.spells_Harry, v.spells_Voldemort)

        # check for wrong spells
        while power_HarrySpell == 'Not Spell' or power_VoldemortSpell == 'Not Spell':
            print('Enter the two spells again')
            power_HarrySpell, power_VoldemortSpell = w.input(h.spells_Harry, v.spells_Voldemort)

        # checks for number of shields the wizards used
        if power_HarrySpell == 0:
            i += 1
            if i == 4:
                while power_HarrySpell == 0:
                    print('Harry finished his shields! Enter the two spells again')
                    power_HarrySpell, power_VoldemortSpell = w.input(h.spells_Harry, v.spells_Voldemort)

        if power_VoldemortSpell == 0:
            j += 1
            if j == 4:
                while power_VoldemortSpell == 0:
                    print('Voldemort finished his shields! Enter the two spells again')
                    power_HarrySpell, power_VoldemortSpell = w.input(h.spells_Harry, v.spells_Voldemort)

        # editing the energy of each wizard after each spell
        h.set_energyH(h.get_energyH() - power_HarrySpell)
        v.set_energyV(v.get_energyV() - power_VoldemortSpell)

        # editing the health of each wizard after each spell
        if power_VoldemortSpell > power_HarrySpell:
            if power_HarrySpell == 0:
                print()
            else:
                h.set_healthH(h.get_healthH() - abs(power_HarrySpell - power_VoldemortSpell))

        elif power_HarrySpell > power_VoldemortSpell:
            if power_VoldemortSpell == 0:
                print()
            else:
                v.set_healthV(v.get_healthV() - abs(power_HarrySpell - power_VoldemortSpell))

        # printing the result
        print('         Harry       Voldemort')
        print('Health : ' + str(h.get_healthH()) + '         ' + str(v.get_healthV()))
        print('Energy : ' + str(h.get_energyH()) + '         ' + str(v.get_energyV()))

    # printing the winner if one of the wizards has health equal to zero or less
    if h.get_healthH() <= 0:
        print('        Voldemort is the winner..')
    elif v.get_healthV() <= 0:
        print('        Harry is the winner..')
