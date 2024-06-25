//Ordenamiento de un Array: 
//Escribir un programa que ordene un array de enteros utilizando ¡Pero hazlo en C++! :)

#include <iostream>
#include <algorithm>

using namespace std;


int main(){
    int numeros [5] = {1, 4, 6, 3, 2};
    
    cout<<"Arreglo original: "<< endl;
        for (int i=0; i<5;i++) // bucle for que recorre el arreglo 
        cout<<numeros[i]<<" "; //imprime en consola todos los elementos seguido por un espacio " "
        cout<<endl; //salto de linea
    

    sort(numeros, numeros+5); //funcion sort para ordenar en un rango de elementos desde numeros hasta numeros+5

    cout<<"Arreglo ordenado"<<endl;
        for (int i=0; i<5; i++) //bucle for que recorre e imprime el arreglo ordenado
        cout<<numeros[i]<< " ";
        cout<<endl;




    return 0;
}