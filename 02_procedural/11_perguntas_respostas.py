print('\n* * * * Prova * * * *\n')


perguntas = {
    'Pergunta 1': {
        'pergunta': 'Quanto é 2 + 2?',
        'respostas': {
            'a': '1',
            'b': '4',
            'c': '5'
        },
        'resposta_certa': 'b'
    },
    'Pergunta 2': {
        'pergunta': 'Quanto é 3 x 2?',
        'respostas': {
            'a': '4',
            'b': '101',
            'c': '6'
        },
        'resposta_certa': 'c'
    }
}

print()

respostas_certas = 0

for pergunta, dados_pergunta in perguntas.items():
    print(f'{pergunta}: {dados_pergunta["pergunta"]}')

    print('Alternativas')
    for resposta, dados_resposta in dados_pergunta['respostas'].items():
        print(f'[{resposta}]: {dados_resposta}')

    resposta_usuario = input('Sua resposta: ')

    if resposta_usuario == dados_pergunta['resposta_certa']:
        print('Você acertou!')
        respostas_certas += 1
    else:
        print('Você errou!')
    
    print()

quantidade_perguntas = len(perguntas)
porcentagem_acerto = respostas_certas / quantidade_perguntas * 100

print(f'\nVocê acertou {respostas_certas} respostas.')
print(f'Sua porcentagem de acerto foi: {porcentagem_acerto}%\n')