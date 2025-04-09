// this solves the area of a circle 
#include<iostream> 
#define PI3.1415927
using namespace std; 
 
double Area (double r) 
{ 
return(PI3*r*r); 
} 
double Circumference(double r) 
{ 
return(2*PI3*r*r); 
} 


int main( ) 
{ 
double radius,a,c; 
cout<<"Enter radius: "; 
cin>>radius; 
a=Area(radius); 
c=Circumference(radius); 
cout<<"The circumference " 
<<"of the circle is "<<c<<endl; 
cout<<"The area of " 
<<"the circle is "<<a<<endl; 

return 0; 
} 
