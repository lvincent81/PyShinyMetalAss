# coding=utf-8
import re
import pint

from pint import UnitRegistry
ureg = UnitRegistry()
Q__ = ureg.Quantity


def calc_mashvol(massofgrain):
    '''
    Calculates the required volume of brewing liquor for mashing a given grain bill in the Grainfather™.
    :param massofgrain: Measured mass of the grainbill in as a Quantity in pound units (see Pint package)
    :return: Volume of brewing liquor needs as a Quantity in gallon units (see Pint package)
    '''
    return Q__(((0.34 * massofgrain.magnitude) + 0.9),'gallon')

if __name__ == '__main__':


    while True:
        print("Welcome to the Grainfather™ Python Calculator:\n---------------------------------")
        gmass_raw = raw_input("What is the grain bill total? ")
        #volumeunit = raw_input("What unit of volume would you like the volume of brewing liquor returned in (quart, gallon, or liter)? ")
        if re.match(r'\d+ *([Kk][Gg]*\.*|[Kk]ilo)', str(gmass_raw)):
            print('********Entered value is in meteric, assuming kilograms and liters')
            gmass_tgt = Q__(float(filter(str.isdigit,gmass_raw)), 'kilograms')
            mashvol = calc_mashvol(gmass_tgt.to('pounds')).to('liters')

        else:
            gmass_tgt = Q__(gmass_raw, 'pounds')
            mashvol = calc_mashvol(gmass_tgt)

        print("\tTotal Mash Volume needed: " + '{:P}'.format(mashvol) + '\n\n')