#include <stdio.h>
#include <stdlib.h>

typedef struct robot
{
    char* name;
    char* type;
    float height;
    float weight;
    int degreesOfFreedom;
    void (*sayHelloToRobot)(struct robot);

}ROBOT;

void sayHelloToRobot(ROBOT a_robot){
    printf( "%s", "hello Tiago", a_robot.name);
    scanf("%s", a_robot.name);
}
