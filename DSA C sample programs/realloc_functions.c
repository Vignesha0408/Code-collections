#include<stdio.h>
#include<stdlib.h>
void main()
{
	int n,*ptr,i,j,k,x,l;
	printf("Enter the size of array\n");
	scanf("%d",&n);
	ptr= (int * )calloc(n,sizeof(int));
	x=n;
	printf("Enter the %d elements\n",n);
	for(i=0;i<n;i++)
		scanf("%d",ptr+i);
	printf("Elements are\n");
	for (j=0;j<n;j++)
		printf("%d\n",*(ptr+j));
	
	printf("Enter the new size of array\n");
	scanf("%d",&n);
	ptr = (int *)realloc(ptr,n*sizeof(int));
	printf("Enter the %d more elements\n",n-x);
	for(k=x;k<n;k++)
		scanf("%d",ptr+k);
	printf("Elements are after updated\n");
	for(l=0;l<n;l++)
		printf("%d\n",*(ptr+l));
	
}/*main*/