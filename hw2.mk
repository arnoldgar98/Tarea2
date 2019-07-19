XY_met_dt VxVy_met_dt Mome_met_dt Ener_met_dt FFtIm ImProceso ImHybrid: Fourier.py Plots_hw2.py datos.dat datos1.dat datos2.dat datos3.dat datos4.dat datos5.dat datos6.dat datos7.dat datos8.dat
	python Plots_hw2.py
	python Fourier.py    
datos.dat datos1.dat datos2.dat datos3.dat datos4.dat datos5.dat datos6.dat datos7.dat datos8.dat: a.out
	./a.out
a.out: ODEs.cpp
	g++ ODEs.cpp
 