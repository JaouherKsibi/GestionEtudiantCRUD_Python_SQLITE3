#coding:utf-8
class Etudiant:
    def __init__(self,id1=0,nom1="",prenom1="",email1="",password1=""):
        self.__id=id1
        self.__nom=nom1
        self.__prenom=prenom1
        self.__email=email1
        self.__password=password1
    def getId(self):
        return self.__id
    def getNom(self):
        return self.__nom
    def getPrenom(self):
        return self.__prenom
    def getEmail(self):
        return self.__email
    def getPassword(self):
        return self.__password
    def setId(self,id):
        self.__id= id
    def setNom(self,nom):
        self.__nom=nom
    def setPrenom(self,prenom):
        self.__prenom=prenom
    def setEmail(self,email):
        self.__email=email
    def setPassword(self,password):
        self.__password=password
    def __str__(self):
        return "Etudiant[id="+str(self.__id)+",nom="+self.__nom+",prenom="+self.__prenom+",email="+self.__email+",password="+self.__password+"]"
    def __repr__(self):
        return str(self)