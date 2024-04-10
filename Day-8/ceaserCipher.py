def cipher(msg, shift, isEncode):
    capital = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    small = capital.lower()
    ans = ""
    for i in range(len(msg)):
        if msg[i] in capital:
            ind = capital.find(msg[i])
            if(isEncode == True):
                ind += shift
            else:
                ind -= shift
            ind %= 26
            ans = ans + capital[ind]
        elif msg[i] in small:
            ind = small.find(msg[i])
            if(isEncode == True):
                ind += shift
            else:
                ind -= shift
            ind %= 26
            ans = ans + small[ind]
        else: 
            ans = ans + msg[i]
    return ans

while True:
    msg = input("Enter your message: ")
    sh = int(input("Enter shift degit: "))
    isEnc = int(input("Enter 1 to encrypt, 2 to decrypt: "))
    if isEnc == 1:
        print(f"Encrypted text: {cipher(msg, sh, True)}")
    else:
        print(f"Decrypted text: {cipher(msg, sh, False)}")
    
    ip = input("\nEnter y to continue, n to close: ").lower()
    if ip == 'n':
        break

    