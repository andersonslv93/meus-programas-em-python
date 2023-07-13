#variavel
primeiro = float(input('Digite o índice de p0luição: '))

#processamento
if primeiro == 0.3:
    print('O 1º grupo deve suspender suas atividades imediatamente!')
elif primeiro == 0.4:
    print('O 1º e o 2º grupo devem suspender suas atividades imediatamente!')
elif primeiro >= 0.5:
    print('TODOS os grupos devem suspender suas atividades imediatamente!')
else:
    print('Todos os grupos podem continuar com suas atividades normalmente.')
