#coding:utf-8

import os.path
import sqlite3
from Model import Etudiant 
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "../BDD.db")
class GestionEtudiant:
    def __init__(self):
        self.connection = sqlite3.connect(db_path)
        self.cursor=self.connection.cursor()
        
    def getEtudiantById(self):
        
        try:
            req="SELECT * FROM Etudiant where id={0}".format(int(input("l'id de l'etudiant que vous allez trouver  ")))
            self.cursor.execute(req)
            row=self.cursor.fetchone()
            e1=Etudiant(id1=row[0],nom1=row[1],prenom1=row[2],email1=row[3],password1=row[4])
            return e1
        except:
            print("s'il vous plait d'entrer un entier ")
        
    def addEtudiant(self,etudiant:Etudiant):
        self.connection.execute("INSERT INTO Etudiant (nom,prenom,email,password) VALUES ('{0}', '{1}', '{2}', '{3}')".format(etudiant.getNom(),etudiant.getPrenom(),etudiant.getEmail(),etudiant.getPassword()))
        self.connection.commit()
        print("l'ajout de l'etudiant a ete fait avec succes !")

    def getAllEtudiant(self):
        list1=[]
        req="SELECT * FROM Etudiant"
        self.cursor.execute(req)
        records = self.cursor.fetchall()
        for row in records:
            e=Etudiant(id1=row[0],nom1=row[1],prenom1=row[2],email1=row[3],password1=row[4])
            list1.append(e)
        print(list1)
        return list1
    def deleteEtudiantById(self):
        try:
            print("vous etes dans la methode de suppression d'un etudiant par id ")
            req = "delete from Etudiant where id={0}".format(int(input("entrez l'id de l'element que vous venez de supprimer!"))) 
            self.cursor.execute(req)  
            self.connection.commit() 
        except:
            print("s'il vous plai d'entrer un id valide (un entier )")
    def update(self,etudaint:Etudiant):
        print(etudaint)
        self.cursor.execute("UPDATE Etudiant SET nom ='{0}' , prenom = '{1}' , email = '{2}' , password = '{3}' where id = {4};".format(etudaint.getNom(), etudaint.getPrenom(), etudaint.getEmail(),etudaint.getPassword(),etudaint.getId()))
        self.connection.commit()

    

