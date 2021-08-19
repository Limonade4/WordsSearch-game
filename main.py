import tkinter
from tkinter import *
import random
import string
from tkinter import font
from PIL import ImageTk, Image

window = Tk()

window.title("Patate")
window.config(bg="#DFEFEC")
window.geometry('1400x700')
window.minsize(width=1000, height=500)

grille_2D = []
inter = []
final = []
taille_grille = 13
mots_placé = 0
verif_cond = False
etape = 0.22
police = font.Font(weight="bold", size= 10)

mots = ["CHEVAL", "SOURIS", "LIBELLULE", "PANGOLIN", "NASIQUE", "OURS", "CHIEN", "CHAT", "MOLLUSQUE", "DROMADAIRE", "MAKI", "HIBOUX", "PAPILLON",
            "CROCODILE", "KANGOUROU", "COCHON", "ZEBRE", "ESCARGOT", "MOUSTIQUE", "PARESSEUX", "ABEILLE", "GUEPE", "FRELON", "BOURDON", "SCARABEE", "MITE",
            "SAUTERELLE", "VISON", "GIRAFE", "AIGLE", "TIGRE", "PANDA", "FURET", "POULPE", "MANGOUSTE", "BALEINE", "PIEUVRE", "ANEMONE", "REQUIN",
            "MOINEAU", "HIPPOCAMPE", "MOUCHE", "MESANGE", "CERF", "LION", "RENARD", "CANARD", "CAFARD", "OIE", "PERRUCHE", "PERROQUET", "HYENE", "SANGLIER",
            "HAMSTER", "GORILLE", "PHACOCHERE", "SURICATE", "ANTILOPE", "LIMACE", "TORTUE", "ELEPHANT", "ALABATROS", "PIGEON", "MEDUSE", "JAGUAR", "GUEPARD",
        "MOUTON", "GLOUTON", "CHEVRE", "BLAIREAU", "FOUINE", "LAPIN", "FOURMILLIER", "AUTRUCHE", "CANARI", "LOUP", "SERPENT", "ANACONDA", "MYGALE", "SARDINE",
        "SAUMON", "THON", "ARA", "DODO", "ANKYLOSAURE", "STEGOSAURE", "VELOCIRAPTOR", "CARNOTAURE", "RAT", "ECUREUIL", "TARDIGRADE", "LAMA", "GRENOUILLE",
        "CRAPAUD", "FAUCON", "HERISSON", "LIEVRE", "ORNITORYNQUE", "CASTOR", "MOUETTE", "POULE", "PONEY", "MORUE", "CRABE", "FENNEC", "GNOU", "GOELAND",
        "HIRONDELLE", "ORIGNAL", "CREVETTE", "MOULE", "HUITRE", "DAUPHIN", "RAGONDIN", "GERBOISE", "ORQUE", "TAUPE", "VER", "BOUQUETIN", "VACHE", "TAUREAU",
        "COLOMBE", "FOURMI", "CORBEAU", "GRUE", "KIWI", "COLIBRI", "TATOU", "WALLABY", "IGUANE", "PANTHERE", "CHAMEAU", "HIPPOPOTAME", "CYGNE", "ANE",
        "KOALA", "BICHE", "PAON", "FAISAN", "CARPE", "COQ", "PERDRIX", "OUISTITI", "LEMURIEN", "MACAQUE", "MANDRILL", "SAIMIRI", "BLOBFISH", "BROCHET",
        "LOTTE", "OTARIE", "PHOQUE", "BUSE", "CHOUETTE", "CORNEILLE", "EPERVIER", "MERLE", "MURENE", "RAIE", "MAQUEREAU", "ESTURGEON", "BELUGA", "MARSOUIN",
        "PINGOUIN", "LANGOUSTE", "HOMARD", "BIGORNEAU", "NAUTILUS", "CORAIL", "EPONGE", "MORSE", "CAMELEON", "BOUC", "DINDON", "DINDE", "BELIER", "MARMOTTE",
        "CHAMOIS", "CHENILLE", "COCINELLE", "CYGALE", "PUCE", "CHINCHILLA", "GERBILLE", "COBAYE", "MUSARAIGNE", "DIPLODOCUS", "MOSASAURE", "PTERODACTYLE",
        "TRICERATOPS", "WAPITI", "SALAMANDRE", "PUMA", "PYGARGUE", "MOUFETTE", "MARTRE", "CHEVREUIL", "COYOTE", "LYCAON", "BELETTE", "BLATTE", "BISON",
        "MAMMOUTH", "VAUTOUR", "PIE", "LOUTRE", "PUTOIS", "HERMINE", "ZEBU", "MACAREUX", "PELICAN", "TOUCAN","RHINOCEROS", "LEOPARD", "CYGOGNE", "LYNX",
        "CLOPORTE", "VIPERE", "ORVET", "PYTHON", "COULEUVRE", "ECREVISE", "COLIN", "CALAMARE", "CABILLAUD", "EMEU", "TAPIR", "TIQUE", "BONOBO", "CHIMPANZEE",
        "MANCHOT", "ALOUETTE", "COUTEAU", "SOLE", "HARENG"]

pi = len(mots)
DIRECTION_RIGHT = 1
DIRECTION_LEFT = 2
DIRECTION_DOWN = 3
DIRECTION_UP = 4

# definir position mot, possibilité d'écriture et écriture
def position_mot(mot, block = 0):

 if block != taille_grille*taille_grille:
    global mots_placé
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

            for pos in range(x, x + len(mot) ):

                if grille_2D[y][pos] != 0:
                    position_mot(mot, block)
                    return

            lettres = list(mot)
            for pos in range(0, len(mot)):

                grille_2D[y][pos + x] = lettres[pos]
                crea_boutons(y, pos + x, lettres[pos])
            mots_placé +=1
            final.append(mot)
            print(mot)

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
            mots_placé += 1
            final.append(mot)
            print(mot)

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
            mots_placé += 1
            final.append(mot)
            print(mot)

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
            mots_placé += 1
            final.append(mot)
            print(mot)

#choisi les mots à mettre dans la grille (les ajoute dans une liste intermédiaire)

def mots_choisis(quantité = 1):
    limite = 0
    global pi
    while limite < quantité:
        random_numb = random.randint(0, pi-1)
        receptacle = mots[random_numb]

        if (receptacle in inter):
            limite -= 1
        else:
            inter.append(receptacle)

        limite +=1


#donne deux index random de la grille 2D

def mots_grille():

    for pont in range(0, len(inter)):

        if len(inter[pont]) <= taille_grille:

            position_mot(inter[pont], 0)



def crea_boutons(row, column, texte):

            Boutons_grille = tkinter.Button(Cadre, width=1, padx=18, pady=10, bg="#F0F3F4", bd=1,
                                            text=texte, font=police, command=lambda: Button_state(Boutons_grille))
            Boutons_grille.grid(row=row, column=column)

def Button_state(Boutons_grille):

        if Boutons_grille["bg"] == "#F0F3F4":
            Boutons_grille['bg'] = "#FFB5CF"

        else:
            Boutons_grille['bg'] = "#F0F3F4"

def revel_mots():

    global verif_cond
    global etape
    if verif_cond == False:
        for a in range(0, len(final)-1):

            mot_list = Label(window, text=final[a], bg="#DFEFEC", font=police, justify='right')
            mot_list.place(relx=0.065, rely=etape)
            etape += 0.045
            verif_cond = True

    if verif_cond == True:
        print("chien")

#défini grille 2D en remplissant de 0

for ligne in range(0, taille_grille):
    temp_0 = []

    for oui in range(0, taille_grille):
        temp_0.append(0)

    grille_2D.append(temp_0)

for a in range(1, 100):

    window.grid_columnconfigure(a, weight=1)
    window.grid_rowconfigure(a, weight=1)

Cadre = tkinter.Frame(window, bg="black", bd=1, padx=1, pady=1)
Cadre.grid(row= 50, column= 50)


print(pi)
mots_choisis(10)

mots_grille()

i = 0
for index in range(0, taille_grille):

    for i in range(0, len(grille_2D[index])):
        if grille_2D[index][i] == 0:
            Lettres_remplissage = random.choice(string.ascii_uppercase)
            grille_2D[index][i] = Lettres_remplissage
            crea_boutons(index, i, Lettres_remplissage)

largeur = 15
print(final)
print(len(final)- 1)

border_button1 = Frame(window, bg="black", bd=1)
border_button1.place(relx= 0.065, rely=0.15)

police_button1 = font.Font(size=13)
button1 = Button(border_button1, text="Montrer les mots", bd=1, relief='flat',
                 font=police_button1, width=largeur, command=revel_mots)
button1.pack()



print(mots_placé)


window.mainloop()

