#include<iostream>
#include<fstream>
using namespace std;


//definicion de las dos derivadas
//En X
double dvenx(float tiempo, float xx, float vx)
{
    double G = 6.674*pow(10, -11);
    double M = 1.989*pow(10, 30);
    //Unidades astronomicas
    double r12= 1;
    return (-G*M/r12)*0.1163;
}
double dxenx(float tiempo,float xx, float vx){
    return vx;
}
//En Y
double dveny(float tiempo, float yy, float vy)
{
    double G = 6.674*pow(10, -11);
    double M = 1.989*pow(10, 30);
    //Unidades astronomicas
    double r12= 1;
    return (-G*M/r12)*0.9772;
}
double dxeny(float ti, float yy, float vy)
{
    return vy;
}

//primer método: Euler

float euler(int fin, int ini, int puntos)
{
    //creacion de arreglos
    double dif= 0.01;
    float x[puntos], y[puntos], vy[puntos], vx[puntos], tiem[puntos];
    //inicializar con condiciones del enunciado
    x[0]=0.1163;
    y[0]=0.9772;
    vx[0]=-6.35;
    vy[0]=0.606;
    dt=(fin-ini)/puntos;
    //desde 1, porque ya usamos la condicion inicial
    for(int i=1; i<puntos;i++)
    {
        //avance del tiempo
        tiem[i]=tiem[i-1]+dt;
        //retroalimentacion de las variables al mismo tiempo
        x[i]=x[i-1]+ dif*(dxenx(tiem[i-1],x[i-1],vx[i-1]));
        y[i]=y[i-1]+ dif*(dyenx(tiem[i-1],x[i-1],vy[i-1]));
        vx[i]=vx[i-1]+ dif*(dvenx(tiem[i-1],x[i-1],vx[i-1]));
        vy[i]=vy[i-1]+ dif*(dveny(tiem[i-1],x[i-1],vx[i-1]));
    }           
}

//Segundo Método:Leap frog
float leap_frog(int fin, int ini, int puntos)
{
    double dif= 0.01;
    //creacion de arreglos
    float x[puntos], y[puntos], vy[puntos], vx[puntos], tiem[puntos];
    //inicializacion con condiciones del enunciado
    x[0]=0.1163;
    y[0]=0.9772;
    vx[0]=-6.35;
    vy[0]=0.606;
    dt=(fin-ini)/puntos;
    //desde 1, porque ya usamos la condicion inicial
    for(int i=1; i<puntos;i++)
    {
        //avance del tiempo
        tiem[i]=tiem[i-1]+dt;
        //retroalimentacion de las variables al mismo tiempo
        x[i]=x[i-1]+ dif*0.5*(dxenx(tiem[i-1],x[i-1],vx[i-1]));
        y[i]=y[i-1]+ dif*0.5*(dyenx(tiem[i-1],x[i-1],vy[i-1]));
        vx[i]=vx[i-1]+ dif*(dvenx(tiem[i-1],x[i-1],vx[i-1]));
        vy[i]=vy[i-1]+ dif*(dveny(tiem[i-1],x[i-1],vx[i-1]));
    } 
}
//Tercer método: Runge-kutta 4orden
float rungekutta(int fin, int ini, int puntos)
{
    double dif= 0.01;
    //creacion de arreglos
    float x[puntos], y[puntos], vy[puntos], vx[puntos], tiem[puntos];
    float k1x,k2x,k3x,k4x,k1vx,k2vx,k3vx,k4vx,promex,promevx;
    float k1y,k2y,k3y,k4y,k1vy,k2vy,k3vy,k4vy,promey,promevy;
    //inicializacion con condiciones del enunciado
    x[0]=0.1163;
    y[0]=0.9772;
    vx[0]=-6.35;
    vy[0]=0.606;
    dt=(fin-ini)/puntos;
 
    for(int i=1;i<=puntos;i++)
    {
        //Pasos para X
        k1x=dif*dxenx(tiem[i-1],x[i-1],vx[i-1]);
        k1vx=dif*dvenx(tiem[i-1],x[i-1],vx[i-1]);
            
        k2x=dif*dxenx(tiem[i-1]+0.5*dif, x[i-1]+0.5*k1x,vx[i-1]+0.5*k1vx);
        k2vx=dif*dvenx(tiem[i-1]+0.5*dif, x[i-1]+0.5*k1x,vx[i-1]+0.5*k1x);
            
        k3x=dif*dxenx(tiem[i-1]+0.5*dif, x[i-1]+0.5*k2x,vx[i-1]+0.5*k2vx);
        k3vx=dif*dvenx(tiem[i-1]+0.5*dif,x[i-1]+0.5*k2x,vx[i-1]+0.5*k2x);
            
        k4x =delta*dxenx(tiem[i-1]+dif, x[i-1]+k3x, vx[i-1]+ k3vx);
        k4v =delta*dvenx(tiem[i-1]+dif, x[i-1]+k3x, vx[i-1]+ k3x);
        
        //Pasos para Y
        k1y=dif*dxeny(tiem[i-1],y[i-1],vy[i-1]);
        k1vy=dif*dveny(tiem[i-1],y[i-1],vy[i-1]);
            
        k2y=dif*dxeny(tiem[i-1]+0.5*dif, x[i-1]+0.5*k1y,vy[i-1]+0.5*k1vy);
        k2vy=dif*dveny(tiem[i-1]+0.5*dif, x[i-1]+0.5*k1y,vy[i-1]+0.5*k1y);
            
        k3y=dif*dxeny(tiem[i-1]+0.5*dif, y[i-1]+0.5*k2y,vy[i-1]+0.5*k2vy);
        k3vy=dif*dveny(tiem[i-1]+0.5*dif,y[i-1]+0.5*k2y,vy[i-1]+0.5*k2y);
            
        k4y =delta*dxeny(tiem[i-1]+dif, y[i-1]+k3y, vy[i-1]+ k3vy);
        k4vy =delta*dveny(tiem[i-1]+dif, y[i-1]+k3y, vy[i-1]+ k3y);
        
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
    euler(20,0,100);
    leap_frog(20,0,100);
    rungekutta(20,0,100);
        
    return 0;
}
