import pandas as pd
import numpy as np
from metalearn import Metafeatures

base = pd.read_csv('iris.csv')

print("Informações da Base de Dados")
print("Quantidade de linhas e colunas: ", base.shape)
print("Descrição do Index: ", base.index)
print("Colunas presentes: ", base.columns)
print("Colunas presentes: ", base.count)

X = base.drop('variety', axis=1)
Y = base['variety']

metafeatures = Metafeatures()
mfs = metafeatures.compute(X, Y)

print(mfs)

print("teste")
