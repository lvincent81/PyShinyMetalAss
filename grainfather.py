# coding=utf-8
import re
import pint
def calc_mashvol(massofgrain, volumeunits):
    '''
    Calculates the required volume of brewing liquor for mashing a given grain bill in the Grainfather™.
    :param massofgrain: Measured mass of the grainbill
    :param massunit: Units of the grain mass
    :param volumeunits: Units to return the volume of brewing liquor as
    :return: Volume in units specified by volumeunits argument
    '''
    #if 'lb' in str(massofgrain):

    mashvolume = 0
    justnum = re.compile(r'[^\d+\.*\d*]')
    print(justnum.sub('',massofgrain))
    massvalue = float(justnum.sub('',massofgrain))
    for val in ('lb','#','pound','pounds','lb.','lbs','lbs.'):
            if val in str(massofgrain):
                mashvolume = (0.34 * massvalue) + 0.9
            for val in ('L','L.','Liter','liter','l','l.'):
                if val in str(volumeunits):
                    mashvolume *= 3.78541
                    print('X')
    if volumeunits in ('qt','quart','qt.'):
        mashvolume *= 4
    for val in ('Kg','kg','kg.','Kg.'):
        if val in str(massofgrain):
            mashvolume = (2.7 * massvalue) + 3.5
            if str(volumeunits) in ('gal','Gal','Gallon','gallon','gal.','Gal.'):
                mashvolume *= .264172
    return mashvolume


if __name__ == '__main__':


    while True:
        print("Welcome to the Grainfather™ Python Calculator:\n---------------------------------")
        grainmass = raw_input("What is the grain bill total? ")
        volumeunit = raw_input("What unit of volume would you like the volume of brewing liquor returned in (quart, gallon, or liter)? ")
        print("Total Mash Volume needed: " + str(calc_mashvol(grainmass,volumeunit)) + '\n\n')