import random

def main():
    imena_moski = [
        "Franc", "Janez", "Marko", "Ivan", "Anton", "Andrej", "Jožef", "Jože", "Luka", "Peter",
        "Marjan", "Matej", "Tomaž", "Milan", "Aleš", "Branko", "Bojan", "Robert", "Rok", "Boštjan",
        "Matjaž", "Gregor", "Miha", "Stanislav", "Martin", "David", "Igor", "Jan", "Dejan", "Boris",
        "Dušan", "Nejc", "Žiga", "Jure", "Uroš", "Alojz", "Blaž", "Žan", "Mitja", "Simon",
        "Matic", "Klemen", "Darko", "Primož", "Jernej", "Anže", "Gašper", "Drago", "Aleksander", "Jaka",
        "Jakob", "Aljaž", "Miran", "Tadej", "Denis", "Roman", "Nik", "Štefan", "Vladimir", "Damjan",
        "Matija", "Borut", "Srečko", "Slavko", "Filip", "Janko", "Tilen", "Zoran", "Mirko", "Alen",
        "Miroslav", "Domen", "Vid", "Danijel", "Goran", "Mark", "Tim", "Stanko", "Mihael", "Leon",
        "Matevž", "Urban", "Sašo", "Jurij", "Andraž", "Iztok", "Marijan", "Vinko", "Dragan", "Alojzij",
        "Maks", "Viktor", "Benjamin", "Erik", "Lovro", "Zvonko", "Samo", "Gal", "Zdravko", "Rudolf"
    ]

    imena_zenske = [
        "Marija", "Ana", "Maja", "Irena", "Mojca", "Mateja", "Nina", "Nataša", "Andreja", "Barbara",
        "Jožica", "Petra", "Eva", "Anja", "Katja", "Sara", "Sonja", "Tatjana", "Jožefa", "Katarina",
        "Tanja", "Tina", "Milena", "Alenka", "Vesna", "Nika", "Martina", "Majda", "Urška", "Ivana",
        "Špela", "Tjaša", "Frančiška", "Anica", "Helena", "Dragica", "Darja", "Nada", "Terezija", "Kristina",
        "Simona", "Lara", "Danica", "Marjeta", "Olga", "Suzana", "Zdenka", "Neža", "Lidija", "Ema",
        "Sabina", "Janja", "Marta", "Antonija", "Vida", "Angela", "Ivanka", "Maša", "Silva", "Zala",
        "Veronika", "Karmen", "Darinka", "Aleksandra", "Lana", "Anita", "Ljudmila", "Klara", "Kaja", "Brigita",
        "Alojzija", "Jana", "Lucija", "Metka", "Monika", "Lea", "Stanislava", "Natalija", "Cvetka", "Nevenka",
        "Jasmina", "Štefanija", "Elizabeta", "Renata", "Marjana", "Branka", "Tamara", "Julija", "Slavica", "Saša",
        "Hana", "Manca", "Klavdija", "Ajda", "Bojana", "Bernarda", "Erika", "Teja", "Vera", "Danijela"
    ]

    priimki = [
        "Novak", "Horvat", "Kovačič", "Krajnc", "Zupančič", "Potočnik", "Kovač", "Mlakar", "Vidmar", "Kos",
        "Golob", "Turk", "Kralj", "Božič", "Korošec", "Bizjak", "Zupan", "Hribar", "Kotnik", "Rozman",
        "Kavčič", "Kastelic", "Oblak", "Hočevar", "Petek", "Kolar", "Žagar", "Košir", "Koren", "Klemenčič",
        "Zajc", "Knez", "Medved", "Petrič", "Zupanc", "Pirc", "Hrovat", "Pavlič", "Kuhar", "Lah",
        "Zorko", "Tomažič", "Uršič", "Erjavec", "Babič", "Sever", "Jerman", "Jereb", "Kovačević", "Kranjc",
        "Majcen", "Rupnik", "Pušnik", "Breznik", "Lesjak", "Perko", "Dolenc", "Močnik", "Furlan", "Pečnik",
        "Pavlin", "Vidic", "Logar", "Jenko", "Petrović", "Ribič", "Žnidaršič", "Janežič", "Tomšič", "Marolt",
        "Jelen", "Pintar", "Blatnik", "Maček", "Dolinar", "Černe", "Gregorič", "Hren", "Mihelič", "Cerar",
        "Zadravec", "Fras", "Kokalj", "Lešnik", "Bezjak", "Hodžić", "Leban", "Čeh", "Rus", "Jug",
        "Vidovič", "Kocjančič", "Jovanović", "Kobal", "Bogataj", "Kolenc", "Primožič", "Marković", "Lavrič", "Kolarič"
    ]

    ime = ""
    if random.uniform(0, 1) <= 0.5:
        ime = random.choice(imena_moski)
    else:
        ime = random.choice(imena_zenske)
    
    priimek = random.choice(priimki)

    username = ime.lower() + priimek.lower()

    email = ime.lower() + priimek.lower() + str(random.randint(1000, 9999)) + "@gmail.com"

    print(ime)
    print(priimek)
    print(username)
    print(email)

if __name__ == "__main__":
    main()