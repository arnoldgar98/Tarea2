#include<iostream>
#include<fstream>
#include<cmath>
using namespace std;


//definicion de las dos derivadas
//En X
double dvenx(float tiempo, float xx, float r12)
{
    double G = 1.9825*pow(10,-29);
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

//Segundo Método:Leap frog
float leap_frog(double fin, double ini, int puntos)
{
    
    double dif;
    dif= 0.01;
    //creacion de arreglos
    double dt;
    double x[puntos],y[puntos],vy[puntos],vx[puntos],tiem[puntos],r12[puntos];
    //inicializacion con condiciones del enunciado
    x[0]=0.1163;
    y[0]=0.9772;
    vx[0]=-6.35;
    vy[0]=0.606;
    //inicializar la distancia del radio con condicion inicial
    r12[0]=sqrt(pow(y[0],2) + pow(x[0],2));
    //generacion del paso 1 leap backwards
    x[1]=x[0]+ dif*dxenx(tiem[0],x[0],vx[0]);
    y[1]=y[0]+ dif*dxeny(tiem[0],y[0],vy[0]);
    vx[1]=vx[0]+ dif*dvenx(tiem[0],x[0],r12[0]);
    vy[1]=vy[0]+ dif*dveny(tiem[0],y[0],r12[0]);
    r12[1] = sqrt(pow(y[1],2) + pow(x[1],2));
    //desde 2, porque ya usamos la condicion inicial
    for(int i=2; i<puntos;i++)
    {
        //avance del tiempo
        tiem[i]=tiem[i-1]+dt;
        //retroalimentacion de las variables al mismo tiempo
        vx[i]=vx[i-2]+ dif*2*dvenx(tiem[i-1],x[i-1],r12[i-1]);
        vy[i]=vy[i-2]+ dif*2*dveny(tiem[i-1],x[i-1],r12[i-1]);
        x[i]=x[i-2]+ dif*2*dxenx(tiem[i-1],x[i-1],vx[i-1]);
        y[i]=y[i-2]+ dif*2*dxeny(tiem[i-1],x[i-1],vy[i-1]);
        
        r12[i] = sqrt(pow(y[i],2) + pow(x[i],2));
        
    } 
    ofstream outfile2;
    outfile2.open("datos2.dat");
    for(int i=0;i<puntos;i++)
    {
        outfile2<<x[i]<<";"<<y[i]<<endl;
    }
    outfile2.close();
}
int main()
{
    leap_frog(20,0,1000);
    return 0;
}