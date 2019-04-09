from bitarray import bitarray
from random import random,randint,shuffle
from itertools import izip

def pairwise(iterable):
    "s -> (s0, s1), (s2, s3), (s4, s5), ..."
    a = iter(iterable)
    return izip(a, a)

ganancias = [
    [0,0.28,0.45,0.65,0.78,0.90,1.02,1.13,1.23,1.32,1.38,0,0,0,0,0],
    [0,0.25,0.41,0.55,0.65,0.75,0.80,0.85,0.88,0.90,0.90,0,0,0,0,0],
    [0,0.15,0.25,0.40,0.50,0.62,0.73,0.82,0.90,0.96,1.00,0,0,0,0,0],
    [0,0.20,0.33,0.42,0.48,0.53,0.56,0.58,0.60,0.60,0.60,0,0,0,0,0]
]

class Genotipo:
    def __init__(self,fDecodificar):
        self.genes = []
        self.decodificar = fDecodificar
        self.longitud = 0
    def agregarGene(self,longitud,fEvaluar):
        inicio = self.longitud
        self.longitud = self.longitud+longitud
        self.genes.append(Gene(inicio,self.longitud,fEvaluar,self.decodificar))
    def aptitud(self,individuo):
        ganancias = self.sumarGanancias(individuo)
        sumaValoresGenes = self.sumarValoresGenes(individuo)
        v = 10-sumaValoresGenes
        return ganancias/(500*v+1)
    def sumarValoresGenes(self,individuo):
        return reduce(lambda sum,gene: sum+gene.getValor(individuo),self.genes,0)
    def sumarGanancias(self,individuo):
        return reduce(lambda sum,gene: sum+gene.evaluar(individuo),self.genes,0)
class Gene:
    def __init__(self,inicio,fin,fEvaluar,fDecodificar):
        self.inicio = inicio
        self.fin = fin
        self.evaluar = lambda cadena:fEvaluar(self.getValor(cadena))
        self.decodificar = fDecodificar
    def getValor(self,cadena):
        return self.decodificar(cadena[self.inicio:self.fin])

class TipoDato:
    @classmethod
    def entero(self,bitarr):
        out = 0
        for bit in bitarr:
            out = (out << 1) | bit
        return out

class Poblacion:
    def __init__(self,size,genotipo):
        self.genotipo = genotipo
        self.size = size
        self.individuos = [Poblacion.crearIndividuoAleatorio(genotipo.longitud) for i in range(0,size)]
        self.funcion = max
    def funcionComparativa(self,funcion):
        self.funcion = funcion
    def mejorIndividuo(self):
        return self.funcion(self.individuos)
    @classmethod
    def crearIndividuoAleatorio(self,longitud):
        return bitarray([0 if random()<.5 else 1 for x in range(0,longitud)])
class Torneo:
    def operar(self,poblacion):
        ganadores1 = self.competencia(poblacion)
        poblacion.individuos = ganadores1 + self.competencia(poblacion)
    def competencia(self,poblacion):
        shuffle(poblacion.individuos)
        ganadores = []
        for ind1,ind2 in pairwise(poblacion.individuos):
            if (poblacion.genotipo.aptitud(ind1)>poblacion.genotipo.aptitud(ind2)):
                ganadores.append(ind1)
            else:
                ganadores.append(ind2)
        return ganadores

class Mutacion:
    def __init__(self,porcentaje,noPuntos):
        self.porcentaje = porcentaje
        self.noPuntos = noPuntos
    def operar(self,poblacion):
        for ind1 in poblacion.individuos:
            if (random()<=self.porcentaje):
                puntos = self.puntos(poblacion.genotipo.longitud)
                self.mutar(ind1,puntos)
    def mutar(self,original,puntos):
        for i in puntos:
            original[i] = not original[i]
    def puntos(self,longitud):
        puntos = set()
        while len(puntos)<self.noPuntos:
            puntos.add(randint(0,longitud-1))
        return puntos

class Cruza:
    def __init__(self,porcentaje):
        self.porcentaje = porcentaje
    def operar(self,poblacion):
        hijos = []
        for ind1,ind2 in pairwise(poblacion.individuos):
            if (random()<=self.porcentaje):
                puntos = self.puntos(poblacion.genotipo.longitud)
                hijos.append(self.cruzar(ind1,ind2,puntos))
                hijos.append(self.cruzar(ind2,ind1,puntos))
            else:
                hijos.append(ind1)
                hijos.append(ind2)
        poblacion.individuos = hijos
    def cruzar(self,padre1,padre2,puntos):
        # print("padre1: "+str(padre1)+", padre2: "+str(padre2))
        hijo = padre1[:puntos[0]]+padre2[puntos[0]:puntos[1]]+padre1[puntos[1]:]
        # print("hijo: "+str(hijo))
        return hijo
    def puntos(self,longitudGenotipo):
        # longitud de genotipo debe ser mayor o igual a 3
        p1 = randint(1,longitudGenotipo-2)
        p2 = randint(p1+1,longitudGenotipo-1)
        return (p1,p2)


class AG:
    def __init__(self):
        self.operadores = []
    def agregarOperadorGenetico(self,operador):
        self.operadores.append(operador)
    def ejecutar(self,poblacion,iteraciones):
        for i in range(0,iteraciones):
            self.iteracion(poblacion)
            self.imprimirResIteracion(poblacion,i)
    def iteracion(self,poblacion):
        for operador in self.operadores:
            operador.operar(poblacion)
    @classmethod
    def imprimirResIteracion(self,poblacion,n):
        print("Mejor individuo de iteracion "+str(n))
        mejor = poblacion.mejorIndividuo()
        print(mejor)
        print("aptitud "+str(poblacion.genotipo.aptitud(mejor)))

ag = AG()
ag.agregarOperadorGenetico(Torneo())
ag.agregarOperadorGenetico(Cruza(0.8))
ag.agregarOperadorGenetico(Mutacion(0.1,6))

genotipo = Genotipo(TipoDato.entero)
genotipo.agregarGene(4,lambda x: ganancias[0][x])
genotipo.agregarGene(4,lambda x: ganancias[1][x])
genotipo.agregarGene(4,lambda x: ganancias[2][x])
genotipo.agregarGene(4,lambda x: ganancias[3][x])

print(genotipo.aptitud(bitarray('1000001000000000')))

poblacion = Poblacion(50,genotipo)
ag.ejecutar(poblacion,100)
