# from concurrent.futures import process
from itertools import product
import subprocess

def file_to_bytes(path):
    file = open(path, 'rb')
    file2byte = file.read() # read file to bytes
    file.close()
    return file2byte

def bytes_to_file(path, bytes):
    file = open(path, 'wb')
    file.write(bytes) # write bytes to file
    file.close()

def png_sign(inputBytes):
    header = inputBytes[:8]
    return header


def bruteforce(plaintext, ciphertext):
    # read plaintext
    bin_plain = file_to_bytes(plaintext)
    sig_plain = png_sign(bin_plain)
    print("The plaintext signature is: ", sig_plain)

    #read ciphertext
    bin_cipher = file_to_bytes(ciphertext)
    sig_cipher = png_sign(bin_cipher)
    print("The ciphertext signature is: ", sig_cipher) 

    # brute force
    hashmap1 = {}
    print("Creating dictionary with DES-encryption of png header for each key 0x00 - 0xFF :")
    generate_hex = "0123456789ABCDEF"

    for i in product(generate_hex, repeat = 2):# Mathematics Cartesian Product of two sets
        # print(i)
        key = i[0] + i[1]
        process = subprocess.Popen("openssl enc -des-ecb -K 00000000000000" + key + " -in " + plaintext, stdout = subprocess.PIPE, shell = True)
        # process = subprocess.Popen("openssl enc -des-ecb -K " + key + " -in signature -out " + "enc_" + key, stdout = subprocess.PIPE, shell = True)
        (output, err) = process.communicate()
        process.wait()
        cipher = output[:8]
        hashmap1[cipher] = key
        # bytes_to_file(cipher, "enc_" + key)
        # cipher = file_to_bytes("enc_" + key)[:8]
        # hashmap1[cipher] = key
    print(hashmap1)
    
    print("\n\n\nDecrypting with all possible 1-byte keys 0x00 - 0xFF\n\n\n")

    # hashmap2 is not necessary, just for testing
    hashmap2 = {}
    for i in product(generate_hex, repeat = 2): #2-HEX, should be repeated 2 times.
        key = i[0] + i[1]
        process = subprocess.Popen("openssl enc -d -des-ecb -K 00000000000000" + key + " -in " + ciphertext, stdout = subprocess.PIPE, shell = True)
        # process = subprocess.Popen("openssl enc -d -des-ecb -K " + key + " -in signature_enc -out " + "dec_" + key, stdout = subprocess.PIPE, shell = True)
        (output, err) = process.communicate()
        process.wait()
        plain = output[:8]
        hashmap2[plain] = key
        
        if plain in hashmap1.keys():
            print("Found a match! The key1 is: " +  str(hashmap1[plain]))
            print("The key2 is " + key)
            return
    print(hashmap2)
    print("\nCannot find the matching key.\n")

# shoud modify the path

# def run_mitm():
#     process = subprocess.Popen("openssl enc -d -des-ecb -K 00000000000000" + png_file + " -in " + intermediate.des, stdout = subprocess.PIPE, shell = True)
#     process.wait()
#     process = subprocess.Popen("openssl enc -des-ecb -K 00000000000000" + hashmap2[sig_plain] + " -in " + plaintext, stdout = subprocess.PIPE, shell = True)
#     bruteforce("signature", "signature_enc")
# bruteforce("signature", "signature_enc")


#CODE TO RETRIVE THE ORIGINAL PNG FILE
# processRe = subprocess.Popen("openssl enc -d -des-ecb -K 00000000000000" + hashmap1[sig_cipher] + " -in " + ciphertext, stdout = subprocess.PIPE, shell = True)
# processRe.wait()
# processRe = subprocess.Popen("openssl enc -des-ecb -K 00000000000000" + hashmap2[sig_plain] + " -in " + plaintext, stdout = subprocess.PIPE, shell = True)