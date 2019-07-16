#include<iostream>
#include<fstream>
#include<cmath>
using namespace std;


//definicion de las dos derivadas
//En X
double dvenx(float tiempo, double xx, double r12)
{
    double G = 1.9825*pow(10,-29);
    double M = 1.989*pow(10, 30);
    return (-G*M/pow(r12,3))*xx;
}
double dxenx(float tiempo,double xx, double vx){
    return vx;
}
//En Y
double dveny(float tiempo, double yy, double r12)
{
    double G = 1.982*pow(10,-29);
    double M = 1.989*pow(10, 30);
    return (-G*M/pow(r12,3))*yy;
}
double dxeny(float ti, double yy, double vy)
{
    return vy;
}

//Segundo Método:Leap frog
float rungekutta(double fin, double ini, int puntos)
{
    double dif= 0.01;
    double dt;
    //creacion de arreglos
    double x[puntos], y[puntos], vy[puntos], vx[puntos], tiem[puntos];
    double k1x,k2x,k3x,k4x,k1vx,k2vx,k3vx,k4vx,promex,promevx;
    double k1y,k2y,k3y,k4y,k1vy,k2vy,k3vy,k4vy,promey,promevy;
    //inicializacion con condiciones del enunciado
    x[0]=0.1163;
    y[0]=0.9772;
    vx[0]=-6.35;
    vy[0]=0.606;
    dt=(fin-ini)/puntos;
 
    for(int i=1;i<=puntos;i++)
    {
        //Pasos para X
        k1x=dxenx(tiem[i-1],x[i-1],vx[i-1]);
        k1vx=dvenx(tiem[i-1],x[i-1],vx[i-1]);
            
        k2x=dif*dxenx(tiem[i-1]+0.5*dif, x[i-1]+0.5*k1x,vx[i-1]+0.5*k1vx);
        k2vx=dif*dvenx(tiem[i-1]+0.5*dif, x[i-1]+0.5*k1x,vx[i-1]+0.5*k1x);
            
        k3x=dif*dxenx(tiem[i-1]+0.5*dif, x[i-1]+0.5*k2x,vx[i-1]+0.5*k2vx);
        k3vx=dif*dvenx(tiem[i-1]+0.5*dif,x[i-1]+0.5*k2x,vx[i-1]+0.5*k2x);
            
        k4x =dif*dxenx(tiem[i-1]+dif, x[i-1]+k3x, vx[i-1]+ k3vx);
        k4vx =dif*dvenx(tiem[i-1]+dif, x[i-1]+k3x, vx[i-1]+ k3x);
        
        //Pasos para Y
        k1y=dif*dxeny(tiem[i-1],y[i-1],vy[i-1]);
        k1vy=dif*dveny(tiem[i-1],y[i-1],vy[i-1]);
            
        k2y=dif*dxeny(tiem[i-1]+0.5*dif, x[i-1]+0.5*k1y,vy[i-1]+0.5*k1vy);
        k2vy=dif*dveny(tiem[i-1]+0.5*dif, x[i-1]+0.5*k1y,vy[i-1]+0.5*k1y);
            
        k3y=dif*dxeny(tiem[i-1]+0.5*dif, y[i-1]+0.5*k2y,vy[i-1]+0.5*k2vy);
        k3vy=dif*dveny(tiem[i-1]+0.5*dif,y[i-1]+0.5*k2y,vy[i-1]+0.5*k2y);
            
        k4y =dif*dxeny(tiem[i-1]+dif, y[i-1]+k3y, vy[i-1]+ k3vy);
        k4vy =dif*dveny(tiem[i-1]+dif, y[i-1]+k3y, vy[i-1]+ k3y);
        
        //Paso final de rungekutta
        promex=(1/6)*(k1x+2.0*k2x+2.0*k3x+k4x);
        promevx=(1/6)*(k1vx+2.0*k2vx+2.0*k3vx+k4vx);
            
        promey=(1/6)*(k1y+2.0*k2y+2.0*k3y+k4y);
        promevx=(1/6)*(k1vy+2.0*k2vy+2.0*k3vy+k4vy);
        tiem[i] = tiem[i-1] + dif;
        x[i] = x[i-1] + promex;
        y[i] = y[i-1] + promey;
        vx[i] = vx[i-1] + promevx;
        vy[i] = vy[i-1] + promevy;
    }
    
}
int main()
{
    leap_frog(20,0,1000);
    return 0;
}