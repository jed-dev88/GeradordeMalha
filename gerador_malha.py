import streamlit as st
import pandas as pd
from datetime import timedelta
import numpy as np



st.title("Gerador de Arquivo de Malha")
slot_arr = []
slot_dep = []
slot_op_dupla = []
slot = []



def separador_arr_dep(uploaded_file):
    
    slot = []

    if uploaded_file is not None:
        # Lê o conteúdo como texto
        conteudo = uploaded_file.read().decode("utf-8")
        linhas = conteudo.splitlines()

        for line in linhas:
            if len(line.strip()) > 6:
                slot = line.strip().split()

                if len(slot) == 6 and slot[0][0] == 'H':
                    slot_arr.append(slot)

                elif len(slot) == 7 and slot[0][0] == 'H':
                    slot_dep.append(slot)

                elif len(slot) > 7 and slot[0][0] == 'H':
                    slot_op_dupla.append(slot)




def desembrandor_op_dupla(slot_op_dupla):
  for i in slot_op_dupla:
    arr = i[0],i[2],i[3],i[4],i[5],i[7][0:1]
    dep = "H",i[1],i[2],i[3],i[4],i[6],i[7][0:1]

    arr_str = " ".join(arr)
    dep_str = " ".join(dep)

    slot_arr.append(arr_str.split())
    slot_dep.append(dep_str.split())


def separar_info_chegadas():
  for item in slot_arr:

    item[0] = item[0][1:]

    item[1] = item[1][0:5]  + " " + item[1][5:]

    item[3] = item[3][0:3] + " " +  item[3][3:]

    item[4] = item[4][0:3] + " " + item[4][3:6] + " " + item[4][6:]


def datas_temporada(temporada,df):

  if(temporada == "W18"):
    df['Datas'] = df['Datas'].str.replace('MAR','MAR2019')
    df['Datas'] = df['Datas'].str.replace('DEC','DEC2018')
    df['Datas'] = df['Datas'].str.replace('NOV','NOV2018')
    df['Datas'] = df['Datas'].str.replace('OCT','OCT2018')
    df['Datas'] = df['Datas'].str.replace('JAN','JAN2019')
    df['Datas'] = df['Datas'].str.replace('FEB','FEB2019')

  if(temporada == "S19"):
    df['Datas'] = df['Datas'].str.replace('MAR','MAR2019')
    df['Datas'] = df['Datas'].str.replace('APR','APR2019')
    df['Datas'] = df['Datas'].str.replace('MAY','MAY2019')
    df['Datas'] = df['Datas'].str.replace('JUN','JUN2019')
    df['Datas'] = df['Datas'].str.replace('JUL','JUL2019')
    df['Datas'] = df['Datas'].str.replace('AUG','AUG2019')
    df['Datas'] = df['Datas'].str.replace('SEP','SEP2019')
    df['Datas'] = df['Datas'].str.replace('OCT','OCT2019')

  if(temporada == "W19"):
    df['Datas'] = df['Datas'].str.replace('MAR','MAR2020')
    df['Datas'] = df['Datas'].str.replace('DEC','DEC2019')
    df['Datas'] = df['Datas'].str.replace('NOV','NOV2019')
    df['Datas'] = df['Datas'].str.replace('OCT','OCT2019')
    df['Datas'] = df['Datas'].str.replace('JAN','JAN2020')
    df['Datas'] = df['Datas'].str.replace('FEB','FEB2020')

  if(temporada == "S20"):
    df['Datas'] = df['Datas'].str.replace('MAR','MAR2020')
    df['Datas'] = df['Datas'].str.replace('APR','APR2020')
    df['Datas'] = df['Datas'].str.replace('MAY','MAY2020')
    df['Datas'] = df['Datas'].str.replace('JUN','JUN2020')
    df['Datas'] = df['Datas'].str.replace('JUL','JUL2020')
    df['Datas'] = df['Datas'].str.replace('AUG','AUG2020')
    df['Datas'] = df['Datas'].str.replace('SEP','SEP2020')
    df['Datas'] = df['Datas'].str.replace('OCT','OCT2020')

  if(temporada == "W20"):
    df['Datas'] = df['Datas'].str.replace('MAR','MAR2021')
    df['Datas'] = df['Datas'].str.replace('DEC','DEC2020')
    df['Datas'] = df['Datas'].str.replace('NOV','NOV2020')
    df['Datas'] = df['Datas'].str.replace('OCT','OCT2020')
    df['Datas'] = df['Datas'].str.replace('JAN','JAN2021')
    df['Datas'] = df['Datas'].str.replace('FEB','FEB2021')

  if(temporada == "S21"):
    df['Datas'] = df['Datas'].str.replace('MAR','MAR2021')
    df['Datas'] = df['Datas'].str.replace('APR','APR2021')
    df['Datas'] = df['Datas'].str.replace('MAY','MAY2021')
    df['Datas'] = df['Datas'].str.replace('JUN','JUN2021')
    df['Datas'] = df['Datas'].str.replace('JUL','JUL2021')
    df['Datas'] = df['Datas'].str.replace('AUG','AUG2021')
    df['Datas'] = df['Datas'].str.replace('SEP','SEP2021')
    df['Datas'] = df['Datas'].str.replace('OCT','OCT2021')

  if(temporada == "W21"):
    df['Datas'] = df['Datas'].str.replace('MAR','MAR2022')
    df['Datas'] = df['Datas'].str.replace('DEC','DEC2021')
    df['Datas'] = df['Datas'].str.replace('NOV','NOV2021')
    df['Datas'] = df['Datas'].str.replace('OCT','OCT2021')
    df['Datas'] = df['Datas'].str.replace('JAN','JAN2022')
    df['Datas'] = df['Datas'].str.replace('FEB','FEB2022')

  if(temporada == "S22"):
    df['Datas'] = df['Datas'].str.replace('MAR','MAR2022')
    df['Datas'] = df['Datas'].str.replace('APR','APR2022')
    df['Datas'] = df['Datas'].str.replace('MAY','MAY2022')
    df['Datas'] = df['Datas'].str.replace('JUN','JUN2022')
    df['Datas'] = df['Datas'].str.replace('JUL','JUL2022')
    df['Datas'] = df['Datas'].str.replace('AUG','AUG2022')
    df['Datas'] = df['Datas'].str.replace('SEP','SEP2022')
    df['Datas'] = df['Datas'].str.replace('OCT','OCT2022')

  if(temporada == "W25"):
    df['Datas'] = df['Datas'].str.replace('MAR','MAR2026')
    df['Datas'] = df['Datas'].str.replace('DEC','DEC2025')
    df['Datas'] = df['Datas'].str.replace('NOV','NOV2025')
    df['Datas'] = df['Datas'].str.replace('OCT','OCT2025')
    df['Datas'] = df['Datas'].str.replace('JAN','JAN2026')
    df['Datas'] = df['Datas'].str.replace('FEB','FEB2026')

  if(temporada == "S23"):
    df['Datas'] = df['Datas'].str.replace('MAR','MAR2023')
    df['Datas'] = df['Datas'].str.replace('APR','APR2023')
    df['Datas'] = df['Datas'].str.replace('MAY','MAY2023')
    df['Datas'] = df['Datas'].str.replace('JUN','JUN2023')
    df['Datas'] = df['Datas'].str.replace('JUL','JUL2023')
    df['Datas'] = df['Datas'].str.replace('AUG','AUG2023')
    df['Datas'] = df['Datas'].str.replace('SEP','SEP2023')
    df['Datas'] = df['Datas'].str.replace('OCT','OCT2023')

  if(temporada == "W23"):
    df['Datas'] = df['Datas'].str.replace('MAR','MAR2024')
    df['Datas'] = df['Datas'].str.replace('DEC','DEC2023')
    df['Datas'] = df['Datas'].str.replace('NOV','NOV2023')
    df['Datas'] = df['Datas'].str.replace('OCT','OCT2023')
    df['Datas'] = df['Datas'].str.replace('JAN','JAN2024')
    df['Datas'] = df['Datas'].str.replace('FEB','FEB2024')

  if(temporada == "S24"):
    df['Datas'] = df['Datas'].str.replace('MAR','MAR2024')
    df['Datas'] = df['Datas'].str.replace('APR','APR2024')
    df['Datas'] = df['Datas'].str.replace('MAY','MAY2024')
    df['Datas'] = df['Datas'].str.replace('JUN','JUN2024')
    df['Datas'] = df['Datas'].str.replace('JUL','JUL2024')
    df['Datas'] = df['Datas'].str.replace('AUG','AUG2024')
    df['Datas'] = df['Datas'].str.replace('SEP','SEP2024')
    df['Datas'] = df['Datas'].str.replace('OCT','OCT2024')

  if(temporada == "W24"):
    df['Datas'] = df['Datas'].str.replace('MAR','MAR2025')
    df['Datas'] = df['Datas'].str.replace('DEC','DEC2024')
    df['Datas'] = df['Datas'].str.replace('NOV','NOV2024')
    df['Datas'] = df['Datas'].str.replace('OCT','OCT2024')
    df['Datas'] = df['Datas'].str.replace('JAN','JAN2025')
    df['Datas'] = df['Datas'].str.replace('FEB','FEB2025')

  if(temporada == "S25"):
    df['Datas'] = df['Datas'].str.replace('MAR','MAR2025')
    df['Datas'] = df['Datas'].str.replace('APR','APR2025')
    df['Datas'] = df['Datas'].str.replace('MAY','MAY2025')
    df['Datas'] = df['Datas'].str.replace('JUN','JUN2025')
    df['Datas'] = df['Datas'].str.replace('JUL','JUL2025')
    df['Datas'] = df['Datas'].str.replace('AUG','AUG2025')
    df['Datas'] = df['Datas'].str.replace('SEP','SEP2025')
    df['Datas'] = df['Datas'].str.replace('OCT','OCT2025')


def dias_op_V(linha):
    date=pd.to_datetime(linha['data_op'])
    dia_op = date.strftime('%w')
    if dia_op == "0":
      dia_op = "7"
    if(linha['Doop'].find(dia_op)>=0):
        return "manter"
    else:
        return "eliminar"


def separar_info_dep():
  for item in slot_dep:

    item[2] = item[2][0:5] + " " + item[2][5:]

    item[4] = item[4][0:3] + " " +  item[4][3:]

    if(len(item[5]) == 10):
      item[5] = item[5][0:4] + " " + "0" + " " + item[5][4:7] + " " + item[5][7:]

    if(len(item[5]) == 11):
      item[5] = item[5][0:4] + " " + item[5][4:5] + " " + item[5][5:8] + " " + item[5][8:]


def main():
    nome_arquivo_upload = st.file_uploader("Selecione o arquivo SIR no formato .TXT", type=["TXT"])
    opcao = st.selectbox("Selecione uma opção:", ["W25", "S25"])
    nome_excel = st.text_input("Digite o nome do arquivo que deseja receber (ex: UDI_W25_20250721.csv)")

    if st.button("Executar"):  
        separador_arr_dep(nome_arquivo_upload)
        desembrandor_op_dupla(slot_op_dupla)
        separar_info_chegadas()
        df_chegada = pd.DataFrame(data = slot_arr,columns=['N_Voo','Datas','Doop','Assentos_equipamento','Orig_dep_hora','Tipo_Voo'] )
        datas_temporada(opcao,df_chegada)
      
        df_aux = df_chegada['Datas'].str.split(expand=True)
        df_aux.columns = ['data_inicio_str','data_fim_str']

        df_aux['data_inicio'] = pd.to_datetime(df_aux['data_inicio_str'], format = '%d%b%Y')
        df_aux['data_fim'] = pd.to_datetime(df_aux['data_fim_str'], format = '%d%b%Y')

        df_chegada = pd.concat([df_chegada,df_aux[['data_inicio','data_fim']]],axis=1)
        df_chegada.drop(columns =['Datas'],inplace = True)

    
        a = [pd.date_range(*r, freq='D') for r in df_chegada[['data_inicio', 'data_fim']].values]
        df_aux = df_chegada[['N_Voo', 'Doop','Assentos_equipamento', 'Orig_dep_hora','Tipo_Voo']].join(pd.DataFrame(a)).set_index(['N_Voo', 'Doop','Assentos_equipamento', 'Orig_dep_hora','Tipo_Voo']) \
                          .stack().droplevel(-1).reset_index()    

        df_aux.rename(columns={0: 'data_op'},inplace = True)

        df_aux['dia'] = df_aux['data_op'].dt.strftime('%A')
        df_aux['M'] = df_aux.apply(dias_op_V, axis=1)
        df_arr = df_aux.query(" M == 'manter' ")
        df_arr.drop(columns= {'M'},inplace = True)
        df_aux = df_arr['Assentos_equipamento'].str.split(expand = True)
        df_arr['Assentos'] = df_aux[0]
        df_arr['Equipamento'] = df_aux[1]
        df_aux = df_arr['Orig_dep_hora'].str.split(expand = True)
        df_arr['Orig_Dest'] = df_aux[0]
        df_arr['Escala'] = df_aux[1]
        df_arr['Hora'] = df_aux[2]
        df_arr.drop(columns =['Assentos_equipamento','Orig_dep_hora'],inplace = True)
        df_arr['Hora'] = df_arr['Hora'].astype(str)
        df_arr['Hora'] = df_arr['Hora'].str.rjust(4,'0')
        df_arr['Hora'] = df_arr['Hora'].str[:2] + ':' + df_arr['Hora'].str[-2:]
        df_arr['Arr_Dep'] = 'A'

        df_partida = pd.DataFrame(data = slot_dep,columns=['Cod Acao','N_Voo','Datas','Doop','Assentos_equipamento','Orig_dep_hora','Tipo_Voo'] )
        df_partida.drop(columns="Cod Acao", inplace = True)
        datas_temporada(opcao,df_partida)
        
        df_aux = df_partida['Datas'].str.split(expand=True)

        df_aux['data_inicio_str'] = df_partida['Datas'].str[:9]
        df_aux['data_fim_str'] = df_partida['Datas'].str[9:]

        df_aux['data_inicio'] = pd.to_datetime(df_aux['data_inicio_str'], format = '%d%b%Y')
        df_aux['data_fim'] = pd.to_datetime(df_aux['data_fim_str'], format = '%d%b%Y')

        df_partida = pd.concat([df_partida,df_aux[['data_inicio','data_fim']]],axis=1)
        df_partida.drop(columns =['Datas'],inplace = True)

        a = [pd.date_range(*r, freq='D') for r in df_partida[['data_inicio', 'data_fim']].values]
        df_aux = df_partida[['N_Voo', 'Doop','Assentos_equipamento', 'Orig_dep_hora','Tipo_Voo']].join(pd.DataFrame(a)).set_index(['N_Voo', 'Doop','Assentos_equipamento', 'Orig_dep_hora','Tipo_Voo']) \
                          .stack().droplevel(-1).reset_index()
        df_aux.rename(columns={0: 'data_op'},inplace = True)
        df_aux['dia'] = df_aux['data_op'].dt.strftime('%A')
        df_aux['M'] = df_aux.apply(dias_op_V, axis=1)
        df_dep = df_aux.query(" M == 'manter' ")
        df_dep.drop(columns= "M", inplace = True)
        df_aux = df_dep['Assentos_equipamento'].str.split(expand = True)
        df_dep['Assentos'] = df_dep['Assentos_equipamento'].str[:3]
        df_dep['Equipamento'] = df_dep['Assentos_equipamento'].str[3:]
        df_aux = df_dep['Orig_dep_hora'].str.split(expand = True)
        df_dep['Hora'] = df_dep['Orig_dep_hora'].str[:4]
        df_dep['Orig_Dest'] = df_dep['Orig_dep_hora'].str[4:7]
        df_dep['Escala'] = df_dep['Orig_dep_hora'].str[7:]

        df_dep.drop(columns =['Orig_dep_hora','Assentos_equipamento'],inplace = True)
        df_dep['Hora'] = df_dep['Hora'].astype(str)
        df_dep['Hora'] = df_dep['Hora'].str.rjust(4,'0')
        df_dep['Hora'] = df_dep['Hora'].str[:2] + ':' + df_dep['Hora'].str[-2:]
        df_dep['Arr_Dep'] = 'D'
        df_voos = df_arr._append(df_dep)
        df_voos.reset_index(inplace = True)
        df_voos.set_index('index', inplace = True)

        #Inserindo companhias aéreas
        # Criando uma lista de condicoes
        conditions = [
            (df_voos['N_Voo'].str.startswith('AD')),
            (df_voos['N_Voo'].str.startswith('AZ')),
            (df_voos['N_Voo'].str.startswith('2F')),
            (df_voos['N_Voo'].str.startswith('TP')),
            (df_voos['N_Voo'].str.startswith('WD')),
            (df_voos['N_Voo'].str.startswith('VR')),
            (df_voos['N_Voo'].str.startswith('UX')),
            (df_voos['N_Voo'].str.startswith('SID')),
            (df_voos['N_Voo'].str.startswith('JJ')),
            (df_voos['N_Voo'].str.startswith('G3')),
            (df_voos['N_Voo'].str.startswith('GEC')),
            (df_voos['N_Voo'].str.startswith('CM')),
            (df_voos['N_Voo'].str.startswith('2Z')),
            (df_voos['N_Voo'].str.startswith('IPM')),
            (df_voos['N_Voo'].str.startswith('BRU')),
            (df_voos['N_Voo'].str.startswith('CV')),
            (df_voos['N_Voo'].str.startswith('FP')),
            (df_voos['N_Voo'].str.startswith('L7')),
            (df_voos['N_Voo'].str.startswith('LH')),
            (df_voos['N_Voo'].str.startswith('M3')),
            (df_voos['N_Voo'].str.startswith('UC')),
            (df_voos['N_Voo'].str.startswith('VI')),
            (df_voos['N_Voo'].str.startswith('8I')),
            (df_voos['N_Voo'].str.startswith('LP')),
            (df_voos['N_Voo'].str.startswith('KL')),
            (df_voos['N_Voo'].str.startswith('7M')),
            (df_voos['N_Voo'].str.startswith('OM')),
            (df_voos['N_Voo'].str.startswith('JMK')),
            (df_voos['N_Voo'].str.startswith('5K')),
            (df_voos['N_Voo'].str.startswith('5Y')),
            (df_voos['N_Voo'].str.startswith('AQZ')),
            (df_voos['N_Voo'].str.startswith('TTL')),
            (df_voos['N_Voo'].str.startswith('LO')),
            (df_voos['N_Voo'].str.startswith('TK')),
            (df_voos['N_Voo'].str.startswith('XL')),
            (df_voos['N_Voo'].str.startswith('ZP')),
            (df_voos['N_Voo'].str.startswith('LV')),
            (df_voos['N_Voo'].str.startswith('4M')),
            (df_voos['N_Voo'].str.startswith('AA')),
            (df_voos['N_Voo'].str.startswith('UA')),
            (df_voos['N_Voo'].str.startswith('TA')),
            (df_voos['N_Voo'].str.startswith('SA')),
            (df_voos['N_Voo'].str.startswith('A0')),
            (df_voos['N_Voo'].str.startswith('QR')),
            (df_voos['N_Voo'].str.startswith('AC')),
            (df_voos['N_Voo'].str.startswith('AF')),
            (df_voos['N_Voo'].str.startswith('PZ')),
            (df_voos['N_Voo'].str.startswith('AM')),
            (df_voos['N_Voo'].str.startswith('OB')),
            (df_voos['N_Voo'].str.startswith('AR')),
            (df_voos['N_Voo'].str.startswith('O6')),
            (df_voos['N_Voo'].str.startswith('AT')),
            (df_voos['N_Voo'].str.startswith('LX')),
            (df_voos['N_Voo'].str.startswith('LA')),
            (df_voos['N_Voo'].str.startswith('AV')),
            (df_voos['N_Voo'].str.startswith('BA')),
            (df_voos['N_Voo'].str.startswith('IB')),
            (df_voos['N_Voo'].str.startswith('CA')),
            (df_voos['N_Voo'].str.startswith('H2')),
            (df_voos['N_Voo'].str.startswith('DL')),
            (df_voos['N_Voo'].str.startswith('ET')),
            (df_voos['N_Voo'].str.startswith('DT')),
            (df_voos['N_Voo'].str.startswith('EK')),
            (df_voos['N_Voo'].str.startswith('6C')),
            (df_voos['N_Voo'].str.startswith('T0')),
            (df_voos['N_Voo'].str.startswith('FO')),
            (df_voos['N_Voo'].str.startswith('PLM')),
            (df_voos['N_Voo'].str.startswith('XX')),
            (df_voos['N_Voo'].str.startswith('TE')),
            (df_voos['N_Voo'].str.startswith('0T')),
            (df_voos['N_Voo'].str.startswith('AEC')),
            (df_voos['N_Voo'].str.startswith('WJ'))
            ]

        # Criando os valores para as colunas
        values = ['Azul','Alitalia','Conecta','TAP','Modern Logistics','Cabo Verde Airlines','Air Europa','Sideral','Latam','Gol','Lufthansa Cargo','Copa Airlines','Voe Pass','Itapemirim',
                'Belavia','CargoLux','FlyPelican','Latam Cargo Colombia','Lufthansa','Latam Cargo','Latam Cargo Chile','Volga-Dnepr Airlines','Itapemirim','Latam Cargo Peru','KLM','Voe Pass'
                ,'OMI','JetMagic','Hifly','Atlas Air','Air Italia','Total Linhas Aereas','LOT Polish Airlines','Turkish Airlines','Lan Ecuador','Paranair','Levu','Latam Argentina',
                'American Airlines','United','Avianca El Salvador','South African Airways','Aerolineas Argentinas','Qatar Airways','Air Canada','Air France','Latam Paraguay','Aeromexico',
                'Boliviana de Aviacion','Aerolineas Argentinas','Avianca Brasil','Royal Air Marroc','Swiss','Latam Airlines','Avianca','British Airways','Iberia','Air China','Sky Airline',
                'Delta','Ethiopian Airlines','TAAG Angola','Emirates','Centrafrrique Air Express','Taca','Aero','Wammos Air','Voos Teste','Sky Taxi','Total Linhas Aereas','ACE Skyline',
                'JetSmart']

        # Criando a nova columa é usando o np.select com as condições e as listas de argumentos
        df_voos['Cia'] = np.select(conditions, values, default='Outra')


        # Criando uma lista de condicoes
        conditions = [
            (df_voos['Hora'].str.startswith('00')),
            (df_voos['Hora'].str.startswith('01')),
            (df_voos['Hora'].str.startswith('02')),
            (df_voos['Hora'].str.startswith('03')),
            (df_voos['Hora'].str.startswith('04')),
            (df_voos['Hora'].str.startswith('05')),
            (df_voos['Hora'].str.startswith('06')),
            (df_voos['Hora'].str.startswith('07')),
            (df_voos['Hora'].str.startswith('08')),
            (df_voos['Hora'].str.startswith('09')),
            (df_voos['Hora'].str.startswith('10')),
            (df_voos['Hora'].str.startswith('11')),
            (df_voos['Hora'].str.startswith('12')),
            (df_voos['Hora'].str.startswith('13')),
            (df_voos['Hora'].str.startswith('14')),
            (df_voos['Hora'].str.startswith('15')),
            (df_voos['Hora'].str.startswith('16')),
            (df_voos['Hora'].str.startswith('17')),
            (df_voos['Hora'].str.startswith('18')),
            (df_voos['Hora'].str.startswith('19')),
            (df_voos['Hora'].str.startswith('20')),
            (df_voos['Hora'].str.startswith('21')),
            (df_voos['Hora'].str.startswith('22')),
            (df_voos['Hora'].str.startswith('23')),


            ]

        # Criando os valores para as colunas
        values = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]

        # Criando a nova columa é usando o np.select com as condições e as listas de argumentos
        df_voos['bucket'] = np.select(conditions, values)

        # Criando uma lista de condicoes para dias da semana
        conditions = [
            (df_voos['dia'].str.startswith('Monday')),
            (df_voos['dia'].str.startswith('Tuesday')),
            (df_voos['dia'].str.startswith('Wednesday')),
            (df_voos['dia'].str.startswith('Thursday')),
            (df_voos['dia'].str.startswith('Friday')),
            (df_voos['dia'].str.startswith('Saturday')),
            (df_voos['dia'].str.startswith('Sunday')),
            ]

        # Criando os valores para as colunas
        values = ["Seg","Ter","Qua","Qui","Sex","Sab","Dom"]

        # Criando a nova columa é usando o np.select com as condições e as listas de argumentos
        df_voos['dia'] = np.select(conditions, values, default="None")


        #Classificação por dia da semana
        conditions = [
        (df_voos['bucket'] <= 6 ),
        ((df_voos['bucket'] >= 6) & (df_voos['bucket'] < 12) ),
        ((df_voos['bucket'] >= 12) & (df_voos['bucket'] < 18) ),
        ((df_voos['bucket'] >= 18) & (df_voos['bucket'] <= 24)  ),
        ]

        # Criando os valores para as colunas
        values = ['Madrugada','Manha','Tarde','Noite']

        # Criando a nova columa é usando o np.select com as condições e as listas de argumentos
        df_voos['Periodo'] = np.select(conditions, values,default='None')

        df_voos['Mês'] = df_voos['data_op'].dt.month
        df_voos['Zona'] = 'D'

        #Origem e destinos
        #destinos
        conditions = [
            (df_voos['Cia'] == 'TAP'),
            (df_voos['Orig_Dest'] == 'SET' ),
            (df_voos['Orig_Dest'] == 'JPO' ),
            (df_voos['Orig_Dest'] == 'MCZ' ),
            (df_voos['Orig_Dest'] == 'BSB' ),
            (df_voos['Orig_Dest'] == 'VCP' ),
            (df_voos['Orig_Dest'] == 'VIX' ),
            (df_voos['Orig_Dest'] == 'UDI' ),
            (df_voos['Orig_Dest'] == 'SJP' ),
            (df_voos['Orig_Dest'] == 'POA' ),
            (df_voos['Orig_Dest'] == 'GYN' ),
            (df_voos['Orig_Dest'] == 'RAO' ),
            (df_voos['Orig_Dest'] == 'NAT' ),
            (df_voos['Orig_Dest'] == 'CNF' ),
            (df_voos['Orig_Dest'] == 'CPV' ),
            (df_voos['Orig_Dest'] == 'SDU' ),
            (df_voos['Orig_Dest'] == 'MAO' ),
            (df_voos['Orig_Dest'] == 'AJU' ),
            (df_voos['Orig_Dest'] == 'JPA' ),
            (df_voos['Orig_Dest'] == 'JDO' ),
            (df_voos['Orig_Dest'] == 'SSA' ),
            (df_voos['Orig_Dest'] == 'GRU' ),
            (df_voos['Orig_Dest'] == 'THE' ),
            (df_voos['Orig_Dest'] == 'FOR' ),
            (df_voos['Orig_Dest'] == 'CGB' ),
            (df_voos['Orig_Dest'] == 'SLZ' ),
            (df_voos['Orig_Dest'] == 'FEN' ),
            (df_voos['Orig_Dest'] == 'PNZ' ),
            (df_voos['Orig_Dest'] == 'IMP' ),
            (df_voos['Orig_Dest'] == 'STM' ),
            (df_voos['Orig_Dest'] == 'MVF' ),
            (df_voos['Orig_Dest'] == 'REC' ),
            (df_voos['Orig_Dest'] == 'PMW' ),
            (df_voos['Orig_Dest'] == 'GIG' ),
            (df_voos['Orig_Dest'] == 'AVR' ),
            (df_voos['Orig_Dest'] == 'MXP' ),
            (df_voos['Orig_Dest'] == 'FCO' ),
            (df_voos['Orig_Dest'] == 'PTY' ),
            (df_voos['Orig_Dest'] == 'CWB' ),
            (df_voos['Orig_Dest'] == 'MIA' ),
            (df_voos['Orig_Dest'] == 'SJK' ),
            (df_voos['Orig_Dest'] == 'LIM' ),
            (df_voos['Orig_Dest'] == 'LIS' ),
            (df_voos['Orig_Dest'] == 'SID' ),
            (df_voos['Orig_Dest'] == 'CAU' ),
            (df_voos['Orig_Dest'] == 'QDV' ),
            (df_voos['Orig_Dest'] == 'LUX' ),
            (df_voos['Orig_Dest'] == 'SCL' ),
            (df_voos['Orig_Dest'] == 'ACC' ),
            (df_voos['Orig_Dest'] == 'BOG' ),
            (df_voos['Orig_Dest'] == 'OPO' ),
            (df_voos['Orig_Dest'] == 'ABJ' ),
            (df_voos['Orig_Dest'] == 'FRA' ),
            (df_voos['Orig_Dest'] == 'QSC' ),
            (df_voos['Orig_Dest'] == 'TFS' ),
            (df_voos['Orig_Dest'] == 'IOS' ),
            (df_voos['Orig_Dest'] == 'MDE' ),
            (df_voos['Orig_Dest'] == 'BEL' ),
            (df_voos['Escala'] == 'BAQ' ),
            (df_voos['Escala'] == 'PDL' ),
            (df_voos['Orig_Dest'] == 'CGH' ),
            (df_voos['Orig_Dest'] == 'JJD' ),
            (df_voos['Orig_Dest'] == 'PHB' ),
            (df_voos['Orig_Dest'] == 'BVB' ),
            (df_voos['Orig_Dest'] == 'UBA' ),
            (df_voos['Orig_Dest'] == 'CGR' ),
            (df_voos['Orig_Dest'] == 'PPB' ),
            (df_voos['Orig_Dest'] == 'EZE' ),
            (df_voos['Orig_Dest'] == 'PVH' ),
            (df_voos['Orig_Dest'] == 'FLN' ),
            (df_voos['Orig_Dest'] == 'MCP' ),
            (df_voos['Orig_Dest'] == 'LDB' ),
            (df_voos['Orig_Dest'] == 'BPS' ),
            (df_voos['Orig_Dest'] == 'ARX' ),
            (df_voos['Orig_Dest'] == 'CPT' ),
            (df_voos['Orig_Dest'] == 'PUQ' ),
            (df_voos['Orig_Dest'] == 'AEP' ),
            (df_voos['Orig_Dest'] == 'MAD' ),
            (df_voos['Orig_Dest'] == 'MVD' ),
            (df_voos['Orig_Dest'] == 'ARU' ),
            (df_voos['Orig_Dest'] == 'MEX' ),
            (df_voos['Orig_Dest'] == 'QGP' ),
            (df_voos['Orig_Dest'] == 'GNM' ),
            (df_voos['Orig_Dest'] == 'VVI' ),
            (df_voos['Orig_Dest'] == 'CKY' ),
            (df_voos['Orig_Dest'] == 'TUN' ),
            (df_voos['Orig_Dest'] == 'ARU' ),
            (df_voos['Orig_Dest'] == 'JTC' ),
            (df_voos['Orig_Dest'] == 'IGU' ),
            (df_voos['Orig_Dest'] == 'DSS' ),
            (df_voos['Orig_Dest'] == 'JAW' ),
            (df_voos['Orig_Dest'] == 'NSR' ),
            (df_voos['Orig_Dest'] == 'FEC' ),
            (df_voos['Orig_Dest'] == 'PAV' ),
            (df_voos['Orig_Dest'] == 'CAC' ),
            (df_voos['Orig_Dest'] == 'UBA' ),
            (df_voos['Orig_Dest'] == 'LDB' ),
            (df_voos['Orig_Dest'] == 'PUC' ),
            (df_voos['Orig_Dest'] == 'TNG' ),
            (df_voos['Orig_Dest'] == 'UIO' ),
            (df_voos['Orig_Dest'] == 'FLL' ),
            (df_voos['Orig_Dest'] == 'CFB' ),
            (df_voos['Orig_Dest'] == 'LPA' ),
            (df_voos['Escala'] == 'EZE' ),
            (df_voos['Escala'] == 'AEP' ),
            (df_voos['Escala'] == 'RAI' ),
            (df_voos['Escala'] == 'MCO' ),
            (df_voos['Escala'] == 'TUC' ),
            (df_voos['Escala'] == 'FUE' ),
            (df_voos['Escala'] == 'VAL' ),
            (df_voos['Escala'] == 'CKJ' ),
            (df_voos['Escala'] == 'RRJ' ),
            (df_voos['Escala'] == 'UNA' ),
            (df_voos['Escala'] == 'IPN' ),
            (df_voos['Escala'] == 'NVT' ),
            (df_voos['Escala'] == 'MOC' ),
            (df_voos['Escala'] == 'CLV' ),
            (df_voos['Escala'] == 'BYO' ),
            (df_voos['Escala'] == 'JJG' ),
            (df_voos['Escala'] == 'JOI' ),
            (df_voos['Escala'] == 'IZA' ),
            (df_voos['Escala'] == 'CXJ' ),
            (df_voos['Escala'] == 'MGF' ),
            (df_voos['Escala'] == 'RIA' ),
            (df_voos['Escala'] == 'TXF' ),
            (df_voos['Escala'] == 'URG' ),
            (df_voos['Orig_Dest'] == 'BYO' ),
            (df_voos['Orig_Dest'] == 'ITB' ),
            (df_voos['Orig_Dest'] == 'TMT' ),
            (df_voos['Orig_Dest'] == 'BSE' ),
            (df_voos['Orig_Dest'] == 'XAP' ),
            (df_voos['Orig_Dest'] == 'CJZ' ),
            (df_voos['Orig_Dest'] == 'BZC' ),
            (df_voos['Orig_Dest'] == 'OIA' ),
            (df_voos['Orig_Dest'] == 'PFB' ),
            (df_voos['Orig_Dest'] == 'IST' ),
            (df_voos['Orig_Dest'] == 'ASU' ),
            (df_voos['Orig_Dest'] == 'PIN' ),
            (df_voos['Orig_Dest'] == 'CMN' ),
            (df_voos['Orig_Dest'] == 'RRJ' ),
            (df_voos['Orig_Dest'] == 'PET' ),
            (df_voos['Orig_Dest'] == 'QNS' ),
            (df_voos['Orig_Dest'] == 'GEL' ),
            (df_voos['Orig_Dest'] == 'GYE' ),
            (df_voos['Orig_Dest'] == 'VDC' ),
            (df_voos['Orig_Dest'] == 'IAD' ),
            (df_voos['Orig_Dest'] == 'LAX' ),
            (df_voos['Orig_Dest'] == 'ORD' ),
            (df_voos['Orig_Dest'] == 'JFK' ),
            (df_voos['Orig_Dest'] == 'EWR' ),
            (df_voos['Orig_Dest'] == 'DFW' ),
            (df_voos['Orig_Dest'] == 'IAH' ),
            (df_voos['Orig_Dest'] == 'YYZ' ),
            (df_voos['Orig_Dest'] == 'JNB' ),
            (df_voos['Orig_Dest'] == 'CDG' ),
            (df_voos['Orig_Dest'] == 'DOH' ),
            (df_voos['Orig_Dest'] == 'CBB' ),
            (df_voos['Orig_Dest'] == 'LHR' ),
            (df_voos['Orig_Dest'] == 'PEK' ),
            (df_voos['Orig_Dest'] == 'MAD' ),
            (df_voos['Orig_Dest'] == 'ZRH' ),
            (df_voos['Orig_Dest'] == 'ATL' ),
            (df_voos['Orig_Dest'] == 'LAD' ),
            (df_voos['Orig_Dest'] == 'TLV' ),
            (df_voos['Orig_Dest'] == 'DXB' ),
            (df_voos['Orig_Dest'] == 'AMS' ),
            (df_voos['Orig_Dest'] == 'BRC' ),
            (df_voos['Orig_Dest'] == 'ADD' ),
            (df_voos['Orig_Dest'] == 'RBR' ),
            (df_voos['Orig_Dest'] == 'MUC' ),
            (df_voos['Orig_Dest'] == 'MDZ' ),
            (df_voos['Orig_Dest'] == 'BOS' ),
            (df_voos['Orig_Dest'] == 'PUJ' ),
            (df_voos['Orig_Dest'] == 'PDP' ),
            (df_voos['Orig_Dest'] == 'ROS' ),
            (df_voos['Orig_Dest'] == 'COR' ),
            (df_voos['Orig_Dest'] == 'BCN' ),
            (df_voos['Orig_Dest'] == 'LAS' ),
            (df_voos['Orig_Dest'] == 'OPS' ),
            (df_voos['Orig_Dest'] == 'SBD' ),
            (df_voos['Orig_Dest'] == 'EPA' ),
            (df_voos['Orig_Dest'] == 'DOU' ),
            (df_voos['Orig_Dest'] == 'FDF' ),
            (df_voos['Orig_Dest'] == 'YUL' ),
            (df_voos['Orig_Dest'] == 'LGG' ),
            (df_voos['Orig_Dest'] == 'RVD' ),
            (df_voos['Orig_Dest'] == 'MAB' ),
            (df_voos['Orig_Dest'] == 'MPN' ),
            (df_voos['Orig_Dest'] == 'RAK' ),
            (df_voos['Orig_Dest'] == 'MBJ' ),
            (df_voos['Orig_Dest'] == 'AUH' ),
            (df_voos['Orig_Dest'] == 'BQN' ),
            (df_voos['Orig_Dest'] == 'HAV' ),
            (df_voos['Orig_Dest'] == 'ISL' ),
            (df_voos['Orig_Dest'] == 'LOS' ),
            (df_voos['Orig_Dest'] == 'SJO' ),
            (df_voos['Orig_Dest'] == 'DWC' ),
            (df_voos['Orig_Dest'] == 'BSL' ),
            (df_voos['Orig_Dest'] == 'PTP' ),
            (df_voos['Orig_Dest'] == 'SJU' ),
            (df_voos['Orig_Dest'] == 'MGF' ),
            (df_voos['Orig_Dest'] == 'POS' ),
            (df_voos['Orig_Dest'] == 'BYJ' ),
            (df_voos['Orig_Dest'] == 'BGA' ),
            (df_voos['Orig_Dest'] == 'MLA' ),
            (df_voos['Orig_Dest'] == 'ANF' ),
            (df_voos['Orig_Dest'] == 'WDH' ),
            (df_voos['Orig_Dest'] == 'ALG' ),
            (df_voos['Orig_Dest'] == 'FAO' ),
            (df_voos['Orig_Dest'] == 'TEV' ),
            (df_voos['Orig_Dest'] == 'EEA' ),
            (df_voos['Orig_Dest'] == 'USH' ),
            (df_voos['Orig_Dest'] == 'FAB' ),


            ]

        # Criando os valores para as colunas
        values = ['I','D','D','D','D','D','D','D','D','D','D','D','D','D','D','D','D','D',
                'D','D','D','D','D','D','D','D','D','D','D','D','D','D','D','D','I',
                'I','I','I','D','I','D','I','I','I','D','D','I','I','I','I','I','I',
                'I','D','I','D','I','D','I','I','D','D','D','D','D','D','D','I','D','D',
                'D','D','D','D','I','I','I','I','I','D','I','D','D','I','I','I','D','D','D','I','D','D','D','D','D'
                ,'D','D','I','I','I','I','D','I','I','I','I','I','I','I','D','D','D','D','D','D','D','D','D','D','D'
                ,'D','D','D','D','D','D','D','D','D','D','D','D','D','D','D','I','I','D','I','D','D','D','D','I','D'
                ,'I','I','I','I','I','I','I','I','I','I','I','I','I','I','I','I','I','I','I','I','I','I','I','D','I'
                ,'I','I','I','I','I','I','I','I','D','I','I','D','I','I','I','D','D','I','I','I','I','I','I','I','I'
                ,'I','I','I','I','I','D','I','I','I','I','I','I','I','I','I','D','I','I'

                ]
        # Criando a nova columa é usando o np.select com as condições e as listas de argumentos
        df_voos['Zona'] = np.select(conditions, values,default='None')

        Conditions = [
        (df_voos['Orig_Dest'] == df_voos['Escala']),
        (df_voos['Orig_Dest'] != df_voos['Escala']),
        ]

        # Criando os valores para as colunas
        values = ['Voo Direto','Voo Com escala']

        # Criando a nova columa é usando o np.select com as condições e as listas de argumentos
        df_voos['Direto_Escala'] = np.select(Conditions, values, default='None')

        #destinos
        conditions = [
            (df_voos['Orig_Dest'] == 'LIS'),
            (df_voos['Orig_Dest'] == 'SET' ),
            (df_voos['Orig_Dest'] == 'JPO' ),
            (df_voos['Orig_Dest'] == 'MCZ' ),
            (df_voos['Orig_Dest'] == 'BSB' ),
            (df_voos['Orig_Dest'] == 'VCP' ),
            (df_voos['Orig_Dest'] == 'VIX' ),
            (df_voos['Orig_Dest'] == 'UDI' ),
            (df_voos['Orig_Dest'] == 'SJP' ),
            (df_voos['Orig_Dest'] == 'POA' ),
            (df_voos['Orig_Dest'] == 'GYN' ),
            (df_voos['Orig_Dest'] == 'RAO' ),
            (df_voos['Orig_Dest'] == 'NAT' ),
            (df_voos['Orig_Dest'] == 'CNF' ),
            (df_voos['Orig_Dest'] == 'CPV' ),
            (df_voos['Orig_Dest'] == 'SDU' ),
            (df_voos['Orig_Dest'] == 'MAO' ),
            (df_voos['Orig_Dest'] == 'AJU' ),
            (df_voos['Orig_Dest'] == 'JPA' ),
            (df_voos['Orig_Dest'] == 'JDO' ),
            (df_voos['Orig_Dest'] == 'SSA' ),
            (df_voos['Orig_Dest'] == 'GRU' ),
            (df_voos['Orig_Dest'] == 'THE' ),
            (df_voos['Orig_Dest'] == 'FOR' ),
            (df_voos['Orig_Dest'] == 'CGB' ),
            (df_voos['Orig_Dest'] == 'SLZ' ),
            (df_voos['Orig_Dest'] == 'FEN' ),
            (df_voos['Orig_Dest'] == 'PNZ' ),
            (df_voos['Orig_Dest'] == 'IMP' ),
            (df_voos['Orig_Dest'] == 'STM' ),
            (df_voos['Orig_Dest'] == 'MVF' ),
            (df_voos['Orig_Dest'] == 'REC' ),
            (df_voos['Orig_Dest'] == 'PMW' ),
            (df_voos['Orig_Dest'] == 'GIG' ),
            (df_voos['Orig_Dest'] == 'AVR' ),
            (df_voos['Orig_Dest'] == 'MXP' ),
            (df_voos['Orig_Dest'] == 'FCO' ),
            (df_voos['Orig_Dest'] == 'PTY' ),
            (df_voos['Orig_Dest'] == 'CWB' ),
            (df_voos['Orig_Dest'] == 'MIA' ),
            (df_voos['Orig_Dest'] == 'SJK' ),
            (df_voos['Orig_Dest'] == 'LIM' ),
            (df_voos['Orig_Dest'] == 'LIS' ),
            (df_voos['Orig_Dest'] == 'SID' ),
            (df_voos['Orig_Dest'] == 'CAU' ),
            (df_voos['Orig_Dest'] == 'QDV' ),
            (df_voos['Orig_Dest'] == 'LUX' ),
            (df_voos['Orig_Dest'] == 'SCL' ),
            (df_voos['Orig_Dest'] == 'ACC' ),
            (df_voos['Orig_Dest'] == 'BOG' ),
            (df_voos['Orig_Dest'] == 'OPO' ),
            (df_voos['Orig_Dest'] == 'ABJ' ),
            (df_voos['Orig_Dest'] == 'FRA' ),
            (df_voos['Orig_Dest'] == 'QSC' ),
            (df_voos['Orig_Dest'] == 'TFS' ),
            (df_voos['Orig_Dest'] == 'IOS' ),
            (df_voos['Orig_Dest'] == 'MDE' ),
            (df_voos['Orig_Dest'] == 'BEL' ),
            (df_voos['Escala'] == 'BAQ' ),
            (df_voos['Escala'] == 'PDL' ),
            (df_voos['Orig_Dest'] == 'CGH' ),
            (df_voos['Orig_Dest'] == 'JJD' ),
            (df_voos['Orig_Dest'] == 'PHB' ),
            (df_voos['Orig_Dest'] == 'BVB' ),
            (df_voos['Orig_Dest'] == 'UBA' ),
            (df_voos['Orig_Dest'] == 'CGR' ),
            (df_voos['Orig_Dest'] == 'PPB' ),
            (df_voos['Orig_Dest'] == 'EZE' ),
            (df_voos['Orig_Dest'] == 'PVH' ),
            (df_voos['Orig_Dest'] == 'FLN' ),
            (df_voos['Orig_Dest'] == 'MCP' ),
            (df_voos['Orig_Dest'] == 'LDB' ),
            (df_voos['Orig_Dest'] == 'BPS' ),
            (df_voos['Orig_Dest'] == 'ARX' ),
            (df_voos['Orig_Dest'] == 'CPT' ),
            (df_voos['Orig_Dest'] == 'PUQ' ),
            (df_voos['Orig_Dest'] == 'AEP' ),
            (df_voos['Orig_Dest'] == 'MAD' ),
            (df_voos['Orig_Dest'] == 'MVD' ),
            (df_voos['Orig_Dest'] == 'ARU' ),
            (df_voos['Orig_Dest'] == 'MEX' ),
            (df_voos['Orig_Dest'] == 'QGP' ),
            (df_voos['Orig_Dest'] == 'GNM' ),
            (df_voos['Orig_Dest'] == 'VVI' ),
            (df_voos['Orig_Dest'] == 'CKY' ),
            (df_voos['Orig_Dest'] == 'TUN' ),
            (df_voos['Orig_Dest'] == 'ARU' ),
            (df_voos['Orig_Dest'] == 'JTC' ),
            (df_voos['Orig_Dest'] == 'IGU' ),
            (df_voos['Orig_Dest'] == 'DSS' ),
            (df_voos['Orig_Dest'] == 'JAW' ),
            (df_voos['Orig_Dest'] == 'NSR' ),
            (df_voos['Orig_Dest'] == 'FEC' ),
            (df_voos['Orig_Dest'] == 'PAV' ),
            (df_voos['Orig_Dest'] == 'CAC' ),
            (df_voos['Orig_Dest'] == 'UBA' ),
            (df_voos['Orig_Dest'] == 'LDB' ),
            (df_voos['Orig_Dest'] == 'PUC' ),
            (df_voos['Orig_Dest'] == 'TNG' ),
            (df_voos['Orig_Dest'] == 'UIO' ),
            (df_voos['Orig_Dest'] == 'FLL' ),
            (df_voos['Orig_Dest'] == 'CFB' ),
            (df_voos['Orig_Dest'] == 'LPA' ),
            (df_voos['Escala'] == 'EZE' ),
            (df_voos['Escala'] == 'AEP' ),
            (df_voos['Escala'] == 'RAI' ),
            (df_voos['Escala'] == 'MCO' ),
            (df_voos['Escala'] == 'TUC' ),
            (df_voos['Escala'] == 'FUE' ),
            (df_voos['Escala'] == 'VAL' ),
            (df_voos['Escala'] == 'CKJ' ),
            (df_voos['Escala'] == 'RRJ' ),
            (df_voos['Escala'] == 'UNA' ),
            (df_voos['Escala'] == 'IPN' ),
            (df_voos['Escala'] == 'NVT' ),
            (df_voos['Escala'] == 'MOC' ),
            (df_voos['Escala'] == 'CLV' ),
            (df_voos['Escala'] == 'BYO' ),
            (df_voos['Escala'] == 'JJG' ),
            (df_voos['Escala'] == 'JOI' ),
            (df_voos['Escala'] == 'IZA' ),
            (df_voos['Escala'] == 'CXJ' ),
            (df_voos['Escala'] == 'MGF' ),
            (df_voos['Escala'] == 'RIA' ),
            (df_voos['Escala'] == 'TXF' ),
            (df_voos['Escala'] == 'URG' ),
            (df_voos['Orig_Dest'] == 'BYO' ),
            (df_voos['Orig_Dest'] == 'ITB' ),
            (df_voos['Orig_Dest'] == 'TMT' ),
            (df_voos['Orig_Dest'] == 'BSE' ),
            (df_voos['Orig_Dest'] == 'XAP' ),
            (df_voos['Orig_Dest'] == 'CJZ' ),
            (df_voos['Orig_Dest'] == 'BZC' ),
            (df_voos['Orig_Dest'] == 'OIA' ),
            (df_voos['Orig_Dest'] == 'PFB' ),
            (df_voos['Orig_Dest'] == 'IST' ),
            (df_voos['Orig_Dest'] == 'ASU' ),
            (df_voos['Orig_Dest'] == 'PIN' ),
            (df_voos['Orig_Dest'] == 'CMN' ),
            (df_voos['Orig_Dest'] == 'RRJ' ),
            (df_voos['Orig_Dest'] == 'PET' ),
            (df_voos['Orig_Dest'] == 'QNS' ),
            (df_voos['Orig_Dest'] == 'GEL' ),
            (df_voos['Orig_Dest'] == 'GYE' ),
            (df_voos['Orig_Dest'] == 'VDC' ),
            (df_voos['Orig_Dest'] == 'IAD' ),
            (df_voos['Orig_Dest'] == 'LAX' ),
            (df_voos['Orig_Dest'] == 'ORD' ),
            (df_voos['Orig_Dest'] == 'JFK' ),
            (df_voos['Orig_Dest'] == 'EWR' ),
            (df_voos['Orig_Dest'] == 'DFW' ),
            (df_voos['Orig_Dest'] == 'IAH' ),
            (df_voos['Orig_Dest'] == 'YYZ' ),
            (df_voos['Orig_Dest'] == 'JNB' ),
            (df_voos['Orig_Dest'] == 'CDG' ),
            (df_voos['Orig_Dest'] == 'DOH' ),
            (df_voos['Orig_Dest'] == 'CBB' ),
            (df_voos['Orig_Dest'] == 'LHR' ),
            (df_voos['Orig_Dest'] == 'PEK' ),
            (df_voos['Orig_Dest'] == 'MAD' ),
            (df_voos['Orig_Dest'] == 'ZRH' ),
            (df_voos['Orig_Dest'] == 'ATL' ),
            (df_voos['Orig_Dest'] == 'LAD' ),
            (df_voos['Orig_Dest'] == 'TLV' ),
            (df_voos['Orig_Dest'] == 'DXB' ),
            (df_voos['Orig_Dest'] == 'AMS' ),
            (df_voos['Orig_Dest'] == 'BRC' ),
            (df_voos['Orig_Dest'] == 'ADD' ),
            (df_voos['Orig_Dest'] == 'RBR' ),
            (df_voos['Orig_Dest'] == 'MUC' ),
            (df_voos['Orig_Dest'] == 'MDZ' ),
            (df_voos['Orig_Dest'] == 'BOS' ),
            (df_voos['Orig_Dest'] == 'PUJ' ),
            (df_voos['Orig_Dest'] == 'PDP' ),
            (df_voos['Orig_Dest'] == 'ROS' ),
            (df_voos['Orig_Dest'] == 'COR' ),
            (df_voos['Orig_Dest'] == 'BCN' ),
            (df_voos['Orig_Dest'] == 'LAS' ),
            (df_voos['Orig_Dest'] == 'OPS' ),
            (df_voos['Orig_Dest'] == 'SBD' ),
            (df_voos['Orig_Dest'] == 'EPA' ),
            (df_voos['Orig_Dest'] == 'DOU' ),
            (df_voos['Orig_Dest'] == 'FDF' ),
            (df_voos['Orig_Dest'] == 'YUL' ),
            (df_voos['Orig_Dest'] == 'LGG' ),
            (df_voos['Orig_Dest'] == 'RVD' ),
            (df_voos['Orig_Dest'] == 'MAB' ),
            (df_voos['Orig_Dest'] == 'MPN' ),
            (df_voos['Orig_Dest'] == 'RAK' ),
            (df_voos['Orig_Dest'] == 'MBJ' ),
            (df_voos['Orig_Dest'] == 'AUH' ),
            (df_voos['Orig_Dest'] == 'BQN' ),
            (df_voos['Orig_Dest'] == 'HAV' ),
            (df_voos['Orig_Dest'] == 'ISL' ),
            (df_voos['Orig_Dest'] == 'LOS' ),
            (df_voos['Orig_Dest'] == 'SJO' ),
            (df_voos['Orig_Dest'] == 'DWC' ),
            (df_voos['Orig_Dest'] == 'BSL' ),
            (df_voos['Orig_Dest'] == 'PTP' ),
            (df_voos['Orig_Dest'] == 'SJU' ),
            (df_voos['Orig_Dest'] == 'MGF' ),
            (df_voos['Orig_Dest'] == 'EEA' ),
            (df_voos['Orig_Dest'] == 'USH' ),
            (df_voos['Orig_Dest'] == 'FAB' ),
            
        ]

        values = [
            'Lisboa',  # TAP
            'Serra Talhada (PE)',  # SET
            'João Pessoa (PB)',  # JPO
            'Maceió (AL)',  # MCZ
            'Brasília',  # BSB
            'Campinas (SP)',  # VCP
            'Vitória (ES)',  # VIX
            'Uberlândia (MG)',  # UDI
            'São José do Rio Preto (SP)',  # SJP
            'Porto Alegre (RS)',  # POA
            'Goiânia (GO)',  # GYN
            'Ribeirão Preto (SP)',  # RAO
            'Natal (RN)',  # NAT
            'Confins (MG)',  # CNF
            'Campina Grande (PB)',  # CPV
            'Rio de Janeiro (Santos Dumont) - RJ',  # SDU
            'Manaus (AM)',  # MAO
            'Aracaju (SE)',  # AJU
            'João Pessoa (PB)',  # JPA
            'Juazeiro do Norte (CE)',  # JDO
            'Salvador (BA)',  # SSA
            'São Paulo (Guarulhos) (SP)',  # GRU
            'Teresina (PI)',  # THE
            'Fortaleza (CE)',  # FOR
            'Cuiabá (MT)',  # CGB
            'São Luís (MA)',  # SLZ
            'Fernando de Noronha (PE)',  # FEN
            'Petrolina (PE)',  # PNZ
            'Imperatriz (PE)',  # IMP
            'Santarém (PA)',  # STM
            'Mossoró (RN)',  # MVF
            'Recife (PE)',  # REC
            'Palmas (TO)',  # PMW
            'Rio de Janeiro (Galeão) (RJ)',  # GIG
            'Aveiro - PT',  # AVR
            'Milão (Malpensa)',  # MXP
            'Roma (Fiumicino)',  # FCO
            'Cidade do Panamá',  # PTY
            'Curitiba (PR)',  # CWB
            'Miami',  # MIA
            'São José dos Campos (SP)',  # SJK
            'Lima',  # LIM
            'Lisboa',  # LIS
            'Praia (Cabo Verde)',  # SID
            'Caruaru (PE)',  # CAU
            'Jundiaí (SP)',  # QDV
            'Luxemburgo',  # LUX
            'Santiago - CH',  # SCL
            'Acra',  # ACC
            'Bogotá',  # BOG
            'Porto',  # OPO
            'Abidjan',  # ABJ
            'Frankfurt',  # FRA
            'São Carlos (SP)',  # QSC
            'Tenerife',  # TFS
            'Ilhéus (BA)',  # IOS
            'Medellín',  # MDE
            'Belém (PA)',  # BEL
            'Barranquilla',  # BAQ
            'Ponta Delgada',  # PDL
            'São Paulo (Congonhas) - SP',  # CGH
            'Juiz de Fora (MG)',  # JJD
            'Parnaíba (PI)',  # PHB
            'Boa Vista (RR)',  # BVB
            'Uberaba (MG)',  # UBA
            'Campo Grande (MS)',  # CGR
            'Presidente Prudente (SP)',  # PPB
            'Buenos Aires (Ezeiza)',  # EZE
            'Porto Velho (RO)',  # PVH
            'Florianópolis (SC)',  # FLN
            'Macapá (AP)',  # MCP
            'Londrina (PR)',  # LDB
            'Porto Seguro (BA)',  # BPS
            'Araxá (MG)',  # ARX
            'Cidade do Cabo',  # CPT
            'Punta Arenas',  # PUQ
            'Buenos Aires (Aeroparque)',  # AEP
            'Madri',  # MAD
            'Montevidéu',  # MVD
            'Araçatuba (SP)',  # ARU
            'Cidade do México',  # MEX
            'Garanhuns (PE)',  # QGP
            'Guanambi (BA)',  # GNM
            'Santa Cruz de la Sierra',  # VVI
            'Conakry',  # CKY
            'Túnis',  # TUN
            'Araçatuba (SP)',  # ARU (duplicado na lista original)
            'Bauru (SP)',  # JTC
            'Foz do Iguaçu (PR)',  # IGU
            'Dakar',  # DSS
            'Araripina (PE)',  # JAW
            'Natal (RN)',  # NSR
            'Feira de Santana (BA)',  # FEC
            'Paulo Afonso (BA)',  # PAV
            'Cascavel (PR)',  # CAC
            'Uberaba  (MG)',  # UBA
            'Londrina (PR)',  # LDB
            'Price',  # PUC
            'Tânger',  # TNG
            'Quito',  # UIO
            'Fort Lauderdale',  # FLL
            'Cabo Frio (RJ)',  # CFB
            'Las Palmas',  # LPA
            'Buenos Aires (Ezeiza)',  # EZE
            'Buenos Aires (Aeroparque)',  # AEP
            'Praia (Cabo Verde)',  # RAI
            'Orlando',  # MCO
            'Tucumán',  # TUC
            'Fuerteventura',  # FUE
            'Valença',  # VAL
            'Chkalovsk',  # CKJ
            'Jacarepagua (RJ)',  # RRJ
            'Una (MG)',  # UNA
            'Ipatinga (MG)',  # IPN
            'Navegantes (SC)',  # NVT
            'Montes Claros (MG)',  # MOC
            'Caldas Novas (GO)',  # CLV
            'Bonito (MS)',  # BYO
            'Jaguaruna (SC)',  # JJG
            'Joinville (SC)',  # JOI
            'Juiz de Fora (MG)',  # IZA
            'Caxias do Sul (RS)',  # CXJ
            'Maringá (PR)',  # MGF
            'Santa Maria (RS)',  # RIA
            'Teixeira de Freitas (BA)',  # TXF
            'Uruguaiana (RS)',  # URG
            'Bonito (MS)',  # BYO
            'Itabuna (BA)',  # ITB
            'Porto Trombetas (PA)',  # TMT
            'Sematan',  # BSE
            'Chapecó (PR)',  # XAP
            'Cajazeiras (PB)',  # CJZ
            'Búzios (RJ)',  # BZC
            'Ourilândia do Norte (PA)',  # OIA
            'Passo Fundo (RS)',  # PFB
            'Istambul',  # IST
            'Assunção',  # ASU
            'Parintins (AM)',  # PIN
            'Casablanca',  # CMN
            'Jacarepagua (RJ)',  # RRJ
            'Pelotas (RS)',  # PET
            'Canoas (RS)',  # QNS
            'Santo Ângelo (RS)',  # GEL
            'Guayaquil',  # GYE
            'Vitória da Conquista (BA)',  # VDC
            'Washington (Dulles)',  # IAD
            'Los Angeles',  # LAX
            'Chicago (O\'Hare)',  # ORD
            'Nova York (JFK)',  # JFK
            'Newark',  # EWR
            'Dallas/Fort Worth',  # DFW
            'Houston',  # IAH
            'Toronto',  # YYZ
            'Joanesburgo',  # JNB
            'Paris (Charles de Gaulle)',  # CDG
            'Doha',  # DOH
            'Cochabamba',  # CBB
            'Londres (Heathrow)',  # LHR
            'Pequim',  # PEK
            'Madri',  # MAD
            'Zurique',  # ZRH
            'Atlanta',  # ATL
            'Luanda',  # LAD
            'Tel Aviv',  # TLV
            'Dubai',  # DXB
            'Amsterdã',  # AMS
            'Bariloche',  # BRC
            'Addis Ababa',  # ADD
            'Rio Branco (AC)',  # RBR
            'Munique',  # MUC
            'Mendoza',  # MDZ
            'Boston',  # BOS
            'Punta Cana',  # PUJ
            'Punta del Este',  # PDP
            'Rosário',  # ROS
            'Córdoba',  # COR
            'Barcelona',  # BCN
            'Las Vegas',  # LAS
            'Sinop (MS)',  # OPS
            'San Bernardino',  # SBD
            'El Palomar',  # EPA
            'Dourados',  # DOU
            'Fort-de-France',  # FDF
            'Montreal',  # YUL
            'Liège',  # LGG
            'Rio Verde (GO)',  # RVD
            'Marabá (PA)',  # MAB
            'Mount Pleasant',  # MPN
            'Marrakech',  # RAK
            'Montego Bay',  # MBJ
            'Abu Dhabi',  # AUH
            'Aguadilla',  # BQN
            'Havana',  # HAV
            'Istambul',  # ISL
            'Lagos',  # LOS
            'San José',  # SJO
            'Dubai (World Central)',  # DWC
            'Basileia',  # BSL
            'Pointe-à-Pitre',  # PTP
            'San Juan',  # SJU
            'Maringá (PR)',  # MGF
            'Lajes (PR)', #EEA
            'Ushuaia (ARG)' #USH
            'Farnborough (ING)' #FAB
                
        ]

        # Substituir no DataFrame
        df_voos['Cidades'] = np.select(conditions, values,default='None')

        csv = df_voos.to_csv(index=False).encode('utf-8')

        st.download_button(
           label="📥 Baixar arquivo CSV",
           data=csv,  
           file_name = nome_excel,
           mime = 'text/csv'
        )

if __name__ == "__main__":

    main()
