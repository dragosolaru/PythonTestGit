
class Angajati:

  prema = 0
  numar_angajati = 0

  def __init__(self, nume, prenume, salar):
    self.nume = nume
    self.prenume = prenume
    self.salar = salar
    Angajati.numar_angajati += 1

  def da_prema(self, prema):
    self.salar = self.salar + self.salar * prema / 100
    return self.salar

  def afiseaza_angajat(self):
    return '{} {} {}'.format(self.prenume, self.nume, self.salar)

  def afiseaza_numar_angajati(self):
    return self.numar_angajati

  def concediaza(self):
    numar_angajati_actual = self.numar_angajati
    Angajati.numar_angajati -= 1
    return 'Numarul angajatilor a fost {}, iar acum este {}'.format(numar_angajati_actual, self.numar_angajati)


angajat1 = Angajati("Olaru", "Dragos", 1000)
angajat2 = Angajati("test", "testut", 2000)

angajat1.da_prema(5)
print (angajat1.afiseaza_angajat())

angajat2.da_prema(20)
print (angajat2.afiseaza_angajat())

angajat3 = Angajati("costel", "lover", 2500)


print (Angajati.numar_angajati)

print (Angajati.concediaza(angajat3))
