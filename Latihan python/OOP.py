class Person:
    def __init__(self, name, age,address):
        self.nama = name
        self.umur = age
        self.alamat = address

    def myfunc(self):
        print("Hello nama saya adalah " + self.nama)
        
p1 = Person("jhon", 39,"Jakarta")
p1.myfunc()

print("Nama     ",p1.nama)
print("Umur     ",p1.umur)
print("Alamat   ",p1.alamat)