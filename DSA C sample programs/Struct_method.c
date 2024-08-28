#include<stdio.h>

struct student
{   char name[40];
    int usn;
    int age;
    int marks; 
};

void main()
{
struct student s1,s2;

s1.usn= 423060;
s1.age = 18;
s1.marks= 100;

s2.usn= 423007;
s2.age = 18;
s2.marks= 100;

printf(" \n usn = %d \n age = %d\n marks %d\n usn = %d\n age = %d\n marks %d",s1.usn,s1.age,s1.marks,s2.usn,s2.age,s2.marks);
}  /*void*/