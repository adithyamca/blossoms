#include <stdio.h>
 int main()
{
 int i,n,a[50];
 printf("\n\n To read & dispaly element of an array\n");
 printf("\n Enter the size of an array:");
 scanf("%d",&n);
 printf("\n n Enter the element:");
 for(i=0;i<n;i++)
{
 	scanf("%d",&a[i]);
}

 printf("\n Elements of array are:\n");
 for(i=0; i<n; i++)
   {
    	printf("%d",a[i]);
   }
return(0);
}

