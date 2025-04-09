#include<iostream> 
using namespace std;

int main() 
{ 
int i, j; 
cout<<"Enter two number:" ; 
cin>>i>>j; 
cout<<i<<" AND "<<j<<" is "<<(i&&j)<<'\n'; 
cout<<i<<" OR "<<j<<" is "<<(i||j)<<'\n'; 
cout<<" NOT " <<j<<" is "<<(!i)<<'\n'; 
return 0; 
} 