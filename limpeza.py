#Importando as bibliotecas necessárias
import pandas as pd
import numpy as np

#Leitura do arquivo CSV
df_sujo = pd.read_csv('dados/Base Varejo.csv', sep=';')

#Copiando para limpeza
df = df_sujo.copy()

print(df.head())

def relatorio_qualidade(df):
    """Gera um relatório completo de qualidade do DataFrame."""

    print("=" * 60)
    print("        RELATÓRIO DE QUALIDADE DOS DADOS")
    print("=" * 60)
    print(f"\n Total de linhas:   {df.shape[0]:,}")
    print(f" Total de colunas: {df.shape[1]:,}")
    print(f"Linhas duplicadas: {df.duplicated().sum():,}")

    print("\n Valores ausentes por coluna:")
    nulos = df.isnull().sum()
    pct_nulos = (df.isnull().sum() / len(df) * 100).round(2)

    relatorio = pd.DataFrame({
        'Tipo': df.dtypes,
        'Nulos': nulos,
        '% Nulos': pct_nulos,
        'Únicos': df.nunique()
    })
    print(relatorio)
    print("=" * 60)

relatorio_qualidade(df)

#Verificando nulo escondido
print(df['PR_CAT'].value_counts())
print(df['PR_NOME'].value_counts())

#Padronização de valores inválidos
df.replace(['#N/D','NULL', 'N/A', '', ' '], np.nan, inplace=True)

#Remoção de colunas inúteis
df = df.drop(columns=['Unnamed: 10', 'Unnamed: 11', 'Unnamed: 12', 'Unnamed: 13'])

#Remoção de duplicados
df = df.drop_duplicates()

#Conversão de data
df['DATA'] = pd.to_datetime(df['DATA'],dayfirst=True,errors='coerce')

#Preenchendo valores nulos (if/else)
df['PR_NOME'] = [
    'Sem Nome' if pd.isna(valor) else valor
    for valor in df['PR_NOME']
]

df['PR_CAT'] = [
    'Sem Categoria' if pd.isna(valor) else valor
    for valor in df['PR_CAT']
]

#Padronização de texto
df['PR_CAT'] = df['PR_CAT'].str.title().str.strip()
df['PR_NOME'] = df['PR_NOME'].str.title().str.strip()

#Relatório final de qualidade
relatorio_qualidade(df)

#Visualização final
print("Dados apos limpeza")
print(df.head())

#Versão final limpa
df_limpo = df.copy()

#Salvar dataframe limpo
df_limpo.to_csv('dados/base_varejo_limpa.csv', sep=';',index=False)












