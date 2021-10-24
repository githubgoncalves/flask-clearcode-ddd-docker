# Sobre o Desevolvimento e Execução do Projeto

As APIs REST são construídas usando o framework Flask e Bancos de Dados SqlLite. 

Arquitetura Clean Code baseada em (https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html).

Pré-commits como Git Hooks - são um mecanismo do sistema de controle de versão git. Eles permitem que você execute o código antes do commit.


### Requisitos iniciais 

- Instalar Docker

Clone o projeto usando o comando:
```bash
git clone https://github.com/githubgoncalves/flask-clearcode-ddd-docker.git
```

### Como iniciar a API usando Docker

Vá para o diretório do projeto:
```bash
cd flask-clearcode-ddd-docker
```
Execute o aplicativo com o seguinte comando para executar o container docker:
```bash

docker build -t api-flask-ddd . 

docker run -p 5000:5000 api-flask-ddd 

```

### API


Gerar um token com a API:
```bash

http://localhost:5000/api/auth

```

Utilizar no Authorization (Bearer Token) o Token Gerado, e o uid (12) no Header:
```bash

http://localhost:5000/api/consulta-api

```


**Contato com [DANIEL GONÇALVES](danielgoncalves.info@gmail.com)!**