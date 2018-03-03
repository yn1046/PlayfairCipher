def arr(str):
    return [x for x in str]

text = input("Please, enter the text to encrypt:\n").upper()
text = arr(text)
for i in range(1, len(text)):
    if text[i] == text[i-1]:
        text.insert(i, "X")

if len(text) % 2 != 0:
    text.append("X")

for i in range(len(text)):
    if text[i] == "J":
        text[i] = "I"

matrix = [
    arr("CRYPT"),
    arr("OGAHB"),
    arr("DEFIK"),
    arr("LMNQS"),
    arr("UVWXZ")
]

binary = []
k = ""
for i in text:
    k += i
    if len(k) == 2:
        binary.append(k)
        k = ""
print("Open set:", binary)

encrypt = ""
switch = 0
for i in range(len(binary)):
    for k in range(2):
        for x in range(len(matrix)):
            for y in range(len(matrix[x])):
                if matrix[x][y] == binary[i][k]:
                    if binary[i][0] in matrix[x] and binary[i][1] in matrix [x]:
                        if matrix[x][y] != matrix[x][-1]:
                            encrypt += matrix[x][y-1]
                        else:
                            encrypt += matrix[x][y-4]

                    else:
                        for a in range (len(matrix)):
                            for b in range (len(matrix[a])):
                                if matrix[a][b] == binary[i][0]:
                                    x0 = a
                                if matrix[a][b] == binary[i][1]:
                                    x1 = a

                        if switch == 0:
                            encrypt += matrix[x1][y]
                            switch = 1
                        else:
                            encrypt += matrix[x0][y]
                            switch = 0

print("Open set:", binary)
print("Encrypted message:", encrypt)


binary = []
k = ""
for i in encrypt:
    k += i
    if len(k) == 2:
        binary.append(k)
        k = ""
print("Encrypted set:", binary)

decrypt = []
switch = 0
for i in range(len(binary)):
    for k in range(2):
        for x in range(len(matrix)):
            for y in range(len(matrix[x])):
                if matrix[x][y] == binary[i][k]:
                    if binary[i][0] in matrix[x] and binary[i][1] in matrix[x]:
                        if matrix[x][y] != matrix[x][0]:
                            decrypt.append(matrix[x][y-1])
                        else:
                            decrypt.append(matrix[x][y+4])
                    else:
                        for a in range(len(matrix)):
                            for b in range(len(matrix[a])):
                                if matrix[a][b] == binary[i][0]:
                                    x0 = a
                                if matrix[a][b] == binary[i][1]:
                                    x1 = a
                        if switch == 0:
                            decrypt += matrix[x1][y]
                            switch = 1
                        else:
                            decrypt += matrix[x0][y]
                            switch = 0

for i in range(len(decrypt)-1):
    if decrypt[i] == "X":
        if decrypt[i] != decrypt[-1]:
            if decrypt[i-1] == decrypt[i+1]:
                decrypt.remove(decrypt[i])
        else:
            decrypt.remove(decrypt[i])

print("Decrypted message:", "".join(decrypt))
