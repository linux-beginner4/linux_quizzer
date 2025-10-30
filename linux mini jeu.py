#on importe le module random pour choisir les questions de façon aléatoire
import random

#on crée un dictionnaire avec toutes nos questions et reponses
dico={
    "Afficher le chemin complet du repertoire courant" : "pwd",
    "lister les fichiers et dossiers dans le repertoire courant":"ls",
    "lister detaillé avec permissions, proprietaires, dates" : "ls -l",
    "changer de repertoire courant" : "cd",
    "creer un dossier vide" : "mkdir",
    "copier un fichier " : "cp",
    "deplacer ou renommer un fichier ou un dossier" : "mv",
    "supprimer un fichier" : "rm",
    "supprimer un dossier et son contenu" : "rm -r",
    "lister les fichiers cachés" :"ls -a" ,
    "copier un dossier et son contenu" : "cp -r",
}

#on crée une fonction mini_quiz avec les parametres nb_questions=5 pour choisir le nombre de questions

def mini_quiz(nb_questions=5):
    #on crée la variable texte avec laquelle on associe *bienvenue sur votre jeu: linux quizzer* qui sera
    texte= "🎮 bienvenue sur votre jeu: linux quizzer 🎮"

    #on associe la valeur 50 à la variable largeur qui est une valeur virtuelle pour centrer le texte avec: texte.center
    largeur= 50
    print(texte.center(largeur))

    #on initialise la variable score à 0
    score = 0
    questions = random.sample (list(dico.items()),nb_questions)

    #on utilise la boucle for pour pouvoir affecter les questions à plusieurs conditions
    for question,answer in questions:

        "  print(\n👉+question) est utilisé pour afficher les questions et le \n permet de mettre chaque question a la ligne"
        print("\n👉"+question)

        #on utilise la boucle while true pour dire que tant que c'est vrai on execute les instructions qui vont suivre
        while True :

            #on attribut a la variable user_answer input pour que l'utilisateur puisse entrer sa reponse #
            #NB: .strip() sert à supprimer les espaces inutiles
            user_answer = input("votre reponse:").strip()

            #on met une condition avec if pour que l'utilisateur entre obligatoirement une reponse
            if user_answer == "":

                #si l'utilisation n'entre rien du tout ce message s'affiche
                print ("veuillez entrer une reponse")

                #on ajoute else pour prendre en compte le cas contraire et break sert a sortir de la boucle
            else:
                    break

            #on ajoute une condition pour qu'un message s'affiche quand la reponse de l'utilisateur est juste
        if user_answer == answer:
            print("correct✅")

            #lorsque la reponse est correcte on ajoute 1 au score du joueur
            score += 1

            #on affiche un message lorsque la reponse de l'utilisateur est incorrect
        else:
            print("incorrect❌. La bonne reponse était:" +answer)

        #on crée une variable score_final qui va recevoir notre score final
        score_final = score

        #on met une condition pour afficher un message si le score de l'utilisateur est superieur ou egale à 3
    if score >= 3:
        print(score)
        print("🎉félicitation votre score final:", score)

        #on met une autre condition pour afficher un message si le score est inferieur à 3
    else:
        print(score)
        print("☠️vous n'avez pas reussis le test")


#on appel notre fonction mini_quiz
mini_quiz()


