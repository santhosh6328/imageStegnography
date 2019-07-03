import cv2
from LSBSteg import *
cap = cv2.VideoCapture(0)
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        cv2.imshow('RGB',frame)
        if(cv2.waitKey(50) == ord('q')):
            print("Enter a info to hide: ")
            info = str(raw_input())
            ret,img = cap.read()
            cv2.imwrite('img.png',img)
            while(True):
                print("1.Encode\n2.Decode\nEnter Your Choice: ")
                choice = int(input())
                if(choice == 1):
                    steg = LSBSteg(cv2.imread('img.png'))
                    img_encoded = steg.encode_text(info)
                    cv2.imwrite("Hidden.png", img_encoded)
                elif (choice == 2):
                    # decoding
                    im = cv2.imread("Hidden.png")
                    steg = LSBSteg(im)
                    print("Text value:", steg.decode_text())
                    break
    else:
        break
cap.release()
cv2.destroyAllWindows()

def encode_text(self, txt):
    l = len(txt)
    binl = self.binary_value(l, 16)
    self.put_binary_value(binl)
    for char in txt: # And put all the chars
        c = ord(char)
        self.put_binary_value(self.byteValue(c))
    return self.image
def decode_text(self):
    ls = self.read_bits(16) # Read the text size in bytes
    l = int(ls, 2)
    i = 0
    unhideTxt = ""
    while i < l: # Read all bytes of the text
        tmp = self.read_byte() # So one byte
        i += 1
        unhideTxt += chr(int(tmp, 2))
    return unhideTxt
   
def binary_value(self, val, bitsize):
    binval = bin(val)[2:]
    if len(binval) > bitsize:
        raise SteganographyException("binary value larger than the expected size")
    while len(binval) < bitsize:
        binval = "0" + binval
    return binval
   
def put_binary_value(self, bits):
    for c in bits:
        val = list(self.image[self.curheight, self.curwidth])
    if int(c) == 1:
        val[self.curchan] = int(val[self.curchan]) | self.maskONE
    else:
        val[self.curchan] = int(val[self.curchan]) & self.maskZERO # AND with maskZERO
    self.image[self.curheight, self.curwidth] = tuple(val)
    self.next_slot() # Move "cursor" to the next space
