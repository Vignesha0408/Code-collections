#include<stdio.h>

union employee
{
    int age;
    int usn;
}p1;

void main()
{
    p1.age=15;
    p1.usn=423060;

    printf("%d,%d",p1.age,p1.usn);
}