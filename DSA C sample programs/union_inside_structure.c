#include <stdio.h> 
struct student 
{ 
union 
{ 
char name[20]; 
int roll_no; 
}; 
int marks; 
}; 
int main() 
{ 
struct student stud; 
char ch; 
printf("\n Do you want to enter the name? (Y or N): "); 
scanf(“%c”,&ch); 
if(ch= ='Y') 
{ 
printf("\n Enter the name: "); 
gets(stud.name); 
} 
else 
{ 
printf("\n Enter the roll number: "); 
scanf("%d", &stud.roll_no); 
} 
printf("\n Enter the marks: "); 
scanf("%d", &stud.marks); 
}