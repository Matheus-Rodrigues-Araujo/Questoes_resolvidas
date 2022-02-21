'''
    Academia Técnica Capgemini 2022
      * Questão 2
      * Linguagem utilizado: Python 3.10.1
'''

'''
    Variável 'senha' irá receber a senha
'''

senha = input('Digite sua senha: ')

'''
    Foi criada a função 'gerenciador_Senha', com somente um parâmetro, que recebe a senha que o usuário digitou
'''
def gerenciador_Senha(senha):
    # Instrução 'try': É uma instrução que irá verificar se o código funciona, se não houver erro, é executada normalmente.
    try:
        while True:

            '''
                 * Abaixo foram criadas variáveis, que serão os contadores dos caracteres específicos. Se o contador de um
                caractere estiver vazio, significa que o usuário não supriu os requisitos mínimos, logo a senha é inválida e não segura.
                 
                 * Se o contador for igual ou maior que um, o requisito de determinado caractere foi completo. Se o requisito de todos 
                 os caracteres requisitdos forem atendidos, a senha é válida e segura.
            '''
            cont_digitos = 0
            cont_letras_Maiusculas = 0
            cont_letras_Minusculas = 0
            cont_caracteres_Especiais = 0
            '''
                * Esta parte irá verificar se a senha que o usuário digitou atende a quantidade mínima de caracteres, que é 6.
            '''
            if len(senha)>=6:
                ''' 
                    * Se a senha atender o requisito anterior, agora irá ser verificado através de um 'for' e estruturas de condicionais, se na senha, há no mínimo:
                        1 caractere do tipo dígito
                        1 caractere com letra maiúscula
                        1 caractere com letra minúscula
                        1 caractere especial
                    
                '''
                for p in senha:
                    'Aqui verifica-se se tal caractere existe, se sim, o contador é incrementado'
                    # ----------- -      Verificar os dígitos    ---------------------
                    if p.isdigit():
                        cont_digitos += 1
                    
                    # ----------- Verificar as letras maiúsculas  ---------------------
                    elif p.isupper():
                        cont_letras_Maiusculas += 1
                    
                    # ----------- Verificar as letras minúsculas  ---------------------
                    elif p.islower():
                        cont_letras_Minusculas += 1
                    
                    # ----------- Verificar os caracteres especias -------------------
                    # Esse 'else' serve para identificar os caracteres especiais
                    else:
                        cont_caracteres_Especiais +=1
                
                ''' 
                     * Essa parte irá verificar os valores dos contadores. Se cada contador não estiver zerado, significa que
                      a senha do usuário é válida e segura.
                      
                     * Se houver um contador zerado, é utilizado um 'else', que informará os caracteres que faltam.
                '''
                if cont_digitos >=1 and cont_letras_Maiusculas >=1 and cont_letras_Minusculas >=1 and cont_caracteres_Especiais>=1:
                    return 'Parabéns, sua senha é válida e segura'
                
                else:
                    print('>>> ERRO: Sua senha é inválida')
                    print('------------- Atenção ---------------')
                    if cont_digitos == 0:
                        print('  > Adicione ao menos um dígito')
                    
                    if cont_letras_Maiusculas == 0:
                        print('  > Adicione ao menos uma letra maiúscula')
                    
                    if cont_letras_Minusculas == 0:
                        print('  > Adicione ao menos uma letra minúscula')
                    
                    if cont_caracteres_Especiais == 0:
                        print('  > Adicione ao menos um caractere especial.')
                        print('     * Deve ter ao menos um desses: "!@#$%^&*()-+"')
                    # É utilizado outra vez a variável 'senha' para o usuário tentar mais uma vez
                    senha = input('Digite sua senha: ')
            
            # Se a senha tiver menos que 6 caracteres, é utilizado um 'else', em que o código informará
            # quantos caracteres faltam para a senha atingir o tamanho mínimo
            else:
                print('>>> ERRO: Sua senha é inválida')
                print('------------- Atenção ---------------')
                print(f'>>> Sua senha precisa ter mais {6 - len(senha)} caracteres para atingir o tamanho mínimo')
                senha = input('Digite sua senha: ')
    
    # Instrução 'except': É um comando que levantará erros ocorridos durante a execução do código.
    # Se não soubermos quais os tipos de erros, colocamos 'Exception', que mostra quais o(s) erro(s).
    except Exception as e:
        return e

# Esse código executa o arquivo principal, que é esse no caso é o 'questao2.py'
if __name__ == '__main__':
    print(gerenciador_Senha(senha))
