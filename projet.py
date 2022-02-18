import tkinter as tk                    
from tkinter import ttk
from tkinter import * # le programme va aller chercher toutes les fonctions de la librairie Tkinter 

# fonction de chiffrement cesar
def cesar():
    zt3.delete(0,END)
    phrase = zt1.get()
    cle = zt2.get()
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ',
                'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    result = ""# chaîne de caractères qui contiendra le cryptogramme.
    i,a = 0,0
    b,o = 0,0
    if (cle.isdigit()):    
        while len(result) < len(phrase):
            if phrase[i] in alphabet:
                if phrase[i] == alphabet[a]:
                    b = int(cle[o])
                    result = result + alphabet[
                        (a+b)%53]# mise à l'echelle <53
                    i += 1
                    o = (o+1)%len(cle)
                a = (a+1)%53
            else:
                result = result + " "# concaténation des caractères de rang len(result2) < len(phrase) pour obtenir le texte clair
                i += 1
        zt3.insert(0,result)
    else:
        zt3.insert(0,"verifier les valeur en entrante ")
# fonction de dechiffrement cesar
def dechiffrementcesar():
    zt32.delete(0,END)
    phrase = zt12.get()
    cle = zt22.get()
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ',
                'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    result2 = "" # chaîne de caractères qui contiendra le décryptogramme.
    i,a = 0,0
    b,o = 0,0
    if (cle.isdigit()): 
        while len(result2) < len(phrase):
            if phrase[i] in alphabet:
                if phrase[i] == alphabet[a]:
                    b = int(cle[o])
                    result2 = result2 + alphabet[
                        (a-b)%53]# mise à l'echelle <53
                    i += 1
                    o = (o+1)%len(cle)
                a = (a+1)%53
            else:
                result2 = result2 + " "# concaténation des caractères de rang len(result2) < len(phrase) pour obtenir le texte clair
                i += 1
        zt32.insert(0,result2)
    else:
         zt3.insert(0,"verifier les valeur en entrante ")
# fonction de chiffrement par clé        
def chiffrementparcle():

    result = ''
    alphabet='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz '
    zt33.delete(0,END)
    phrase = zt13.get()
    cle = zt23.get()
    for i in range(len(phrase)):
        letter_n = alphabet.index(phrase[i])
        cle_n = alphabet.index(cle
                               [i % len(cle)])

        value = (letter_n + cle_n) % len(alphabet)# concaténation des caractères de rang i pour obtenir le texte clair
       
        result += alphabet[value]

    zt33.insert(0,result)
# fonction de dechiffrement par clé        
def dechiffrementparcle():

    result = ''
    alphabet='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz '
    zt34.delete(0,END)
    phrase = zt14.get()
    cle = zt24.get()
    for i in range(len(phrase)):
        letter_n = alphabet.index(phrase[i])
        cle_n = alphabet.index(cle
                               [i % len(cle)])

        value = (letter_n - cle_n) % len(alphabet)# concaténation des caractères de rang i pour obtenir le texte clair       

        result += alphabet[value]

    zt34.insert(0,result)

 
# ---------------------------------------------------
# Debut
# ---------------------------------------------------
# création de la fenêtre
Fenetre = tk.Tk()#Nous initialisons notre fenêtre Tkinter, en la nommant Fenetre
Fenetre.title("Cryptage/décryptage")#Mise en place d'un titre pour notre fenêtre
Fenetre.geometry("600x500") # définie la dimension minimale de la fenêtre
Fenetre.maxsize(1024,768) # En définissant la taille maximal de notre fenêtre, cela signifie que l'utilisateur ne pourra pas changer la taille en dessous d'une largeur 
#de 1024 et d'une hauteur de 768. C'est une taille en pixels.

ongletControl = ttk.Notebook(Fenetre)
  
onglet1 = ttk.Frame(ongletControl)
onglet2 = ttk.Frame(ongletControl)
onglet3 = ttk.Frame(ongletControl)
onglet4 = ttk.Frame(ongletControl)
  
ongletControl.add(onglet1, text ='Cryptage Cesar')
ongletControl.add(onglet2, text ='Décryptage Cesar')
ongletControl.add(onglet3, text ='Cryptage par clé')
ongletControl.add(onglet4, text ='Cryptage par clé')
ongletControl.pack(expand = 1, fill ="both")

#Création des zones de saisie à partir de la classe Label().
# pour saisir pour onglet 1 #####################################################################################################
e1 = Label(onglet1, text = " Texte à crypté ")
e1.grid(row=1, column=1)
crypter = StringVar()
zt1 = Entry(onglet1, width=50,textvariable = crypter)#  Nous créons le widget zt1 , un champ de saisie ('champ de saisie'), et le lions à la onglet .
zt1.grid(row=1, column=2)
crypter.set("écrire le Texte à crypté ici")

# pour saisir le décalage
e2 = Label(onglet1, text = "valeur du décalage  ")
e2.grid(row=2, column=1)
zt2 = Entry(onglet1, width=50)# # Nous créons le widget zt2 , un champ de saisie ('champ de saisie'), et le lions à la onglet1 .
zt2.grid(row=2, column=2)

# Bouton de commande 
b1 = Button(onglet1, text = "cryptage", command=cesar)#Nous créons le widget b1 , un bouton qui soumettra notre entrée. L'argument «texte» définit le texte à afficher sur le bouton.Nous attacher à la onget1 et les dimensions définies.
b1.grid(row=3, column=2)

# pour afficher le résultat
e3 = Label(onglet1, text = "résultat du cryptage par Cesar")
e3.grid(row=4, column=1)
zt3 = Entry(onglet1, width=50)# # Nous créons le widget zt3 , un champ de saisie ('champ de saisie'), et le lions à la onglet1 .
zt3.grid(row=4, column=2)


# pour saisir pour onglet 2#####################################################################################################
e12 = Label(onglet2, text = " Texte à décrypté ")
e12.grid(row=1, column=1)
crypter = StringVar()# variable pour recevoir le texte saisi
zt12 = Entry(onglet2, width=50,textvariable = crypter)# saisie du texte
zt12.grid(row=1, column=2)
crypter.set("écrire le Texte à décrypté ici")

# pour saisir le décalage
e22 = Label(onglet2, text = "valeur du décalage  ")
e22.grid(row=2, column=1)
zt22 = Entry(onglet2, width=50)# saisie du texte
zt22.grid(row=2, column=2)

# Bouton de commande 
b12 = Button(onglet2, text = "décryptage", command=dechiffrementcesar)
b12.grid(row=3, column=2)

# pour afficher le résultat
e32 = Label(onglet2, text = "résultat du décryptage par Cesar")
e32.grid(row=4, column=1)
zt32 = Entry(onglet2, width=50)# saisie du texte
zt32.grid(row=4, column=2)


# pour saisir pour onglet 3#####################################################################################################
e13 = Label(onglet3, text = " Texte à crypté ")
e13.grid(row=1, column=1)
crypter = StringVar()# variable pour recevoir le texte saisi
zt13 = Entry(onglet3, width=50,textvariable = crypter)# saisie du texte
zt13.grid(row=1, column=2)
crypter.set("écrire le Texte à crypté ici")

# pour saisir le décalage
e23 = Label(onglet3, text = "valeur de la clé  ")
e23.grid(row=2, column=1)
zt23 = Entry(onglet3, width=50)# saisie du texte
zt23.grid(row=2, column=2)

# Bouton de commande 
b13 = Button(onglet3, text = "cryptage", command=chiffrementparcle)
b13.grid(row=3, column=2)

# pour afficher le résultat
e33 = Label(onglet3, text = "résultat du cryptage par cle")
e33.grid(row=4, column=1)
zt33 = Entry(onglet3, width=50)# saisie du texte
zt33.grid(row=4, column=2)


# pour saisir pour onglet 4#####################################################################################################
e14 = Label(onglet4, text = " Texte à crypté ")
e14.grid(row=1, column=1)
crypter = StringVar()# variable pour recevoir le texte saisi
zt14 = Entry(onglet4, width=50,textvariable = crypter)# Nous créons le widget zt14 , un champ de saisie ('champ de saisie'), et le lions à la onglet4 .
zt14.grid(row=1, column=2)
crypter.set("écrire le Texte à crypté ici")

# pour saisir le décalage
e24 = Label(onglet4, text = "valeur de la clé  ")
e24.grid(row=2, column=1)
zt24 = Entry(onglet4, width=50)# saisie du texte
zt24.grid(row=2, column=2)

# Bouton de commande 
b14 = Button(onglet4, text = "décryptage", command=dechiffrementparcle)
b14.grid(row=3, column=2)

# pour afficher le résultat
e34 = Label(onglet4, text = "résultat du décryptage par cle")
e34.grid(row=4, column=1)
zt34 = Entry(onglet4, width=50)# saisie du texte
zt34.grid(row=4, column=2)  

Fenetre.mainloop()## En utilisant .mainloop (), nous initions une boucle infinie pour exécuter notre fenêtre. Il restera actif, écoutant («attendant») un événement, 
#le traitant. La fenêtre restera active tant qu'elle n'est pas fermée (ou rencontre une erreur).
