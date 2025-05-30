class Liza:  
    def __init__(self, first_name=None, last_name=None, birth_year=None):  
        self.first_name = first_name  
        self.last_name = last_name  
        self.birth_year = birth_year  

    def get_year(self):  
        if self.birth_year is None:  
            return "Рік народження не вказано"  

        current_year = 2025  
        age = current_year - self.birth_year  

        if 15 <= age < 17:  
            return "перший курс"  
        elif 17 <= age < 18:  
            return "другий курс"  
        elif 18 <= age < 19:  
            return "третій курс"  
        elif 19 <= age < 20:  
            return "четвертий курс"  
        else:  
            return "не студент"  

    def get_info(self):  
        if self.first_name and self.last_name:  
            return f"{self.first_name} {self.last_name} – {self.get_year()}."  
        else:  
            return "Дані не вказані"
         
student1 = Liza("Софія", "Олександрівна", 2009)  
student2 = Liza("Оля", "Іванівна", 2007)  
student3 = Liza("Володимир")
student4 = Liza("Катерина", "Сергіївна", 2000)

print(student1.get_info())  
print(student2.get_info())  
print(student3.get_info())  
print(student4.get_info())
