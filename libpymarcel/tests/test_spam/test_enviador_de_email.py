import pytest
from libpymarcel.spam.enviador_de_email import Enviador, EmailInvalido


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


@pytest.mark.parametrize(
    'remetente',
    ['foo@bar.com.br ', 'marcellatorraca@gmail.com']
)
def test_remetente(remetente):
    enviador = Enviador()
    resultado = enviador.enviar(
        remetente,
        'kamila_ld@hotmail.com',
        'Teste de envio',
        'E-mail enviado para teste'
    )
    assert remetente in resultado


@pytest.mark.parametrize(
    'remetente',
    ['', 'marcellatorraca']
)
def test_remetente_invalido(remetente):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(
            remetente,
            'kamila_ld@hotmail.com',
            'Teste de envio',
            'E-mail enviado para teste'
        )
