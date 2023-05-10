
aluno = {}
aluno["nome"] = input()
aluno["notas"] = [7,2,8,10,3]

x = aluno["notas"]

y = 0
for i in x:
    y = y+i

print("\n{} tirou: {}".format(aluno["nome"],y/5))
