#include <stdio.h>
#include<stdlib.h>

int i;
float add=0;
float x=0;
float av=0;

int main(int argc, char* argv[]){
    
    for (i=1; i<argc; i++){ 
        x = atof(argv[i]);
        add += x;
        av = (add)/i;
    if (i==(argc-1)){
    printf("Average:%.3f\n", av);  
    }
   
    }

    return 0;
}

 