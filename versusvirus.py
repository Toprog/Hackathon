import tkinter as tk
import random


root = tk.Tk()
root.title("Kid's daily planer")

canvas = tk.Canvas(root, height=450, width=800, bg='white')
canvas.pack()

#background_image = tk.PhotoImage(file='landscape.png')
#background_label = tk.Label(root, image=background_image)
#background_label.place(relwidth=1, relheight=1)


####################################Frame 1##############################################

frame1  = tk.Frame(root, bg='white')
frame1.place(relx=0.025, rely=0.025, relwidth=0.95, relheight=0.26)

label0 = tk.Label(frame1, text="Allgemeines", bg='white', fg='blue')
label1 = tk.Label(frame1, text="Alter", bg='white')
label2 = tk.Label(frame1, text="Anzahl Geschwister", bg='white')
label3 = tk.Label(frame1, text="Beschäftigungsgrad der Eltern", bg='white')
label4 = tk.Label(frame1, text="Mutter", bg='white')
label5 = tk.Label(frame1, text="Vater", bg='white')
label9 = tk.Label(frame1, text="Anzahl Stunden Schule", bg='white')
label0.place(relx=0.5, rely=0, relwidth=0.1, relheight=0.2, anchor='n')
label1.place( rely=0.2, relwidth=0.14)
label2.place(relx=0.2, rely=0.2, relwidth=0.15)
label3.place(relx=0.775, rely=0, relwidth=0.21, relheight=0.2, anchor='n')
label4.place(relx=0.64, rely=0.25, relwidth=0.06)
label5.place(relx=0.64, rely=0.6, relwidth=0.06)
label9.place(relx=0.5, rely=0.6, relheight=0.2, anchor='center')

spinbox1 = tk.Spinbox(frame1, from_=0, to=100, increment='10')
spinbox2 = tk.Spinbox(frame1, from_=0, to=100, increment='10')
spinbox4 = tk.Spinbox(frame1, from_=0, to=6)
spinbox1.place(relx=0.72, rely=0.25, relwidth=0.1)
spinbox2.place(relx=0.72, rely=0.6, relwidth=0.1)
spinbox4.place(relx=0.5, rely=0.75, relwidth=0.1, anchor='center')

#entry1 = tk.Entry(frame1, bg='white')
#entry2 = tk.Entry(frame1, bg='white')
#entry1.place(relx=0.025, rely=0.6, relwidth=0.2)
#entry2.place(relx=0.24, rely=0.6, relwidth=0.2)
spinbox8 = tk.Spinbox(frame1, from_=6, to=15)
spinbox9 = tk.Spinbox(frame1, from_=0, to=5)
spinbox8.place(relx=0.025, rely=0.4, relwidth=0.1)
spinbox9.place(relx=0.225, rely=0.4, relwidth=0.1)

#scrollbarAge =tk.Scrollbar(frame1)
#scrollbarAge.place(relx=0.1, rely=0.4, relheight=0.5)
#agelist = tk.Listbox(frame1, yscrollcommand = scrollbarAge.set)
#for line in range(6,16):
    #agelist.insert('end', str(line))
#agelist.place(relx=0.025, rely=0.4, relwidth=0.075,relheight=0.5)
#scrollbarAge.config(command = agelist.yview)

#scrollbarSiblings =tk.Scrollbar(frame1)
#scrollbarSiblings.place(relx=0.3, rely=0.4, relheight=0.5)
#siblingslist = tk.Listbox(frame1, yscrollcommand = scrollbarSiblings.set)
#for line in range(0, 5):
    #siblingslist.insert('end', str(line))
#siblingslist.insert('end', ">4")
#siblingslist.place(relx=0.225, rely=0.4, relwidth=0.075,relheight=0.5)
#scrollbarSiblings.config(command = siblingslist.yview)


CheckVar1 = tk.IntVar()
CheckVar2 = tk.IntVar()
CheckVar17 = tk.IntVar()
C1 = tk.Checkbutton(frame1, text = "Homeoffice", variable = CheckVar1, onvalue = 1, offvalue = 0, bg='white')
C2 = tk.Checkbutton(frame1, text = "Homeoffice", variable = CheckVar2, onvalue = 1, offvalue = 0, bg='white')
C17 = tk.Checkbutton(frame1, text = "Haustier", variable = CheckVar17, onvalue = 1, offvalue = 0, bg='white')
C1.place(relx=0.85, rely=0.25, relwidth=0.12, relheight=0.2)
C2.place(relx=0.85, rely=0.6, relwidth=0.12, relheight=0.2)
C17.place(relx=0.5, rely=0.35, relwidth=0.12, relheight=0.2, anchor='center')
C1.deselect()

####################################Frame 2##############################################

frame2 = tk.Frame(root, bg='white')
frame2.place(relx=0.025, rely=0.31, relwidth=0.95, relheight=0.26)

label6 = tk.Label(frame2, text="Hobbies", bg='white', fg='red')
label7 = tk.Label(frame2, text="Sportlich", bg='white')
label6.place(relx=0.5, rely=0, relwidth=0.1, relheight=0.2, anchor='n')
label7.place(relx=0.85, rely=0.3)

CheckVar3 = tk.IntVar()
CheckVar4 = tk.IntVar()
CheckVar5 = tk.IntVar()
CheckVar6 = tk.IntVar()
C3 = tk.Checkbutton(frame2, text = "Sport", variable = CheckVar3, onvalue = 1, offvalue = 0, bg='white')
C4 = tk.Checkbutton(frame2, text = "Musik", variable = CheckVar4, onvalue = 1, offvalue = 0, bg='white')
C5 = tk.Checkbutton(frame2, text = "Zuhause durchführbar", variable = CheckVar5, onvalue = 1, offvalue = 0, bg='white')
C6 = tk.Checkbutton(frame2, text = "Zuhause durchführbar", variable = CheckVar6, onvalue = 1, offvalue = 0, bg='white')
C3.place(relx=0.06, rely=0.2, relwidth=0.12, relheight=0.2)
C4.place(relx=0.06, rely=0.6, relwidth=0.12, relheight=0.2)
C5.place(relx=0.56, rely=0.2)
C6.place(relx=0.56, rely=0.6)

entry3 = tk.Entry(frame2, bg='white')
entry4 = tk.Entry(frame2, bg='white')
entry3.place(relx=0.24, rely=0.2, relwidth=0.2, relheight=0.2)
entry4.place(relx=0.24, rely=0.6, relwidth=0.2, relheight=0.2)

spinbox3 = tk.Spinbox(frame2, from_=1, to=10)
spinbox3.place(relx=0.8, rely=0.56)

####################################Frame 3##############################################

frame3 = tk.Frame(root, bg='white')
frame3.place(relx=0.025, rely=0.595, relwidth=0.95, relheight=0.285)

label8 = tk.Label(frame3, text="Interessen", bg='white', fg='green')
label8.place(relx=0.5, rely=0, relwidth=0.1, relheight=0.2, anchor='n')

CheckVar7 = tk.IntVar()
CheckVar8 = tk.IntVar()
CheckVar9 = tk.IntVar()
CheckVar10 = tk.IntVar()
CheckVar11 = tk.IntVar()
CheckVar12 = tk.IntVar()
CheckVar13 = tk.IntVar()
CheckVar14 = tk.IntVar()
CheckVar15 = tk.IntVar()
CheckVar16 = tk.IntVar()
C7 = tk.Checkbutton(frame3, text = "Kreativität", variable = CheckVar7, onvalue = 1, offvalue = 0, bg='white')
C8 = tk.Checkbutton(frame3, text = "Kochen/Backen", variable = CheckVar8, onvalue = 1, offvalue = 0, bg='white')
C9 = tk.Checkbutton(frame3, text = "Spielen", variable = CheckVar9, onvalue = 1, offvalue = 0, bg='white')
C10 = tk.Checkbutton(frame3, text = "Natur", variable = CheckVar10, onvalue = 1, offvalue = 0, bg='white')
C11 = tk.Checkbutton(frame3, text = "Gesellschaftspiele", variable = CheckVar11, onvalue = 1, offvalue = 0, bg='white')
C12 = tk.Checkbutton(frame3, text = "Naturwissenschaften", variable = CheckVar12, onvalue = 1, offvalue = 0, bg='white')
C13 = tk.Checkbutton(frame3, text = "Lesen", variable = CheckVar13, onvalue = 1, offvalue = 0, bg='white')
C14 = tk.Checkbutton(frame3, text = "Technik", variable = CheckVar14, onvalue = 1, offvalue = 0, bg='white')
C15 = tk.Checkbutton(frame3, text = "Sport", variable = CheckVar15, onvalue = 1, offvalue = 0, bg='white')
C16 = tk.Checkbutton(frame3, text = "Basteln/Zeichnen", variable = CheckVar16, onvalue = 1, offvalue = 0, bg='white')
C7.place(relx=0.025, rely=0.22, relwidth=0.15)
C8.place(relx=0.025, rely=0.62, relwidth=0.15)
C9.place(relx=0.2, rely=0.22, relwidth=0.15)
C10.place(relx=0.2, rely=0.62, relwidth=0.15)
C11.place(relx=0.4, rely=0.22, relwidth=0.2)
C12.place(relx=0.4, rely=0.62, relwidth=0.2)
C13.place(relx=0.8, rely=0.22, relwidth=0.15, anchor='ne')
C14.place(relx=0.8, rely=0.62, relwidth=0.15, anchor='ne')
C15.place(relx=0.975, rely=0.22, relwidth=0.15, anchor='ne')
C16.place(relx=0.975, rely=0.62, relwidth=0.15, anchor='ne')

####################################Functions##############################################
    
def run():
    Young: bool = int(spinbox8.get())  < 11
    School: int = int(spinbox4.get())
    Alone: bool = int(spinbox1.get() + spinbox2.get()) > 150
    Sport1: bool = int(CheckVar5.get()) == 1
    Musik: bool = int(CheckVar6.get()) == 1

    Kreativität: bool = int(CheckVar7.get()) == 1
    KochenBacken: bool = int(CheckVar8.get()) == 1
    Spielen: bool = int(CheckVar9.get()) == 1
    Natur: bool = int(CheckVar10.get()) == 1
    Gesellschaftsspiele: bool = int(CheckVar11.get()) == 1
    Naturwissenschaften: bool = int(CheckVar12.get()) == 1
    Lesen: bool = int(CheckVar13.get()) == 1
    Technik: bool = int(CheckVar14.get()) == 1
    Sport2: bool = int(CheckVar15.get()) == 1
    BastelnZeichnen: bool = int(CheckVar16.get()) == 1

    counter: float = 8
    Day1: list = []
    Day2: list = []
    Day3: list = []
    Day4: list = []
    Day5: list = []
    
    for i in range(School):
        Day1.append("School")
        Day2.append("School")
        Day3.append("School")
        Day4.append("School")
        Day5.append("School")
        counter -= 1
        
    counter -= 0.5 #für Ämtli
    
    #counter -= 1 #Bildschrmzeit
    Day1.append("Ämtli")
    Day2.append("Ämtli")
    Day3.append("Ämtli")
    Day4.append("Ämtli")
    Day5.append("Ämtli")
    #Day1.append("Bildschirmzeit")
    #Day2.append("Bildschirmzeit")
    #Day3.append("Bildschirmzeit")
    #Day4.append("Bildschirmzeit")
    #Day5.append("Bildschirmzeit")
    
    sport: bool = False
    if Sport1:
        counter -= 1
        Day1.append("SportHobby")
        Day2.append("SportHobby")
        Day3.append("SportHobby")
        Day4.append("SportHobby")
        Day5.append("SportHobby")
        sport=True
        
    if Musik:
        counter -= 0.5
        Day1.append("Musik")
        Day2.append("Musik")
        Day3.append("Musik")
        Day4.append("Musik")
        Day5.append("Musik")
    if not sport:
        counter -= 1
        Day1.append("Sport")
        Day2.append("Sport")
        Day3.append("Sport")
        Day4.append("Sport")      
        Day5.append("Sport")
    if Young:
        counter -= 0.5
        Day1.append("SportYoung")
        Day2.append("SportYoung")
        Day3.append("SportYoung")
        Day4.append("SportYoung")      
        Day5.append("SportYoung")
    if counter > 0:
        Interests: list = []
        if Kreativität:
            Interests.append("Kreativität")
        if Sport2:
            Interests.append("Sport")
        if KochenBacken:
            Interests.append("KochenBacken")
        if Spielen:
            Interests.append("Spielen")
        if Natur:
            Interests.append("Natur")
        if Gesellschaftsspiele:
            Interests.append("Gesellschaftsspiele")
        if Technik:
            Interests.append("Technik")
        if Lesen:
            Interests.append("Lesen")
        if Naturwissenschaften:
            Interests.append("Naturwissenschaften")
        if BastelnZeichnen:
            Interests.append("BastelnZeichnen")
        if len(Interests) == 0:
            print("Error: Mindesten ein Interesse angeben")
        elif len(Interests) == 1:
            for i in range(int((8-counter)*2)):
                Day1.append(Interests)
                Day2.append(Interests)
                Day3.append(Interests)
                Day4.append(Interests)
                Day5.append(Interests)
        else:
            a = random.randint(0, len(Interests)-1)
            b = random.randint(0, len(Interests)-1)
            c = random.randint(0, len(Interests)-1)
            d = random.randint(0, len(Interests)-1)
            e = random.randint(0, len(Interests)-1)
            for i in range(int((counter*2))):
                Day1.append(Interests[a])
                Day2.append(Interests[b])
                Day3.append(Interests[c])
                Day4.append(Interests[d])
                Day5.append(Interests[e])
                
            if counter >= 2:
                f = random.randint(0, len(Interests)-1)
                g = random.randint(0, len(Interests)-1)
                h = random.randint(0, len(Interests)-1)
                i = random.randint(0, len(Interests)-1)
                j = random.randint(0, len(Interests)-1)
                for z in range (int((counter-2)*2)):
                    Day1[len(Day1)-1-z] = Interests[f]
                    Day2[len(Day2)-1-z] = Interests[g]
                    Day3[len(Day3)-1-z] = Interests[h]
                    Day4[len(Day4)-1-z] = Interests[i]
                    Day5[len(Day5)-1-z] = Interests[j]
                    



    f= open('output.txt', 'w+')                

        

    Amtliyoung: list = ["Tisch decken", "Kochen helfen", "Wäsche aufhängen", "Pflanzen giessen", "Briefkasten leeren",
                "Bett machen", "Aufräumen"]
    Amtliold: list = Amtliyoung
    Amtliold.append("Geschirrspühler aus-/einräumen")
    Amtliold.append("Staubsaugen/Abstauben")
    Amtliold.append("Abfall entsorgen")
    Amtliold.append("Rasenmähen")
    Amtliold.append("Einkaufen")



    KreativitätYU: list = ["Fotografieren", "Verkleiden und Fotoshooting", "Lied schreiben", "Lieblingsbuck als Theaterstück umseten", "Eigene Geschichte schreiben/ Zeichnen", "Brief an Freunde oder Grosseltern schreiben", "Kalligraphie lernen", "Gedicht schreiben", "Neue Frisuren ausprobieren", "Zaubershow einstudieren und am Abend vorführen", "Zirkusshow einstudieren und am Abend vorführen", "Videos filmen", "Geheimsprache erfinden"]
    KochenBackenYB: list = ["Toast Hawaii zubereiten", "Würstchen im Teig zubereiten", "Pizza zubereiten", "Karotten- oder Grukensalat machen", "Sandwich machen", "Apfelmuss machen", "Obstspiesse zubereiten", "Drink mixen", "Schlangenbrot machen", "Fruchtsalat machen", "Flammkuchen machen", "Nudelgerichte zubereiten", "Rösti machen", "Muffins backen", "Kuchen backen", "Zopf/Brot backen", "Kekse backen"]
    SportYU: list = ["Federball spielen", "Fussball spielen", "Basketball spielen", "Seilspringen", "Fangen", "Hüpfspiele mit Kreide", "Bodenturnen auf dem Rasen(z.B.: Rad, Kopfstand lernen)", "Jonglieren lernen", "Youtube Video: Krafttraining Kinder suchen & ausführen", "Yoga machen", "Trampolin springen", "Sackhüpfen", "Tanzen", "Ping-pong", "Frisbee", "STV fit at home workout aussuchen & machen"]
    SpielenYU: list = ["Versteck aus Kissen und Tücher bauen", "Seifenblasen machen", "Mit Puppen spielen", "Playmobil/Lego spielen", "Murmelbahn aus Klopapierrollen bauen", "Drachen steigen lassen", "Fingerfussballturnier machen", "Hindernisparkour in Wohnung aufbauen", "Gumitwist hüfen", "Bowling mit Wasserflaschen", "Verstecken spielen", "Seilspringen", "Detektiv spielen", "Wasserschlacht machen(Draussen!)", "Suchspiele spielen", "Rennbahn bauen", "Büchsen werfen(mit WC Papierrollen)", "Zaubertricks lernen(mit Youtube)", "Show zum vorzeigen einstudieren", "Rubiks cube lösen", "Domino spielen"]
    GesellschaftsspieleYU: list = ["Puzzle machen", "Mensch ärgere dich nicht spielen", "Memory spielen", "Puzzle zusammensetzen", "Jenga spielen", "Leiterli-Spiel spielen", "Skip-Bo spielen", "Schach spielen", "Monopoly spielen", "Lotti karotti spielen", "Domino spielen", "Uno spielen", "Mühle spielen", "4 gewinnt spielen", "Eile mit Weile spielen", "Ligretto spielen", "Wizard spielen", "Bieberbande spielen", "Dobble spielen", "Jungle Speed spielen", "Quartett spielen", "Mikado spielen", "Schach"]
    KreativitätYB: list = KreativitätYU
    KochenBackenYU: list = ["Sandwich machen", "Obstspiesse zubereiten", "Sommerdrink zubereiten", "Pizza vorbereiten", "Würstchen im Teig vorbereiten", "Flammkuchen vorbereiten", "Tost Hawaii vorbereiten"]
    SportYB: list = SportYU
    GesellschaftsspieleYB: list = GesellschaftsspieleYU
    SpielenYB: list = SpielenYU
    
    KreativitätYB.append("Slushy Slime")
    KreativitätYB.append("Perlenbilder")
    KreativitätYB.append("Papierflieger")
    KreativitätYB.append("Seilbahn durch die Wohnung")
    KreativitätYB.append("Kettenreaktion")
    KreativitätYB.append("Traumfänger basteln")
    KreativitätYB.append("Lochkamera bauen")

    SportYU.append("Fahrrad fahren")
    SportYU.append("Joggen gehen")
    SportYU.append("Hindernisparcour aufbauen& machen")

    KreativitätO: list = KreativitätYB
    KreativitätO.append("Seife selber machen")
    KreativitätO.append("Bullet journal")
    KochenBackenO: list = KochenBackenYB
    KochenBackenO.append("Einfache Desserts kreieren")
    KochenBackenO.append("Marshmallows machen")
    SportO: list = SportYB
    GesellschaftsspieleO: list = GesellschaftsspieleYB
    GesellschaftsspieleO.append("Jazzy spielen")
    GesellschaftsspieleO.append("Cluedo spielen")
    GesellschaftsspieleO.append("Tichu spielen")
    GesellschaftsspieleO.append("Exit spielen")
    GesellschaftsspieleO.append("Mühle spielen")
    GesellschaftsspieleO.append("Solitaire spielen")
    GesellschaftsspieleO.append("Jassen")
    GesellschaftsspieleO.append("Tabu spielen")
    GesellschaftsspieleO.append("Time's up spielen")

    SpielenO: list =["Lego spielen", "Slackline", "Drachen steigen lassen", "Hindernisparkour aufbauen", "Bowling mit Flaschen", "Seilspringen", "Wasserschlacht", "Rennbahn bauen", "Büchsen werfen(mit WC-Papierrollen)", "Zaubertricks lernen(mit Youtube)", "Rubiks cube", "Domino"]

    BastelnZeichnenYoungmit: list = ["Kalligraphie lernen", "Schmuck basteln", "Papierflieger basteln", "Puppenhaus aus Kartonschachtel",
            "Freundschaftsband knüpfen", "Traumfänger basteln", "Sandbilder: mit Kleber zeichnen, Sand darüberstreuen, trocknen lassen, abschüteln",
            "Mandala malen", "Zeichnen/Malen", "DIY: z.B. Zimmerdeko", "T-Shirt bemalen", "Aus Recyclingmaterial etwa basteln",
            "Murmelbahn aus Klopapierrollen bauen", "Bastelideen, DIY's, Rezepte und vieles mehr auf: https://www.schaeresteipapier.ch/"]

    BastelnZeichnenYoungohne: list = ["Kalligraphie lernen", "Schmuck basteln", "Papierflieger basteln", "Puppenhaus aus Kartonschachtel",
            "Freundschaftsband knüpfen", "Sandbilder: mit Kleber zeichnen, Sand darüberstreuen, trocknen lassen, abschüteln",
            "Mandala malen", "Zeichnen/Malen", "Aus Recyclingmaterial etwa basteln"
            , "Bastelideen, DIY's, Rezepte und vieles mehr auf: https://www.schaeresteipapier.ch/"]

    BastelnZeichnenOld: list = BastelnZeichnenYoungmit


    NaturwissenschaftenYoungmit: list = ["Kristalle aus Salz züchten: https://www.simplyscience.ch/tl_files/content/Bilder%20Import/Experimente/Experimente%20aus%20dem%20Kinderlabor/Kristall/SA_Kristalle_Experimentier-Anleitung.pdf",
            "Kristalle aus Salz züchten: https://www.simplyscience.ch/tl_files/content/Bilder%20Import/Experimente/Experimente%20aus%20dem%20Kinderlabor/Kristall/SA_Kristalle_Experimentier-Anleitung.pdf",
            "Experimente auf Geolino: https://www.geo.de/geolino/basteln/15225-thma-experimente", "Sudoku lösen", "Logicals",
            "rätsel lösen: https://www.ratehase.de oder https://www.raetseldino.de/ ", "Kresse/Kräutergarten züchten", "Vögel beobachten / Arten lernen",
            "Vierblättriges Kleeblatt suchen", "Familienstammbaum zeichnen", "Aufgabenblätter, Bastel- und Spielideen des Zürich Zoo",
            "Mit Haustier spielen / beobachten", "Sternenbilder lernen", "Vogelgezwischter hören/lernen", "Tierspuren lesen lernen", "Flaggen lernen"]

    NaturwissenschaftenYoungohne: list = ["Kristalle aus Salz züchten: https://www.simplyscience.ch/tl_files/content/Bilder%20Import/Experimente/Experimente%20aus%20dem%20Kinderlabor/Kristall/SA_Kristalle_Experimentier-Anleitung.pdf",
            "Kristalle aus Salz züchten: https://www.simplyscience.ch/tl_files/content/Bilder%20Import/Experimente/Experimente%20aus%20dem%20Kinderlabor/Kristall/SA_Kristalle_Experimentier-Anleitung.pdf",
            "Experimente auf Geolino: https://www.geo.de/geolino/basteln/15225-thma-experimente", "Sudoku lösen", "Logicals",
            "rätsel lösen: https://www.ratehase.de oder https://www.raetseldino.de/ ", "Kresse/Kräutergarten züchten", "Vögel beobachten / Arten lernen",
            "Vierblättriges Kleeblatt suchen", "Familienstammbaum zeichnen", "Aufgabenblätter, Bastel- und Spielideen des Zürich Zoo",
            "Mit Haustier spielen / beobachten", "Sternenbilder lernen", "Vogelgezwischter hören/lernen", "Tierspuren lesen lernen", "Flaggen lernen"]

    NaturwissenschaftenOld: list = ["Kristalle aus Salz züchten: https://www.simplyscience.ch/tl_files/content/Bilder%20Import/Experimente/Experimente%20aus%20dem%20Kinderlabor/Kristall/SA_Kristalle_Experimentier-Anleitung.pdf",
            "Kristalle aus Salz züchten: https://www.simplyscience.ch/tl_files/content/Bilder%20Import/Experimente/Experimente%20aus%20dem%20Kinderlabor/Kristall/SA_Kristalle_Experimentier-Anleitung.pdf",
            "Experimente auf Geolino: https://www.geo.de/geolino/basteln/15225-thma-experimente", "Kommunikationsmuseum di-fr 13:30 livestream aus dem Museum", "Sudoku lösen", "Logicals",
            "rätsel lösen: https://www.ratehase.de oder https://www.raetseldino.de/ ", "SSternbilder lernen", "Vogelgezwitscher hören/lernen", "Tierspuren lesen lernen", 
            "Berge der Schweiz lernen", "Hauptstädte lernen", "Flaggen lernen"]


    LesenYoungmit: list = ["Lieblingsbuch als Theaterstück umsetzen", "Eigene Geschichte schreiben", "400 gratis ebooks auf Amazon: https://www.amazon.de/s?rh=n%3A652886031&rd=1 ",
            "Finde ein neues Buch, dass deinen Interessen entspricht: https://www.literaturlandkarte.de/", "Buchtipps und persönliche Beratung für ein neues Buch: www.chinderbuechlade.ch",
            "Hörbuch hören", "Buch vorlesen", "chreib einen Brief an deine Freunde oder Grosseltern"]

    LesenYoungohne: list = LesenYoungmit

    LesenOld: list = ["Eigene Geschichte schreiben", "Briefe schreiben", "Hörbücher", "400 gratis ebooks auf Amazon: https://www.amazon.de/s?rh=n%3A652886031&rd=1 ",
            "Finde ein neues Buch, dass deinen Interessen entspricht: https://www.literaturlandkarte.de/", "Buchtipps und persönliche Beratung für ein neues Buch: www.chinderbuechlade.ch"]


    TechnikYoungmit: list = ["Technorama @ home Experimente für zuhause: https://www.technorama.ch/de/besuchen/technorama-blog", "Geolino: https://www.geo.de/geolino/basteln/15225-thma-experimente", 
            "Roboter", "Programmieren", "Video drehen/zusammenschneiden"]

    TechnikYoungohne: list = TechnikYoungmit

    TechnikOld: list = ["Programmieren lernen", "Videos aufnehmen/schneiden", "Photoshop lernen", "Roboter bauen",
            "Einfache Schaltkreise (z.B. Glübirne zum leuchten bringen"]

    
    NaturYoungmit: list = ["Vögel beobachten / Arten zählen", "Vierblättriges Kleeblatt suchen", "Gärtnern", "Aufgabenblätter, Bastel- und Spielideen des Zürich Zoo", 
            "Drachen steigen lassen", "Kresse/Kräutergarten pflanzen", "Mit der Lupe den Garten erkunden", "Gänseblümchenkette knüpfen", "Blumenstrauss pflücken", 
            "Mit Haustier spielen", "Staumauer bauen", "Spazieren", "Pfeilenbogen bauen", "Irgendwas aus natürlichen Sachen bauen (z.B. Stadt, Burg…)", 
            "Vogelgezwitscher hören/lernen", "Tierspuren lesen lernen"]

    NaturYoungohne: list = ["Vögel beobachten / Arten zählen", "Vierblättriges Kleeblatt suchen", "Gärtnern", "Aufgabenblätter, Bastel- und Spielideen des Zürich Zoo",
            "Kresse/Kräutergarten pflanzen", "Mit der Lupe den Garten erkunden", "Gänseblümchenkette knüpfen", "Blumenstrauss pflücken", 
            "Mit Haustier spielen", "Staumauer bauen", "Irgendwas aus natürlichen Sachen bauen (z.B. Stadt, Burg…)", 
            "Vogelgezwitscher hören/lernen", "Tierspuren lesen lernen"]

    NaturOld: list = ["Gärtnern", "Kräuter anpflanzen", "Staumauer bauen", "Spazieren", "Pfeilenbogen bauen",
            "Irgendwas aus natürlichen Sachen bauen (z.B. Stadt, Burg…)", "Feuer machen(inklusive Stock schnitzen", "Vogelgezwitscher hören/lernen",
            "Tierspuren lesen lernen"]


    

    #########################Tag1#######################
    f.write("Tag 1")
    f.write("\n")
    for i in Day1:
        if i =="School":
            f.write("1h Schule")
            f.write("\n")
        elif i =="Ämtli":
            if Young:
                pointer: int = random.randint(0,6)
                f.write(Amtliyoung[pointer])
                f.write("\n")
            else:
                pointer: int = random.randint(0, 11)
                f.write(Amtliold[pointer])
                f.write("\n")
        elif i == "SportHobby":
            f.write("Sport Hobby")
            f.write("\n")
        elif i == "Sport" or i == "SportYoung":
            if not Young:
                pointer: int = random.randint(0, len(SportO)-1)
                f.write(SportO[pointer])
                f.write("\n")
            elif Young and Alone:
                pointer: int = random.randint(0, len(SportYU)-1)
                f.write(SportYU[pointer])
                f.write("\n")
            else:
                pointer: int = random.randint(0, len(SportYB)-1)
                f.write(SportYB[pointer])
                f.write("\n")
        elif i == "Musik":
            f.write("Musik")
            f.write("\n")
        elif i == "Kreativität":
            if not Young:
                pointer: int = random.randint(0, len(KreativitätO)-1)
                f.write(KreativitätO[pointer])
                f.write("\n")
            elif Young and Alone:
                pointer: int = random.randint(0, len(KreativitätYU)-1)
                f.write(KreativitätYU[pointer])
                f.write("\n")
            else:
                pointer: int = random.randint(0, len(KreativitätYB)-1)
                f.write(KreativitätYB[pointer])
                f.write("\n")
        elif i == "Sport":
            if not Young:
                pointer: int = random.randint(0, len(SportO)-1)
                f.write(SportO[pointer])
                f.write("\n")
            elif Young and Alone:
                pointer: int = random.randint(0, len(SportYU)-1)
                f.write(SportYU[pointer])
                f.write("\n")
            else:
                pointer: int = random.randint(0, len(SportYB)-1)
                f.write(SportYB[pointer])
                f.write("\n")
        elif i == "KochenBacken":
            if not Young:
                pointer: int = random.randint(0, len(KochenBackenO)-1)
                f.write(KochenBackenO[pointer])
                f.write("\n")
            elif Young and Alone:
                pointer: int = random.randint(0, len(KochenBackenYU)-1)
                f.write(KochenBackenYU[pointer])
                f.write("\n")
            else:
                pointer: int = random.randint(0, len(KochenBackenYB)-1)
                f.write(KochenBackenYB[pointer])
                f.write("\n")
        elif i == "Spielen":
            if not Young:
                pointer: int = random.randint(0, len(SpielenO)-1)
                f.write(SpielenO[pointer])
                f.write("\n")
            elif Young and Alone:
                pointer: int = random.randint(0, len(SpielenYU)-1)
                f.write(SpielenYU[pointer])
                f.write("\n")
            else:
                pointer: int = random.randint(0, len(SpielenYB)-1)
                f.write(SpielenYB[pointer])
                f.write("\n")
        elif i == "Natur":
            if not Young:
                pointer: int = random.randint(0, len(NaturOld)-1)
                f.write(NaturOld[pointer])
                f.write("\n")
            elif Young and Alone:
                pointer: int = random.randint(0, len(NaturYoungohne)-1)
                f.write(NaturYoungohne[pointer])
                f.write("\n")
            else:
                pointer: int = random.randint(0, len(NaturYoungmit)-1)
                f.write(NaturYoungmit[pointer])
                f.write("\n")
        elif i == "Gesellschaftspiele":
            if not Young:
                pointer: int = random.randint(0, len(GesellschaftsspieleO)-1)
                f.write(GesellschaftsspieleO[pointer])
                f.write("\n")
            elif Young and Alone:
                pointer: int = random.randint(0, len(GesellschaftsspieleYU)-1)
                f.write(GesellschaftsspieleYU[pointer])
                f.write("\n")
            else:
                pointer: int = random.randint(0, len(GesellschaftsspieleYB)-1)
                f.write(GesellschaftsspieleYB[pointer])
                f.write("\n")
        elif i == "Technik":
            if not Young:
                pointer: int = random.randint(0, len(TechnikOld)-1)
                f.write(TechnikOld[pointer])
                f.write("\n")
            elif Young and Alone:
                pointer: int = random.randint(0, len(TechnikYoungohne)-1)
                f.write(TechnikYoungohne[pointer])
                f.write("\n")
            else:
                pointer: int = random.randint(0, len(TechnikYoungmit)-1)
                f.write(TechnikYoungmit[pointer])
                f.write("\n")
        elif i == "Lesen":
            if not Young:
                pointer: int = random.randint(0, len(LesenOld)-1)
                f.write(LesenOld[pointer])
                f.write("\n")
            elif Young and Alone:
                pointer: int = random.randint(0, len(LesenYoungohne)-1)
                f.write(LesenYoungohne[pointer])
                f.write("\n")
            else:
                pointer: int = random.randint(0, len(LesenYoungmit)-1)
                f.write(LesenYoungmit[pointer])
                f.write("\n")
        elif i == "Naturwissenschaften":
            if not Young:
                pointer: int = random.randint(0, len(NaturwissenschaftenOld)-1)
                f.write(NaturwissenschaftenOld[pointer])
                f.write("\n")
            elif Young and Alone:
                pointer: int = random.randint(0, len(NaturwissenschaftenYoungohne)-1)
                f.write(NaturwissenschaftenYoungohne[pointer])
                f.write("\n")
            else:
                pointer: int = random.randint(0, len(NaturwissenschaftenYoungmit)-1)
                f.write(NaturwissenschaftenYoungmit[pointer])
                f.write("\n")
        elif i == "BastelnZeichnen":
            if not Young:
                pointer: int = random.randint(0, len(BastelnZeichnenOld)-1)
                f.write(BastelnZeichnenOld[pointer])
                f.write("\n")
            elif Young and Alone:
                pointer: int = random.randint(0, len(BastelnZeichnenYoungohne)-1)
                f.write(BastelnZeichnenYoungohne[pointer])
                f.write("\n")
            else:
                pointer: int = random.randint(0, len(BastelnZeichnenYoungmit)-1)
                f.write(BastelnZeichnenYoungmit[pointer])
                f.write("\n")
    f.write("\n")




    #########################Tag2#######################
    f.write("Tag 2")
    f.write("\n")
    for i in Day2:
        if i =="School":
            f.write("1h Schule")
            f.write("\n")
        elif i =="Ämtli":
            if Young:
                pointer: int = random.randint(0,6)
                f.write(Amtliyoung[pointer])
                f.write("\n")
            else:
                pointer: int = random.randint(0, 11)
                f.write(Amtliold[pointer])
                f.write("\n")
        elif i == "SportHobby":
            f.write("Sport Hobby")
            f.write("\n")
        elif i == "Sport" or i == "SportYoung":
            if not Young:
                pointer: int = random.randint(0, len(SportO)-1)
                f.write(SportO[pointer])
                f.write("\n")
            elif Young and Alone:
                pointer: int = random.randint(0, len(SportYU)-1)
                f.write(SportYU[pointer])
                f.write("\n")
            else:
                pointer: int = random.randint(0, len(SportYB)-1)
                f.write(SportYB[pointer])
                f.write("\n")
        elif i == "Musik":
            f.write("Musik")
            f.write("\n")
        elif i == "Kreativität":
            if not Young:
                pointer: int = random.randint(0, len(KreativitätO)-1)
                f.write(KreativitätO[pointer])
                f.write("\n")
            elif Young and Alone:
                pointer: int = random.randint(0, len(KreativitätYU)-1)
                f.write(KreativitätYU[pointer])
                f.write("\n")
            else:
                pointer: int = random.randint(0, len(KreativitätYB)-1)
                f.write(KreativitätYB[pointer])
                f.write("\n")
        elif i == "Sport":
            if not Young:
                pointer: int = random.randint(0, len(SportO)-1)
                f.write(SportO[pointer])
                f.write("\n")
            elif Young and Alone:
                pointer: int = random.randint(0, len(SportYU)-1)
                f.write(SportYU[pointer])
                f.write("\n")
            else:
                pointer: int = random.randint(0, len(SportYB)-1)
                f.write(SportYB[pointer])
                f.write("\n")
        elif i == "KochenBacken":
            if not Young:
                pointer: int = random.randint(0, len(KochenBackenO)-1)
                f.write(KochenBackenO[pointer])
                f.write("\n")
            elif Young and Alone:
                pointer: int = random.randint(0, len(KochenBackenYU)-1)
                f.write(KochenBackenYU[pointer])
                f.write("\n")
            else:
                pointer: int = random.randint(0, len(KochenBackenYB)-1)
                f.write(KochenBackenYB[pointer])
                f.write("\n")
        elif i == "Spielen":
            if not Young:
                pointer: int = random.randint(0, len(SpielenO)-1)
                f.write(SpielenO[pointer])
                f.write("\n")
            elif Young and Alone:
                pointer: int = random.randint(0, len(SpielenYU)-1)
                f.write(SpielenYU[pointer])
                f.write("\n")
            else:
                pointer: int = random.randint(0, len(SpielenYB)-1)
                f.write(SpielenYB[pointer])
                f.write("\n")
        elif i == "Natur":
            if not Young:
                pointer: int = random.randint(0, len(NaturOld)-1)
                f.write(NaturOld[pointer])
                f.write("\n")
            elif Young and Alone:
                pointer: int = random.randint(0, len(NaturYoungohne)-1)
                f.write(NaturYoungohne[pointer])
                f.write("\n")
            else:
                pointer: int = random.randint(0, len(NaturYoungmit)-1)
                f.write(NaturYoungmit[pointer])
                f.write("\n")
        elif i == "Gesellschaftspiele":
            if not Young:
                pointer: int = random.randint(0, len(GesellschaftsspieleO)-1)
                f.write(GesellschaftsspieleO[pointer])
                f.write("\n")
            elif Young and Alone:
                pointer: int = random.randint(0, len(GesellschaftsspieleYU)-1)
                f.write(GesellschaftsspieleYU[pointer])
                f.write("\n")
            else:
                pointer: int = random.randint(0, len(GesellschaftsspieleYB)-1)
                f.write(GesellschaftsspieleYB[pointer])
                f.write("\n")
        elif i == "Technik":
            if not Young:
                pointer: int = random.randint(0, len(TechnikOld)-1)
                f.write(TechnikOld[pointer])
                f.write("\n")
            elif Young and Alone:
                pointer: int = random.randint(0, len(TechnikYoungohne)-1)
                f.write(TechnikYoungohne[pointer])
                f.write("\n")
            else:
                pointer: int = random.randint(0, len(TechnikYoungmit)-1)
                f.write(TechnikYoungmit[pointer])
                f.write("\n")
        elif i == "Lesen":
            if not Young:
                pointer: int = random.randint(0, len(LesenOld)-1)
                f.write(LesenOld[pointer])
                f.write("\n")
            elif Young and Alone:
                pointer: int = random.randint(0, len(LesenYoungohne)-1)
                f.write(LesenYoungohne[pointer])
                f.write("\n")
            else:
                pointer: int = random.randint(0, len(LesenYoungmit)-1)
                f.write(LesenYoungmit[pointer])
                f.write("\n")
        elif i == "Naturwissenschaften":
            if not Young:
                pointer: int = random.randint(0, len(NaturwissenschaftenOld)-1)
                f.write(NaturwissenschaftenOld[pointer])
                f.write("\n")
            elif Young and Alone:
                pointer: int = random.randint(0, len(NaturwissenschaftenYoungohne)-1)
                f.write(NaturwissenschaftenYoungohne[pointer])
                f.write("\n")
            else:
                pointer: int = random.randint(0, len(NaturwissenschaftenYoungmit)-1)
                f.write(NaturwissenschaftenYoungmit[pointer])
                f.write("\n")
        elif i == "BastelnZeichnen":
            if not Young:
                pointer: int = random.randint(0, len(BastelnZeichnenOld)-1)
                f.write(BastelnZeichnenOld[pointer])
                f.write("\n")
            elif Young and Alone:
                pointer: int = random.randint(0, len(BastelnZeichnenYoungohne)-1)
                f.write(BastelnZeichnenYoungohne[pointer])
                f.write("\n")
            else:
                pointer: int = random.randint(0, len(BastelnZeichnenYoungmit)-1)
                f.write(BastelnZeichnenYoungmit[pointer])
                f.write("\n")
    f.write("\n")





    #########################Tag3#######################
    f.write("Tag 3")
    f.write("\n")
    for i in Day3:
        if i =="School":
            f.write("1h Schule")
            f.write("\n")
        elif i =="Ämtli":
            if Young:
                pointer: int = random.randint(0,6)
                f.write(Amtliyoung[pointer])
                f.write("\n")
            else:
                pointer: int = random.randint(0, 11)
                f.write(Amtliold[pointer])
                f.write("\n")
        elif i == "SportHobby":
                f.write("Sport Hobby")
                f.write("\n")
        elif i == "Sport" or i == "SportYoung":
            if not Young:
                pointer: int = random.randint(0, len(SportO)-1)
                f.write(SportO[pointer])
                f.write("\n")
            elif Young and Alone:
                pointer: int = random.randint(0, len(SportYU)-1)
                f.write(SportYU[pointer])
                f.write("\n")
            else:
                pointer: int = random.randint(0, len(SportYB)-1)
                f.write(SportYB[pointer])
                f.write("\n")
        elif i == "Musik":
            f.write("Musik")
            f.write("\n")
        elif i == "Kreativität":
            if not Young:
                pointer: int = random.randint(0, len(KreativitätO)-1)
                f.write(KreativitätO[pointer])
                f.write("\n")
            elif Young and Alone:
                pointer: int = random.randint(0, len(KreativitätYU)-1)
                f.write(KreativitätYU[pointer])
                f.write("\n")
            else:
                pointer: int = random.randint(0, len(KreativitätYB)-1)
                f.write(KreativitätYB[pointer])
                f.write("\n")
        elif i == "Sport":
            if not Young:
                pointer: int = random.randint(0, len(SportO)-1)
                f.write(SportO[pointer])
                f.write("\n")
            elif Young and Alone:
                pointer: int = random.randint(0, len(SportYU)-1)
                f.write(SportYU[pointer])
                f.write("\n")
            else:
                pointer: int = random.randint(0, len(SportYB)-1)
                f.write(SportYB[pointer])
                f.write("\n")
        elif i == "KochenBacken":
            if not Young:
                pointer: int = random.randint(0, len(KochenBackenO)-1)
                f.write(KochenBackenO[pointer])
                f.write("\n")
            elif Young and Alone:
                pointer: int = random.randint(0, len(KochenBackenYU)-1)
                f.write(KochenBackenYU[pointer])
                f.write("\n")
            else:
                pointer: int = random.randint(0, len(KochenBackenYB)-1)
                f.write(KochenBackenYB[pointer])
                f.write("\n")
        elif i == "Spielen":
            if not Young:
                pointer: int = random.randint(0, len(SpielenO)-1)
                f.write(SpielenO[pointer])
                f.write("\n")
            elif Young and Alone:
                pointer: int = random.randint(0, len(SpielenYU)-1)
                f.write(SpielenYU[pointer])
                f.write("\n")
            else:
                pointer: int = random.randint(0, len(SpielenYB)-1)
                f.write(SpielenYB[pointer])
                f.write("\n")
        elif i == "Natur":
            if not Young:
                pointer: int = random.randint(0, len(NaturOld)-1)
                f.write(NaturOld[pointer])
                f.write("\n")
            elif Young and Alone:
                pointer: int = random.randint(0, len(NaturYoungohne)-1)
                f.write(NaturYoungohne[pointer])
                f.write("\n")
            else:
                pointer: int = random.randint(0, len(NaturYoungmit)-1)
                f.write(NaturYoungmit[pointer])
                f.write("\n")
        elif i == "Gesellschaftspiele":
            if not Young:
                pointer: int = random.randint(0, len(GesellschaftsspieleO)-1)
                f.write(GesellschaftsspieleO[pointer])
                f.write("\n")
            elif Young and Alone:
                pointer: int = random.randint(0, len(GesellschaftsspieleYU)-1)
                f.write(GesellschaftsspieleYU[pointer])
                f.write("\n")
            else:
                pointer: int = random.randint(0, len(GesellschaftsspieleYB)-1)
                f.write(GesellschaftsspieleYB[pointer])
                f.write("\n")
        elif i == "Technik":
            if not Young:
                pointer: int = random.randint(0, len(TechnikOld)-1)
                f.write(TechnikOld[pointer])
                f.write("\n")
            elif Young and Alone:
                pointer: int = random.randint(0, len(TechnikYoungohne)-1)
                f.write(TechnikYoungohne[pointer])
                f.write("\n")
            else:
                pointer: int = random.randint(0, len(TechnikYoungmit)-1)
                f.write(TechnikYoungmit[pointer])
                f.write("\n")
        elif i == "Lesen":
            if not Young:
                pointer: int = random.randint(0, len(LesenOld)-1)
                f.write(LesenOld[pointer])
                f.write("\n")
            elif Young and Alone:
                pointer: int = random.randint(0, len(LesenYoungohne)-1)
                f.write(LesenYoungohne[pointer])
                f.write("\n")
            else:
                pointer: int = random.randint(0, len(LesenYoungmit)-1)
                f.write(LesenYoungmit[pointer])
                f.write("\n")
        elif i == "Naturwissenschaften":
            if not Young:
                pointer: int = random.randint(0, len(NaturwissenschaftenOld)-1)
                f.write(NaturwissenschaftenOld[pointer])
                f.write("\n")
            elif Young and Alone:
                pointer: int = random.randint(0, len(NaturwissenschaftenYoungohne)-1)
                f.write(NaturwissenschaftenYoungohne[pointer])
                f.write("\n")
            else:
                pointer: int = random.randint(0, len(NaturwissenschaftenYoungmit)-1)
                f.write(NaturwissenschaftenYoungmit[pointer])
                f.write("\n")
        elif i == "BastelnZeichnen":
            if not Young:
                pointer: int = random.randint(0, len(BastelnZeichnenOld)-1)
                f.write(BastelnZeichnenOld[pointer])
                f.write("\n")
            elif Young and Alone:
                pointer: int = random.randint(0, len(BastelnZeichnenYoungohne)-1)
                f.write(BastelnZeichnenYoungohne[pointer])
                f.write("\n")
            else:
                pointer: int = random.randint(0, len(BastelnZeichnenYoungmit)-1)
                f.write(BastelnZeichnenYoungmit[pointer])
                f.write("\n")
    f.write("\n")



    #########################Tag4#######################
    f.write("Tag 4")
    f.write("\n")
    for i in Day4:
        if i =="School":
            f.write("1h Schule")
            f.write("\n")
        elif i =="Ämtli":
            if Young:
                pointer: int = random.randint(0,6)
                f.write(Amtliyoung[pointer])
                f.write("\n")
            else:
                pointer: int = random.randint(0, 11)
                f.write(Amtliold[pointer])
                f.write("\n")
        elif i == "SportHobby":
            f.write("Sport Hobby")
            f.write("\n")
        elif i == "Sport" or i == "SportYoung":
            if not Young:
                pointer: int = random.randint(0, len(SportO)-1)
                f.write(SportO[pointer])
                f.write("\n")
            elif Young and Alone:
                pointer: int = random.randint(0, len(SportYU)-1)
                f.write(SportYU[pointer])
                f.write("\n")
            else:
                pointer: int = random.randint(0, len(SportYB)-1)
                f.write(SportYB[pointer])
                f.write("\n")
        elif i == "Musik":
            f.write("Musik")
            f.write("\n")
        elif i == "Kreativität":
            if not Young:
                pointer: int = random.randint(0, len(KreativitätO)-1)
                f.write(KreativitätO[pointer])
                f.write("\n")
            elif Young and Alone:
                pointer: int = random.randint(0, len(KreativitätYU)-1)
                f.write(KreativitätYU[pointer])
                f.write("\n")
            else:
                pointer: int = random.randint(0, len(KreativitätYB)-1)
                f.write(KreativitätYB[pointer])
                f.write("\n")
        elif i == "Sport":
            if not Young:
                pointer: int = random.randint(0, len(SportO)-1)
                f.write(SportO[pointer])
                f.write("\n")
            elif Young and Alone:
                pointer: int = random.randint(0, len(SportYU)-1)
                f.write(SportYU[pointer])
                f.write("\n")
            else:
                pointer: int = random.randint(0, len(SportYB)-1)
                f.write(SportYB[pointer])
                f.write("\n")
        elif i == "KochenBacken":
            if not Young:
                pointer: int = random.randint(0, len(KochenBackenO)-1)
                f.write(KochenBackenO[pointer])
                f.write("\n")
            elif Young and Alone:
                pointer: int = random.randint(0, len(KochenBackenYU)-1)
                f.write(KochenBackenYU[pointer])
                f.write("\n")
            else:
                pointer: int = random.randint(0, len(KochenBackenYB)-1)
                f.write(KochenBackenYB[pointer])
                f.write("\n")
        elif i == "Spielen":
            if not Young:
                pointer: int = random.randint(0, len(SpielenO)-1)
                f.write(SpielenO[pointer])
                f.write("\n")
            elif Young and Alone:
                pointer: int = random.randint(0, len(SpielenYU)-1)
                f.write(SpielenYU[pointer])
                f.write("\n")
            else:
                pointer: int = random.randint(0, len(SpielenYB)-1)
                f.write(SpielenYB[pointer])
                f.write("\n")
        elif i == "Natur":
            if not Young:
                pointer: int = random.randint(0, len(NaturOld)-1)
                f.write(NaturOld[pointer])
                f.write("\n")
            elif Young and Alone:
                pointer: int = random.randint(0, len(NaturYoungohne)-1)
                f.write(NaturYoungohne[pointer])
                f.write("\n")
            else:
                pointer: int = random.randint(0, len(NaturYoungmit)-1)
                f.write(NaturYoungmit[pointer])
                f.write("\n")
        elif i == "Gesellschaftspiele":
            if not Young:
                pointer: int = random.randint(0, len(GesellschaftsspieleO)-1)
                f.write(GesellschaftsspieleO[pointer])
                f.write("\n")
            elif Young and Alone:
                pointer: int = random.randint(0, len(GesellschaftsspieleYU)-1)
                f.write(GesellschaftsspieleYU[pointer])
                f.write("\n")
            else:
                pointer: int = random.randint(0, len(GesellschaftsspieleYB)-1)
                f.write(GesellschaftsspieleYB[pointer])
                f.write("\n")
        elif i == "Technik":
            if not Young:
                pointer: int = random.randint(0, len(TechnikOld)-1)
                f.write(TechnikOld[pointer])
                f.write("\n")
            elif Young and Alone:
                pointer: int = random.randint(0, len(TechnikYoungohne)-1)
                f.write(TechnikYoungohne[pointer])
                f.write("\n")
            else:
                pointer: int = random.randint(0, len(TechnikYoungmit)-1)
                f.write(TechnikYoungmit[pointer])
                f.write("\n")
        elif i == "Lesen":
            if not Young:
                pointer: int = random.randint(0, len(LesenOld)-1)
                f.write(LesenOld[pointer])
                f.write("\n")
            elif Young and Alone:
                pointer: int = random.randint(0, len(LesenYoungohne)-1)
                f.write(LesenYoungohne[pointer])
                f.write("\n")
            else:
                pointer: int = random.randint(0, len(LesenYoungmit)-1)
                f.write(LesenYoungmit[pointer])
                f.write("\n")
        elif i == "Naturwissenschaften":
            if not Young:
                pointer: int = random.randint(0, len(NaturwissenschaftenOld)-1)
                f.write(NaturwissenschaftenOld[pointer])
                f.write("\n")
            elif Young and Alone:
                pointer: int = random.randint(0, len(NaturwissenschaftenYoungohne)-1)
                f.write(NaturwissenschaftenYoungohne[pointer])
                f.write("\n")
            else:
                pointer: int = random.randint(0, len(NaturwissenschaftenYoungmit)-1)
                f.write(NaturwissenschaftenYoungmit[pointer])
                f.write("\n")
        elif i == "BastelnZeichnen":
            if not Young:
                pointer: int = random.randint(0, len(BastelnZeichnenOld)-1)
                f.write(BastelnZeichnenOld[pointer])
                f.write("\n")
            elif Young and Alone:
                pointer: int = random.randint(0, len(BastelnZeichnenYoungohne)-1)
                f.write(BastelnZeichnenYoungohne[pointer])
                f.write("\n")
            else:
                pointer: int = random.randint(0, len(BastelnZeichnenYoungmit)-1)
                f.write(BastelnZeichnenYoungmit[pointer])
                f.write("\n")
    f.write("\n")



    ####################Day5####################
    f.write("Tag 5")
    f.write("\n")
    for i in Day5:
        if i =="School":
            f.write("1h Schule")
            f.write("\n")
        elif i =="Ämtli":
            if Young:
                pointer: int = random.randint(0,6)
                f.write(Amtliyoung[pointer])
                f.write("\n")
            else:
                pointer: int = random.randint(0, 11)
                f.write(Amtliold[pointer])
                f.write("\n")
        elif i == "SportHobby":
            f.write("Sport Hobby")
            f.write("\n")
        elif i == "Sport" or i == "SportYoung":
            if not Young:
                pointer: int = random.randint(0, len(SportO)-1)
                f.write(SportO[pointer])
                f.write("\n")
            elif Young and Alone:
                pointer: int = random.randint(0, len(SportYU)-1)
                f.write(SportYU[pointer])
                f.write("\n")
            else:
                pointer: int = random.randint(0, len(SportYB)-1)
                f.write(SportYB[pointer])
                f.write("\n")
        elif i == "Musik":
            f.write("Musik")
            f.write("\n")
        elif i == "Kreativität":
            if not Young:
                pointer: int = random.randint(0, len(KreativitätO)-1)
                f.write(KreativitätO[pointer])
                f.write("\n")
            elif Young and Alone:
                pointer: int = random.randint(0, len(KreativitätYU)-1)
                f.write(KreativitätYU[pointer])
                f.write("\n")
            else:
                pointer: int = random.randint(0, len(KreativitätYB)-1)
                f.write(KreativitätYB[pointer])
                f.write("\n")
        elif i == "Sport":
            if not Young:
                pointer: int = random.randint(0, len(SportO)-1)
                f.write(SportO[pointer])
                f.write("\n")
            elif Young and Alone:
                pointer: int = random.randint(0, len(SportYU)-1)
                f.write(SportYU[pointer])
                f.write("\n")
            else:
                pointer: int = random.randint(0, len(SportYB)-1)
                f.write(SportYB[pointer])
                f.write("\n")
        elif i == "KochenBacken":
            if not Young:
                pointer: int = random.randint(0, len(KochenBackenO)-1)
                f.write(KochenBackenO[pointer])
                f.write("\n")
            elif Young and Alone:
                pointer: int = random.randint(0, len(KochenBackenYU)-1)
                f.write(KochenBackenYU[pointer])
                f.write("\n")
            else:
                pointer: int = random.randint(0, len(KochenBackenYB)-1)
                f.write(KochenBackenYB[pointer])
                f.write("\n")
        elif i == "Spielen":
            if not Young:
                pointer: int = random.randint(0, len(SpielenO)-1)
                f.write(SpielenO[pointer])
                f.write("\n")
            elif Young and Alone:
                pointer: int = random.randint(0, len(SpielenYU)-1)
                f.write(SpielenYU[pointer])
                f.write("\n")
            else:
                pointer: int = random.randint(0, len(SpielenYB)-1)
                f.write(SpielenYB[pointer])
                f.write("\n")
        elif i == "Natur":
            if not Young:
                pointer: int = random.randint(0, len(NaturOld)-1)
                f.write(NaturOld[pointer])
                f.write("\n")
            elif Young and Alone:
                pointer: int = random.randint(0, len(NaturYoungohne)-1)
                f.write(NaturYoungohne[pointer])
                f.write("\n")
            else:
                pointer: int = random.randint(0, len(NaturYoungmit)-1)
                f.write(NaturYoungmit[pointer])
                f.write("\n")
        elif i == "Gesellschaftspiele":
            if not Young:
                pointer: int = random.randint(0, len(GesellschaftsspieleO)-1)
                f.write(GesellschaftsspieleO[pointer])
                f.write("\n")
            elif Young and Alone:
                pointer: int = random.randint(0, len(GesellschaftsspieleYU)-1)
                f.write(GesellschaftsspieleYU[pointer])
                f.write("\n")
            else:
                pointer: int = random.randint(0, len(GesellschaftsspieleYB)-1)
                f.write(GesellschaftsspieleYB[pointer])
                f.write("\n")
        elif i == "Technik":
            if not Young:
                pointer: int = random.randint(0, len(TechnikOld)-1)
                f.write(TechnikOld[pointer])
                f.write("\n")
            elif Young and Alone:
                pointer: int = random.randint(0, len(TechnikYoungohne)-1)
                f.write(TechnikYoungohne[pointer])
                f.write("\n")
            else:
                pointer: int = random.randint(0, len(TechnikYoungmit)-1)
                f.write(TechnikYoungmit[pointer])
                f.write("\n")
        elif i == "Lesen":
            if not Young:
                pointer: int = random.randint(0, len(LesenOld)-1)
                f.write(LesenOld[pointer])
                f.write("\n")
            elif Young and Alone:
                pointer: int = random.randint(0, len(LesenYoungohne)-1)
                f.write(LesenYoungohne[pointer])
                f.write("\n")
            else:
                pointer: int = random.randint(0, len(LesenYoungmit)-1)
                f.write(LesenYoungmit[pointer])
                f.write("\n")
        elif i == "Naturwissenschaften":
            if not Young:
                pointer: int = random.randint(0, len(NaturwissenschaftenOld)-1)
                f.write(NaturwissenschaftenOld[pointer])
                f.write("\n")
            elif Young and Alone:
                pointer: int = random.randint(0, len(NaturwissenschaftenYoungohne)-1)
                f.write(NaturwissenschaftenYoungohne[pointer])
                f.write("\n")
            else:
                pointer: int = random.randint(0, len(NaturwissenschaftenYoungmit)-1)
                f.write(NaturwissenschaftenYoungmit[pointer])
                f.write("\n")
        elif i == "BastelnZeichnen":
            if not Young:
                pointer: int = random.randint(0, len(BastelnZeichnenOld)-1)
                f.write(BastelnZeichnenOld[pointer])
                f.write("\n")
            elif Young and Alone:
                pointer: int = random.randint(0, len(BastelnZeichnenYoungohne)-1)
                f.write(BastelnZeichnenYoungohne[pointer])
                f.write("\n")
            else:
                pointer: int = random.randint(0, len(BastelnZeichnenYoungmit)-1)
                f.write(BastelnZeichnenYoungmit[pointer])
                f.write("\n")

    f.close()





####################################Interacting##############################################


button = tk.Button(root, text="Enter", bg='white', command=lambda: run())
button.place(relx=0.5, rely=0.995, relwidth=0.95, relheight=0.1, anchor='s')



root.mainloop()