#include <iostream>
#include <cstdlib>
using namespace std;
int main(){
    char lanjut;
    while(true){
        cout << "Mau main dadu ??";
        cin >> lanjut;
        if(lanjut == 'y'){
            cout << 1 + (rand() % 6) << endl;
        }
        else if(lanjut == 'n'){
            cout << "Oke terimakasih" << endl;
        }
        else {
            cout << "masukkan yang bener kak!!" << endl;
        }
    }
    cin.get();
    return 0;
}
