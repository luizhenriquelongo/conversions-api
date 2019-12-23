# Conversions API
API desenvolvida com foco no desafio-problema sugerido pela empresa Movidesk

## Tecnologias Utilizadas:
- Python 3.6.9
- Flask 1.1.1
- HTML5, CSS3 e JavaScript
- MongoDB

## Instalação:

### Ambiente Linux: 
Para podermos rodar o projeto, precisamos primeiro criar um ambiente virtual para instalar todas as dependências e para isso utiliaremos o virtualenv.

Utilize o seguinte comando para instalar o virtualenv caso não o tenha instalado:

```sudo apt install virtualenv -y```

Com o virtualenv instalado, podemos criar o ambiente virtual e instalar os pacotes. No diretório do projeto utilize o seguinte comando:

```virtualenv -p python3 --clear venv```

Utilize os seguintes comandos para entrar e sair do ambiente virtual:

```
source venv/bin/activate # ativar o ambiente virtual
deactivate 				 # desativar o ambiente virtual

```

Com o ambiente virtual ativo, utilize o comando abaixo para installar as dependencias:

``` pip install -r requirements.txt```

Para o acesso ao banco de dados, o sistema utiliza de duas variáveis de ambiente, para crialas nativamente utilize os comandos:

```bash
    export 'MONGO_USER'='<user>' 
    export 'MONGO_PASSWORD'='<password>' 
```

P.S.: Também é possível simular essas variaveis de ambiente em alguns editores de texto ou IDEs.

## Uso:

Para iniciar o servidor, da pasta raiz do projeto, podemos acessar a pasta 'src' e usar o seguinte comando:

```flask run```

Caso este comando não funcione, podemos inicia-lo através do próprio python:

```python app.py```

Desta forma o servidor estará funcionando e disponível para acesso no link: http://127.0.0.1:5000/

## Endpoints

Formulário de inserção de dados: 

- http://127.0.0.1:5000/

Para que a API realize e retorne a análise de dados, é necessário passar a data inicial e final do filtro via url:

- Padrão de data aceito: DD-MM-YYYY
-  http://127.0.0.1:5000/api/v1/conversions/<data_inicial>/<data_final>

Acesso aos dados do banco de dados (limitado a 50 documentos):
- http://127.0.0.1:5000/api/v1/conversions/

## Populando o Banco de Dados

*Para popular o banco de dados foi utilizado o scrip que se encontra na pasta src/db/populating_db.py*

**Não rodar o script novamente pois isso ocasionará a duplicação dos dados no servidor, o script não foi pensado pra atualizar dados e sim para agilizar o processo de inserção**

## To-do:

- Refatorar alguns arquivos;
- Organizar melhor a estrutura de pastas e arquivos;
- Realizar testes unitários;
- Realizar testes dos endpoints;
- Disponibilizar um endpoint para que os dados possam ser inseridos via json na API;

## Autores:

- [Luiz Henrique Longo](https://www.linkedin.com/in/luizhenriquelongo/)