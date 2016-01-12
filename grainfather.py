def calc_mashvol(massofgrain, massunit, volumeunits):
    '''
    Calculates the required volume of brewing liquor for mashing a given grain bill in the Grainfather™.
    :param massofgrain: Measured mass of the grainbill
    :param massunit: Units of the grain mass
    :param volumeunits: Units to return the volume of brewing liquor as
    :return: Volume in units specified by volumeunits argument
    '''

    mashvolume = 0
    if massunit == 'lb':
        mashvolume = (0.34 * massofgrain) + 0.9
    if volumeunits == 'qt':
        mashvolume *= 4
    if volumeunits == 'l' and massunit == 'kg':
        mashvolume = (2.7 * massofgrain) + 3.5
    return mashvolume


if __name__ == '__main__':
    print calc_mashvol(7, 'lb', 'gal')
    print calc_mashvol(7, 'lb', 'qt"""