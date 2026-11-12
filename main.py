def is_mausig(mausig):
    if mausig == "Ja" or mausig == "ja":
        return True
    else:
        return False

def greet_user(is_mausig, name):
    if is_mausig == True:
        print(f"Hiii {name}iiiii, schöni, dass du hieri bisti (ᵔᴥᵔ)")
    else:
        print(f"Schade {name}, ich hoffe du fühlst dich bald mausiger (/・・)ノ")

def main():
    mausig = input("Fühlst du dich heute mausig? (Ja/Nein)")
    name = input("Wie ist dein Name?")
    mausigkeit = is_mausig(mausig)
    greet_user(mausigkeit, name)
if __name__ == "__main__":
    main()
