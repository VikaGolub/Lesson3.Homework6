'''
Codewars: Are You Playing Banjo?
'''
def areYouPlayingBanjo(name):
    if name[0].lower() == 'r':   
        return name + ' plays banjo'
    elif name[0].upper() == 'R':
        return name + ' plays banjo'
    else:
        return name + ' does not play banjo'