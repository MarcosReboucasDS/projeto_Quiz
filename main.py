from quiz import *

#oh my got

if __name__ == "__main__":
    q1 = Quiz(10, 2)
    print(q1)
    q2 = Quiz2A(10, 2)
    print(q2)
    q3 = Quiz3A(10, 2)
    print(q3)

    lista_quiz = [q1, q2, q3]
    aluno1 = Aluno(1, "Elais", lista_quiz)
    print(aluno1)
    aluno2 = Aluno(2, "Annalice", lista_quiz)
    print(aluno2)
    try:
        poo = Disciplina("POO", "Érika", 2024, 2)
        poo.add_aluno(aluno1)
        poo.add_aluno(aluno2)
        poo.add_aluno(aluno1)
    except Exception as e:
        print(poo)