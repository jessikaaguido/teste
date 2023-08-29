# Sobre estruturas de decisão e repetição

1. Os estatísticos gostariam de ter um conjunto de funções para calcular a __mediana__ e o __modo__ de uma lista de números. 
A mediana é o número de apareceria no ponto médio de uma lista se ela fosse ordenada. O modo é o número que aparece com maior 
frequência na lista. Defina essas funções em um módulo chamado stats.py. Também incluir uma função chamada __mean__ , que 
calcula a média de um conjunto de números. Cada função espera uma lista de números como um argumento e retorna um único número.
Seguem exemplos de entrada:
  * Exemplo 01:
    ```
    Lista01: {10, 5, 10, 6, 9, 10, 5, 8, 21, 1, 2, 3}
    Saida esperada:
      mediana: 6 8
      modo: 10
    ```
    _obs._ Quando a lista tem um número par de elementos a mediana é dada pelos dois elementos centrais caso a lista
    estivesse ordenada.
    
  * Exemplo 02:
    ```
    Lista01: {16, 7, 10, 11, 18, 18, 12, 15, 4, 6, 8}
    Saida esperada:
      mediana: 11
      modo: 18
    ```
    
2. Em um dicionário (__dict__) Python foi armazenado o resultado dos testes realizados em um software. Processe o dicionário e
indique quais módulos tem uma cobertura de código menor que um certo percentual.

Entradas:
  * A estatística de cobertura em um arquivo;
  * O limite do percentual de cobertura;

O arquivo __outros/cobertura.txt__ pode ser usado como exemplo de entrada. Utilize as funções de leitura de linhas __readline()__ para ler cada 
entrada do arquivo. A cobertura coleta está indicada a última coluna (_cover_) do arquivo texto.


Saída:
  Nome dos módulos com cobertura menor que o percentual desejado. Informe o nome do módulo e o percentual de cobertura (por exemplo, 80%). 
  É possível que tenham mais que um módulo.

3. Escreva um programa que permita o usuário navegar pelas linhas de texto em um arquivo. O programa deve solicitar ao usuário um nome de
   arquivo e inserir as linhas de texto em uma lista. O programa então deve entrar em um laço do qual imprima o número de linhas no arquivo
   e solicite ao usuário um número de linha. Os números reais das linhas variam de 1 ao número de linhas no arquivo. Se a entrada for 0(zero),
   o programa deve ser encerrado. Do contrário, o programa deve imprimir a linha associada a esse número.

   Uso o arquivo em __outros/arquivo_texto.md__ para testar a sua solução.

   
