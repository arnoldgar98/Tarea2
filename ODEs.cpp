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

float euler(double fin, double ini, double dif, string name)
    {ofstream outfile;
    outfile.open(name);
    //creacion de arreglos
    int puntos= (fin-ini)/dif;
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


//Segundo Método:Leap frog
float leap_frog(double fin, double ini, double dif, string name)
{
    
    int puntos= 20/dif;
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
   
   
    //desde 2, porque ya usamos la condicion inicial
    for(int i=1; i<puntos;i++)
    {
        //avance del tiempo
        tiem[i]=tiem[i-1]+dt;
        //retroalimentacion de las variables al mismo tiempo
        x[i]=x[i-1]+ dif*0.5*dxenx(tiem[i-1],x[i-1],vx[i-1]);
        y[i]=y[i-1]+ dif*0.5*dxeny(tiem[i-1],y[i-1],vy[i-1]);
        r12[i] = sqrt(pow(y[i],2) + pow(x[i],2));
        vx[i]=vx[i-1]+ dif*dvenx(tiem[i-1],x[i-1],r12[i-1]);
        vy[i]=vy[i-1]+ dif*dveny(tiem[i-1],y[i-1],r12[i-1]);
        
        
        
        
    } 
    ofstream outfile2;
    outfile2.open(name);
    for(int i=0;i<puntos;i++)
    {
        outfile2<<x[i]<<";"<<y[i]<<endl;
    }
    outfile2.close();
}
//Tercer método: Runge-kutta 4orden
float rungekutta(double fin, double ini, double dif, string name)
{
    int puntos= (fin-ini)/dif;
    double dt;
    //creacion de arreglos
    float x[puntos], y[puntos], vy[puntos], vx[puntos], tiem[puntos],r12[puntos];
    float k1x,k2x,k3x,k4x,k1vx,k2vx,k3vx,k4vx,promex,promevx;
    float k1y,k2y,k3y,k4y,k1vy,k2vy,k3vy,k4vy,promey,promevy;
    //inicializacion con condiciones del enunciado
    x[0]=0.1163;
    y[0]=0.9772;
    vx[0]=-6.35;
    vy[0]=0.606;
    r12[0]=sqrt(pow(y[0],2) + pow(x[0],2));
    dt=(fin-ini)/puntos;
 
    for(int i=1;i<=puntos;i++)
    {
        //Pasos para X
        k1x=dif*dxenx(tiem[i-1],x[i-1],vx[i-1]);
        k1y=dif*dxeny(tiem[i-1],y[i-1],vy[i-1]);
        k1vx=dif*dvenx(tiem[i-1],x[i-1],r12[i-1]);
        k1vy=dif*dveny(tiem[i-1],y[i-1],r12[i-1]);
            
        k2x=dif*dxenx(tiem[i-1], (x[i-1]+0.5*k1x),(vx[i-1]+0.5*k1vx));
        k2y=dif*dxeny(tiem[i-1], (y[i-1]+0.5*k1y),(vy[i-1]+0.5*k1vy));
        k2vx=dif*dvenx(tiem[i-1], (x[i-1]+0.5*k1y),r12[i-1]);
        k2vy=dif*dveny(tiem[i-1], (y[i-1]+0.5*k1y),r12[i-1]);    
            
        k3x=dif*dxenx(tiem[i-1], (x[i-1]+0.5*k2x),(vx[i-1]+0.5*k2vx));
        k3y=dif*dxeny(tiem[i-1], (y[i-1]+0.5*k2y),(vy[i-1]+0.5*k2vy));
        k3vx=dif*dvenx(tiem[i-1], (x[i-1]+0.5*k2y),r12[i-1]);
        k3vy=dif*dveny(tiem[i-1], (y[i-1]+0.5*k2y),r12[i-1]);  
        
        k4x=dif*dxenx(tiem[i-1],x[i-1],vx[i-1]);
        k4y=dif*dxeny(tiem[i-1],y[i-1],vy[i-1]);
        k4vx=dif*dvenx(tiem[i-1],x[i-1],r12[i-1]);
        k4vy=dif*dveny(tiem[i-1],y[i-1],r12[i-1]);
        //Paso final de rungekutta
        promex=(1.0/6.0)*(k1x+2.0*k2x+2.0*k3x+k4x);
        promey=(1.0/6.0)*(k1y+2.0*k2y+2.0*k3y+k4y);
        promevx=(1.0/6.0)*(k1vx+2.0*k2vx+2.0*k3vx+k4vx);
        promevy=(1.0/6.0)*(k1vy+2.0*k2vy+2.0*k3vy+k4vy);
        
        x[i] = x[i-1] + promex;
        y[i] = y[i-1] + promey;
        vx[i] = vx[i-1] + promevx;
        vy[i] = vy[i-1] + promevy;
        r12[i]=sqrt(pow(y[i],2) + pow(x[i],2));
    }
    ofstream outfile3;
    outfile3.open(name);
    for(int i=0;i<puntos;i++)
    {
        outfile3<<x[i]<<";"<<y[i]<<endl;
    }
    outfile3.close();
    
}
int main()
{
    euler(20,0,0.01,"datos.dat");
    euler(20,0,0.001,"datos1.dat");
    euler(20,0,0.0001,"datos2.dat");
    leap_frog(20,0,0.01,"datos3.dat");
    leap_frog(20,0,0.001,"datos4.dat");
    leap_frog(20,0,0.006,"datos5.dat");
    rungekutta(20,0,0.01,"datos6.dat");
    rungekutta(20,0,0.001,"datos7.dat");
    rungekutta(20,0,0.0001,"datos8.dat");
    return 0;
}