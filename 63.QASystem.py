"""
Sistema de perguntas e respostas utilizando diionários em Python
"""

print()
print('Sistema de perguntas e respostas.')
print('Você verá algumas perguntas, ao final escolha uma resposta que julgar correta.')
respostas_certas = 0


perguntas = {
    'pergunta 1': {
        'pergunta': 'Quanto é 2+2?',
        'respostas': {'a': '3', 'b': '4', 'c': '6'},
        'resposta_certa': 'b'
    },
    'pergunta 2': {
        'pergunta': 'Quanto é 3x5?',
        'respostas': {'a': '12', 'b': '18', 'c': '15'},
        'resposta_certa': 'c'
    }
}
print()

for pk, pv in perguntas.items():
    print(f'{pk}: {pv["pergunta"]}')

    print('Respostas: ')
    for rk, rv in pv['respostas'].items():
        print(f'[{rk}]: {rv}')

    resposta_user = input('Sua resposta: ')
    print()

    if resposta_user == pv['resposta_certa']:
        print('Obaaa!!!! Você acertooou! ><><><><')
        respostas_certas += 1
    else:
        print('Oops, você errou. :( ')

print(f'Total de acertos: {respostas_certas}')
qtd_perguntas = len(perguntas)
porc_acertos = (respostas_certas * 100) / qtd_perguntas
print(f'Você teve um aproveitamento de {porc_acertos}% de respostas certas')
