from PIL import Image
import binascii


def toString(binaryString):
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
    """Convertir un ascii en binaire"""
    var_long = len(var)
    var_bin = []

    for i in range(0, var_long):
        var_ascii = ord(var[i])
        var_bin.append(bin(var_ascii))

    str_bin = "".join(var_bin)
    return str_bin

def conversion_str_to_bin_space(var):
    """Convertir un ascii en binaire"""
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




if __name__ == "__main__":
    im = Image.open("python_img.png")
    width, height = im.size
    r, g, b, a = im.split()
    redList = list(r.getdata())
    mot ="Lacoste TN"

    """Conversion de notre message en binaire"""
    mot_encoder = conversion_str_to_bin(mot)
    mot_encoder_space = conversion_str_to_bin_space(mot)
    """Initialisation de l'image et attribution des listes de pixel"""


    redList_copy = encode_message(mot_encoder,redList[:])
    test = decode_message(mot_encoder,redList,redList_copy)

    for i in range(0, len(test)):
    message = toString(bin_space)

    for i in range(0, len(message)):
        if (message[i] == "@"):
            message[i] = " "

    print(message)