# --- LAGER-PROGRAMM (Schritt 3: Artikel anzeigen) ---

lager = []

def artikel_hinzufuegen():
    name = input("Gib den Namen des Artikels ein: ")
    menge = int(input("Gib die Menge ein: "))
    
    neuer_artikel = {"name": name, "menge": menge}
    lager.append(neuer_artikel)
    print(f"'{name}' wurde erfolgreich mit {menge} Stück hinzugefügt!\n")

def artikel_anzeigen():
    print("\n--- AKTUELLE LAGERLISTE ---")
    
    # Prüfen, ob das Lager leer ist
    if len(lager) == 0:
        print("Das Lager ist derzeit leer.")
    else:
        # Wir gehen jeden Artikel in unserer Liste einzeln durch
        for artikel in lager:
            print(f"- Artikel: {artikel['name']} | Menge: {artikel['menge']}")
    print("---------------------------\n")

def zeige_menue():
    print("\n--- LAGERVERWALTUNG ---")
    print("1. Artikel hinzufügen")
    print("2. Artikel anzeigen")
    print("3. Beenden")

if __name__ == "__main__":
    print("Das Lager-System wurde gestartet!")
    
    while True:
        zeige_menue()
        auswahl = input("Wähle eine Option (1, 2 oder 3): ")
        
        if auswahl == "1":
            artikel_hinzufuegen()
        elif auswahl == "2":
            artikel_anzeigen()
        elif auswahl == "3":
            print("Programm wird beendet. Auf Wiedersehen!")
            break
        else:
            print("Ungültige Eingabe, bitte wähle 1, 2 oder 3.") 
            