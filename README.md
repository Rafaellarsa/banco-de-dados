# banco-de-dados
Projeto para a disciplina de Banco de Dados I (2021.2), do professor Leonardo Oliveira.

## Equipe
| Nome               | Matricula |  
|--------------------|-----------|
| Ellen Pessoa       | 473928    |   
| Ivna Almeida       | 469887    |    
| Rafaella Sampaio   | 469886    |  
| Rebecca Cavalcante | 473196    | 
| Vaneska Sousa      | 476389    | 

## Sobre o Projeto:

### Quick Finder: Artefatos
* Apresentação em vídeo: https://drive.google.com/file/d/1N-DZYbYjv5vYluKupx8RRww8H79styOf/view?usp=sharing
* Repositório: https://github.com/Rafaellarsa/banco-de-dados
* MER: https://i.imgur.com/BEUvB4a.png
* Banco de dados (.sql): https://github.com/Rafaellarsa/banco-de-dados/tree/master/database

* MER - Modelo Relacional
![](https://i.imgur.com/BEUvB4a.png)
> Clique na imagem acima para dar zoom.

### Pré-requisitos:
- [Python](https://www.python.org/downloads/);
- [PyCharm](https://www.jetbrains.com/pt-br/pycharm/download/) (ou outra IDE);
- [Psycopg2](https://kb.objectrocket.com/postgresql/how-to-install-psycopg2-in-windows-1460);
- [PgAdmin4](https://www.pgadmin.org/download/) (ou outro que leia postgree)

### Para rodar a aplicação:
1. Baixar ou clonar este repositorio;
2. Abrir o arquivo [voluntariado.sql](https://github.com/Rafaellarsa/banco-de-dados/blob/master/database/voluntariado) no pgadmin4
3. Importar o projeto no Pycharm (ou na IDE de sua preferencia)
4. Abrir o arquivo [PsycopgParameters.py](https://github.com/Rafaellarsa/banco-de-dados/blob/master/PsycopgParameters.py) e alterar os campos *password, port e user para ficar de acordo ao que foi configurado no pgadmin*. <br>
5. Executar o arquivo [main.py](https://github.com/Rafaellarsa/banco-de-dados/blob/master/main.py).
