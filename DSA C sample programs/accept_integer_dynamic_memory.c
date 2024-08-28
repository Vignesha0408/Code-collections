/*werite a program to accept n integers from console and print 
use dynamically allocated memory space */

#include<stdio.h>
#include<stdlib.h>
void main()
{ 
int n,*p;
printf("enter size");
scanf("%d",&n);
p=(int *)malloc(n*sizeof(int));
printf("enter the %d elements ",n);
for(int i=0;i<n;i++)
{
	scanf("%d",p+i);
}/*for*/	

for(int i=0;i<n;i++)
{
	printf("%d ",*(p+i));
}/*for*/

}/* main*/
