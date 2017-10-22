import pytest

# Test.assert_equals(pig_it('Pig latin is cool'),'igPay atinlay siay oolcay')
# Test.assert_equals(pig_it('This is my string'),'hisTay siay ymay tringsay')

STRINGS = [
    ('Pig latin is cool', 'igPay atinlay siay oolcay'),
    ('This is my string', 'hisTay siay ymay tringsay'),
    ('Bob The Builder', 'obBay heTay uilderBay'),
    ('She sells seashells', 'heSay ellssay eashellssay'),
    ('lollipop lady madonna', 'ollipoplay adylay adonnamay'),
    ('boy for sale !', 'oybay orfay alesay !'),
    ('once twice three times a lady', 'nceoay wicetay hreetay imestay aay adylay'),
    ('second exit on the left', 'econdsay xiteay noay hetay eftlay')
]

@pytest.mark.parametrize('py_string, result', STRINGS)
def test_words_in_string_are_converted_to_py_latin(py_string, result):
    from simple_pig_latin import pig_it
    assert pig_it(py_string) == result
