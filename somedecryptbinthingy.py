#joel killed me so i had to solve it as well

base2bits = {"A":"00", "C":"01", "G":"10", "T":"11"}

table = []
with open('key.txt', 'rt') as f: #read text of the key file 
    seq = f.read()
    for quartet in [seq[i:i+4] for i in range(0, len(seq), 4)]:
        table.append(quartet)

with open('encrypted.bin', 'rb') as ineedtocrackthis, open('decrypted.txt', 'wt') as output_decryptfile: #rb - read binary and then wt - write text as out
    data = ineedtocrackthis.read()
    for byte in data:
        base_quartet = table[int(byte)]
        binary = ""
        for base in  base_quartet:
            binary += base2bits[base]
        output_decryptfile.write(chr(int(binary, 2)))
        #pray to god 
