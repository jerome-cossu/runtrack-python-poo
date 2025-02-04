class Student:
    def __init__(self, nom, prenom, numero_etudiant):
        self.__nom = nom
        self.__prenom = prenom
        self.__numero_etudiant = numero_etudiant
        self.__credits = 0

    def __student_eval(self):
        if self.__credits >= 90:
            return "Excellent"
        elif self.__credits >= 80:
            return "Très bien"
        elif self.__credits >= 70:
            return "Bien"
        elif self.__credits >= 60:
            return "Passable"
        else :
            return "Insuffisant"
        
    def add_credits(self, credits):
        if credits > 0:
            self.__credits += credits
            self.__niveau = self.__student_eval()
    
    def student_info(self):
        print(f"Nom = {self.__nom}")
        print(f"Prenom = {self.__prenom}")
        print(f"id = {self.__numero_etudiant}")
        print(f"Nombre de crédits = {self.__niveau}")

student1 = Student("John", "Doe", 145)

student1.add_credits(30)
student1.add_credits(20)
student1.add_credits(40)

student1.student_info()