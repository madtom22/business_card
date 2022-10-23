from faker import Faker
fake = Faker('pl_PL')

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
       super().__init__(name, surname, None, None, email)
       self.phone = phone

    def contact(self):
        return f'Wybieram numer prywatny {self.phone} i dzwonię do {self.name} {self.surname}'

    @property
    def len_name_surname(self):
        len_people = len(self.name) + len(self.surname) + 1
        return f'Długość imienia i nazwiska {self.name} {self.surname} łącznie ze spacją między nimi wynosilen: {len_people}'


class BusinessContact(People):
    def __init__(self, name, surname, company, position, business_phone ):
        super().__init__(name, surname, company, position, None)
        self.business_phone = business_phone
        
    def contact(self):
        return f'Wybieram numer służbowy {self.business_phone} i dzwonię do {self.name} {self.surname}'

    @property
    def len_name_surname(self):
        len_people = len(self.name) + len(self.surname) + 1
        return f'Długość imienia i nazwiska {self.name} {self.surname} łącznie ze spacją między nimi wynosilen: {len_people}'


customers1 = People(name='Tomasz', surname='Madej', company='Starostwo Powiatowe w Puławach', position='kierownik', email='madtom@pulawy.powiat.pl') # ten i poniższy zapis są równoznaczne
customers2 = People('Anna', 'Koper', 'ZETO sp. z o.o.', 'kierownik', 'akoper@zeto.pl') # ten i powyższy zapis są równoznaczne w przekazywaniu parametów do klasy
customers3 = People('Barbara', 'Olszak', 'VIM sp. k.', 'CEO', 'b.olszakm@vim.com')
customers4 = People('Joanna', 'Capała', 'Butik Joanna', 'CEO', 'biuro@butikjoanna.com.pl')
customers5 = People(fake.first_name(),fake.last_name(),fake.company(),fake.job(),fake.free_email())
customers6 = People(fake.first_name(),fake.last_name(),fake.company(),fake.job(),fake.free_email())
customers7 = People(fake.first_name(),fake.last_name(),fake.company(),fake.job(),fake.free_email())
customers8= People(fake.first_name(),fake.last_name(),fake.company(),fake.job(),fake.free_email())

customers9 = BaseContact('Barbara', 'Kruk', 'kruk@wp.pl', 988237722) # ten i poniższy zapis są równoznaczne
customers10 = BaseContact(name='Paweł', surname='Gębal', email='pawel33@poczte.onet.pl', phone=989343452) # ten i powyższy zapis są równoznaczne w przekazywaniu parametów do klasy
customers11 = BaseContact('Agnieszka', 'Pawelec', 'apawelec@wp.pl', 985555722)
customers12 = BaseContact('Jadwiga', 'Osiak', 'jadzia@poczte.onet.pl', 9678943452)
customers13= BaseContact(fake.first_name(),fake.last_name(),fake.free_email(),fake.phone_number())
customers14= BaseContact(fake.first_name(),fake.last_name(),fake.free_email(),fake.phone_number())
customers15= BaseContact(fake.first_name(),fake.last_name(),fake.free_email(), fake.phone_number())
customers16= BaseContact(fake.first_name(),fake.last_name(),fake.free_email(),fake.phone_number())

customers17 = BusinessContact('Barbara', 'Kruk','Starostwo', 'inspektor', 34437722)
customers18 = BusinessContact('Agnieszka', 'Pawelec', 'Poczta Polska', 'kierownik', 94443452)
customers19 = BusinessContact('Paweł', 'Pawlos', 'Wodociągi', 'magazynier', 66637722) # ten i poniższy zapis są równoznaczne
customers20 = BusinessContact(name='Paweł', surname='Gębal', company='VIXON', position='CEO', business_phone=989343452) # ten i powyższy zapis są równoznaczne w przekazywaniu parametów do klasy
customers21 = BusinessContact(fake.first_name(),fake.last_name(),fake.company(),fake.job(),fake.phone_number())
customers22 = BusinessContact(fake.first_name(),fake.last_name(),fake.company(),fake.job(),fake.phone_number())
customers23 = BusinessContact(fake.first_name(),fake.last_name(),fake.company(),fake.job(),fake.phone_number())
customers24 = BusinessContact(fake.first_name(),fake.last_name(),fake.company(),fake.job(),fake.phone_number())


customers =[customers1, customers2, customers3, customers4, customers5, customers7, customers6, customers7, customers8]
customers_base =[customers9, customers10, customers11, customers12, customers13, customers14, customers15, customers16]
customers_business =[customers17, customers18, customers19, customers20, customers21, customers22, customers23, customers24]

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
print('')

for i in customers_base:
    print(i.contact())
print('')

for i in customers_base:
    print(i.len_name_surname)
print('')

for i in customers_business:
    print(i.contact())
print('')

for i in customers_business:
    print(i.len_name_surname)
print('')