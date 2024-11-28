def rekenmachine():
    print("Kies een bewerking:")
    print("1. Optellen")
    print("2. Aftrekken")
    print("3. Vermenigvuldigen")
    print("4. Delen")

    keuze = input("Voer je keuze in (1/2/3/4): ")

    if keuze in ['1', '2', '3', '4']:
        getal1 = float(input("Voer het eerste getal in: "))
        getal2 = float(input("Voer het tweede getal in: "))

        if keuze == '1':
            resultaat = getal1 + getal2
            print(f"Resultaat: {getal1} + {getal2} = {resultaat}")
        elif keuze == '2':
            resultaat = getal1 - getal2
            print(f"Resultaat: {getal1} - {getal2} = {resultaat}")
        elif keuze == '3':
            resultaat = getal1 * getal2
            print(f"Resultaat: {getal1} * {getal2} = {resultaat}")
        elif keuze == '4':
            if getal2 != 0:
                resultaat = getal1 / getal2
                print(f"Resultaat: {getal1} / {getal2} = {resultaat}")
            else:
                print("Fout: Delen door nul is niet toegestaan.")
    else:
        print("Ongeldige keuze.")

# Voer de rekenmachine uit
rekenmachine()