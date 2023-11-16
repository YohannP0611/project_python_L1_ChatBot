def toLowerCAses(text):
    for elt in text:
        if ord(elt)>=ord('A') and ord(elt)<ord('a'):
            elt =chr(ord(elt)+26)
        elif ord(elt)>ord(' ') and ord(elt)<ord('A'):
            elt= ' '
    pass
def delete_punctation(text):
    pass

def addTocleanedspeeches(text):
    pass

