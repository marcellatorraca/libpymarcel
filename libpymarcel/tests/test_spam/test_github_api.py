from unittest.mock import Mock

import pytest

from libpymarcel import github_api


@pytest.fixture
def avatar_url(mocker):
    resp_mock = Mock()
    url = 'https://avatars0.githubusercontent.com/u/26558863?v=4'
    resp_mock.json.return_value = {
        'login': 'marcellatorraca', 'id': 26558863,
        'avatar_url': url,
    }
    get_mock = mocker.patch('libpymarcel.github_api.requests.get')
    get_mock.return_value = resp_mock
    return url


def test_buscar_avatar(avatar_url):
    url = github_api.buscar_avatar('marcellatorraca')
    assert avatar_url == url


def test_buscar_avatar_integracao():
    url = github_api.buscar_avatar('marcellatorraca')
    assert 'https://avatars0.githubusercontent.com/u/26558863?v=4' == url
