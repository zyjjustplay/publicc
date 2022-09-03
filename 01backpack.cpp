#include<iostream>
#include<cstdio>
#define ll long long
using namespace std;
int n,m,i,j,w[35],c[35],f[35][205];
int main(){
    scanf("%d%d",&m,&n);
    for(i=1;i<=n;i++) scanf("%d%d",&w[i],&c[i]);
    for(i=1;i<=n;i++){
        for(j=1;j<=m;j++)f[i][j]=max(f[i-1][j-w[i]]+c[i],f[i-1][j]);
    }
    cout<<f[n][m];
    system("pause");
    return 0;
}