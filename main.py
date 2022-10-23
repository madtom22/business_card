class People:
    def __init__(self, name, surname, company, position, email):
        self.name = name
        self.surname = surname
        self.company = company
        self.position = position
        self.email = email
        

    def show_customers_information(self):
        return f'Imię: {self.name} Nazwisko: {self.surname} Firma: {self.company} stanowisko: {self.position} e-mail: {self.email}'

    def show_customers_quick(self):
        return f'{self.name} {self.surname} {self.email}'

    def contact(self):
        return f'Kontaktuj się z {self.name} {self.surname} {self.position} {self.email}'

    @property
    def len_name_surname(self):
        len_people = len(self.name) + len(self.surname) + 1
        return f'Długość imienia i nazwiska {self.name} {self.surname} łącznie ze spacją między nimi wynosilen: {len_people}'
        
    
class BaseContact(People):
    def __init__(self, name, surname, email, phone):
        super().__init__(name, surname, email)
        self.phone = phone

    def contact(self):
        return f'Wybieram numer {self.phone} i dzwonię do {self.name} {self.surname}'


class BusinessContact(People):
    def __init__(self, position, company, business_phone ):
        super().__init__(company, position)
        self.business_phone = business_phone

    def contact(self):
        return f'Wybieram numer {self.business_phone} i dzwonię do {self.name} {self.surname}'


customers1 = People('Tomasz', 'Madej', 'Starostwo Powiatowe w Puławach', 'kierownik', 'madtom@pulawy.powiat.pl')
customers2 = People('Anna', 'Koper', 'ZETO sp. z o.o.', 'kierownik', 'akoper@zeto.pl')
customers3 = People('Barbara', 'Olszak', 'VIM sp. k.', 'CEO', 'b.olszakm@vim.com')
customers4 = People('Joanna', 'Capała', 'Butik Joanna', 'CEO', 'biuro@butikjoanna.com.pl')
customers5 = People('Katarzyna', 'Cieślak', 'F.H ZŁOM', 'kadrowa', 'kadry@zlom.pulawy.pl')

customers =[customers1, customers2, customers3, customers4, customers5]

by_name = sorted(customers, key=lambda people: people.name)
by_surname = sorted(customers, key=lambda people: people.surname)
by_email = sorted(customers, key=lambda people: people.email)

print('Sortowanie po imieniu: ')
for i in by_name:
    print(i.show_customers_quick())
print('')

print('Sortowanie po nazwisku: ')
for i in by_surname:
    print(i.show_customers_quick())
print('')

print('Sortowanie po emailu: ')
for i in by_email:
    print(i.show_customers_quick())
print('')

for i in customers:
    print(i.show_customers_information())
print('')

for i in customers:
    print(i.len_name_surname)
