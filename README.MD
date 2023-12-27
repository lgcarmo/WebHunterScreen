**Web Hunter Screen**

- [x] O Web Hunter Screen realiza o acesso automatizado às URLs e cria um screenshot de cada página.

**Principais opções:**

- `-p`: Cria a pasta do projeto para armazenar as imagens.
- `-f`: Carrega uma lista contendo URLs (Ex. https://site.com.br) por [K40S](https://github.com/lgcarmo/Scrap_Forever).
- `--sqlite`: Carrega arquivo SQLite gerado pelo TurboSearch por [M4v3r1cK](https://github.com/helviojunior/turbosearch).

**USO:**
```bash
$ python3 webhunterscreen.py -f /file/domains.txt -p PROJECT
```
```bash
$ python3 webhunterscreen.py --sqlite FILE
```
**Ferramentas relacionadas:**

O Helvio Junior (M4v3r1cK) criou a ferramenta TurboSearch. Esta é uma ferramenta de busca (estilo brute-force) baseada em uma lista de palavras para automatizar o mapeamento de diretórios. A ferramenta está preparada para salvar seus resultados em um arquivo SQLite que pode ser consumido pelo Web Hunter Screen.

O Luiz Carmo (K40S) criou a ferramenta Scrap Forever. Esta ferramenta é utilizada para coletar URLs em uma página de forma que não termine enquanto não chegar à última página.
