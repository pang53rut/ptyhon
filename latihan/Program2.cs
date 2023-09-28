using System;

class Program
{
    static void Main()
    {
        Console.WriteLine("Program Penjumlahan Dua Angka");
        
        // Meminta pengguna untuk memasukkan angka pertama
        Console.Write("Masukkan angka pertama: ");
        string inputAngka1 = Console.ReadLine();
        
        // Meminta pengguna untuk memasukkan angka kedua
        Console.Write("Masukkan angka kedua: ");
        string inputAngka2 = Console.ReadLine();
        
        // Mengonversi input pengguna menjadi bilangan bulat
        int angka1 = int.Parse(inputAngka1);
        int angka2 = int.Parse(inputAngka2);
        
        // Menghitung jumlah kedua angka
        int jumlah = angka1 + angka2;
        
        // Menampilkan hasilnya
        Console.WriteLine($"Hasil penjumlahan {angka1} dan {angka2} adalah {jumlah}");
    }
}
