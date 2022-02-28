%% Calculo de capacitancias interdigitales planares
% Para este calculo se usara el principio de paralelismo de las
% capacitancias que establece que aparecen 2N-1 capacitancias cada vez que
% hayan N "fingers" en cada cara de la capacitancia interdigital
%
% (2N - 1)EoA/(d/2) = 2(2N - 1)EoA/d
clc;
clear all;
close all;
% Print information of the simulator to users
sprintf('Calculador de capacitancias intergiditadas \nFabricacion de Biosensores\nJohann F. Osma\nBasado en el trabajo de Zahira Gonzalez\n')


%% Toma de datos
%
N= input('Numero de fingers de la capacitancia? > ');
d= input('Distancia entre fingers del mismo lado? (mm) > ');
l= input('Largo de los fingers? (mm) > ');
w= input('Ancho de los fingers? (mm) > ');
h= input('Alto de los fingers? (mm) > ');
delta= input('Distancia de separacion entre los fingers de un lado y el comb del otro lado? (mm) > ');
Eo= input('Permitividad relativa? > ');
Eo=Eo*8.8541878176E-12; %Multiplicar por la permitividad del vacio
%
%% Calculo de la capacitancia
%
Area_efectiva=(l-delta)*h; % Largo efectivo=largo de fingers - delta y se multiplica por la altura (mm^2)
Area_efectiva=Area_efectiva/1000000; % Area en m^2
Distancia_efectiva=(d-w)/2; % Distancia efectiva es separacion entre fingers menos los anchos de un finger del otro lado sobre 2
Distancia_efectiva=Distancia_efectiva/1000; % Distancia en m
Capacitancia=2*(2*N-1)*Eo*Area_efectiva/Distancia_efectiva;
sprintf('El Area efectiva es de %3.5g m^2 \nEl Area efectiva es de %3.5g um^2 \n',Area_efectiva,Area_efectiva*1E12)
sprintf('La Distancia efectiva equivale a %3.5g m \nLa Distancia efectiva equivale a %3.5g um \n',Distancia_efectiva,Distancia_efectiva*1E6)
str_value=sprintf('La Capacitancia equivale a %3.5g F \n',Capacitancia)
%% Dibujo de la capacitancia
%
figure
ancho_total=(N*(w+d))+(w/2)-(d/2); % ancho total del electrodo
%Pintamos el primer electrodo con una profundidad de 1
rectangle('Position',[0 0 ancho_total 1],'LineWidth',1,'EdgeColor','r','Facecolor','r')
%Pintamos el segundo electrodo con una profundidad de 1
origen=1+l+delta;
rectangle('Position',[0 origen ancho_total 1],'LineWidth',1,'EdgeColor','b','Facecolor','b')
for i=1:N
    %Pintamos el finger i del electrodo rojo de abajo
    rectangle('Position',[(i-1)*(w+d) 1 w l],'LineWidth',1,'EdgeColor','r','Facecolor','r')
    %Pintamos el finger i del electrodo azul de arriba
    rectangle('Position',[((i-1)*(w+d))+(w/2)+(d/2) origen-l w l],'LineWidth',1,'EdgeColor','b','Facecolor','b')
end
daspect([1,1,1])
xlabel('mm');
ylabel('mm');
text(1,origen+2,str_value);


