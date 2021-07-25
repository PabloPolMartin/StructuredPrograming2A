#include <stdio.h>
#include<stdlib.h>

char user;
int age=18;

int main(){ 

    printf("Enter username: \n"); 
    scanf("%s", &user);

    printf("Enter your age: \n"); 
    scanf("%d", &age);

    if (age<18){
        printf("You are not old enough to access this page\n");
    }
    else{
        printf("Hello there!\n");
    }

    return 0;
}