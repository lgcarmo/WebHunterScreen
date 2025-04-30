# 🕷️ WebHunterScreen

Ferramenta de captura automatizada de screenshots de páginas web com suporte a múltiplas threads, modo headless e entrada via arquivo ou banco SQLite. Ideal para reconhecimento de ativos em pentests.

---

## ⚙️ Funcionalidades

- Captura screenshots de sites usando Selenium + Chrome
- Suporte a entrada via `.txt` ou banco SQLite (`TurboSearch`)
- Execução em paralelo com múltiplas threads
- Modo `headless` opcional (sem abrir a janela do navegador)
- Delay configurável entre carregamento e captura
- Armazena capturas em uma pasta com o nome do projeto

---

## 📦 Instalação

### 1. Clone o repositório

```bash
git clone https://github.com/seuusuario/WebHunterScreen.git
cd WebHunterScreen
```

### 2. (Opcional) Crie um ambiente virtual

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

> Requisitos do sistema:
> - Python 3.8+
> - Google Chrome ou Chromium instalado
> - ChromeDriver será instalado automaticamente via `webdriver-manager`

---

## 🚀 Uso

### A partir de um arquivo `.txt` com URLs

```bash
python3 webhunterscreen.py -f urls.txt -p projeto_site
```

### A partir de um banco SQLite (`TurboSearch`)

```bash
python3 webhunterscreen.py --sqlite resultados.db -p projeto_sqlite
```

### Usando modo `headless` e delay de 5 segundos

```bash
python3 webhunterscreen.py -f urls.txt -p meu_projeto --headless --delay 5
```

---

## 🔧 Parâmetros

| Parâmetro         | Descrição                                                                 |
|-------------------|---------------------------------------------------------------------------|
| `-f`              | Caminho do arquivo `.txt` com uma URL por linha                          |
| `--sqlite`        | Caminho do banco SQLite com a tabela `stats` e a coluna `uri`            |
| `-p`              | Nome do projeto (pasta onde os screenshots serão salvos)                 |
| `-t`              | Número de threads para execução paralela (padrão: 4)                     |
| `--headless`      | Executa o navegador em modo invisível (sem abrir a janela gráfica)       |
| `--delay`         | Delay em segundos antes de capturar o screenshot (padrão: 2 segundos)    |

⚠️ Use apenas um dos parâmetros de entrada: `-f` ou `--sqlite`.

---

## 🗂️ Exemplo de saída

```
projeto_site/
├── www.google.com.png
├── api.empresa.com.br.png
└── login.sistema.local.png
```

---

## 🧪 Exemplo de entrada (urls.txt)

```
https://www.google.com
http://painel.minhaempresa.local
https://admin.site.com.br
```

---

## 📁 requirements.txt

Crie um arquivo chamado `requirements.txt` com o seguinte conteúdo:

```
selenium>=4.10.0
webdriver-manager>=3.8.6
```

---

## 👨‍💻 Autor

Desenvolvido por [Seu Nome](https://github.com/seuusuario)  
Inspirado em atividades de automação de reconhecimento em segurança ofensiva.

---

## 🛡️ Licença

Distribuído sob a Licença MIT.  
Use com responsabilidade e ética profissional em segurança da informação.
