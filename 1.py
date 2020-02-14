# http://www.pythonchallenge.com/pc/def/274877906944.html
# http://www.pythonchallenge.com/pc/def/map.html
#
# K->M
# O->Q
# E->G
#
# everybody thinks twice before solving this.
#
# g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.

message = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

alphabet            = "abcdefghijklmnopqrstuvwxyz ()."
alphabet_plus_three = "cdefghijklmnopqrstuvwxyzab ()."

# create a tuple with the value, and translation value
list = list(zip(alphabet, alphabet_plus_three))
print(list)

nmessage = ""

# Iterate over the message and get the value from the tuple
for i in range( len(message) ):
    for x in range(len(list)):
        if(message[i] == list[x][0]):
            nmessage = nmessage + list[x][1]

print("Encrypted message: " + message)
print("Decrypted message: " + nmessage)
