/*Write a program to implement the stack operation push, pop and display*/


#include <stdio.h>
#include<stdlib.h>
#define MAX 10
int stack[MAX];
int top=-1;
 
void push(int x);
int pop();
void display();
 
 void main()
 { int ch,x,i;
	 do{printf("stack options:\n1.Push\n2.Pop\n3.Display\n4.Exit\n");
 printf("Enter choice");
 scanf("%d",&ch);
 
 switch(ch)
 {
	case 1:printf("Enter the data..");	
		   scanf("%d",&x);
		   push(x);
           break;
	case 2:x = pop();
		   printf("%d poped out",x);
		   break;
	case 3:display();
	break;

 }/*switch*/
 
 }while(ch<4);
 
if(ch==4)
{exit(0);
}
 }/*main */
 
 
 
 void push(int x)
 {   if (top == MAX - 1) {
        printf("Stack is full\n");
        return;
    }
    top ++;
    stack[top] = x;
} /* push*/


int pop()
{
	if (top == -1) {
        printf("Stack is empty\n");
        return -1;
    }
	int x;
	x = stack[top];
	top--;
}/*pop*/

void display()
{
	if(top==-1)
	{ printf("stack is empty");
      return;
	}
	
	for(int i=top;i>=0;i--)
	{
		printf("%d",stack[i]);
	}
	
}/*display*/