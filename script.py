def aendere_mutable_variable(liste: list):
    """Ändert den Inhalt einer mutable Variablen."""
    print(f"Ursprüngliche Liste in der Funktion (mutable): {liste}")
    print(f"    Speicheradresse: {id(liste)}")
    liste.append(100)  # Mutable Variablen wie Listen werden im selben Speicherplatz verändert
    print(f"Geänderte Liste in der Funktion (mutable): {liste}")
    print(f"    Speicheradresse: {id(liste)}")

# Beispiel mit einer mutable Variable
meine_liste = [1, 2, 3]
print(f"Vor Funktionsaufruf (mutable): {meine_liste}")
print(f"    Speicheradresse: {id(meine_liste)}")
aendere_mutable_variable(meine_liste)
print(f"Nach Funktionsaufruf (mutable): {meine_liste}")
print(f"    Speicheradresse: {id(meine_liste)}")



# Wie verändere ich eine Liste ohne das Original abzurufen?
andere_liste = meine_liste
print(f"\n\nAndere Liste : {andere_liste}")
print(f"    Speicheradresse: {id(andere_liste)}")
andere_liste.remove(100)
print(f"Andere Liste : {andere_liste}")
print(f"    Speicheradresse: {id(andere_liste)}")
print(f"normale Liste: {meine_liste}")
print(f"    Speicheradresse: {id(meine_liste)}")


# -> indem ich eine Copy ziehe
meine_liste.append(100)
wieder_andere_liste = meine_liste.copy()
print(f"\n\nWieder Andere Liste : {wieder_andere_liste}")
print(f"    Speicheradresse: {id(wieder_andere_liste)}")
wieder_andere_liste.remove(100)
print(f"Wieder Andere Liste : {wieder_andere_liste}")
print(f"    Speicheradresse: {id(wieder_andere_liste)}")
print(f"normale Liste: {meine_liste}")
print(f"    Speicheradresse: {id(meine_liste)}")
