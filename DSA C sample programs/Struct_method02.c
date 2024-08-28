/*ARRAY ACCED IN STRUCTURE , HOW POINTER STRUCTURE DEFINED 
Q. write a program to accept the n student details and print it*/
#include<stdio.h>
#include<stdlib.h>

struct student
{   char name[40];
    char usn[10];
	char branch[5];
    int marks[5]; 
	struct {int d,m,y;}DOB;
} *students; /*pointer to structure*/

void main()
{ int n,i,j;
  printf("Enter the number of students \n");
  scanf("%d",&n);
  students=(struct student *)calloc(n,sizeof(struct student));

for(i=0;i<n;i++)
{
	printf("Enter student %d details\n",i+1);
	printf("Name =  ");	scanf("%s",students[i].name );
	printf("USN =   ");	scanf("%s",students[i].usn );
	printf("branch= ");	scanf("%s",students[i].branch );
	printf("DOB ='dd-mm-yyyy'");scanf("%d-%d-%d",&students[i].DOB.d,&students[i].DOB.m,&students[i].DOB.y);	
	printf("enter 5 sub Marks = ");
	for(j=0;j<5;j++)
	{	
	scanf("%d",&students[i].marks[j]);	
	}/*for marks*/		
}/*for*/

/*scanf complete*/

for(i=0;i<n;i++)
{
printf(" student %d details \n",i+1);
printf("Name = %s\n",students[i].name );
printf("USN = %s\n",students[i].usn );	
printf("branch= %s\n",students[i].branch );	
printf("DOB = %02d-%02d-%04d \n",students[i].DOB.d,students[i].DOB.m,students[i].DOB.y);		
for(j=1;j<6;j++)
{	printf("Marks of sub %d = %d\n",j,students[i].marks[j]);	
}/*for marks*/

}/*for*/
/*printf complete*/

free(students);/*free*/


}  /*void*/