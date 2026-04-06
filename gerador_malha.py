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
    global slot_arr, slot_dep, slot_op_dupla

    if uploaded_file is not None:
        uploaded_file.seek(0)  # garante leitura do início do arquivo
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


  if(temporada == "S26"):
    df['Datas'] = df['Datas'].str.replace('MAR','MAR2026')
    df['Datas'] = df['Datas'].str.replace('APR','APR2026')
    df['Datas'] = df['Datas'].str.replace('MAY','MAY2026')
    df['Datas'] = df['Datas'].str.replace('JUN','JUN2026')
    df['Datas'] = df['Datas'].str.replace('JUL','JUL2026')
    df['Datas'] = df['Datas'].str.replace('AUG','AUG2026')
    df['Datas'] = df['Datas'].str.replace('SEP','SEP2026')
    df['Datas'] = df['Datas'].str.replace('OCT','OCT2026')


def dias_op_V(linha):
    data = pd.to_datetime(linha['data_op'], errors='coerce')

    if pd.isna(data):
        return "eliminar"

    doop = str(linha['Doop']) if pd.notna(linha['Doop']) else ""

    # Monday=0 ... Sunday=6  ->  1 a 7
    dia_op = str(data.dayofweek + 1)

    return "manter" if dia_op in doop else "eliminar"

def separar_info_dep():
  for item in slot_dep:

    item[2] = item[2][0:5] + " " + item[2][5:]

    item[4] = item[4][0:3] + " " +  item[4][3:]

    if(len(item[5]) == 10):
      item[5] = item[5][0:4] + " " + "0" + " " + item[5][4:7] + " " + item[5][7:]

    if(len(item[5]) == 11):
      item[5] = item[5][0:4] + " " + item[5][4:5] + " " + item[5][5:8] + " " + item[5][8:]


def main():
    global slot_arr, slot_dep, slot_op_dupla

    nome_arquivo_upload = st.file_uploader("Selecione o arquivo SIR no formato .TXT", type=["txt", "TXT"])
    opcao = st.selectbox("Selecione uma opção:", ["W23", "S24", "W24", "W25", "S25", "S26"])
    nome_excel = st.text_input("Digite o nome do arquivo que deseja receber (ex: UDI_W25_20250721.csv)")

    if st.button("Executar"):

        if nome_arquivo_upload is None:
            st.error("Selecione um arquivo TXT antes de executar.")
            return

        # limpa listas globais para não acumular dados entre execuções
        slot_arr.clear()
        slot_dep.clear()
        slot_op_dupla.clear()

        separador_arr_dep(nome_arquivo_upload)
        desembrandor_op_dupla(slot_op_dupla)
        separar_info_chegadas()

        if len(slot_arr) == 0 and len(slot_dep) == 0:
            st.error("Nenhum registro válido foi encontrado no arquivo enviado.")
            return

        # -------------------------
        # CHEGADAS
        # -------------------------
        df_chegada = pd.DataFrame(
            data=slot_arr,
            columns=['N_Voo', 'Datas', 'Doop', 'Assentos_equipamento', 'Orig_dep_hora', 'Tipo_Voo']
        )

        datas_temporada(opcao, df_chegada)

        df_aux = df_chegada['Datas'].str.split(expand=True)
        df_aux.columns = ['data_inicio_str', 'data_fim_str']

        df_aux['data_inicio'] = pd.to_datetime(df_aux['data_inicio_str'], format='%d%b%Y', errors='coerce')
        df_aux['data_fim'] = pd.to_datetime(df_aux['data_fim_str'], format='%d%b%Y', errors='coerce')

        df_chegada = pd.concat([df_chegada, df_aux[['data_inicio', 'data_fim']]], axis=1)
        df_chegada.drop(columns=['Datas'], inplace=True)
        df_chegada = df_chegada.dropna(subset=['data_inicio', 'data_fim']).copy()

        a = [pd.date_range(inicio, fim, freq='D') for inicio, fim in df_chegada[['data_inicio', 'data_fim']].values]

        df_aux = (
            df_chegada[['N_Voo', 'Doop', 'Assentos_equipamento', 'Orig_dep_hora', 'Tipo_Voo']]
            .join(pd.DataFrame(a))
            .set_index(['N_Voo', 'Doop', 'Assentos_equipamento', 'Orig_dep_hora', 'Tipo_Voo'])
            .stack()
            .droplevel(-1)
            .reset_index()
        )

        df_aux.rename(columns={0: 'data_op'}, inplace=True)
        df_aux['data_op'] = pd.to_datetime(df_aux['data_op'], errors='coerce')
        df_aux = df_aux[df_aux['data_op'].notna()].copy()

        df_aux['dia'] = df_aux['data_op'].dt.strftime('%A')
        df_aux['M'] = df_aux.apply(dias_op_V, axis=1)

        df_arr = df_aux.query("M == 'manter'").copy()
        df_arr.drop(columns=['M'], inplace=True)

        df_aux = df_arr['Assentos_equipamento'].str.split(expand=True)
        df_arr['Assentos'] = df_aux[0]
        df_arr['Equipamento'] = df_aux[1]

        df_aux = df_arr['Orig_dep_hora'].str.split(expand=True)
        df_arr['Orig_Dest'] = df_aux[0]
        df_arr['Escala'] = df_aux[1]
        df_arr['Hora'] = df_aux[2]

        df_arr.drop(columns=['Assentos_equipamento', 'Orig_dep_hora'], inplace=True)
        df_arr['Hora'] = df_arr['Hora'].astype(str)
        df_arr['Hora'] = df_arr['Hora'].str.rjust(4, '0')
        df_arr['Hora'] = df_arr['Hora'].str[:2] + ':' + df_arr['Hora'].str[-2:]
        df_arr['Arr_Dep'] = 'A'

        # -------------------------
        # PARTIDAS
        # -------------------------
        separar_info_dep()

        df_partida = pd.DataFrame(
            data=slot_dep,
            columns=['Cod Acao', 'N_Voo', 'Datas', 'Doop', 'Assentos_equipamento', 'Orig_dep_hora', 'Tipo_Voo']
        )
        df_partida.drop(columns="Cod Acao", inplace=True)

        datas_temporada(opcao, df_partida)

        df_aux = pd.DataFrame()
        df_aux['data_inicio_str'] = df_partida['Datas'].str[:9]
        df_aux['data_fim_str'] = df_partida['Datas'].str[9:]

        df_aux['data_inicio'] = pd.to_datetime(df_aux['data_inicio_str'], format='%d%b%Y', errors='coerce')
        df_aux['data_fim'] = pd.to_datetime(df_aux['data_fim_str'], format='%d%b%Y', errors='coerce')

        df_partida = pd.concat([df_partida, df_aux[['data_inicio', 'data_fim']]], axis=1)
        df_partida.drop(columns=['Datas'], inplace=True)
        df_partida = df_partida.dropna(subset=['data_inicio', 'data_fim']).copy()

        a = [pd.date_range(inicio, fim, freq='D') for inicio, fim in df_partida[['data_inicio', 'data_fim']].values]

        df_aux = (
            df_partida[['N_Voo', 'Doop', 'Assentos_equipamento', 'Orig_dep_hora', 'Tipo_Voo']]
            .join(pd.DataFrame(a))
            .set_index(['N_Voo', 'Doop', 'Assentos_equipamento', 'Orig_dep_hora', 'Tipo_Voo'])
            .stack()
            .droplevel(-1)
            .reset_index()
        )

        df_aux.rename(columns={0: 'data_op'}, inplace=True)
        df_aux['data_op'] = pd.to_datetime(df_aux['data_op'], errors='coerce')
        df_aux = df_aux[df_aux['data_op'].notna()].copy()

        df_aux['dia'] = df_aux['data_op'].dt.strftime('%A')
        df_aux['M'] = df_aux.apply(dias_op_V, axis=1)

        df_dep = df_aux.query("M == 'manter'").copy()
        df_dep.drop(columns=['M'], inplace=True)

        df_dep['Assentos'] = df_dep['Assentos_equipamento'].str[:3]
        df_dep['Equipamento'] = df_dep['Assentos_equipamento'].str[3:]
        df_dep['Hora'] = df_dep['Orig_dep_hora'].str[:4]
        df_dep['Orig_Dest'] = df_dep['Orig_dep_hora'].str[4:7]
        df_dep['Escala'] = df_dep['Orig_dep_hora'].str[7:]

        df_dep.drop(columns=['Orig_dep_hora', 'Assentos_equipamento'], inplace=True)
        df_dep['Hora'] = df_dep['Hora'].astype(str)
        df_dep['Hora'] = df_dep['Hora'].str.rjust(4, '0')
        df_dep['Hora'] = df_dep['Hora'].str[:2] + ':' + df_dep['Hora'].str[-2:]
        df_dep['Arr_Dep'] = 'D'

        # concatena chegadas e partidas
        df_voos = pd.concat([df_arr, df_dep], ignore_index=True)

        # Inserindo companhias aéreas
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

        values = [
            'Azul','Alitalia','Conecta','TAP','Modern Logistics','Cabo Verde Airlines','Air Europa','Sideral','Latam','Gol',
            'Lufthansa Cargo','Copa Airlines','Voe Pass','Itapemirim','Belavia','CargoLux','FlyPelican','Latam Cargo Colombia',
            'Lufthansa','Latam Cargo','Latam Cargo Chile','Volga-Dnepr Airlines','Itapemirim','Latam Cargo Peru','KLM','Voe Pass',
            'OMI','JetMagic','Hifly','Atlas Air','Air Italia','Total Linhas Aereas','LOT Polish Airlines','Turkish Airlines',
            'Lan Ecuador','Paranair','Levu','Latam Argentina','American Airlines','United','Avianca El Salvador',
            'South African Airways','Aerolineas Argentinas','Qatar Airways','Air Canada','Air France','Latam Paraguay',
            'Aeromexico','Boliviana de Aviacion','Aerolineas Argentinas','Avianca Brasil','Royal Air Marroc','Swiss',
            'Latam Airlines','Avianca','British Airways','Iberia','Air China','Sky Airline','Delta','Ethiopian Airlines',
            'TAAG Angola','Emirates','Centrafrrique Air Express','Taca','Flybondi','Wammos Air','Voos Teste','Sky Taxi',
            'Total Linhas Aereas','ACE Skyline','JetSmart'
        ]

        df_voos['Cia'] = np.select(conditions, values, default='Outra')

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

        values = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
        df_voos['bucket'] = np.select(conditions, values, default=0)

        conditions = [
            (df_voos['dia'].str.startswith('Monday')),
            (df_voos['dia'].str.startswith('Tuesday')),
            (df_voos['dia'].str.startswith('Wednesday')),
            (df_voos['dia'].str.startswith('Thursday')),
            (df_voos['dia'].str.startswith('Friday')),
            (df_voos['dia'].str.startswith('Saturday')),
            (df_voos['dia'].str.startswith('Sunday')),
        ]

        values = ["Seg", "Ter", "Qua", "Qui", "Sex", "Sab", "Dom"]
        df_voos['dia'] = np.select(conditions, values, default="None")

        conditions = [
            (df_voos['bucket'] <= 6),
            ((df_voos['bucket'] >= 6) & (df_voos['bucket'] < 12)),
            ((df_voos['bucket'] >= 12) & (df_voos['bucket'] < 18)),
            ((df_voos['bucket'] >= 18) & (df_voos['bucket'] <= 24)),
        ]

        values = ['Madrugada', 'Manha', 'Tarde', 'Noite']
        df_voos['Periodo'] = np.select(conditions, values, default='None')

        df_voos['Mês'] = df_voos['data_op'].dt.month
        df_voos['Zona'] = 'D'

        # ============================================
        # MANTENHA DAQUI PARA BAIXO O RESTANTE DO SEU
        # CÓDIGO EXATAMENTE COMO JÁ ESTÁ:
        # - bloco de Zona com Orig_Dest/Escala
        # - Direto_Escala
        # - bloco de Cidades
        # ============================================

        # Origem e destinos
        # destinos
        conditions = [
            (df_voos['Cia'] == 'TAP'),
            (df_voos['Orig_Dest'] == 'SET'),
            (df_voos['Orig_Dest'] == 'JPO'),
            (df_voos['Orig_Dest'] == 'MCZ'),
            (df_voos['Orig_Dest'] == 'BSB'),
            (df_voos['Orig_Dest'] == 'VCP'),
            (df_voos['Orig_Dest'] == 'VIX'),
            (df_voos['Orig_Dest'] == 'UDI'),
            (df_voos['Orig_Dest'] == 'SJP'),
            (df_voos['Orig_Dest'] == 'POA'),
            (df_voos['Orig_Dest'] == 'GYN'),
            (df_voos['Orig_Dest'] == 'RAO'),
            (df_voos['Orig_Dest'] == 'NAT'),
            (df_voos['Orig_Dest'] == 'CNF'),
            (df_voos['Orig_Dest'] == 'CPV'),
            (df_voos['Orig_Dest'] == 'SDU'),
            (df_voos['Orig_Dest'] == 'MAO'),
            (df_voos['Orig_Dest'] == 'AJU'),
            (df_voos['Orig_Dest'] == 'JPA'),
            (df_voos['Orig_Dest'] == 'JDO'),
            (df_voos['Orig_Dest'] == 'SSA'),
            (df_voos['Orig_Dest'] == 'GRU'),
            (df_voos['Orig_Dest'] == 'THE'),
            (df_voos['Orig_Dest'] == 'FOR'),
            (df_voos['Orig_Dest'] == 'CGB'),
            (df_voos['Orig_Dest'] == 'SLZ'),
            (df_voos['Orig_Dest'] == 'FEN'),
            (df_voos['Orig_Dest'] == 'PNZ'),
            (df_voos['Orig_Dest'] == 'IMP'),
            (df_voos['Orig_Dest'] == 'STM'),
            (df_voos['Orig_Dest'] == 'MVF'),
            (df_voos['Orig_Dest'] == 'REC'),
            (df_voos['Orig_Dest'] == 'PMW'),
            (df_voos['Orig_Dest'] == 'GIG'),
            (df_voos['Orig_Dest'] == 'AVR'),
            (df_voos['Orig_Dest'] == 'MXP'),
            (df_voos['Orig_Dest'] == 'FCO'),
            (df_voos['Orig_Dest'] == 'PTY'),
            (df_voos['Orig_Dest'] == 'CWB'),
            (df_voos['Orig_Dest'] == 'MIA'),
            (df_voos['Orig_Dest'] == 'SJK'),
            (df_voos['Orig_Dest'] == 'LIM'),
            (df_voos['Orig_Dest'] == 'LIS'),
            (df_voos['Orig_Dest'] == 'SID'),
            (df_voos['Orig_Dest'] == 'CAU'),
            (df_voos['Orig_Dest'] == 'QDV'),
            (df_voos['Orig_Dest'] == 'LUX'),
            (df_voos['Orig_Dest'] == 'SCL'),
            (df_voos['Orig_Dest'] == 'ACC'),
            (df_voos['Orig_Dest'] == 'BOG'),
            (df_voos['Orig_Dest'] == 'OPO'),
            (df_voos['Orig_Dest'] == 'ABJ'),
            (df_voos['Orig_Dest'] == 'FRA'),
            (df_voos['Orig_Dest'] == 'QSC'),
            (df_voos['Orig_Dest'] == 'TFS'),
            (df_voos['Orig_Dest'] == 'IOS'),
            (df_voos['Orig_Dest'] == 'MDE'),
            (df_voos['Orig_Dest'] == 'BEL'),
            (df_voos['Escala'] == 'BAQ'),
            (df_voos['Escala'] == 'PDL'),
            (df_voos['Orig_Dest'] == 'CGH'),
            (df_voos['Orig_Dest'] == 'JJD'),
            (df_voos['Orig_Dest'] == 'PHB'),
            (df_voos['Orig_Dest'] == 'BVB'),
            (df_voos['Orig_Dest'] == 'UBA'),
            (df_voos['Orig_Dest'] == 'CGR'),
            (df_voos['Orig_Dest'] == 'PPB'),
            (df_voos['Orig_Dest'] == 'EZE'),
            (df_voos['Orig_Dest'] == 'PVH'),
            (df_voos['Orig_Dest'] == 'FLN'),
            (df_voos['Orig_Dest'] == 'MCP'),
            (df_voos['Orig_Dest'] == 'LDB'),
            (df_voos['Orig_Dest'] == 'BPS'),
            (df_voos['Orig_Dest'] == 'ARX'),
            (df_voos['Orig_Dest'] == 'CPT'),
            (df_voos['Orig_Dest'] == 'PUQ'),
            (df_voos['Orig_Dest'] == 'AEP'),
            (df_voos['Orig_Dest'] == 'MAD'),
            (df_voos['Orig_Dest'] == 'MVD'),
            (df_voos['Orig_Dest'] == 'ARU'),
            (df_voos['Orig_Dest'] == 'MEX'),
            (df_voos['Orig_Dest'] == 'QGP'),
            (df_voos['Orig_Dest'] == 'GNM'),
            (df_voos['Orig_Dest'] == 'VVI'),
            (df_voos['Orig_Dest'] == 'CKY'),
            (df_voos['Orig_Dest'] == 'TUN'),
            (df_voos['Orig_Dest'] == 'ARU'),
            (df_voos['Orig_Dest'] == 'JTC'),
            (df_voos['Orig_Dest'] == 'IGU'),
            (df_voos['Orig_Dest'] == 'DSS'),
            (df_voos['Orig_Dest'] == 'JAW'),
            (df_voos['Orig_Dest'] == 'NSR'),
            (df_voos['Orig_Dest'] == 'FEC'),
            (df_voos['Orig_Dest'] == 'PAV'),
            (df_voos['Orig_Dest'] == 'CAC'),
            (df_voos['Orig_Dest'] == 'UBA'),
            (df_voos['Orig_Dest'] == 'LDB'),
            (df_voos['Orig_Dest'] == 'PUC'),
            (df_voos['Orig_Dest'] == 'TNG'),
            (df_voos['Orig_Dest'] == 'UIO'),
            (df_voos['Orig_Dest'] == 'FLL'),
            (df_voos['Orig_Dest'] == 'CFB'),
            (df_voos['Orig_Dest'] == 'LPA'),
            (df_voos['Escala'] == 'EZE'),
            (df_voos['Escala'] == 'AEP'),
            (df_voos['Escala'] == 'RAI'),
            (df_voos['Escala'] == 'MCO'),
            (df_voos['Escala'] == 'TUC'),
            (df_voos['Escala'] == 'FUE'),
            (df_voos['Escala'] == 'VAL'),
            (df_voos['Escala'] == 'CKJ'),
            (df_voos['Escala'] == 'RRJ'),
            (df_voos['Escala'] == 'UNA'),
            (df_voos['Escala'] == 'IPN'),
            (df_voos['Escala'] == 'NVT'),
            (df_voos['Escala'] == 'MOC'),
            (df_voos['Escala'] == 'CLV'),
            (df_voos['Escala'] == 'BYO'),
            (df_voos['Escala'] == 'JJG'),
            (df_voos['Escala'] == 'JOI'),
            (df_voos['Escala'] == 'IZA'),
            (df_voos['Escala'] == 'CXJ'),
            (df_voos['Escala'] == 'MGF'),
            (df_voos['Escala'] == 'RIA'),
            (df_voos['Escala'] == 'TXF'),
            (df_voos['Escala'] == 'URG'),
            (df_voos['Orig_Dest'] == 'BYO'),
            (df_voos['Orig_Dest'] == 'ITB'),
            (df_voos['Orig_Dest'] == 'TMT'),
            (df_voos['Orig_Dest'] == 'BSE'),
            (df_voos['Orig_Dest'] == 'XAP'),
            (df_voos['Orig_Dest'] == 'CJZ'),
            (df_voos['Orig_Dest'] == 'BZC'),
            (df_voos['Orig_Dest'] == 'OIA'),
            (df_voos['Orig_Dest'] == 'PFB'),
            (df_voos['Orig_Dest'] == 'IST'),
            (df_voos['Orig_Dest'] == 'ASU'),
            (df_voos['Orig_Dest'] == 'PIN'),
            (df_voos['Orig_Dest'] == 'CMN'),
            (df_voos['Orig_Dest'] == 'RRJ'),
            (df_voos['Orig_Dest'] == 'PET'),
            (df_voos['Orig_Dest'] == 'QNS'),
            (df_voos['Orig_Dest'] == 'GEL'),
            (df_voos['Orig_Dest'] == 'GYE'),
            (df_voos['Orig_Dest'] == 'VDC'),
            (df_voos['Orig_Dest'] == 'IAD'),
            (df_voos['Orig_Dest'] == 'LAX'),
            (df_voos['Orig_Dest'] == 'ORD'),
            (df_voos['Orig_Dest'] == 'JFK'),
            (df_voos['Orig_Dest'] == 'EWR'),
            (df_voos['Orig_Dest'] == 'DFW'),
            (df_voos['Orig_Dest'] == 'IAH'),
            (df_voos['Orig_Dest'] == 'YYZ'),
            (df_voos['Orig_Dest'] == 'JNB'),
            (df_voos['Orig_Dest'] == 'CDG'),
            (df_voos['Orig_Dest'] == 'DOH'),
            (df_voos['Orig_Dest'] == 'CBB'),
            (df_voos['Orig_Dest'] == 'LHR'),
            (df_voos['Orig_Dest'] == 'PEK'),
            (df_voos['Orig_Dest'] == 'MAD'),
            (df_voos['Orig_Dest'] == 'ZRH'),
            (df_voos['Orig_Dest'] == 'ATL'),
            (df_voos['Orig_Dest'] == 'LAD'),
            (df_voos['Orig_Dest'] == 'TLV'),
            (df_voos['Orig_Dest'] == 'DXB'),
            (df_voos['Orig_Dest'] == 'AMS'),
            (df_voos['Orig_Dest'] == 'BRC'),
            (df_voos['Orig_Dest'] == 'ADD'),
            (df_voos['Orig_Dest'] == 'RBR'),
            (df_voos['Orig_Dest'] == 'MUC'),
            (df_voos['Orig_Dest'] == 'MDZ'),
            (df_voos['Orig_Dest'] == 'BOS'),
            (df_voos['Orig_Dest'] == 'PUJ'),
            (df_voos['Orig_Dest'] == 'PDP'),
            (df_voos['Orig_Dest'] == 'ROS'),
            (df_voos['Orig_Dest'] == 'COR'),
            (df_voos['Orig_Dest'] == 'BCN'),
            (df_voos['Orig_Dest'] == 'LAS'),
            (df_voos['Orig_Dest'] == 'OPS'),
            (df_voos['Orig_Dest'] == 'SBD'),
            (df_voos['Orig_Dest'] == 'EPA'),
            (df_voos['Orig_Dest'] == 'DOU'),
            (df_voos['Orig_Dest'] == 'FDF'),
            (df_voos['Orig_Dest'] == 'YUL'),
            (df_voos['Orig_Dest'] == 'LGG'),
            (df_voos['Orig_Dest'] == 'RVD'),
            (df_voos['Orig_Dest'] == 'MAB'),
            (df_voos['Orig_Dest'] == 'MPN'),
            (df_voos['Orig_Dest'] == 'RAK'),
            (df_voos['Orig_Dest'] == 'MBJ'),
            (df_voos['Orig_Dest'] == 'AUH'),
            (df_voos['Orig_Dest'] == 'BQN'),
            (df_voos['Orig_Dest'] == 'HAV'),
            (df_voos['Orig_Dest'] == 'ISL'),
            (df_voos['Orig_Dest'] == 'LOS'),
            (df_voos['Orig_Dest'] == 'SJO'),
            (df_voos['Orig_Dest'] == 'DWC'),
            (df_voos['Orig_Dest'] == 'BSL'),
            (df_voos['Orig_Dest'] == 'PTP'),
            (df_voos['Orig_Dest'] == 'SJU'),
            (df_voos['Orig_Dest'] == 'MGF'),
            (df_voos['Orig_Dest'] == 'POS'),
            (df_voos['Orig_Dest'] == 'BYJ'),
            (df_voos['Orig_Dest'] == 'BGA'),
            (df_voos['Orig_Dest'] == 'MLA'),
            (df_voos['Orig_Dest'] == 'ANF'),
            (df_voos['Orig_Dest'] == 'WDH'),
            (df_voos['Orig_Dest'] == 'ALG'),
            (df_voos['Orig_Dest'] == 'FAO'),
            (df_voos['Orig_Dest'] == 'TEV'),
            (df_voos['Orig_Dest'] == 'EEA'),
            (df_voos['Orig_Dest'] == 'JPR'),
        ]

        values = [
            'I','D','D','D','D','D','D','D','D','D','D','D','D','D','D','D','D','D','D','D','D','D','D','D','D','D',
            'D','D','D','D','D','D','D','D','I','I','I','I','D','I','D','I','I','I','D','D','I','I','I','I','I','I',
            'I','D','I','D','I','D','I','I','D','D','D','D','D','D','D','I','D','D','D','D','D','D','I','I','I','I',
            'I','D','I','D','D','I','I','I','D','D','D','I','D','D','D','D','D','D','D','D','I','I','I','I','D','I',
            'I','I','I','I','I','I','D','D','D','D','D','D','D','D','D','D','D','D','D','D','D','I','I','D','I','D',
            'D','D','D','I','D','I','I','I','I','I','I','I','I','I','I','I','I','I','I','I','I','I','I','I','I','D',
            'I','I','I','I','I','I','I','I','D','I','I','D','I','I','I','D','D','I','I','I','I','I','I','I','I','I',
            'I','I','I','I','I','D','I','I','I','I','I','I','I','I','I','D','D'
        ]

        df_voos['Zona'] = np.select(conditions, values, default='None')

        Conditions = [
            (df_voos['Orig_Dest'] == df_voos['Escala']),
            (df_voos['Orig_Dest'] != df_voos['Escala']),
        ]

        values = ['Voo Direto', 'Voo Com escala']
        df_voos['Direto_Escala'] = np.select(Conditions, values, default='None')

        # Mantenha também o seu bloco de Cidades exatamente como estava
        # Para não estourar a resposta aqui, ele permanece igual ao seu código original

        conditions = [
            (df_voos['Orig_Dest'] == 'LIS'),
            (df_voos['Orig_Dest'] == 'SET'),
            (df_voos['Orig_Dest'] == 'JPO'),
            (df_voos['Orig_Dest'] == 'MCZ'),
            (df_voos['Orig_Dest'] == 'BSB'),
            (df_voos['Orig_Dest'] == 'VCP'),
            (df_voos['Orig_Dest'] == 'VIX'),
            (df_voos['Orig_Dest'] == 'UDI'),
            (df_voos['Orig_Dest'] == 'SJP'),
            (df_voos['Orig_Dest'] == 'POA'),
            (df_voos['Orig_Dest'] == 'GYN'),
            (df_voos['Orig_Dest'] == 'RAO'),
            (df_voos['Orig_Dest'] == 'NAT'),
            (df_voos['Orig_Dest'] == 'CNF'),
            (df_voos['Orig_Dest'] == 'CPV'),
            (df_voos['Orig_Dest'] == 'SDU'),
            (df_voos['Orig_Dest'] == 'MAO'),
            (df_voos['Orig_Dest'] == 'AJU'),
            (df_voos['Orig_Dest'] == 'JPA'),
            (df_voos['Orig_Dest'] == 'JDO'),
            (df_voos['Orig_Dest'] == 'SSA'),
            (df_voos['Orig_Dest'] == 'GRU'),
            (df_voos['Orig_Dest'] == 'THE'),
            (df_voos['Orig_Dest'] == 'FOR'),
            (df_voos['Orig_Dest'] == 'CGB'),
            (df_voos['Orig_Dest'] == 'SLZ'),
            (df_voos['Orig_Dest'] == 'FEN'),
            (df_voos['Orig_Dest'] == 'PNZ'),
            (df_voos['Orig_Dest'] == 'IMP'),
            (df_voos['Orig_Dest'] == 'STM'),
            (df_voos['Orig_Dest'] == 'MVF'),
            (df_voos['Orig_Dest'] == 'REC'),
            (df_voos['Orig_Dest'] == 'PMW'),
            (df_voos['Orig_Dest'] == 'GIG'),
            (df_voos['Orig_Dest'] == 'AVR'),
            (df_voos['Orig_Dest'] == 'MXP'),
            (df_voos['Orig_Dest'] == 'FCO'),
            (df_voos['Orig_Dest'] == 'PTY'),
            (df_voos['Orig_Dest'] == 'CWB'),
            (df_voos['Orig_Dest'] == 'MIA'),
            (df_voos['Orig_Dest'] == 'SJK'),
            (df_voos['Orig_Dest'] == 'LIM'),
            (df_voos['Orig_Dest'] == 'LIS'),
            (df_voos['Orig_Dest'] == 'SID'),
            (df_voos['Orig_Dest'] == 'CAU'),
            (df_voos['Orig_Dest'] == 'QDV'),
            (df_voos['Orig_Dest'] == 'LUX'),
            (df_voos['Orig_Dest'] == 'SCL'),
            (df_voos['Orig_Dest'] == 'ACC'),
            (df_voos['Orig_Dest'] == 'BOG'),
            (df_voos['Orig_Dest'] == 'OPO'),
            (df_voos['Orig_Dest'] == 'ABJ'),
            (df_voos['Orig_Dest'] == 'FRA'),
            (df_voos['Orig_Dest'] == 'QSC'),
            (df_voos['Orig_Dest'] == 'TFS'),
            (df_voos['Orig_Dest'] == 'IOS'),
            (df_voos['Orig_Dest'] == 'MDE'),
            (df_voos['Orig_Dest'] == 'BEL'),
            (df_voos['Escala'] == 'BAQ'),
            (df_voos['Escala'] == 'PDL'),
            (df_voos['Orig_Dest'] == 'CGH'),
            (df_voos['Orig_Dest'] == 'JJD'),
            (df_voos['Orig_Dest'] == 'PHB'),
            (df_voos['Orig_Dest'] == 'BVB'),
            (df_voos['Orig_Dest'] == 'UBA'),
            (df_voos['Orig_Dest'] == 'CGR'),
            (df_voos['Orig_Dest'] == 'PPB'),
            (df_voos['Orig_Dest'] == 'EZE'),
            (df_voos['Orig_Dest'] == 'PVH'),
            (df_voos['Orig_Dest'] == 'FLN'),
            (df_voos['Orig_Dest'] == 'MCP'),
            (df_voos['Orig_Dest'] == 'LDB'),
            (df_voos['Orig_Dest'] == 'BPS'),
            (df_voos['Orig_Dest'] == 'ARX'),
            (df_voos['Orig_Dest'] == 'CPT'),
            (df_voos['Orig_Dest'] == 'PUQ'),
            (df_voos['Orig_Dest'] == 'AEP'),
            (df_voos['Orig_Dest'] == 'MAD'),
            (df_voos['Orig_Dest'] == 'MVD'),
            (df_voos['Orig_Dest'] == 'ARU'),
            (df_voos['Orig_Dest'] == 'MEX'),
            (df_voos['Orig_Dest'] == 'QGP'),
            (df_voos['Orig_Dest'] == 'GNM'),
            (df_voos['Orig_Dest'] == 'VVI'),
            (df_voos['Orig_Dest'] == 'CKY'),
            (df_voos['Orig_Dest'] == 'TUN'),
            (df_voos['Orig_Dest'] == 'ARU'),
            (df_voos['Orig_Dest'] == 'JTC'),
            (df_voos['Orig_Dest'] == 'IGU'),
            (df_voos['Orig_Dest'] == 'DSS'),
            (df_voos['Orig_Dest'] == 'JAW'),
            (df_voos['Orig_Dest'] == 'NSR'),
            (df_voos['Orig_Dest'] == 'FEC'),
            (df_voos['Orig_Dest'] == 'PAV'),
            (df_voos['Orig_Dest'] == 'CAC'),
            (df_voos['Orig_Dest'] == 'UBA'),
            (df_voos['Orig_Dest'] == 'LDB'),
            (df_voos['Orig_Dest'] == 'PUC'),
            (df_voos['Orig_Dest'] == 'TNG'),
            (df_voos['Orig_Dest'] == 'UIO'),
            (df_voos['Orig_Dest'] == 'FLL'),
            (df_voos['Orig_Dest'] == 'CFB'),
            (df_voos['Orig_Dest'] == 'LPA'),
            (df_voos['Escala'] == 'EZE'),
            (df_voos['Escala'] == 'AEP'),
            (df_voos['Escala'] == 'RAI'),
            (df_voos['Escala'] == 'MCO'),
            (df_voos['Escala'] == 'TUC'),
            (df_voos['Escala'] == 'FUE'),
            (df_voos['Escala'] == 'VAL'),
            (df_voos['Escala'] == 'CKJ'),
            (df_voos['Escala'] == 'RRJ'),
            (df_voos['Escala'] == 'UNA'),
            (df_voos['Escala'] == 'IPN'),
            (df_voos['Escala'] == 'NVT'),
            (df_voos['Escala'] == 'MOC'),
            (df_voos['Escala'] == 'CLV'),
            (df_voos['Escala'] == 'BYO'),
            (df_voos['Escala'] == 'JJG'),
            (df_voos['Escala'] == 'JOI'),
            (df_voos['Escala'] == 'IZA'),
            (df_voos['Escala'] == 'CXJ'),
            (df_voos['Escala'] == 'MGF'),
            (df_voos['Escala'] == 'RIA'),
            (df_voos['Escala'] == 'TXF'),
            (df_voos['Escala'] == 'URG'),
            (df_voos['Orig_Dest'] == 'BYO'),
            (df_voos['Orig_Dest'] == 'ITB'),
            (df_voos['Orig_Dest'] == 'TMT'),
            (df_voos['Orig_Dest'] == 'BSE'),
            (df_voos['Orig_Dest'] == 'XAP'),
            (df_voos['Orig_Dest'] == 'CJZ'),
            (df_voos['Orig_Dest'] == 'BZC'),
            (df_voos['Orig_Dest'] == 'OIA'),
            (df_voos['Orig_Dest'] == 'PFB'),
            (df_voos['Orig_Dest'] == 'IST'),
            (df_voos['Orig_Dest'] == 'ASU'),
            (df_voos['Orig_Dest'] == 'PIN'),
            (df_voos['Orig_Dest'] == 'CMN'),
            (df_voos['Orig_Dest'] == 'RRJ'),
            (df_voos['Orig_Dest'] == 'PET'),
            (df_voos['Orig_Dest'] == 'QNS'),
            (df_voos['Orig_Dest'] == 'GEL'),
            (df_voos['Orig_Dest'] == 'GYE'),
            (df_voos['Orig_Dest'] == 'VDC'),
            (df_voos['Orig_Dest'] == 'IAD'),
            (df_voos['Orig_Dest'] == 'LAX'),
            (df_voos['Orig_Dest'] == 'ORD'),
            (df_voos['Orig_Dest'] == 'JFK'),
            (df_voos['Orig_Dest'] == 'EWR'),
            (df_voos['Orig_Dest'] == 'DFW'),
            (df_voos['Orig_Dest'] == 'IAH'),
            (df_voos['Orig_Dest'] == 'YYZ'),
            (df_voos['Orig_Dest'] == 'JNB'),
            (df_voos['Orig_Dest'] == 'CDG'),
            (df_voos['Orig_Dest'] == 'DOH'),
            (df_voos['Orig_Dest'] == 'CBB'),
            (df_voos['Orig_Dest'] == 'LHR'),
            (df_voos['Orig_Dest'] == 'PEK'),
            (df_voos['Orig_Dest'] == 'MAD'),
            (df_voos['Orig_Dest'] == 'ZRH'),
            (df_voos['Orig_Dest'] == 'ATL'),
            (df_voos['Orig_Dest'] == 'LAD'),
            (df_voos['Orig_Dest'] == 'TLV'),
            (df_voos['Orig_Dest'] == 'DXB'),
            (df_voos['Orig_Dest'] == 'AMS'),
            (df_voos['Orig_Dest'] == 'BRC'),
            (df_voos['Orig_Dest'] == 'ADD'),
            (df_voos['Orig_Dest'] == 'RBR'),
            (df_voos['Orig_Dest'] == 'MUC'),
            (df_voos['Orig_Dest'] == 'MDZ'),
            (df_voos['Orig_Dest'] == 'BOS'),
            (df_voos['Orig_Dest'] == 'PUJ'),
            (df_voos['Orig_Dest'] == 'PDP'),
            (df_voos['Orig_Dest'] == 'ROS'),
            (df_voos['Orig_Dest'] == 'COR'),
            (df_voos['Orig_Dest'] == 'BCN'),
            (df_voos['Orig_Dest'] == 'LAS'),
            (df_voos['Orig_Dest'] == 'OPS'),
            (df_voos['Orig_Dest'] == 'SBD'),
            (df_voos['Orig_Dest'] == 'EPA'),
            (df_voos['Orig_Dest'] == 'DOU'),
            (df_voos['Orig_Dest'] == 'FDF'),
            (df_voos['Orig_Dest'] == 'YUL'),
            (df_voos['Orig_Dest'] == 'LGG'),
            (df_voos['Orig_Dest'] == 'RVD'),
            (df_voos['Orig_Dest'] == 'MAB'),
            (df_voos['Orig_Dest'] == 'MPN'),
            (df_voos['Orig_Dest'] == 'RAK'),
            (df_voos['Orig_Dest'] == 'MBJ'),
            (df_voos['Orig_Dest'] == 'AUH'),
            (df_voos['Orig_Dest'] == 'BQN'),
            (df_voos['Orig_Dest'] == 'HAV'),
            (df_voos['Orig_Dest'] == 'ISL'),
            (df_voos['Orig_Dest'] == 'LOS'),
            (df_voos['Orig_Dest'] == 'SJO'),
            (df_voos['Orig_Dest'] == 'DWC'),
            (df_voos['Orig_Dest'] == 'BSL'),
            (df_voos['Orig_Dest'] == 'PTP'),
            (df_voos['Orig_Dest'] == 'SJU'),
            (df_voos['Orig_Dest'] == 'MGF'),
            (df_voos['Orig_Dest'] == 'EEA'),
            (df_voos['Orig_Dest'] == 'JPR'),
        ]

        values = [
            'Lisboa','Serra Talhada (PE)','João Pessoa (PB)','Maceió (AL)','Brasília','Campinas (SP)','Vitória (ES)','Uberlândia (MG)',
            'São José do Rio Preto (SP)','Porto Alegre (RS)','Goiânia (GO)','Ribeirão Preto (SP)','Natal (RN)','Confins (MG)',
            'Campina Grande (PB)','Rio de Janeiro (Santos Dumont) - RJ','Manaus (AM)','Aracaju (SE)','João Pessoa (PB)',
            'Juazeiro do Norte (CE)','Salvador (BA)','São Paulo (Guarulhos) (SP)','Teresina (PI)','Fortaleza (CE)','Cuiabá (MT)',
            'São Luís (MA)','Fernando de Noronha (PE)','Petrolina (PE)','Imperatriz (PE)','Santarém (PA)','Mossoró (RN)','Recife (PE)',
            'Palmas (TO)','Rio de Janeiro (Galeão) (RJ)','Aveiro - PT','Milão (Malpensa)','Roma (Fiumicino)','Cidade do Panamá',
            'Curitiba (PR)','Miami','São José dos Campos (SP)','Lima','Lisboa','Praia (Cabo Verde)','Caruaru (PE)','Jundiaí (SP)',
            'Luxemburgo','Santiago - CH','Acra','Bogotá','Porto','Abidjan','Frankfurt','São Carlos (SP)','Tenerife','Ilhéus (BA)',
            'Medellín','Belém (PA)','Barranquilla','Ponta Delgada','São Paulo (Congonhas) - SP','Juiz de Fora (MG)','Parnaíba (PI)',
            'Boa Vista (RR)','Uberaba (MG)','Campo Grande (MS)','Presidente Prudente (SP)','Buenos Aires (Ezeiza)','Porto Velho (RO)',
            'Florianópolis (SC)','Macapá (AP)','Londrina (PR)','Porto Seguro (BA)','Araxá (MG)','Cidade do Cabo','Punta Arenas',
            'Buenos Aires (Aeroparque)','Madri','Montevidéu','Araçatuba (SP)','Cidade do México','Garanhuns (PE)','Guanambi (BA)',
            'Santa Cruz de la Sierra','Conakry','Túnis','Araçatuba (SP)','Bauru (SP)','Foz do Iguaçu (PR)','Dakar','Araripina (PE)',
            'Natal (RN)','Feira de Santana (BA)','Paulo Afonso (BA)','Cascavel (PR)','Uberaba  (MG)','Londrina (PR)','Price','Tânger',
            'Quito','Fort Lauderdale','Cabo Frio (RJ)','Las Palmas','Buenos Aires (Ezeiza)','Buenos Aires (Aeroparque)',
            'Praia (Cabo Verde)','Orlando','Tucumán','Fuerteventura','Valença','Chkalovsk','Jacarepagua (RJ)','Una (MG)',
            'Ipatinga (MG)','Navegantes (SC)','Montes Claros (MG)','Caldas Novas (GO)','Bonito (MS)','Jaguaruna (SC)',
            'Joinville (SC)','Juiz de Fora (MG)','Caxias do Sul (RS)','Maringá (PR)','Santa Maria (RS)','Teixeira de Freitas (BA)',
            'Uruguaiana (RS)','Bonito (MS)','Itabuna (BA)','Porto Trombetas (PA)','Sematan','Chapecó (PR)','Cajazeiras (PB)',
            'Búzios (RJ)','Ourilândia do Norte (PA)','Passo Fundo (RS)','Istambul','Assunção','Parintins (AM)','Casablanca',
            'Jacarepagua (RJ)','Pelotas (RS)','Canoas (RS)','Santo Ângelo (RS)','Guayaquil','Vitória da Conquista (BA)',
            'Washington (Dulles)','Los Angeles',"Chicago (O'Hare)",'Nova York (JFK)','Newark','Dallas/Fort Worth','Houston','Toronto',
            'Joanesburgo','Paris (Charles de Gaulle)','Doha','Cochabamba','Londres (Heathrow)','Pequim','Madri','Zurique','Atlanta',
            'Luanda','Tel Aviv','Dubai','Amsterdã','Bariloche','Addis Ababa','Rio Branco (AC)','Munique','Mendoza','Boston',
            'Punta Cana','Punta del Este','Rosário','Córdoba','Barcelona','Las Vegas','Sinop (MS)','San Bernardino','El Palomar',
            'Dourados','Fort-de-France','Montreal','Liège','Rio Verde (GO)','Marabá (PA)','Mount Pleasant','Marrakech','Montego Bay',
            'Abu Dhabi','Aguadilla','Havana','Istambul','Lagos','San José','Dubai (World Central)','Basileia','Pointe-à-Pitre',
            'San Juan','Maringá (PR)','Correia Pinto(PR)','Ji Paraná(RO)'
        ]

        df_voos['Cidades'] = np.select(conditions, values, default='None')

        nome_saida = nome_excel.strip() if nome_excel and nome_excel.strip() else "malha_gerada.csv"
        if not nome_saida.lower().endswith(".csv"):
            nome_saida += ".csv"

        csv = df_voos.to_csv(index=False).encode('utf-8')

        st.download_button(
            label="📥 Baixar arquivo CSV",
            data=csv,
            file_name=nome_saida,
            mime='text/csv'
        )


