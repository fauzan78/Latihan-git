#include <iostream>
using namespace std;
int main(){
    float a,b;
    int pilihan;
    float hasil;
    cout << " 1. Perkalian \n 2. Pertambahan \n 3. Pengurangan \n 4. Pembagian \n" << endl;
    cout << "Masukkan Pilihan :";
    cin >> pilihan;
    cout << "Masukan Nilai pertama = ";
    cin >> a;
    cout << "Masukan Nilai kedua = ";
    cin >> b;
    switch (pilihan)
    {
    case 1 :
            hasil = a*b;
            cout << " Hasil = " << hasil << endl;
        break;
    case 2 :
            hasil = a + b;
            cout << " Hasil = " << hasil << endl;
           
        break;
    case 3 :
            hasil = a - b;
            cout << " Hasil = " << hasil << endl;
           
        break;
    case 4 :
            hasil = a / b;
            cout << " Hasil = " << hasil << endl;
            
        break;
    default:
         cout << "Masukkan Pilihan yang tepat" << endl;
        break;
    }
    
    cin.get();

}