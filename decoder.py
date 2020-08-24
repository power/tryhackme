import base64

i = 0

f = open("b64.txt","r")
data = f.read()
f.close()
while 1:
        data = base64.b64decode(data)
        i = i + 1
        if "flag" in data:
                print("Encoded " + str(i) + " times")
                print("Decode: " + data)
                break
