import pandas as pd
import random

# === MENSAGEM DE AVISO ===
input(
    '⚠️ Verifique se o arquivo "entrada.txt" está na mesma pasta que este script.\n'
    'O arquivo deve seguir o formato: Nome Colaborador,quantidade de cupons\n'
    'Exemplo de linha: Gabriel Jabour,30\n\n'
    'Autor - Gabriel Jabour - 1.0\n'
    'Caso esteja tudo certo, pressione ENTER para prosseguir...\n'
)

# === CONFIGURAÇÃO ===
arquivo_entrada = 'entrada.txt'
arquivo_saida_txt = 'ids_gerados.txt'
arquivo_saida_excel = 'ids_gerados.xlsx'

try:
    # === LEITURA DO TXT DE ENTRADA ===
    df = pd.read_csv(arquivo_entrada, header=None, names=['colaborador', 'quantidade'])

    # === CRIAR LISTA DE IDS GLOBAIS ===
    total_ids = df['quantidade'].sum()
    ids = list(range(1, total_ids + 1))

    # === EMBARALHAR OS IDS ===
    random.shuffle(ids)

    # === GERAR LISTA FINAL DE DISTRIBUIÇÃO ===
    resultados = []

    current_idx = 0

    for _, row in df.iterrows():
        nome = row['colaborador']
        qtd = row['quantidade']
        ids_colaborador = ids[current_idx:current_idx+qtd]
        for id_value in ids_colaborador:
            resultados.append({'id': id_value, 'colaborador': nome})
        current_idx += qtd

    # === CONVERTER EM DATAFRAME ===
    df_result = pd.DataFrame(resultados)

    # === ORDENAR POR ID ===
    df_result = df_result.sort_values(by='id').reset_index(drop=True)

    # === SALVAR COMO TXT ===
    df_result.to_csv(arquivo_saida_txt, index=False, header=False)

    # === SALVAR COMO XLSX ===
    df_result.to_excel(arquivo_saida_excel, index=False)

    print(f"\n✅ IDs gerados e salvos em:\n- {arquivo_saida_txt}\n- {arquivo_saida_excel}")

except FileNotFoundError:
    print('\n❌ Arquivo "entrada.txt" não encontrado! Verifique se ele está na mesma pasta e tente novamente.')
except Exception as e:
    print(f'\n❌ Ocorreu um erro: {e}') 