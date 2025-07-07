# 💡 Gerador de IDs de Cupons

Este projeto permite gerar IDs únicos para cupons de colaboradores, distribuindo-os aleatoriamente, com exportação final em um arquivo `.txt` pronto para sorteios.

## 📄 Sobre

- Você informa **nome do colaborador** e **quantidade de cupons** em um arquivo `entrada.txt`.
- O script distribui os IDs de forma **aleatória**, mas garante que cada colaborador receba exatamente a quantidade de cupons correta.
- O arquivo de saída (`ids_gerados.txt`) fica em **ordem crescente de IDs**, facilitando conferência.

## ⚙️ Como usar

### ✅ 1️⃣ Preparar arquivo `entrada.txt`

No mesmo diretório do script, crie um arquivo chamado `entrada.txt` com o seguinte formato:

```
Nome Colaborador,quantidade de cupons
Exemplo: Gabriel Jabour,30
```

⚠️ **Não coloque cabeçalho e use vírgula para separar.**

### ✅ 2️⃣ Instalar dependências

```
pip install -r requirements.txt
```

### ✅ 3️⃣ Executar o script

```
python gerar_ids.py
```

O script vai exibir uma mensagem pedindo para você confirmar que o arquivo `entrada.txt` está correto. Pressione ENTER para continuar.

### ✅ 4️⃣ Conferir saída

O arquivo `ids_gerados.txt` será gerado no mesmo diretório, com o seguinte formato:

```
1,Gabriel Jabour
2,Outro Colaborador
3,Gabriel Jabour
...
```

## 💻 Como gerar EXE (opcional)

Se quiser transformar em **executável para Windows** (não precisa ter Python instalado):

```
pip install pyinstaller
pyinstaller --onefile gerar_ids.py
```

O arquivo `.exe` final será criado dentro da pasta `dist/`.

## 📦 Estrutura recomendada do repositório

```
/seu-projeto
├── gerar_ids.py
├── entrada.txt
├── requirements.txt
└── README.md
```

## ✍️ Autor

- **Gabriel Jabour**

## 🗓️ Versão

- **1.0**