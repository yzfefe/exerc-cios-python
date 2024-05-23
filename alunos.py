aluno = []

while True:
    nome_aluno = input("insira: ")
    if nome_aluno == "fim":
        break
    aluno_parcial = input('parcial: ')
    aluno_bimestral = input('bimestral: ')
    aluno.append({'nome' : nome_aluno, 'nota parcial' : aluno_parcial, 'bimestral' : aluno_bimestral})
    print(aluno)