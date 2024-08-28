/*write a program to accept n integers from console and print the sum of an array use 
dynamically allocated memory */
#include<stdio.h>
#include<stdlib.h>
void main()
{ int n,*q,i,sum=0,j; 
printf("Enter ths size of array \n");
scanf("%d",&n);
q=(int *)calloc(n,sizeof(int));
printf("Enter the elements \n");
for(i=0;i<n;i++)
{
	scanf("%d",q+i);
}/*for*/

	for(j=0;j<n;j++)
	{
		sum= sum+ *(q+j);
	}/* for */
printf("sum of an array is %d",sum);
free(q);

}/* main*/