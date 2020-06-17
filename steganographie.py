from PIL import Image
import binascii


def toString(binaryString):
    """ Convertit une chaine binaire en chaine de caractére"""
    return "".join([chr(int(binaryString[i:i + 8], 2)) for i in range(0, len(binaryString), 8)])

def bin(n):
    """Convertit un nombre en binaire"""
    q = -1
    res = ''
    while q != 0:
        q = n // 2
        r = n % 2
        res = repr(r) + res
        n = q
    if(len(res) == 6):
        res = res + repr(0)
    return res

def conversion_str_to_bin(var):
    """Convertit un ascii en binaire"""
    var_long = len(var)
    var_bin = []

    for i in range(0, var_long):
        var_ascii = ord(var[i])
        var_bin.append(bin(var_ascii))

    str_bin = "".join(var_bin)
    return str_bin

def conversion_str_to_bin_space(var):
    """Convertit un ascii en binaire"""
    var_long = len(var)
    var_bin = []

    for i in range(0, var_long):
        var_ascii = ord(var[i])
        var_bin.append(bin(var_ascii))

    str_bin = " ".join(var_bin)
    return str_bin

def encode_message(mot_encoder,redList):
    """ Encodage du texte sur les pixel rouge
        règle : - lorsque le nombre est pair et que le binaire du mot encoder est impair alors on rajoute un
                - lorsque le nombre est impair et que le binaire du mot est pair alors on rajoute un
                - Sinon on ne change rien"""
    for i in range(0, len(mot_encoder)):
        if(redList[i]%2 == 0 and int(mot_encoder[i])%2 != 0):

            redList[i] = redList[i] + 1


        if(redList[i]%2 != 0 and int(mot_encoder[i])%2 == 0):

            redList[i] = redList[i] + 1

    return(redList)



def decode_message(mot_encoder, redList_copy, redList):
    """Decode le message encoder précedement"""
    mot_decoder = []
    for i in range(0, len(mot_encoder)):
        if (redList_copy[i] % 2 == 0 and redList_copy[i] != redList[i]):
            mot_decoder.append("1")

        if (redList_copy[i] % 2 == 0 and redList_copy[i] == redList[i]):
            mot_decoder.append("0")

        if (redList_copy[i] % 2 != 0 and redList_copy[i] == redList[i]):
            mot_decoder.append("1")

        if (redList_copy[i] % 2 != 0 and redList_copy[i] != redList[i]):
            mot_decoder.append("0")

    msg_bin = "".join(mot_decoder)
    return msg_bin

def espacement_binaire(chaine_binaire):
    """Rajoute des espaces entre chaque caractére binaire"""
    l = 0
    m = 0
    message = []
    chaine = ""
    for i in range(0, int(len(chaine_binaire)/7)):
        for k in range(l,len(chaine_binaire)):
            chaine = chaine + chaine_binaire[k]
            m = m + 1
            if(m > 6):
                m = 0
                l = l + 7
                message.append(chaine)
                chaine = ""
                break
    message = " ".join(message)

    return message

def remplacement_arobase(message):
    """Remplace les @ dans le message par des espaces"""
    message_space = []
    p = 0
    chaine = ""
    for i in range(0, message.count("@")):
        for k in range(p, len(message)):

            if (message[k] != "@"):
                chaine = chaine + message[k]
            else:
                p = k + 1
                message_space.append(chaine)
                chaine = ""
                break
    message_space = " ".join(message_space)
    return message_space

if __name__ == "__main__":

    """ On ouvre l'image , on récupere sa taille et on sépare les couleurs en liste"""
    im = Image.open("python_img.png")
    width, height = im.size
    r, g, b, a = im.split()
    redList = list(r.getdata())

    """On déclare notre phrase que l'on veut encoder dans l'image"""
    mot ="Lacoste TN ou quoi frere"

    """Conversion de notre message en binaire"""
    mot_encoder = conversion_str_to_bin(mot)

    """On encode notre message dans l'image en utilisant notre règle d'encodage et 
    on récupere dans redList_copy notre nouvelle liste rouge qui contient notre message"""
    redList_copy = encode_message(mot_encoder,redList[:])

    """On decode le message de la liste de couleur rouge et 
    on recupere dans message_decode la conversion binaire du message"""
    message_decode = decode_message(mot_encoder,redList,redList_copy)

    """On rajoute des espaces entre chaque caratères binaire pour pouvoir ensuite les convertir"""
    message = espacement_binaire(message_decode)
    """On convertit le binaire en chaine de caractère lisible par tous"""
    message = toString(message)

    """On rajoute un @ a la fin du message pour delimiter la fin du message"""
    message = message + "@"

    """On remplace les @ par des espaces puis on affiche le message caché dans l'image"""
    message_space = remplacement_arobase(message)
    print(message_space)