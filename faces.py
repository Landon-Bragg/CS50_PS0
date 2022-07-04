def main():
    face = input("How are you feeling today? ")
    result = convert(face)
    print(result)

def convert(face):
    happyface = face.replace("happy",'🙂')
    sadface = happyface.replace(":(",'🙁')
    return sadface

main()