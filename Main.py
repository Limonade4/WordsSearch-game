import tkinter
from tkinter import *
import random
import string
from tkinter import font, Label
from PIL import ImageTk, Image

etape = 0.135
sum_win = 0
check_win = 0
mots_placé = 0
verif_cond = False

grandeur_grille = 13

root = Tk()

root.title("Patate")
root.config(bg="#E3FBFF")
root.geometry('1400x700')
root.minsize(width=1400, height=800)
root.maxsize(width=1550, height=800)

my_pic = Image.open("photo-1579546929662-711aa81148cf.png")


def partie(taille_grille, nombre_mots, check_frame):
    check_frame.grid(row=0, column=0, sticky="nsew")
    check_frame.tkraise()

    grille_2D = []
    inter = []
    final = []
    hidden = []
    global verif_cond
    global pi
    police = font.Font(family="Roboto Black", size=11)
    police2 = font.Font(weight="bold", size=18)
    police_button1 = font.Font(weight="bold", size=13)
    police_check = font.Font(weight="bold", size=15)

    mots = ["CHEVAL", "SOURIS", "LIBELLULE", "PANGOLIN", "NASIQUE", "OURS", "CHIEN", "CHAT", "MOLLUSQUE", "DROMADAIRE",
            "MAKI", "HIBOUX", "PAPILLON", "CROCODILE", "KANGOUROU", "COCHON", "ZEBRE", "ESCARGOT", "MOUSTIQUE",
            "PARESSEUX", "ABEILLE", "GUEPE", "FRELON",
            "BOURDON", "SCARABEE", "MITE", "SAUTERELLE", "VISON", "GIRAFE", "AIGLE", "TIGRE", "PANDA", "FURET",
            "POULPE", "MANGOUSTE", "BALEINE", "PIEUVRE", "ANEMONE", "REQUIN",
            "MOINEAU", "HIPPOCAMPE", "MOUCHE", "MESANGE", "CERF", "LION", "RENARD", "CANARD", "CAFARD", "OIE",
            "PERRUCHE", "PERROQUET", "HYENE", "SANGLIER",
            "HAMSTER", "GORILLE", "PHACOCHERE", "SURICATE", "ANTILOPE", "LIMACE", "TORTUE", "ELEPHANT", "ALABATROS",
            "PIGEON", "MEDUSE", "JAGUAR", "GUEPARD",
            "MOUTON", "GLOUTON", "CHEVRE", "BLAIREAU", "FOUINE", "LAPIN", "FOURMILLIER", "AUTRUCHE", "CANARI", "LOUP",
            "SERPENT", "ANACONDA", "MYGALE", "SARDINE",
            "SAUMON", "THON", "ARA", "DODO", "ANKYLOSAURE", "STEGOSAURE", "VELOCIRAPTOR", "CARNOTAURE", "RAT",
            "ECUREUIL", "TARDIGRADE", "LAMA", "GRENOUILLE",
            "CRAPAUD", "FAUCON", "HERISSON", "LIEVRE", "ORNITORYNQUE", "CASTOR", "MOUETTE", "POULE", "PONEY", "MORUE",
            "CRABE", "FENNEC", "GNOU", "GOELAND",
            "HIRONDELLE", "ORIGNAL", "CREVETTE", "MOULE", "HUITRE", "DAUPHIN", "RAGONDIN", "GERBOISE", "ORQUE", "TAUPE",
            "VER", "BOUQUETIN", "VACHE", "TAUREAU",
            "COLOMBE", "FOURMI", "CORBEAU", "GRUE", "KIWI", "COLIBRI", "TATOU", "WALLABY", "IGUANE", "PANTHERE",
            "CHAMEAU", "HIPPOPOTAME", "CYGNE", "ANE",
            "KOALA", "BICHE", "PAON", "FAISAN", "CARPE", "COQ", "PERDRIX", "OUISTITI", "LEMURIEN", "MACAQUE",
            "MANDRILL", "SAIMIRI", "BLOBFISH", "BROCHET",
            "LOTTE", "OTARIE", "PHOQUE", "BUSE", "CHOUETTE", "CORNEILLE", "EPERVIER", "MERLE", "MURENE", "RAIE",
            "MAQUEREAU", "ESTURGEON", "BELUGA", "MARSOUIN",
            "PINGOUIN", "LANGOUSTE", "HOMARD", "BIGORNEAU", "NAUTILUS", "CORAIL", "EPONGE", "MORSE", "CAMELEON", "BOUC",
            "DINDON", "DINDE", "BELIER", "MARMOTTE",
            "CHAMOIS", "CHENILLE", "COCINELLE", "CYGALE", "PUCE", "CHINCHILLA", "GERBILLE", "COBAYE", "MUSARAIGNE",
            "DIPLODOCUS", "MOSASAURE", "PTERODACTYLE",
            "TRICERATOPS", "WAPITI", "SALAMANDRE", "PUMA", "PYGARGUE", "MOUFETTE", "MARTRE", "CHEVREUIL", "COYOTE",
            "LYCAON", "BELETTE", "BLATTE", "BISON",
            "MAMMOUTH", "VAUTOUR", "PIE", "LOUTRE", "PUTOIS", "HERMINE", "ZEBU", "MACAREUX", "PELICAN", "TOUCAN",
            "RHINOCEROS", "LEOPARD", "CYGOGNE", "LYNX",
            "CLOPORTE", "VIPERE", "ORVET", "PYTHON", "COULEUVRE", "ECREVISSE", "COLIN", "CALAMARE", "CABILLAUD", "EMEU",
            "TAPIR", "TIQUE", "BONOBO", "CHIMPANZEE",
            "MANCHOT", "ALOUETTE", "COUTEAU", "SOLE", "HARENG"]

    pi = len(mots)
    DIRECTION_RIGHT = 1
    DIRECTION_LEFT = 2
    DIRECTION_DOWN = 3
    DIRECTION_UP = 4
    mot_liste = None

    oui = Label(window, image=new_pic)
    oui.place(relx=0, rely=0, relwidth=1)

    # definir position mot, possibilité d'écriture et écriture
    def position_mot(mot, block=0):
        if block != taille_grille * taille_grille:
            global mots_placé
            global sum_win
            block += 1
            x = random.randint(0, taille_grille - 1)
            y = random.randint(0, taille_grille - 1)

            # choix aléatoire des différentes position
            direct = random.randint(1, 4)
            if direct == DIRECTION_RIGHT:

                if len(mot) > taille_grille - x:
                    position_mot(mot, block)
                    return

                if len(mot) <= taille_grille - x:

                    for pos in range(x, x + len(mot)):

                        if grille_2D[y][pos] != 0:
                            position_mot(mot, block)
                            return

                    lettres = list(mot)
                    for pos in range(0, len(mot)):
                        grille_2D[y][pos + x] = lettres[pos]
                        crea_boutons(y, pos + x, lettres[pos])
                        sum_win += ord(lettres[pos])
                    mots_placé += 1
                    final.append(mot)
                    # print(mot)

            if direct == DIRECTION_DOWN:

                if len(mot) > taille_grille - y:
                    position_mot(mot, block)
                    return

                if len(mot) <= taille_grille - y:

                    for pos in range(y, y + len(mot)):

                        if grille_2D[pos][x] != 0:
                            position_mot(mot, block)
                            return

                    lettres = list(mot)
                    for pos in range(0, len(mot)):
                        grille_2D[pos + y][x] = lettres[pos]
                        crea_boutons(pos + y, x, lettres[pos])
                        sum_win += ord(lettres[pos])
                    mots_placé += 1
                    final.append(mot)
                    # print(mot)

            if direct == DIRECTION_UP:

                if len(mot) > 0 + y:
                    position_mot(mot, block)
                    return

                if len(mot) <= 0 + y:
                    boucle = y
                    while boucle >= y - len(mot):

                        if grille_2D[boucle][x] != 0:
                            position_mot(mot, block)
                            return
                        boucle -= 1

                    lettres = list(mot)
                    for pos in range(0, len(mot)):
                        grille_2D[y - pos][x] = lettres[pos]
                        crea_boutons(y - pos, x, lettres[pos])
                        sum_win += ord(lettres[pos])
                    mots_placé += 1
                    final.append(mot)
                    # print(mot)

            if direct == DIRECTION_LEFT:

                if len(mot) > 0 + x:
                    position_mot(mot, block)
                    return

                if len(mot) <= 0 + x:
                    loop = x
                    while loop >= x - len(mot):

                        if grille_2D[y][loop] != 0:
                            position_mot(mot, block)
                            return
                        loop -= 1

                    lettres = list(mot)
                    for pos in range(0, len(mot)):
                        grille_2D[y][x - pos] = lettres[pos]
                        crea_boutons(y, x - pos, lettres[pos])
                        sum_win += ord(lettres[pos])
                    mots_placé += 1
                    final.append(mot)
                    # print(mot)

    # choisi les mots à mettre dans la grille (les ajoute dans une liste intermédiaire)

    def mots_choisis(quantité=1):
        limite = 0
        global pi
        while limite < quantité:
            random_numb = random.randint(0, pi - 1)
            receptacle = mots[random_numb]

            if (receptacle in inter):
                limite -= 1
            else:
                inter.append(receptacle)

            limite += 1

    # donne deux index random de la grille 2D

    def mots_grille():

        for pont in range(0, len(inter)):

            if len(inter[pont]) <= taille_grille:
                position_mot(inter[pont], 0)

    def crea_boutons(row, column, texte):

        Boutons_grille = tkinter.Button(Cadre, width=1, padx=18, pady=10, bg="#F0F3F4", bd=1,
                                        text=texte, font=police, command=lambda: Button_state(Boutons_grille))
        Boutons_grille.grid(row=row, column=column)

    def Button_state(Boutons_grille):

        global check_win

        if Boutons_grille["bg"] == "#F0F3F4":
            Boutons_grille['bg'] = "#ABF3FF"
            check_win += ord(Boutons_grille["text"])

        else:
            Boutons_grille['bg'] = "#F0F3F4"
            check_win -= ord(Boutons_grille["text"])

    def revel_mots():

        global verif_cond
        global etape

        if button1["bg"] == "#F0F3F4":

            button1['bg'] = "#FCC8F7"

        else:
            button1['bg'] = "#F0F3F4"

        if verif_cond == False:
            for _ in range(0, len(hidden)):
                hidden[_].place(relx=0.089, rely=etape)
                etape += 0.087
                verif_cond = True

        elif verif_cond == True:

            for _ in range(0, len(hidden)):
                hidden[_].place_forget()
                etape = 0.135
                verif_cond = False

    def check_ASCII():

        if check_win == sum_win:
            pas_fini.place_forget()
            button_win.place(relx=0.798, rely=0.43)


        else:
            button_win.place_forget()
            pas_fini.place(relx=0.7715, rely=0.43)

        restart.place(relx=0.812, rely=0.5)

    def recommencer():

        start_frame.tkraise()

    # défini grille 2D en remplissant de 0

    for ligne in range(0, taille_grille):
        temp_0 = []

        for oui in range(0, taille_grille):
            temp_0.append(0)

        grille_2D.append(temp_0)

    for a in range(1, 100):
        window.grid_columnconfigure(a, weight=1)
        window.grid_rowconfigure(a, weight=1)

    Cadre = tkinter.Frame(window, bg="black", bd=1, padx=1, pady=1)
    Cadre.grid(row=50, column=50)

    print(pi)
    mots_choisis(nombre_mots)

    mots_grille()

    i = 0
    for index in range(0, taille_grille):

        for i in range(0, len(grille_2D[index])):
            if grille_2D[index][i] == 0:
                Lettres_remplissage = random.choice(string.ascii_uppercase)
                grille_2D[index][i] = Lettres_remplissage
                crea_boutons(index, i, Lettres_remplissage)

    largeur = 15

    if len(final) >= 10:
        num_mots = Label(window, text=f"Trouve les {len(final)} mots !", font=police_button1, padx=10, pady=5,
                         relief="solid", bg="#FFE0FC")
        num_mots.place(relx=0.0785, rely=0.2)
    elif len(final) <= 9:
        num_mots = Label(window, text=f"Trouve les {len(final)} mots !", font=police_button1, padx=15, pady=5,
                         relief="solid", bg="#FFE0FC")
        num_mots.place(relx=0.0785, rely=0.2)

    Cadre_revel = Frame(window, bg="#FFE0FC", height=400, width=180, highlightthickness=2, highlightbackground='black')
    Cadre_revel.place(relx=0.08, rely=0.25)

    for a in range(0, len(final)):
        mot_list = Label(Cadre_revel, text=final[a], bg="#FFE0FC", font=police, justify='right')
        hidden.append(mot_list)

    # Bouton pour afficher les mots
    border_button1 = Frame(Cadre_revel, bg="black", bd=2)
    border_button1.place(relx=0.041, rely=0.02)
    button1 = Button(border_button1, text="Montrer les mots", bd=1, relief='flat',
                     font=police_button1, width=largeur, command=revel_mots, bg="#F0F3F4")
    button1.pack()

    # boutons affichés si check_button est pressé
    pas_fini = Label(window, text="Il te reste des mots à trouver", font=police_button1, padx=15, pady=5,
                     relief="solid")
    button_win = Label(window, text="Bravo tu as réussi !", font=police_button1, padx=15, pady=5, relief="solid")
    restart = Button(window, text="Recommencer", font=police_check, relief="solid", command=recommencer)

    # bouton de check de la victoire
    border_checkbutton = Frame(window, bg="black", bd=2)
    border_checkbutton.place(relx=0.808, rely=0.35)
    check_button = Button(border_checkbutton, text="Check victoire", font=police_check, relief="flat",
                          highlightthickness=2, bg="#E0FFD5", activebackground="#E0FFD5", command=check_ASCII)
    check_button.pack()

    # Label indiquant la taille de la grille
    label_grille = Label(window, text=f"Grille de {taille_grille} x {taille_grille}", bg="#F0F3F4", font=police2,
                         borderwidth=2,
                         relief="solid", padx=10, pady=5)
    label_grille.grid(row=25, column=50)

    # print(mots_placé)


root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
start_frame = Frame(root)

window = Frame(root)

start_frame.grid(row=0, column=0, sticky="nsew")

police_start = font.Font(weight="bold", size=22)
police_titre = font.Font(weight="bold", size=35)

resized = my_pic.resize((1550, 800), Image.ANTIALIAS)
new_pic = ImageTk.PhotoImage(resized)
non = Label(start_frame, image=new_pic)
non.place(relx=0, rely=0, relwidth=1)

border_titre = Label(start_frame, bg="black", width=41, height=5, relief="flat", padx=31, pady=5)
border_titre.place(relx=0.38983, rely=0.096)

label_desc = Label(start_frame, text="Choisissez le nombre de mots", font=police_start, relief="solid", padx=30, pady=9,
                   borderwidth=3)
label_desc.place(relx=0.343, rely=0.18)

label_titre = Label(start_frame, text="Mots cachés", font=police_titre, relief="flat", padx=30, pady=5)
label_titre.place(relx=0.393, rely=0.1)

border_startbutton = Frame(root)

mots_button = Button(start_frame, text="6 mots", font=police_start, relief="solid", borderwidth=3, padx=5,
                     command=lambda: partie(grandeur_grille, 6, window))
mots_button2 = Button(start_frame, text="7 mots", font=police_start, relief="solid", borderwidth=3, padx=5,
                      command=lambda: partie(grandeur_grille, 7, window))
mots_button3 = Button(start_frame, text="8 mots", font=police_start, relief="solid", borderwidth=3, padx=5,
                      command=lambda: partie(grandeur_grille, 8, window))
mots_button4 = Button(start_frame, text="9 mots", font=police_start, relief="solid", borderwidth=3, padx=5,
                      command=lambda: partie(grandeur_grille, 9, window))
mots_button5 = Button(start_frame, text="10 mots", font=police_start, relief="solid", borderwidth=3, padx=5,
                      command=lambda: partie(grandeur_grille, 10, window))

increase = 0.169
for bouton in (mots_button, mots_button2, mots_button3, mots_button4, mots_button5):
    bouton.place(relx=increase, rely=0.45)
    increase += 0.15

root.mainloop()