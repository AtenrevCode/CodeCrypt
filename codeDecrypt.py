import sys
import base64
from codeUtilities import *

usage = "Uso: {0} {1}".format(sys.argv[0], '[archivo]')

class codeDecrypt(object):
    
    def __init__(self, data, key):
        self.data = data
        self.key = key
        self.encryptedByteArray = []
        self.byteArray = bytearray()
    
    def readFile(self):
        file = open(self.data,"rb")
        arrayBlock = []
        # Read file in blocks of 32 bytes
        for l in file:
            # Decode file
            decodedLine = list(base64.b64decode(l))
            for b in decodedLine:
                if len(arrayBlock) < 32:
                    arrayBlock += [b]
                else:
                    self.encryptedByteArray.append(arrayBlock)
                    arrayBlock = [b]
            self.encryptedByteArray.append(arrayBlock)
        file.close()
    # Decrypt each block of 32 bytes
    def decryptFile(self):
        for i in self.encryptedByteArray:
            self.byteArray += ( codeUtilities.operate(i, self.key) )
    # Write the result
    def writeFile(self):
        file = open("{0}.{1}".format("result","decrypt"),"wb")
        file.write(self.byteArray)
        file.close()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        print ()
        print ("\t---- Welcome to CodeCrypt 1.0 ----")
        e = codeDecrypt(sys.argv[1], codeUtilities.generateKey(sys.argv[2]))
        print ()
        print ("Reading file...")
        e.readFile()
        print ()
        print ("Proceeding to decrypt...")
        e.decryptFile()
        print ("Done")
        print ()
        print ("Writing file...")
        e.writeFile()
        print ("Success")
    else:
        print (usage)
