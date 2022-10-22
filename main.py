class People:
    def __init__(self, name, surname, company, position, email):
        self.name = name
        self.surname = surname
        self.company = company
        self.position = position
        self.email = email


    def show_employee_information(self):
        return f'{self.name} {self.surname} {self.company} {self.position} {self.email}'

customers1 = People('Tomasz', 'Madej', 'Starostwo Powiatowe w Puławach', 'kierownik','madtom@pulawy.powiat.pl')
customers2 = People('Anna', 'Koper', 'ZETO sp. z o.o.', 'kierownik','akoper@zeto.pl')
customers3 = People('Adrian', 'Olszak', 'VIM sp. k.', 'CEO','a.olszakm@vim.com')
customers4 = People('Joanna', 'Capała', 'Butik Joanna', 'CEO','biuro@butikjoanna.com.pl')
customers5 = People('Katarzyna', 'Cieślak', 'F.H ZŁOM', 'kadrowa','kadry@zlom.pulawy.pl')

customers =[]

customers.append(customers1.show_employee_information())
customers.append(customers2.show_employee_information())
customers.append(customers3.show_employee_information())
customers.append(customers4.show_employee_information())
customers.append(customers5.show_employee_information())

for i in customers:
    print(i)