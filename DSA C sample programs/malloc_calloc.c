/*werite a program to accept n integers from console and print 
use dynamically allocated memory space */

#include<stdio.h>
#include<stdlib.h>
void main()
{ 
int n,*p1,*p2;
printf("enter size");
scanf("%d",&n);

p1=(int *)malloc(n*sizeof(int));
p2=(int *)calloc(n,sizeof(int));

printf("enter the %d elements ",n);
for(int i=0;i<n;i++)
{
	scanf("%d",p1+i);
}/*for*/

printf("enter the %d elements ",n);
for(int i=0;i<n;i++)
{
	scanf("%d",p2+i);
}/*for*/	



printf("memory allocated using malloc",n);
for(int i=0;i<n;i++)
{
	printf("%d ",*(p1+i));
}/*for*/

printf("memory allocated using calloc",n);
for(int i=0;i<n;i++)
{
	printf("%d ",*(p2+i));
}/*for*/
}/* main*/
