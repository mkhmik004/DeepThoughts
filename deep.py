#MKHABELE MMM
#28/06/2023
def main():
    answer=input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
    if answer.lower()=="forty-two" or answer.lower()=="forty two":
        print("Yes")
    elif answer.strip()=="42":
        print("Yes")
    else :
        print("No")
main()