def calc_MashVol (massofgrain, massunit, volumeunits):
    mashvolume = 0
    if massunit == 'lb':
        mashvolume = (0.34 * massofgrain) + 0.9
    if volumeunits == 'qt':
            mashvolume *= 4
    if volumeunits == 'l' and massunit == 'kg':
        mashvolume = (2.7 * massofgrain) + 3.5
    return mashvolume

if __name__ == '__main__':
    print calc_MashVol(7,'lb','gal')
    print calc_MashVol(7,'lb','qt')