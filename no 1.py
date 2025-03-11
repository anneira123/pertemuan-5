class Cat:
    def jenis(self):
        print("anggora")
    def nama (self):
        print("cimmy")
class Dog:
    def jenis(self):
        print("cihuahua")
    def nama(self):
        print("heli")
cat = Cat()
dog = Dog()
for animals in (cat,dog):
    animals.jenis()
    animals.nama()