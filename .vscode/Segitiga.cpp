#include <iostream>
using namespace std;
int main(){
    int large;
    cout << "masukkan jumlah panjang = ";
    cin >> large;
    cout << "pola ke 1 \n" << endl;
    for ( int i = 1; i <= large; i++){
        for ( int j = 1; j <= i; j++){
            cout << "*";
        }
        cout << " " << endl;
    }
    cout << "pola ke 2 \n" << endl;
    for ( int i = 1; i <= large; i++){
        for ( int j = large; j >= i; j--){
            cout << "*";
        }
        cout << " " << endl;
    }
    cout << "pola ke 3 \n" << endl;
    for ( int i = 1; i <= large; i++){
        for ( int j = 1; j < i; j++){
            cout << " ";
        }
        for ( int k = large; k >= i; k--){
            cout << "*";
        }
        cout << " " << endl;
    }
    cout << "pola ke 4 \n" << endl;
    for ( int i = 1; i <= large; i++){
        for ( int j = large; j >= i; j--){
            cout << " ";
        }
        for ( int k = 1; k <= i; k++){
            cout << "*";
        }
        cout << " " << endl;
    }
    cout << "pola ke 5 \n" << endl;
    for ( int i = 1; i <= large; i++){
        for ( int j = large; j >= i; j--){
            cout << " ";
        }
        for ( int k = 1; k <= (2*i - 1); k++){
            cout << "*";
        }
        cout << " " << endl;
    }
    cout << "pola ke 6 \n" << endl;
    for ( int i = 1; i <= large; i++){
        for ( int j = 1; j < i; j++){
            cout << " ";
        }
        for ( int k = large; k >= (2*i - large) ; k--){
            cout << "*";
        }
        cout << " " << endl;
    }
    cout << "pola ke 7 \n" << endl;
    for ( int i = 1; i <= large; i++){
        for ( int j = large; j >= i; j--){
            cout << " ";
        }
        for ( int k = 1; k <= (2*i - 1); k++){
            cout << "*";
        }
        cout << endl;
    }
    for ( int i = 1; i <= large - 1; i++){
        for ( int j = 1; j <= i + 1; j++){
            cout << " ";
        }
         for (int k = 1; k <= (2 * (large - i) - 1); k++) {
            cout << "*";
        }
        cout << " " << endl;
    }

    cin.get();
    return 0;
}
