#include <stdio.h>
#include <string.h>
#include "./folderTest/utils.h"


int main(int argc, char** argv){

     int otroInt=9;

    UTILS myStructC={1, ShowIntAdress, ShowIntValueAdress, modifyVariablesAddress};
    printf("myInt: %d. &myStructC:%p\n", myStructC.myInt, &myStructC);
    UTILS* myStructP=&myStructC;
    printf("myInt: %d\n", (*myStructP).myInt);

    printf("////////\n");
    myStructC.ShowIntAdress(&otroInt);
    printf("////////\n");
    
    return 0;
}