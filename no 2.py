class Cat:
    def intro(self):
        print("type of cats.")
    def type(self):
        print("banyak sekali tipe bulunya.")
class anggora (Cat):
    def type (self):
        print("anggora memiliki bulu yang panjang")
class british_Shorthair(Cat):
     def type(self):
          print("british short hair memiliki bulu yang pendek")
            
obj_Cat = Cat()
obj_angr = anggora()
obj_bsh = british_Shorthair()
obj_Cat.intro()
obj_Cat.type()
obj_angr.intro()
obj_angr.type
obj_bsh.intro()
obj_bsh.type()