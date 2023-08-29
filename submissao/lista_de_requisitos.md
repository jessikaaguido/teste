# Lista de Requisitos #

### Classe Farmacia:
1. O atributo _nome_ deve iniciar obrigatoriamente com um caracter alfabético e conter 30 caracteres no máximo

2. O atributo _endereco_ é um dicionário que deve seguir minimamente a estrutura abaixo. Importante ressaltar que uma [chave] não deve aceitar um [valor] vazio (''):
    ```
    endereco = {'rua' : '', 'numero' : '', 'complemento': '', 'bairro': '', 'cidade': '', 'estado' : '', 'país': ''}
    ```

3. Tanto o atributo _nome_ quanto as chaves do atributo _estoque_ devem ter seus caracteres alfabéticos armazenados no formato **Lower Case**. Os métodos mutadores devem garantir e validar este requisito.

4. O atributo _estoque_ é um dicionário com a seguinte estrutura obrigatória:
    ```
    estoque = {'medicamento' : 'quantidade', ...}
    ```

5. A _quantidade_ [valor] deve ser armazenada como string, embora retrate um inteiro, cujo valor default é 0.0 (zero) e, eventualmente, possa ser negativo.

6. Métodos acessores e mutadores: *get_nome()*, *set_nome()*, *get_endereco()*, *set_endereco()*, *get_estoque()* e *set_estoque()*

7. O método *exibir_informacoes_cadastrais()* deve imprimir uma string formatada contendo o atributo _nome_ e o atributo _endereco_; se algum desses atributos não estiver presente, uma **mensagem de erro** _Cadastro incompleto ou inválido_ deve ser impressa

8. O método *exibir_estoque()* deve imprimir uma string formatada do _estoque_, do seguinte modo:
    ```
    Estoque
    Medicamento 1: xx unidade(s)
    Medicamento 2: yy unidade(s)
    ...
    Medicamento N: ww unidade(s)
    ```

### Classe FarmaciaVarejo:
1. O atributo *quantidade_clientes* deve ser um inteiro não negativo.

2. O atributo *quantidade_funcionarios* deve ser um inteiro não negativo.

3. Métodos acessores e mutadores: *get_quantidade_clientes()*, *set_quantidade_clientes()*, *get_quantidade_funcionarios()*, *set_quantidade_funcionarios()*, *get_faturamento_mensal()* e *set_faturamento_mensal()*

4. O método *comprar_medicamento (medicamento: string, quantidade: int)* deve representar a aquisição/entrada de medicamentos para o estoque, isto é, o método deve modificar positivamente o atributo _estoque_. Para tanto:  
(1) se a _quantidade_ [valor] indicada do _medicamento_ [chave] for igual a ou menor que 0 (zero), uma **mensagem de erro** _Quantidade inválida_ será impressa.  
(2) se o _medicamento_ [chave] já existe no dicionário _estoque_, o método apenas incrementará a _quantidade_ [valor] existente.  
(3) se o _medicamento_ [chave] ainda não existe no dicionário _estoque_, o método deve criar uma nova entrada no dicionário _estoque_. 

5. O método *vender_medicamento (medicamento: string, quantidade: int)* deve representar a saída de medicamentos do estoque, isto é, o método deve modificar negativamente o atributo _estoque_. Uma venda só é realizada:  
(1) se o _medicamento_ [chave] já existe no dicionário _estoque_; e  
(2) se a _quantidade_ indicada [valor] do _medicamento_ [chave] não for superior à _quantidade_ [valor] constante no _estoque_:  

6. Uma venda não será realizada:  
(1) se a _quantidade_ [valor] indicada do _medicamento_ [chave] for igual a ou menor que 0 (zero). Nessa situação, uma **mensagem de erro** _Quantidade inválida_ será impressa.   
(2) se a _quantidade_ [valor] indicada do _medicamento_ [chave] for superior à _quantidade_ [valor] já registrada no _estoque_. Uma **mensagem de erro** _Quantidade solicitada superior à disponível no Estoque_ deverá ser impressa   
(3) se o _medicamento_ [chave] não existe no dicionário _estoque_. Uma **mensagem de erro** _Medicamento inexistente no Estoque_ será impressa

### Classe FarmaciaPopular:
1. O atributo *desconto_medicamentos* é um dicionário que representa os medicamentos e seus respectivos descontos. Ele possui a seguinte estrutura obrigatória:
    ```
    desconto_medicamentos = {'medicamento' : 'desconto', ...}
    ```
2. O _desconto_ [valor] deve ser armazenado como string, embora retrate um número real. Esse valor não pode ser negativo; caso seja, nenhuma alteração ocorrerá.

3. O atributo *faturamento_mensal* é um dicionário com a seguinte estrutura obrigatória:  
    ```
    faturamento_mensal = {'mes' : 'faturamento_do_mes', ...}
    ```
4. A chave do atributo *faturamento_mensal* só admite caracteres alfabéticos, e no formato **Lower Case*. Quer a chave _março_, quer a chave _marco_, ambas são válidas.

5. O *faturamento_do_mes* [valor] deve ser armazenado como string, embora retrate um número real e, eventualmente, possa ser negativo.

6. Métodos acessores e mutadores: *get_desconto_medicamentos()*, *set_desconto_medicamentos()*, *get_convenios()* e *set_convenios()*

7. O método *aplicar_desconto (medicamento: string)* deve retornar o valor do percentual de _desconto_ de um dado _medicamento_. Para tanto, uma consulta ao atributo _estoque_ e ao atributo *desconto_medicamentos* deve ser realizada. Se o _medicamento_ ou o _convenio_ informado não existir naqueles atributos, retornar o valor 0.0 (zero).

8. O método *calcular_faturamento_anual()* deve retornar o somatório dos registros constantes no dicionário *faturamento_mensal*.

# Modelos válidos de objetos #

```
# nome: string
nome = 'Farma 10'
    
# endereco: dict
endereco = {'rua' : 'rua baker', 'numero' : '221b', 'complemento': '', 'bairro': '', 'cidade': 'londres', 'estado' : 'am', 'país': 'br'} 
    
# estoque: dict
estoque = {'dipirona' : '10', 'ibuprufeno' : '2', 'aspirina' : '0', ...}
    
# faturamento_mensal: dict
faturamento_mensal = {'janeiro' : '2000.00', 'fevereiro' : '0.0', 'março' : '-100.00', ...}
    
# desconto_medicamentos: dict
desconto_medicamentos = {'dipirona' : '0.12', 'ibuprufeno' : '0.4', 'aspirina' : '0.0', ...}

```    
