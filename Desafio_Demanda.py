#PREVISÃO DE DEMANDA POR MÉDIA MÓVEL EXPONENCIAL

#SEGUE O DESAFIO DE PREVISÃO DE DEMANDA PARA O PERÍODO ENTRE 21/01 E 25/01, FOI UTILIZADO O MÉTODO DE MÉDIA MÓVEL EXPONENCIAL DEVIDO
#AO FATO DESSA SER MAIS UTILIZADA PARA PERÍODOS MAIS CURTOS COMO O EM QUESTÃO, NA QUAL OS DADOS MAIS RECENTES POSSUEM UM MAIOR PODER
#EM RELAÇÃO AOS DEMAIS, LOGO É POSSÍVEL TER UMA MELHOR NOÇÃO SOBRE AS TENDÊNCIAS.

import numpy as np

#FOI FEITA UMA SEPARAÇÃO POR DIAS DA SEMANA 

dados_diarios=[[1366, 1050, 821, 814, 1317], #DADOS DE TODAS AS SEGUNDAS
        [870, 1213, 711, 572, 679, 807], #DADOS DE TODAS AS TERÇAS
        [868, 1055, 745, 429, 712, 923], #DADOS DE TODAS AS QUARTAS
        [1189, 1343, 1009, 638, 1229, 1265], #DADOS DE TODAS AS QUINTAS
        [742, 832, 18, 106, 821, 892], #DADOS DE TODAS AS SEXTAS
        [317, 240, 40, 54, 319], #DADOS DE TODAS OS SÁBADOS
        [685, 235, 67, 144, 317]] #DADOS DE TODAS OS DOMINGOS

dados_fechamento=[1692, 1097, 1302, 1405, 945, 289, 566] #ultimo dado registrado, logo tem mais valor para calcular uma curva de tendência

media_dia=[] #sem os dados de fechamento
media_exponencial=[]

for i in range(0,7):
    media_dia.append(np.mean(dados_diarios[i]))
    mme=(2/(len(dados_diarios[i])+1))*(dados_fechamento[i]-media_dia[i])+media_dia[i]
    media_exponencial.append(mme)

print("A previsão de demanda para o dia 21/01 = ", round(media_exponencial[5]))
print("A previsão de demanda para o dia 22/01 = ", round(media_exponencial[6]))
print("A previsão de demanda para o dia 23/01 = ", round(media_exponencial[0]))
print("A previsão de demanda para o dia 24/01 = ", round(media_exponencial[1]))
print("A previsão de demanda para o dia 25/01 = ", round(media_exponencial[2]))
