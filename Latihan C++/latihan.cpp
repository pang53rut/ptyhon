#include<iostream>
using namespace std;

int main() {
    int harga = 15000;
    int *indeks;
    indeks = &harga;
    harga = 17000;
    int diskon = 35;
    cout << "Harga sebelum diskon adalah Rp " << harga << endl;
    cout << "Hello World " << *indeks << endl;
    cout << indeks;
    return 0;
}