from bruteforce import SolnSpace, Bruteforce, WordHopping
boolActive = True
def main():
    strMsg = input("Input String Message:\n").rstrip()
    ch_lang = input("Choose Language: (1) en_us | (2) tl_ph: ")
    if ch_lang == "1":
        lang = "en_us"
    elif ch_lang == "2":
        lang = "tl_ph"
    else:
        lang = "en_us"
    print("-----------------------------------------------------------")
    try:
        print("Key: " + str(Bruteforce(SolnSpace(strMsg), lang)[0]))
        print("Message: " + str(SolnSpace(strMsg)[Bruteforce(SolnSpace(strMsg), lang)[0]]))
        print("Reference Word: " + str(Bruteforce(SolnSpace(strMsg), lang)[1]).upper())
    except Exception as e:
        print(e)
        print("No Solution Set :(")

main()

while boolActive == True:
    ch = input("\nInput another string? (y/n): ")
    print("-----------------------------------------------------------")
    if ch == "y" or ch == "Y":
        main()
    else:
        boolActive = False

delay = input("Press any key to exit...\n")