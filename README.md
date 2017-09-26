# BDOdonto
Aplicação feita com Django para alimentar um banco de dados com fichas de atendimento para o Curso de Odontologia da UFPI

## Dependencias
* mysql >= 5.7
* Python3
* Django >= 1.10

## Preparação
* Edite o arquivo `bdOdonto/config.ini` substituindo o `user_bd` e `password_bd` pelo nome de usuario e senha do banco de dados, respectivamente.
```
[mysql] 
host=localhost
user=user_bd    
database=bdodonto
password=password_bd
```

## Execução
`python3 manage.py runserver`
