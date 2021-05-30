#coding:utf-8
from Model import Etudiant
from Controler import GestionEtudiant
""" 
    creation et remplissage des attribut d un objet de type Etudiant 
"""
etudiant1=Etudiant (id1=5)


etudiant1.setNom(input("Quel est votre nom ? "))
etudiant1.setPrenom(input("Quel est votre prenom ? "))
etudiant1.setEmail(input("Quel est votre email ? "))
etudiant1.setPassword(input("Quel est votre passwoed ? "))


""" 
    insertion de l'objet dans la table Etudiant de la base BDD
"""
g=GestionEtudiant()
g.getAllEtudiant()
#g.deleteEtudiantById()
g.update(etudiant1)
g.getAllEtudiant()

#g.getEtudiantById()