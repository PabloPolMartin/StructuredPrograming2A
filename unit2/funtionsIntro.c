#include <stdio.h>
int myNumber = 3;
float myFloat = 3.1416;
char myString[255] = "Hola mundo";


// primer metodo para funciones

//Declarar y definirla
void sayHello( char message[] ){
    printf( "%s\n", message );
}

// segundo metodo para funciones

//1-. Declaro
void sayMyName( char message[] );

int main( ){
    sayHello( "Hello world" );
    sayMyName( "Luis" );
    return 0;
}

// Segundo metodo para funciones
//2-. Definimos
void sayMyName( char message [] ){
    printf( "%s\n", message );
}