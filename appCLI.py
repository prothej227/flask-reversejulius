from bruteforce import SolnSpace, Bruteforce, WordHopping
import sys

boolActive = True
print("ReverseJulius v1.2: Please copy and paste your ciphertext here.\n"
        "To end recording Press CTRL+d on Linux/Mac on CTRL+z on Windows then hit Enter.\n"
        "-------------------------------------------------------------------------------".upper())
def main():
    lines = []
    try:
        while True:
            lines.append(input())
    except EOFError:
        pass
    strMsg = "\n".join(lines)
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
        print("\nReference Word/Method: " + str(Bruteforce(SolnSpace(strMsg), lang)[1]).upper())
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