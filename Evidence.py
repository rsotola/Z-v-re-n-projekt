class Pojisteny:
    
    def __init__(self, jmeno, prijmeni, vek, telefon):
        self.__jmeno = jmeno
        self.__prijmeni = prijmeni
        self.__vek = vek
        self.__telefon = telefon
    
    def __str__(self):
        return str("{0}\t{1}\t{2}\t{3}\n".format(self.__jmeno,
                                               self.__prijmeni,
                                               self.__vek,
                                               self.__telefon))
        
class Evidence:

    def __vycisti_obrazovku(self):
        import sys as _sys
        import subprocess as _subprocess
        if _sys.platform.startswith("win"):
            _subprocess.call(["cmd.exe", "/C", "cls"])
        else:
            _subprocess.call(["clear"])
    
    def vypis_zpravu(self, zprava):
        print(zprava)
    
    def pridej_pojisteneho(self):
        self.__vycisti_obrazovku()
        print("Zadej jméno pojištěného:")
        jmeno = input()
        
        print("Zadej příjmení pojištěného:")
        prijmeni = input()
        
        while True:
            try:
                print("Zadej věk pojištěného:")        
                vek = int(input())
                break
            except:
                print("Nezadal jsi číslo!")    
        
        while True:
            try:
                print("Zadej telefonní číslo pojištěného:")
                telefon = int(input())
                if len(telefon) > 9:
                    return False
                break
            except:
                print("Neplatné zadání!")        
                
        novy_zaznam = str(Pojisteny(jmeno, prijmeni, vek, telefon))
        
        try:
            zapis = open("databaze.poj", "a")
        except:
            zapis = open("databaze.poj", "x")
        finally:
            zapis.write(novy_zaznam)   
            zapis.close()

        self.__zprava = "Záznam byl uložen do databáze.\n"
        self.vypis_zpravu(self.__zprava)
        
        input("Pokračujte libovolnou klávesou...\n\n")
        evidence.__vycisti_obrazovku()
            
    def vypis_vsechny(self):
        self.__vycisti_obrazovku()
        try:
            databaze = open("databaze.poj", "r")
            print(databaze.read())
        except:
            print("Nelze číst databázi!")
        finally:
            databaze.close()
        input("Pokračujte libovolnou klávesou...\n\n")
        evidence.__vycisti_obrazovku()
    
    def vyhledej_pojisteneho(self):
        self.__vycisti_obrazovku()
        print("Zadej jméno pojištěného:")
        jmeno = input()
        
        print("Zadej příjmení pojištěného:")
        prijmeni = input()        

        klic = jmeno + "\t" + prijmeni
        
        try:
            databaze = open("databaze.poj", "r")
            databaze_txt = databaze.read()        
        except:
            print("Nelze číst databázi!")
        finally:            
            if databaze_txt.find(klic) != -1:
                databaze = open("databaze.poj", "r")
                for i in databaze:
                    if i.startswith(klic):
                        print("\n" + i)
                    else:
                        pass
            else:
                print("\nPojištěný {0} {1} není v databázi.\n".format(jmeno, prijmeni))
            
        databaze.close()
        input("Pokračujte libovolnou klávesou...\n\n")
        evidence.__vycisti_obrazovku()
    
  

evidence = Evidence()

pokracovat = True

while (pokracovat == True):
    print("----------------------\nEVIDENCE POJIŠTĚNÝCH\n----------------------\n")
    print("Vyber si akci:")
    print("1 - Přidat nového pojištěného")
    print("2 - Vypsat všechny pojištěné")
    print("3 - Vyhledat pojištěného")
    print("4 - Konec")
    akce = int(input())
            
    if akce == 1:
        evidence.pridej_pojisteneho()
    elif akce == 2:
        evidence.vypis_vsechny()
    elif akce == 3:
        evidence.vyhledej_pojisteneho()
    elif akce == 4:
        pokracovat = False
    else:
        print("\nZadal jsi neplatné zadání.")
print("\nDěkuji za použití evidence.")
