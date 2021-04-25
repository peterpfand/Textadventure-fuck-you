answer = input("Haste bock auf n kleines game oder was?\n")                      #frage zum Spielanfang
if answer.lower().strip() in ["ja","klar","na sichi","jap","jup","ja klar","yes","ok"]:
    print ("\nNice...")
else:
    why = input("\nWat genau machst du dann mit dem programm?" + "\n")
    if why.lower().strip() in ["i dont know","keine ahnung","idk","weis nicht"]:
            print("\nalso hast du auch nichts besseres zu tun oder?")
            if input().lower().strip() in ["nope","nein","nö","eigentlich nicht"]:
                print("\nja dann kannst duc auch fix das Game spielen oder?")
                if input().lower().strip() in ["ja","ok","ja schon","eigentlich schon","jap","yes"]:
                    print("\nPerfekt")
                else:
                    print("\nok byeeeeeeeeee.....")
                    exit()
            else:
                print("\nja dann mach mal das wichtige zuerst und komm später wieder.....")
                exit()
    else:
        print("\nja juckt mich eigentlich eher weniger tschüss.......")
        exit()





print("""
----------------------------------SPIELANFANG----------------------------------""")
