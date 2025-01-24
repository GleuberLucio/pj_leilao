import pandas as pd

# Caminho do arquivo baixado
CAMINHO_ARQUIVO = r"C:\Users\gleuber.silva\Downloads\Lista_imoveis_DF (4).csv"

def ler_e_formatar_arquivo_csv(caminho_arquivo):
    try:
        # Lendo o arquivo CSV
        df = pd.read_csv(caminho_arquivo, encoding="utf-8", sep=";")  # Ajuste o separador e encoding conforme necessário
        print("Arquivo lido com sucesso!")

        # Exibindo as primeiras linhas para inspecionar
        print(df.head())

        # Formatação básica (mesmo processo do Excel)
        df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]
        df = df.dropna(how="all")
        df = df.drop_duplicates()

        # Salvando o arquivo formatado
        df.to_csv("consulta_formatada.csv", index=False)
        print("Arquivo formatado e salvo como 'consulta_formatada.csv'.")

        return df

    except Exception as e:
        print(f"Erro ao ler ou formatar o arquivo: {e}")
        return None

# Chamando a função
df_formatado = ler_e_formatar_arquivo_csv(CAMINHO_ARQUIVO)
