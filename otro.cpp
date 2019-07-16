#include<iostream>
#include<fstream>
#include<math.h>
using namespace std;


//definicion de las dos derivadas
//En X
double dvenx(float tiempo, float xx, float r12)
{
    double G = 1.982*pow(10,-29);
    double M = 1.989*pow(10, 30);
    return (-G*M/pow(r12,3))*xx;
}
double dxenx(float tiempo,float xx, float vx){
    return vx;
}
//En Y
double dveny(float tiempo, float yy, float r12)
{
    double G = 1.982*pow(10,-29);
    double M = 1.989*pow(10, 30);
    return (-G*M/pow(r12,3))*yy;
}
double dxeny(float ti, float yy, float vy)
{
    return vy;
}

//primer método: Euler
ofstream outfile;
float euler(int fin, int ini, int puntos)
{
    outfile.open("datos.dat");
    //creacion de arreglos
    double dt;
    float dif;
    dif= 0.01;
    cout<<fin<<endl;
    cout<<ini<<endl;
    cout<<puntos<<endl;
    cout<<dif<<endl;
    float x[puntos], y[puntos], vy[puntos], vx[puntos], tiem[puntos],r12[puntos];
    //inicializar con condiciones del enunciado
    x[0]=0.1163;
    y[0]=0.9772;
    vx[0]=-6.35;
    vy[0]=0.606;
    //inicializar la distancia del radio con condicion inicial
    r12[0]=sqrt(pow(y[0],2) + pow(x[0],2));
    //desde 1, porque ya usamos la condicion inicial
    for(int i=1; i<puntos;i++)
    {
        //avance del tiempo
        tiem[i]=tiem[i-1]+dt;
        //retroalimentacion de las variables al mismo tiempo
        x[i]=x[i-1]+ dif*(dxenx(tiem[i-1],x[i-1],vx[i-1]));
        y[i]=y[i-1]+ dif*(dxeny(tiem[i-1],y[i-1],vy[i-1]));
        r12[i] = sqrt(pow(y[i],2) + pow(x[i],2));
        vx[i]=vx[i-1]+ dif*(dvenx(tiem[i-1],x[i-1],r12[i-1]));
        vy[i]=vy[i-1]+ dif*(dveny(tiem[i-1],y[i-1],r12[i-1]));
    }    
    for(int i=0;i<puntos;i++)
    {
        outfile<<x[i]<<";"<<y[i]<<";"<<vx[i]<<";"<<vy[i]<<";"<<tiem[i]<<endl;
    }
    outfile.close();
        
        
}
int main()
{
    euler(1,0,100);
    return 0;
}