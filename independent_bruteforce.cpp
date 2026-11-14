#include <bits/stdc++.h>
using namespace std;
int main(){for(int n=1;n<=11;n++){vector<int> a(n);iota(a.begin(),a.end(),1); vector<long long>c(n+1),b(n+1);do{bool good=true;int occ=0;for(int i=0;i+2<n;i++){int x=a[i],y=a[i+1],z=a[i+2];if((x<y&&y<z)||(x<z&&z<y)||(y<z&&z<x)){good=false;break;}if(x>y&&y>z)occ++;}if(good){c[a.back()]++;b[a.back()]+=occ;}}while(next_permutation(a.begin(),a.end()));cout<<n<<" C";for(int k=1;k<=n;k++)cout<<" "<<c[k];cout<<" B";for(int k=1;k<=n;k++)cout<<" "<<b[k];cout<<"\n";}}
