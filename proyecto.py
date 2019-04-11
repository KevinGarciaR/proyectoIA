"""Con la finalidad de aclarar mejor los conceptos cubiertos previamente, presentaremos ahora
una sencilla aplicación del algoritmo genético a un problema de optimización:
Un grupo de financieros mexicanos ha resuelto invertir 10 millones de pesos en la nueva
marca de vino "Carta Nueva". Así pues, en 4 ciudades de las principales de México se decide
iniciar una vigorosa campaña comercial: México en el centro, Monterrey en el noroeste,
Guadalajara en el occidente y Veracruz en el oriente. A esas 4 ciudades van a corresponder
las zonas comerciales I, II, III y IV. Un estudio de mercado ha sido realizado en cada una de
las zonas citadas y han sido establecidas curvas de ganancias medias, en millones de pesos,
en función de las inversiones totales (almacenes, tiendas de venta, representantes,
publicidad, etc.) Estos datos se ilustran en la tabla 2 y en la figura 4. Para simplificar los
cálculos, supondremos que las absignaciones de créditos o de inversiones deben hacerse por
unidades de 1 millón de pesos. La pregunta es: ¿en dónde se deben de asignar los 10
millones de pesos de los que se dispone para que la ganancia total sea máxima? 
"""

#
from decimal import Decimal
from random import randint

def decimalabinario(num, precision) : 
  
    binario = ""  
  
    # Fetch a la parte integral
    # Numero decimal 
    Integral = int(num)  
  
    # Fetch a la parte decimal
    # Numero decimal
    fraccional = num - Integral 
  
    # Conversion a integral a su
    # Equivalente en Binario
    while (Integral) : 
          
        rem = Integral % 2
  
        # Append 0 in binario  
        binario += str(rem);  
  
        Integral //= 2
      
    # Invertir String para obtener
    # equivalente binario 
    binario = binario[ : : -1]  
  
    # Añadir punto antes de la conversion
    # de la parte fraccional 
    binario += '.'
  
    # Conversion de la parte fraccional 
    # a su equivalente en binario 
    while (precision) : 
          
        # Encontrar el proximo bit en la parte fraccional 
        fraccional *= 2
        fract_bit = int(fraccional)  
  
        if (fract_bit == 1) : 
              
            fraccional -= fract_bit  
            binario += '1'
              
        else : 
            binario += '0'
  
        precision -= 1
  
    return binario  
def binarioaDecimal(binario, length) : 
      
    # Fetch punto 
    punto = binario.find('.') 
  
    # Actualizar punto si no se encuentra 
    if (punto == -1) : 
        punto = length  
  
    intDecimal = 0
    fracDecimal = 0
    dos = 1
  
    # Convertir parte integral de binario
    # a su equivalente en decimal 
    for i in range(punto-1, -1, -1) :  
          
        # Obtener '0' para convertir
        # el caracter en entero  
        intDecimal += ((ord(binario[i]) - 
                        ord('0')) * dos)  
        dos *= 2
  
    # Convertir la parte fraccional de binario 
    # a su eqivalente en decimal 
    dos = 2
      
    for i in range(punto + 1, length): 
          
        fracDecimal += ((ord(binario[i]) -
                         ord('0')) / dos);  
        dos *= 2.0
  
    # Fusionar integral+decimal
    sol = intDecimal + fracDecimal 
      
    return sol

#Nombre Empresa
empresa="Carta Nueva";
#Regiones
ciudades=[["I","México Centro"],["II","Monterrey noroeste"],["III","Guadalajara Occidente"],["IV","Veracruz Oriente"]];
print("Optimización de la empresa",empresa);
print("");
print("Lista de Regiones");
for ciudad in enumerate(ciudades):
 print(ciudad);

print("");
#Probamos algun valor decimal
valor=10.42;
#Seteamos precision
precision=8;
#temp= Guarda el valor Binario de "Valor"
print("Ejemplo de Prueba");
print("Convertiremos el valor",valor)
temp=decimalabinario(valor,precision);
print(valor, "en binario es",decimalabinario(valor,precision));

#temp2= Guarda el valor convertido de decimal a binario
temp2=binarioaDecimal(temp,len(temp));
print("Convertimos el binario",temp,"a decimal: ",binarioaDecimal(temp,len(temp)));

#Redondeamos el Temp2 para obtener el valor real de Valor antes de ser convertido
output = round(temp2,2);
print("Redondeamos el valor binario para que quede igual a su valor real",output);
print("");print("");

listabeneficiosdec=[[0.00,0.00,0.00,0.00,0.00],
				 [1,0.28,0.25,0.15,0.20],
				 [2,0.45,0.41,0.25,0.33],
				 [3,0.65,0.55,0.40,0.42],
				 [4,0.78,0.65,0.50,0.48],
				 [5,0.90,0.75,0.62,0.53],
				 [6,1.02,0.80,0.73,0.56],
				 [7,1.13,0.85,0.82,0.58],
				 [8,1.23,0.88,0.90,0.60],
				 [9,1.32,0.90,0.96,0.60],
				 [10,1.38,0.90,1.00,0.60]
				 ];
print("Inversión en millones"+"         "+"Beneficio I"+"                 "+"Beneficio II"+"            "+"Beneficio III"+"              "+"Beneficio IV");
pos=-1;
for tabla in enumerate(listabeneficiosdec):
 pos+=1;
 print("        ",listabeneficiosdec[pos][0],"                     ",listabeneficiosdec[pos][1],"                     ",listabeneficiosdec[pos][2],
 	  "                     ",listabeneficiosdec[pos][3],"                     ",listabeneficiosdec[pos][4]);


 #Convertimos todo a binario
listabeneficiosbin=[];
pos=-1;
for tabla in enumerate(listabeneficiosdec):
 pos+=1;
 listabeneficiosbin.append([decimalabinario(listabeneficiosdec[pos][0],8),decimalabinario(listabeneficiosdec[pos][1],8),decimalabinario(listabeneficiosdec[pos][2],8),decimalabinario(listabeneficiosdec[pos][3],8),decimalabinario(listabeneficiosdec[pos][4],8)]);

#Imprimos la lista en Binario
pos=-1;
for tabla in enumerate(listabeneficiosbin):
 pos+=1;
 print("Posicion",pos,"   Inversion en Millones=",listabeneficiosbin[pos][0],"   Beneficio I= ",listabeneficiosbin[pos][1],"   Beneficio II:",listabeneficiosbin[pos][2],"   Beneficio III:",listabeneficiosbin[pos][3],"   Beneficio IV:",listabeneficiosbin[pos][4]);


#Probamos imprimiendo la posicion 7, convirtiendo de Binario a Decimal (Inversion en Millones=5)
tempInv=binarioaDecimal(listabeneficiosbin[7][0],len(listabeneficiosbin[7][0]));
tempBeneficioI=binarioaDecimal(listabeneficiosbin[7][1],len(listabeneficiosbin[7][1]));
tempBeneficioII=binarioaDecimal(listabeneficiosbin[7][2],len(listabeneficiosbin[7][2]));
tempBeneficioIII=binarioaDecimal(listabeneficiosbin[7][3],len(listabeneficiosbin[7][3]));
tempBeneficioIV=binarioaDecimal(listabeneficiosbin[7][4],len(listabeneficiosbin[7][4]));
output1 = round(tempInv,2);
output2 = round(tempBeneficioI,2);
output3 = round(tempBeneficioII,2);
output4 = round(tempBeneficioIII,2);
output5 = round(tempBeneficioIV,2);
print("El valor convertido de Binario a Decimal de la Posicion 7 es");
print(output1,output2,output3,output4,output5);
generarpoblacioninicial();



def generarpoblacioninicial():
 primer_random=randint(0, 10); # 6
 if (primer_random == 10):
  print(primer_random ,0,0,0)
  primer_resta=10-primer_random; # 4
  segundo_random=randint(0,primer_resta); #3
 if ((primer_random+segundo_random) == 10):
  print(primer_random, segundo_random,0,0);
  segunda_resta=10-(primer_random+segundo_random)
  tercer_random =randint(0, segunda_resta); #3
 if ((primer_random+segundo_random+tercer_random) == 10):
  print(primer_random, segundo_random,tercer_random,0)
  tercer_resta= 10-(primer_random+segundo_random+tercer_random)
  Cuarto_random=tercer_resta
  print(primer_random, segundo_random,tercer_random,Cuarto_random)	
