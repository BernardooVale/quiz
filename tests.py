import pytest
from model import Question


def test_create_question():    
    question = Question(title='q1')
    assert question.id != None

def test_create_multiple_questions():
    question1 = Question(title='q1')
    question2 = Question(title='q2')
    assert question1.id != question2.id

def test_create_question_with_invalid_title():
    with pytest.raises(Exception):
        Question(title='')
    with pytest.raises(Exception):
        Question(title='a'*201)
    with pytest.raises(Exception):
        Question(title='a'*500)

def test_create_question_with_valid_points():
    question = Question(title='q1', points=1)
    assert question.points == 1
    question = Question(title='q1', points=100)
    assert question.points == 100

def test_create_choice():
    question = Question(title='q1')
    
    question.add_choice('a', False)

    choice = question.choices[0]
    assert len(question.choices) == 1
    assert choice.text == 'a'
    assert not choice.is_correct
    
def test_cria_opcao_invalida():
    
    p = Question(title='p')
    
    with pytest.raises(Exception):
        p.add_choice("")
    with pytest.raises(Exception):
        p.add_choice("p"*101)
        
def test_pontuacao_invalida():
    
    with pytest.raises(Exception):
        Question(title='p', points=0)
    with pytest.raises(Exception):
        Question(title='p', points=-1)
    with pytest.raises(Exception):
        Question(title='p', points=101)
    
def test_cria_multiplas_opcoes_corretas():
    
    pergunta = Question(title="p", max_selections=2)
    
    pergunta.add_choice('a', True)
    pergunta.add_choice('b', True)
    
    r1 = pergunta.choices[0]
    r2 = pergunta.choices[1]
    
    assert len(pergunta.choices) == 2
    assert r1.is_correct
    assert r2.is_correct

def test_resposta_correta():
    
    pergunta = Question(title='p', max_selections=1)
    
    pergunta.add_choice('a', True)
    pergunta.add_choice('b', False)
    
    r1 = pergunta.choices[0]
    
    lista = pergunta.correct_selected_choices([r1.id])
    
    assert len(lista) == 1
    
    assert lista[0] == r1.id

def test_respota_errada():
    
    pergunta = Question(title='p', max_selections=1)
    
    pergunta.add_choice('a', True)
    pergunta.add_choice('b', False)
    
    r2 = pergunta.choices[1]
    
    lista = pergunta.correct_selected_choices([r2.id])
    
    assert len(lista) == 0
    
def test_remove_todas_opcoes():
    
    pergunta = Question(title='p')
    
    pergunta.add_choice('a')
    pergunta.add_choice('b')
    
    pergunta.remove_all_choices()
    
    assert len(pergunta.choices) == 0
    
def test_def_opcao_correta():
    
    p = Question(title='p')
    
    p.add_choice('a')
    
    assert not p.choices[0].is_correct
    
    p.set_correct_choices([p.choices[0].id])
    
    assert p.choices[0].is_correct
    
def test_def_opcoes_corretas():
    
    p = Question(title='p', max_selections=2)
    
    p.add_choice('a')
    p.add_choice('b')
    
    assert not p.choices[0].is_correct
    assert not p.choices[1].is_correct
    
    p.set_correct_choices([p.choices[0].id, p.choices[1].id])
    
    assert p.choices[0].is_correct
    assert p.choices[1].is_correct
    
def test_ids_unicos_por_opcoes():
    
    p = Question('p')
    
    p.add_choice('a')
    p.add_choice('b')
    
    assert p.choices[0] != p.choices[1]
    
def test_max_opcoes_selecionadas():
    
    p = Question('p')
    
    p.add_choice('a')
    p.add_choice('b')
    
    with pytest.raises(Exception):
        p.correct_selected_choices([p.choices[0].id, p.choices[1].id])