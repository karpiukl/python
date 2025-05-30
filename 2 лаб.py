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


class Lizka(Liza):
    def __init__(self, first_name=None, last_name=None, birth_year=None,
                 specialty=None, rating=None, group=None):
        super().__init__(first_name, last_name, birth_year)
        self.specialty = specialty
        self.rating = rating
        self.group = group

    def get_extended_info(self):
        base_info = self.get_info()
        extra_info = f" Спеціальність: {self.specialty}, Група: {self.group}."
        return base_info + extra_info

    def _calculate_scholarship(self):
        if self.rating is None:
            return "Немає даних про рейтинг"
        elif self.rating >= 90:
            return "Підвищена стипендія"
        elif self.rating >= 70:
            return "Звичайна стипендія"
        else:
            return "Стипендія не призначена"


student = Lizka("Рома", "Новак", 2007, "ІСТ", 88, "ІСТ-21")

print(student.get_extended_info())
print(student._calculate_scholarship())
print(student.get_year())
