
'''
    Academia Técnica Capgemini 2022
      * Questão 1
      * Linguagem utilizado: Python 3.10.1
'''

'''
    1° Passo: Pedir ao usuário uma entrada(variável 'valor_entrada'), cuja é a quantidade de linhas com asterisco que o programa irá criar a cada iteração;
'''
valor_entrada = int(input('Digite o valor: '))

'''
    2° Passo:   O valor da entrada(valor_entrada) é inserido no método 'range', fazendo então um looping.
              Uma variável 'val' recebe os valores a cada iteração do looping. Se a entrada
              recebesse, por exemplo valor 6, a variável 'val' teria valores de 0 até 5, já que a
              linguagem Python não conta o último valor, nesse caso o valor 6.
'''
for val in range(valor_entrada):
        """
            3° Passo: Para mostrarmos o resultado, temos de conhecer o seguinte código, cujo está divido nos seguintes passos:
                
                1°:   Para saber a quantidade de espaços necessários, temos de 'multiplicar' a string, que é o espaço(" "), vezes
                      o número de espaço que desejamos. Abaixo temos a demonstração lógica e a demonstração com código:
                    
                       * Expressão sem código : 
                            quantidade de espaço vezes (valor_entrada - (val+1)).
                       
                       * Expressão com código:
                            " " * (valor_entrada - (val+1))               
                
                2°:    Agora iremos concatenar com os espaços a quantidade de '*' por linha. Para isso, temos que primeiro determinar
                       a quantidade de asteriscos, e isso é feito através da 'multiplicação' de '*' pelo valor de 'val' + 1, e faz que
                       o número de asteriscos seja igual ao índice.

                       *Obs: val + 1 porque, como foi dito antes, o último valor do intervalo é excluído. Por isso deve-se somar mais 1,
                             para termos a quantidade de asteriscos na quantidade certa e ficar mais fácil de entender.
                
                3° : A cada iteração o número de espaços vai diminuindo, e o número de asteriscos vai aumentando por linha
                
        """
        print(" " * (valor_entrada - (val+1)) + "*" * (val+1)
    )
