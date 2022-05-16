"""
93. Exercício - Undo e Redo

Fazer uma lista de tarefas com as seguintes opções:
    Adicionar tarefas
    Listar tarefas
    Desfazer (remove a ultima tarefa cada vez que for chamado)
    Refazer (Adiciona a ultima tarefa removida)
"""


# Listas vazias
tasks = []
desfeitas = []

# Entrada do usuário
print('1. Adicionar tarefas\n'
      '2. Listar tarefas\n'
      '3. Remover ultima tarefa adicionada\n'
      '4. Desfazer')
nova_task = int(input('Digite o que deseja fazer: '))
