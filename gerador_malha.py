import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Gerador de Arquivo de Malha", layout="wide")

SEASON_MONTH_YEAR = {
    "W18": {"MAR": "MAR2019", "DEC": "DEC2018", "NOV": "NOV2018", "OCT": "OCT2018", "JAN": "JAN2019", "FEB": "FEB2019"},
    "S19": {"MAR": "MAR2019", "APR": "APR2019", "MAY": "MAY2019", "JUN": "JUN2019", "JUL": "JUL2019", "AUG": "AUG2019", "SEP": "SEP2019", "OCT": "OCT2019"},
    "W19": {"MAR": "MAR2020", "DEC": "DEC2019", "NOV": "NOV2019", "OCT": "OCT2019", "JAN": "JAN2020", "FEB": "FEB2020"},
    "S20": {"MAR": "MAR2020", "APR": "APR2020", "MAY": "MAY2020", "JUN": "JUN2020", "JUL": "JUL2020", "AUG": "AUG2020", "SEP": "SEP2020", "OCT": "OCT2020"},
    "W20": {"MAR": "MAR2021", "DEC": "DEC2020", "NOV": "NOV2020", "OCT": "OCT2020", "JAN": "JAN2021", "FEB": "FEB2021"},
    "S21": {"MAR": "MAR2021", "APR": "APR2021", "MAY": "MAY2021", "JUN": "JUN2021", "JUL": "JUL2021", "AUG": "AUG2021", "SEP": "SEP2021", "OCT": "OCT2021"},
    "W21": {"MAR": "MAR2022", "DEC": "DEC2021", "NOV": "NOV2021", "OCT": "OCT2021", "JAN": "JAN2022", "FEB": "FEB2022"},
    "S22": {"MAR": "MAR2022", "APR": "APR2022", "MAY": "MAY2022", "JUN": "JUN2022", "JUL": "JUL2022", "AUG": "AUG2022", "SEP": "SEP2022", "OCT": "OCT2022"},
    "S23": {"MAR": "MAR2023", "APR": "APR2023", "MAY": "MAY2023", "JUN": "JUN2023", "JUL": "JUL2023", "AUG": "AUG2023", "SEP": "SEP2023", "OCT": "OCT2023"},
    "W23": {"MAR": "MAR2024", "DEC": "DEC2023", "NOV": "NOV2023", "OCT": "OCT2023", "JAN": "JAN2024", "FEB": "FEB2024"},
    "S24": {"MAR": "MAR2024", "APR": "APR2024", "MAY": "MAY2024", "JUN": "JUN2024", "JUL": "JUL2024", "AUG": "AUG2024", "SEP": "SEP2024", "OCT": "OCT2024"},
    "W24": {"MAR": "MAR2025", "DEC": "DEC2024", "NOV": "NOV2024", "OCT": "OCT2024", "JAN": "JAN2025", "FEB": "FEB2025"},
    "S25": {"MAR": "MAR2025", "APR": "APR2025", "MAY": "MAY2025", "JUN": "JUN2025", "JUL": "JUL2025", "AUG": "AUG2025", "SEP": "SEP2025", "OCT": "OCT2025"},
    "W25": {"MAR": "MAR2026", "DEC": "DEC2025", "NOV": "NOV2025", "OCT": "OCT2025", "JAN": "JAN2026", "FEB": "FEB2026"},
    "S26": {"MAR": "MAR2026", "APR": "APR2026", "MAY": "MAY2026", "JUN": "JUN2026", "JUL": "JUL2026", "AUG": "AUG2026", "SEP": "SEP2026", "OCT": "OCT2026"},
    "W26": {"MAR": "MAR2027", "DEC": "DEC2026", "NOV": "NOV2026", "OCT": "OCT2026", "JAN": "JAN2027", "FEB": "FEB2027"},
}

AIRLINE_PREFIX_MAP = [
    ("AD", "Azul"),
    ("AZ", "Alitalia"),
    ("2F", "Conecta"),
    ("TP", "TAP"),
    ("WD", "Modern Logistics"),
    ("VR", "Cabo Verde Airlines"),
    ("UX", "Air Europa"),
    ("SID", "Sideral"),
    ("JJ", "Latam"),
    ("G3", "Gol"),
    ("GEC", "Lufthansa Cargo"),
    ("CM", "Copa Airlines"),
    ("2Z", "Voe Pass"),
    ("IPM", "Itapemirim"),
    ("BRU", "Belavia"),
    ("CV", "CargoLux"),
    ("FP", "FlyPelican"),
    ("L7", "Latam Cargo Colombia"),
    ("LH", "Lufthansa"),
    ("M3", "Latam Cargo"),
    ("UC", "Latam Cargo Chile"),
    ("VI", "Volga-Dnepr Airlines"),
    ("8I", "Itapemirim"),
    ("LP", "Latam Cargo Peru"),
    ("KL", "KLM"),
    ("7M", "Voe Pass"),
    ("OM", "OMI"),
    ("JMK", "JetMagic"),
    ("5K", "Hifly"),
    ("5Y", "Atlas Air"),
    ("AQZ", "Air Italia"),
    ("TTL", "Total Linhas Aereas"),
    ("LO", "LOT Polish Airlines"),
    ("TK", "Turkish Airlines"),
    ("XL", "Lan Ecuador"),
    ("ZP", "Paranair"),
    ("LV", "Levu"),
    ("4M", "Latam Argentina"),
    ("AA", "American Airlines"),
    ("UA", "United"),
    ("TA", "Avianca El Salvador"),
    ("SA", "South African Airways"),
    ("A0", "Aerolineas Argentinas"),
    ("QR", "Qatar Airways"),
    ("AC", "Air Canada"),
    ("AF", "Air France"),
    ("PZ", "Latam Paraguay"),
    ("AM", "Aeromexico"),
    ("OB", "Boliviana de Aviacion"),
    ("AR", "Aerolineas Argentinas"),
    ("O6", "Avianca Brasil"),
    ("AT", "Royal Air Marroc"),
    ("LX", "Swiss"),
    ("LA", "Latam Airlines"),
    ("AV", "Avianca"),
    ("BA", "British Airways"),
    ("IB", "Iberia"),
    ("CA", "Air China"),
    ("H2", "Sky Airline"),
    ("DL", "Delta"),
    ("ET", "Ethiopian Airlines"),
    ("DT", "TAAG Angola"),
    ("EK", "Emirates"),
    ("6C", "Centrafrrique Air Express"),
    ("T0", "Taca"),
    ("FO", "Flybondi"),
    ("PLM", "Wammos Air"),
    ("XX", "Voos Teste"),
    ("TE", "Sky Taxi"),
    ("0T", "Total Linhas Aereas"),
    ("AEC", "ACE Skyline"),
    ("WJ", "JetSmart"),
]

CITY_ITEMS = [
    ("LIS", "Lisboa"),
    ("SET", "Serra Talhada (PE)"),
    ("JPO", "João Pessoa (PB)"),
    ("MCZ", "Maceió (AL)"),
    ("BSB", "Brasília"),
    ("VCP", "Campinas (SP)"),
    ("VIX", "Vitória (ES)"),
    ("UDI", "Uberlândia (MG)"),
    ("SJP", "São José do Rio Preto (SP)"),
    ("POA", "Porto Alegre (RS)"),
    ("GYN", "Goiânia (GO)"),
    ("RAO", "Ribeirão Preto (SP)"),
    ("NAT", "Natal (RN)"),
    ("CNF", "Confins (MG)"),
    ("CPV", "Campina Grande (PB)"),
    ("SDU", "Rio de Janeiro (Santos Dumont) - RJ"),
    ("MAO", "Manaus (AM)"),
    ("AJU", "Aracaju (SE)"),
    ("JPA", "João Pessoa (PB)"),
    ("JDO", "Juazeiro do Norte (CE)"),
    ("SSA", "Salvador (BA)"),
    ("GRU", "São Paulo (Guarulhos) (SP)"),
    ("THE", "Teresina (PI)"),
    ("FOR", "Fortaleza (CE)"),
    ("CGB", "Cuiabá (MT)"),
    ("SLZ", "São Luís (MA)"),
    ("FEN", "Fernando de Noronha (PE)"),
    ("PNZ", "Petrolina (PE)"),
    ("IMP", "Imperatriz (MA)"),
    ("STM", "Santarém (PA)"),
    ("MVF", "Mossoró (RN)"),
    ("REC", "Recife (PE)"),
    ("PMW", "Palmas (TO)"),
    ("GIG", "Rio de Janeiro (Galeão) (RJ)"),
    ("AVR", "Aveiro - PT"),
    ("MXP", "Milão (Malpensa)"),
    ("FCO", "Roma (Fiumicino)"),
    ("PTY", "Cidade do Panamá"),
    ("CWB", "Curitiba (PR)"),
    ("MIA", "Miami"),
    ("SJK", "São José dos Campos (SP)"),
    ("LIM", "Lima"),
    ("SID", "Praia (Cabo Verde)"),
    ("CAU", "Caruaru (PE)"),
    ("QDV", "Jundiaí (SP)"),
    ("LUX", "Luxemburgo"),
    ("SCL", "Santiago - CH"),
    ("ACC", "Acra"),
    ("BOG", "Bogotá"),
    ("OPO", "Porto"),
    ("ABJ", "Abidjan"),
    ("FRA", "Frankfurt"),
    ("QSC", "São Carlos (SP)"),
    ("TFS", "Tenerife"),
    ("IOS", "Ilhéus (BA)"),
    ("MDE", "Medellín"),
    ("BEL", "Belém (PA)"),
    ("BAQ", "Barranquilla"),
    ("PDL", "Ponta Delgada"),
    ("CGH", "São Paulo (Congonhas) - SP"),
    ("JJD", "Juiz de Fora (MG)"),
    ("PHB", "Parnaíba (PI)"),
    ("BVB", "Boa Vista (RR)"),
    ("UBA", "Uberaba (MG)"),
    ("CGR", "Campo Grande (MS)"),
    ("PPB", "Presidente Prudente (SP)"),
    ("EZE", "Buenos Aires (Ezeiza)"),
    ("PVH", "Porto Velho (RO)"),
    ("FLN", "Florianópolis (SC)"),
    ("MCP", "Macapá (AP)"),
    ("LDB", "Londrina (PR)"),
    ("BPS", "Porto Seguro (BA)"),
    ("ARX", "Araxá (MG)"),
    ("CPT", "Cidade do Cabo"),
    ("PUQ", "Punta Arenas"),
    ("AEP", "Buenos Aires (Aeroparque)"),
    ("MAD", "Madri"),
    ("MVD", "Montevidéu"),
    ("ARU", "Araçatuba (SP)"),
    ("MEX", "Cidade do México"),
    ("QGP", "Garanhuns (PE)"),
    ("GNM", "Guanambi (BA)"),
    ("VVI", "Santa Cruz de la Sierra"),
    ("CKY", "Conakry"),
    ("TUN", "Túnis"),
    ("JTC", "Bauru (SP)"),
    ("IGU", "Foz do Iguaçu (PR)"),
    ("DSS", "Dakar"),
    ("JAW", "Araripina (PE)"),
    ("NSR", "Natal (RN)"),
    ("FEC", "Feira de Santana (BA)"),
    ("PAV", "Paulo Afonso (BA)"),
    ("CAC", "Cascavel (PR)"),
    ("PUC", "Price"),
    ("TNG", "Tânger"),
    ("UIO", "Quito"),
    ("FLL", "Fort Lauderdale"),
    ("CFB", "Cabo Frio (RJ)"),
    ("LPA", "Las Palmas"),
    ("RAI", "Praia (Cabo Verde)"),
    ("MCO", "Orlando"),
    ("TUC", "Tucumán"),
    ("FUE", "Fuerteventura"),
    ("VAL", "Valença"),
    ("CKJ", "Chkalovsk"),
    ("RRJ", "Jacarepagua (RJ)"),
    ("UNA", "Una (BA)"),
    ("IPN", "Ipatinga (MG)"),
    ("NVT", "Navegantes (SC)"),
    ("MOC", "Montes Claros (MG)"),
    ("CLV", "Caldas Novas (GO)"),
    ("BYO", "Bonito (MS)"),
    ("JJG", "Jaguaruna (SC)"),
    ("JOI", "Joinville (SC)"),
    ("IZA", "Juiz de Fora (MG)"),
    ("CXJ", "Caxias do Sul (RS)"),
    ("MGF", "Maringá (PR)"),
    ("RIA", "Santa Maria (RS)"),
    ("TXF", "Teixeira de Freitas (BA)"),
    ("URG", "Uruguaiana (RS)"),
    ("ITB", "Itabuna (BA)"),
    ("TMT", "Porto Trombetas (PA)"),
    ("BSE", "Sematan"),
    ("XAP", "Chapecó (SC)"),
    ("CJZ", "Cajazeiras (PB)"),
    ("BZC", "Búzios (RJ)"),
    ("OIA", "Ourilândia do Norte (PA)"),
    ("PFB", "Passo Fundo (RS)"),
    ("IST", "Istambul"),
    ("ASU", "Assunção"),
    ("PIN", "Parintins (AM)"),
    ("CMN", "Casablanca"),
    ("PET", "Pelotas (RS)"),
    ("QNS", "Canoas (RS)"),
    ("GEL", "Santo Ângelo (RS)"),
    ("GYE", "Guayaquil"),
    ("VDC", "Vitória da Conquista (BA)"),
    ("IAD", "Washington (Dulles)"),
    ("LAX", "Los Angeles"),
    ("ORD", "Chicago (O'Hare)"),
    ("JFK", "Nova York (JFK)"),
    ("EWR", "Newark"),
    ("DFW", "Dallas/Fort Worth"),
    ("IAH", "Houston"),
    ("YYZ", "Toronto"),
    ("JNB", "Joanesburgo"),
    ("CDG", "Paris (Charles de Gaulle)"),
    ("DOH", "Doha"),
    ("CBB", "Cochabamba"),
    ("LHR", "Londres (Heathrow)"),
    ("PEK", "Pequim"),
    ("ZRH", "Zurique"),
    ("ATL", "Atlanta"),
    ("LAD", "Luanda"),
    ("TLV", "Tel Aviv"),
    ("DXB", "Dubai"),
    ("AMS", "Amsterdã"),
    ("BRC", "Bariloche"),
    ("ADD", "Addis Ababa"),
    ("RBR", "Rio Branco (AC)"),
    ("MUC", "Munique"),
    ("MDZ", "Mendoza"),
    ("BOS", "Boston"),
    ("PUJ", "Punta Cana"),
    ("PDP", "Punta del Este"),
    ("ROS", "Rosário"),
    ("COR", "Córdoba"),
    ("BCN", "Barcelona"),
    ("LAS", "Las Vegas"),
    ("OPS", "Sinop (MS)"),
    ("SBD", "San Bernardino"),
    ("EPA", "El Palomar"),
    ("DOU", "Dourados"),
    ("FDF", "Fort-de-France"),
    ("YUL", "Montreal"),
    ("LGG", "Liège"),
    ("RVD", "Rio Verde (GO)"),
    ("MAB", "Marabá (PA)"),
    ("MPN", "Mount Pleasant"),
    ("RAK", "Marrakech"),
    ("MBJ", "Montego Bay"),
    ("AUH", "Abu Dhabi"),
    ("BQN", "Aguadilla"),
    ("HAV", "Havana"),
    ("ISL", "Istambul"),
    ("LOS", "Lagos"),
    ("SJO", "San José"),
    ("DWC", "Dubai (World Central)"),
    ("BSL", "Basileia"),
    ("PTP", "Pointe-à-Pitre"),
    ("SJU", "San Juan"),
    ("POS", "Port of Spain"),
    ("BYJ", "Beja"),
    ("BGA", "Bucaramanga"),
    ("MLA", "Malta"),
    ("ANF", "Antofagasta"),
    ("WDH", "Windhoek"),
    ("ALG", "Argel"),
    ("FAO", "Faro"),
    ("TEV", "Teruel"),
    ("EEA", "Correia Pinto (SC)"),
    ("JPR", "Ji-Paraná (RO)"),
    ("CWF", "Lake Charles"),
]

CITY_MAP = dict(CITY_ITEMS)

INTERNATIONAL_CODES = {
    "LIS", "SID", "AVR", "MXP", "FCO", "PTY", "MIA", "LIM", "LUX", "SCL", "ACC", "BOG", "OPO", "ABJ", "FRA",
    "TFS", "MDE", "BAQ", "PDL", "EZE", "CPT", "PUQ", "AEP", "MAD", "MVD", "MEX", "VVI", "CKY", "TUN", "TNG",
    "UIO", "FLL", "LPA", "RAI", "MCO", "TUC", "FUE", "BSE", "IST", "ASU", "CMN", "GYE", "IAD", "LAX", "ORD",
    "JFK", "EWR", "DFW", "IAH", "YYZ", "JNB", "CDG", "DOH", "CBB", "LHR", "PEK", "ZRH", "ATL", "LAD", "TLV",
    "DXB", "AMS", "BRC", "ADD", "MUC", "MDZ", "BOS", "PUJ", "PDP", "ROS", "COR", "BCN", "LAS", "SBD", "EPA",
    "FDF", "YUL", "LGG", "MPN", "RAK", "MBJ", "AUH", "BQN", "HAV", "ISL", "LOS", "SJO", "DWC", "BSL", "PTP",
    "SJU", "POS", "BYJ", "BGA", "MLA", "ANF", "WDH", "ALG", "FAO", "TEV", "PUC", "CWF"
}

DAY_PT_MAP = {0: "Seg", 1: "Ter", 2: "Qua", 3: "Qui", 4: "Sex", 5: "Sab", 6: "Dom"}


def map_airline(flight_code: str) -> str:
    code = str(flight_code).strip().upper()
    for prefix, airline in AIRLINE_PREFIX_MAP:
        if code.startswith(prefix):
            return airline
    return "Outra"


def replace_season_dates(series: pd.Series, temporada: str) -> pd.Series:
    month_map = SEASON_MONTH_YEAR.get(temporada, {})
    result = series.fillna("").astype(str)
    for month_abbr, replacement in month_map.items():
        result = result.str.replace(month_abbr, replacement, regex=False)
    return result


def split_sir_file(uploaded_file):
    slot_arr, slot_dep, slot_op_dupla = [], [], []

    content = uploaded_file.getvalue().decode("utf-8", errors="ignore")
    for line in content.splitlines():
        line = line.strip()
        if len(line) <= 6:
            continue

        parts = line.split()
        if not parts or not parts[0].startswith("H"):
            continue

        if len(parts) == 6:
            slot_arr.append(parts.copy())
        elif len(parts) == 7:
            slot_dep.append(parts.copy())
        elif len(parts) > 7:
            slot_op_dupla.append(parts.copy())

    for item in slot_op_dupla:
        if len(item) < 8:
            continue

        arr = [item[0], item[2], item[3], item[4], item[5], item[7][:1]]
        dep = ["H", item[1], item[2], item[3], item[4], item[6], item[7][:1]]

        slot_arr.append(arr)
        slot_dep.append(dep)

    return slot_arr, slot_dep


def format_arrivals(records):
    formatted = []
    for item in records:
        if len(item) < 6:
            continue
        row = item.copy()
        row[0] = row[0][1:]
        row[1] = row[1][0:5] + " " + row[1][5:]
        row[3] = row[3][0:3] + " " + row[3][3:]
        row[4] = row[4][0:3] + " " + row[4][3:6] + " " + row[4][6:]
        formatted.append(row)
    return formatted


def format_departures(records):
    formatted = []
    for item in records:
        if len(item) < 7:
            continue
        row = item.copy()
        row[2] = row[2][0:5] + " " + row[2][5:]
        row[4] = row[4][0:3] + " " + row[4][3:]

        if len(row[5]) == 10:
            row[5] = row[5][0:4] + " " + "0" + " " + row[5][4:7] + " " + row[5][7:]
        elif len(row[5]) == 11:
            row[5] = row[5][0:4] + " " + row[5][4:5] + " " + row[5][5:8] + " " + row[5][8:]

        formatted.append(row)
    return formatted


def explode_date_ranges(df: pd.DataFrame) -> pd.DataFrame:
    if df.empty:
        return df.copy()

    ranges = df["Datas"].fillna("").astype(str).str.split(expand=True, n=1)
    if 1 not in ranges.columns:
        ranges[1] = None

    result = df.copy()
    result["data_inicio"] = pd.to_datetime(ranges[0].str.strip(), format="%d%b%Y", errors="coerce")
    result["data_fim"] = pd.to_datetime(ranges[1].str.strip(), format="%d%b%Y", errors="coerce")
    result = result.dropna(subset=["data_inicio", "data_fim"]).copy()

    if result.empty:
        return result

    result["data_op"] = result.apply(
        lambda row: pd.date_range(row["data_inicio"], row["data_fim"], freq="D"),
        axis=1
    )
    result = result.explode("data_op", ignore_index=True)
    return result


def keep_operating_days(df: pd.DataFrame) -> pd.DataFrame:
    if df.empty:
        return df.copy()

    def is_valid_day(row):
        data = pd.to_datetime(row["data_op"], errors="coerce")
        if pd.isna(data):
            return False
        doop = str(row["Doop"]) if pd.notna(row["Doop"]) else ""
        day_num = str(data.dayofweek + 1)
        return day_num in doop

    mask = df.apply(is_valid_day, axis=1)
    return df[mask].copy()


def normalize_hour(series: pd.Series) -> pd.Series:
    extracted = series.fillna("").astype(str).str.extract(r"(\d{1,4})", expand=False).fillna("")
    padded = extracted.where(extracted.eq(""), extracted.str.zfill(4))
    return padded.where(padded.eq(""), padded.str[:2] + ":" + padded.str[2:])


def parse_arrivals(slot_arr, temporada):
    columns = ["N_Voo", "Datas", "Doop", "Assentos_equipamento", "Orig_dep_hora", "Tipo_Voo"]
    if not slot_arr:
        return pd.DataFrame(columns=columns + ["data_op"])

    df = pd.DataFrame(slot_arr, columns=columns)
    df["Datas"] = replace_season_dates(df["Datas"], temporada)
    df = explode_date_ranges(df)
    df = keep_operating_days(df)

    if df.empty:
        return pd.DataFrame(columns=["N_Voo", "Doop", "Tipo_Voo", "data_op", "dia", "Assentos", "Equipamento", "Orig_Dest", "Escala", "Hora", "Arr_Dep"])

    ae = df["Assentos_equipamento"].fillna("").astype(str).str.split(expand=True, n=1)
    if ae.shape[1] < 2:
        ae[1] = ""

    odh = df["Orig_dep_hora"].fillna("").astype(str).str.split(expand=True)
    for col in range(3):
        if col not in odh.columns:
            odh[col] = ""

    out = df.copy()
    out["Assentos"] = ae[0]
    out["Equipamento"] = ae[1]
    out["Orig_Dest"] = odh[0]
    out["Escala"] = odh[1]
    out["Hora"] = normalize_hour(odh[2])
    out["Arr_Dep"] = "A"
    out["dia"] = out["data_op"].dt.dayofweek.map(DAY_PT_MAP).fillna("None")

    return out[["N_Voo", "Doop", "Tipo_Voo", "data_op", "dia", "Assentos", "Equipamento", "Orig_Dest", "Escala", "Hora", "Arr_Dep"]]


def parse_departures(slot_dep, temporada):
    columns = ["Cod Acao", "N_Voo", "Datas", "Doop", "Assentos_equipamento", "Orig_dep_hora", "Tipo_Voo"]
    if not slot_dep:
        return pd.DataFrame(columns=["N_Voo", "Doop", "Tipo_Voo", "data_op", "dia", "Assentos", "Equipamento", "Orig_Dest", "Escala", "Hora", "Arr_Dep"])

    df = pd.DataFrame(slot_dep, columns=columns)
    df = df.drop(columns=["Cod Acao"])
    df["Datas"] = replace_season_dates(df["Datas"], temporada)
    df = explode_date_ranges(df)
    df = keep_operating_days(df)

    if df.empty:
        return pd.DataFrame(columns=["N_Voo", "Doop", "Tipo_Voo", "data_op", "dia", "Assentos", "Equipamento", "Orig_Dest", "Escala", "Hora", "Arr_Dep"])

    ae = df["Assentos_equipamento"].fillna("").astype(str).str.split(expand=True, n=1)
    if ae.shape[1] < 2:
        ae[1] = ""

    odh = df["Orig_dep_hora"].fillna("").astype(str).str.split(expand=True)
    raw_no_space = df["Orig_dep_hora"].fillna("").astype(str).str.replace(" ", "", regex=False)

    hora = odh[0] if 0 in odh.columns else raw_no_space.str[:4]
    if odh.shape[1] >= 4:
        orig_dest = odh[2]
        escala = odh[3]
    elif odh.shape[1] >= 3:
        orig_dest = odh[1]
        escala = odh[2]
    else:
        orig_dest = raw_no_space.str[-6:-3]
        escala = raw_no_space.str[-3:]

    orig_dest = orig_dest.fillna("").astype(str)
    escala = escala.fillna("").astype(str)

    fallback_orig = raw_no_space.str[-6:-3]
    fallback_escala = raw_no_space.str[-3:]

    orig_dest = orig_dest.where(orig_dest.str.len() == 3, fallback_orig)
    escala = escala.where(escala.str.len() == 3, fallback_escala)

    out = df.copy()
    out["Assentos"] = ae[0]
    out["Equipamento"] = ae[1]
    out["Hora"] = normalize_hour(hora)
    out["Orig_Dest"] = orig_dest.str.strip()
    out["Escala"] = escala.str.strip()
    out["Arr_Dep"] = "D"
    out["dia"] = out["data_op"].dt.dayofweek.map(DAY_PT_MAP).fillna("None")

    return out[["N_Voo", "Doop", "Tipo_Voo", "data_op", "dia", "Assentos", "Equipamento", "Orig_Dest", "Escala", "Hora", "Arr_Dep"]]


def compute_bucket(hora_series: pd.Series) -> pd.Series:
    hours = pd.to_numeric(hora_series.fillna("").astype(str).str[:2], errors="coerce")
    bucket = hours.add(1)
    return bucket.fillna(0).astype(int)


def compute_period(bucket_series: pd.Series) -> pd.Series:
    conditions = [
        bucket_series.between(1, 6, inclusive="both"),
        bucket_series.between(7, 11, inclusive="both"),
        bucket_series.between(12, 17, inclusive="both"),
        bucket_series.between(18, 24, inclusive="both"),
    ]
    choices = ["Madrugada", "Manha", "Tarde", "Noite"]
    return pd.Series(np.select(conditions, choices, default="None"), index=bucket_series.index)


def resolve_reference_code(row) -> str:
    orig = str(row.get("Orig_Dest", "")).strip().upper()
    escala = str(row.get("Escala", "")).strip().upper()

    if orig in CITY_MAP:
        return orig
    if escala in CITY_MAP:
        return escala
    return ""


def resolve_zone(row) -> str:
    cia = str(row.get("Cia", "")).strip().upper()
    if cia == "TAP":
        return "I"

    code = resolve_reference_code(row)
    if not code:
        return "None"
    if code in INTERNATIONAL_CODES:
        return "I"
    return "D"


def resolve_city(row) -> str:
    code = resolve_reference_code(row)
    return CITY_MAP.get(code, "None")


def resolve_direct_scale(row) -> str:
    orig = str(row.get("Orig_Dest", "")).strip().upper()
    escala = str(row.get("Escala", "")).strip().upper()
    if not escala or orig == escala:
        return "Voo Direto"
    return "Voo Com escala"


def normalize_output_name(nome_excel: str) -> str:
    nome_saida = nome_excel.strip() if nome_excel and nome_excel.strip() else "malha_gerada.csv"
    if not nome_saida.lower().endswith(".csv"):
        nome_saida += ".csv"
    return nome_saida


def build_output_dataframe(slot_arr, slot_dep, temporada):
    df_arr = parse_arrivals(format_arrivals(slot_arr), temporada)
    df_dep = parse_departures(format_departures(slot_dep), temporada)

    df_voos = pd.concat([df_arr, df_dep], ignore_index=True)
    if df_voos.empty:
        return df_voos

    df_voos["N_Voo"] = df_voos["N_Voo"].fillna("").astype(str).str.strip()
    df_voos["Orig_Dest"] = df_voos["Orig_Dest"].fillna("").astype(str).str.strip().str.upper()
    df_voos["Escala"] = df_voos["Escala"].fillna("").astype(str).str.strip().str.upper()
    df_voos["Assentos"] = df_voos["Assentos"].fillna("").astype(str).str.strip()
    df_voos["Equipamento"] = df_voos["Equipamento"].fillna("").astype(str).str.strip()

    df_voos["Cia"] = df_voos["N_Voo"].apply(map_airline)
    df_voos["bucket"] = compute_bucket(df_voos["Hora"])
    df_voos["Periodo"] = compute_period(df_voos["bucket"])
    df_voos["Mês"] = pd.to_datetime(df_voos["data_op"], errors="coerce").dt.month
    df_voos["Zona"] = df_voos.apply(resolve_zone, axis=1)
    df_voos["Direto_Escala"] = df_voos.apply(resolve_direct_scale, axis=1)
    df_voos["Cidades"] = df_voos.apply(resolve_city, axis=1)

    col_order = [
        "N_Voo",
        "Doop",
        "Tipo_Voo",
        "data_op",
        "dia",
        "Assentos",
        "Equipamento",
        "Orig_Dest",
        "Escala",
        "Hora",
        "Arr_Dep",
        "Cia",
        "bucket",
        "Periodo",
        "Mês",
        "Zona",
        "Direto_Escala",
        "Cidades"
    ]
    
    return df_voos[col_order].sort_values(["data_op", "Hora", "N_Voo"], kind="stable").reset_index(drop=True)


def main():
    st.title("Gerador de Arquivo de Malha")

    nome_arquivo_upload = st.file_uploader("Selecione o arquivo SIR no formato .TXT", type=["txt", "TXT"])
    opcao = st.selectbox("Selecione uma opção:", ["W23", "S24", "W24", "W25", "S25", "S26"])
    nome_excel = st.text_input("Digite o nome do arquivo que deseja receber (ex: UDI_W25_20250721.csv)")

    if st.button("Executar"):
        if nome_arquivo_upload is None:
            st.error("Selecione um arquivo TXT antes de executar.")
            st.stop()

        slot_arr, slot_dep = split_sir_file(nome_arquivo_upload)

        if not slot_arr and not slot_dep:
            st.error("Nenhum registro válido foi encontrado no arquivo enviado.")
            st.stop()

        df_voos = build_output_dataframe(slot_arr, slot_dep, opcao)

        if df_voos.empty:
            st.error("Não foi possível gerar registros com os dados informados.")
            st.stop()

        nome_saida = normalize_output_name(nome_excel)
        csv = df_voos.to_csv(index=False).encode("utf-8-sig")

        st.success(f"Arquivo gerado com sucesso: {len(df_voos)} registros.")
        st.dataframe(df_voos.head(50), use_container_width=True)

        st.download_button(
            label="📥 Baixar arquivo CSV",
            data=csv,
            file_name=nome_saida,
            mime="text/csv",
        )


if __name__ == "__main__":
    main()
