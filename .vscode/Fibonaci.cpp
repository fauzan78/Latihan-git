#include <iostream>
using namespace std;
int main(){
    //Fibnaci adalah menambahkan nilai terakhir dengan nilai sebelumnya
    //Rumus nya Nilai_baru = nilai terakhir + nilai sebelumnya
    int nilai_baru;
    int nilai_1;
    int nilai_0;
    int n;
    cout << "Masukkan Pilihan Fibonaci = ";
    cin >> n;
    nilai_1 = 1;
    nilai_0 = 0;
    nilai_baru = nilai_1 + nilai_0;
    cout << nilai_baru << " ";
    for( int i = 1; i < n; i++){
        nilai_baru = nilai_1 + nilai_0;
        nilai_0 = nilai_1;
        nilai_1 = nilai_baru;
        cout << nilai_baru << " ";
    }
    cin.get();
    return 0;
}