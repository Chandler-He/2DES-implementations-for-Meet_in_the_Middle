# 2DES-implementations-for-Meet_in_the_Middle
This code is desing for 2-des Meet in the Middle attack. To retrive the key 1, key 2 and the original png file.

Before I start, I should know what the file is. So, I Figured out that the plaintext maybe the header hex value of the file, because the origional file is png, it must contains an fixed hex header value. And I draged the file into Cygnus Hex editor, thus found out the ciphertext.
Every png file has the same hex header value.
plaintext: 89504E470D0A1A0A
decimal: 137 80 78 71 13 10 26 10
binary: 00111000 00111001 00110101 00110000 00110100 01000101 00110100 00110111 00110000 01000100 00110000 01000001 00110001 01000001 00110000 01000001
  
ciphertext: 0486DE014605796A
decimal: 4 134 222 1 70 5 121 106
binary: 00110000 00110100 00111000 00110110 01000100 01000101 00110000 00110001 00110100 00110110 00110000 00110101 00110111 00111001 00110110 01000001
Then I created the two files only contain 8 bytes effective keys, called png_sig and enc_sig.
Then, I try to find K1 and K2, using python 2des program.
   
Step1:
On kali linux.
install pip.
#: sudo apt update
#: sudo apt install python3-pip
install pyDES
#: pip install pyDES
install docopt
#: pip install docopt
#: sudo apt-get install python-six
install openssl
#: apt-get install openssl
After installed those requirements, I switched to the main interface of the program.
Step2:
Run the program, catch the effective keys.
This code captures the first 8 bytes of a fixed png file signature, it is the same for all png files.
This code captures the encrypted file’s first 8 bytes signature, which imported from the plant.png.2des.
   
  After ran out the key1 and key2, we can simulate the meet_in_the_middle attack.
K1: AB K2: 12
Step3:
Retrieve the encrypted file.
Just using the same program with some modifications, vim into the py file.
comment the line as follows:
use the retrieve code, save and quit.
   
Run the program.
 Then we saw the plant already generated in the file folder after I ran the code.
So, the plant is: pumpkin.
Conclusion.
This project really took us a lot of time to finish. Firstly, I should know what is the plaintext and ciphertext, if that is not clear, this project cannot be processed. Secondly, create two file_sigs were not simple than I thought. The most important part is the codes. Appearently, I cannot write the codes for now, so, find a good code is the crucial point. After modified the codes a bit, I successfully finished the project. From the project, I graduately knew that how meet in the middle attack works per se, once I know the mechanism, it is easy to realize it.
References.
https://github.com/thomwiggers/des-meet-in-the-middle/blob/master/README.md https://www.rapidtables.com/convert/number/hex-to-ascii.html http://www.softcircuits.com/Products/CygnusFE https://www.youtube.com/watch?v=IZFaZDO3-GQ&feature=youtu.be https://stackoverflow.com/questions/30550346/understanding-image-its-hex-values