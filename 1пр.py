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

        if 15 <= age <= 16:  
            return "1 курс"  
        elif 16 <= age <= 17:  
            return "2 курс"  
        elif 17 <= age <= 18:  
            return "3 курс"  
        elif 18 <= age <= 19:  
            return "4 курс"  
        else:  
            return "Не студент"  

    def get_name_list(self):  
        return [self.first_name, self.last_name]  

  
student1 = Liza("Софія", "Олександрівна", 2009)  
student2 = Liza("Оля", "Іванівна", 2007)  
student3 = Liza()   
 
print(student1.get_year())   
print(student2.get_year()) 
print(student3.get_year()) 

print(student1.get_name_list())  
print(student2.get_name_list()) 
print(student3.get_name_list())  
