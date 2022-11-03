class Aluno:
    def __init__(self,nome,curso,tempoSemDormir) :
        self.nome=nome
        self.curso=curso
        self.tempoSemDormir=tempoSemDormir
    
    def estudar(self,qtdHorasEstudo):
        self.tempoSemDormir+=qtdHorasEstudo
        return self.tempoSemDormir
    
    def dormir(self,qtdHorasSonos):
        self.tempoSemDormir-=qtdHorasSonos
        return self.tempoSemDormir

aluno1= Aluno("Abinoã", "Sistemas de informação",8)
aluno1.estudar(4)
aluno1.dormir(5)
print(aluno1.tempoSemDormir)

       