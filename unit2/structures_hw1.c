#include <stdio.h>

typedef struct discos {

        char* BuscaUnaMujer;
        int* Romance;
        float* Aries;

        
}DISCOS ;

int main(){
    DISCOS LUISMI = {1998, 1991, 1993, "Discografia" };

    printf("BuscaUnaMujer: %f\n Romance: %f\n Aries: %f\n Los años de lanzamiento son %s son: %f\n", LUISMI.BuscaUnaMujer, LUISMI.Romance, LUISMI.Aries, (1998, 1991, 1993));
}