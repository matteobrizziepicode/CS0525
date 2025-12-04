def perimetro_quadrato(lato):
    return 4 * lato

def area_cerchio(raggio):
    return 3.14 * (raggio ** 2)

def perimetro_rettangolo(base, altezza):
    return 2 * (base + altezza)


# --- MENU PRINCIPALE ---
while True:
    print("\n--- MENU GEOMETRIA ---")
    print("1 - Perimetro del quadrato")
    print("2 - Area del cerchio")
    print("3 - Perimetro del rettangolo")
    print("4 - Esci")

    scelta = input("Scegli un'opzione: ")

    # 1) QUADRATO
    if scelta == "1":
        print("\nHai scelto: Perimetro del quadrato")
        lato = float(input("Inserisci il lato del quadrato: "))
        risultato = perimetro_quadrato(lato)
        print(f"Risultato: il perimetro del quadrato è {risultato}")

    # 2) CERCHIO
    elif scelta == "2":
        print("\nHai scelto: Area del cerchio")
        r = float(input("Inserisci il raggio del cerchio: "))
        risultato = area_cerchio(r)
        print(f"Risultato: l'area del cerchio è {risultato}")

    # 3) RETTANGOLO
    elif scelta == "3":
        print("\nHai scelto: Perimetro del rettangolo")
        b = float(input("Inserisci la base del rettangolo: "))
        h = float(input("Inserisci l'altezza del rettangolo: "))
        risultato = perimetro_rettangolo(b, h)
        print(f"Risultato: il perimetro del rettangolo è {risultato}")

    # 4) USCITA
    elif scelta == "4":
        print("\nUscita dal programma...")
        break

    else:
        print("\nScelta non valida. Riprova.")
