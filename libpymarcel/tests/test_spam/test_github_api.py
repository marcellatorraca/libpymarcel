from unittest.mock import Mock

from libpymarcel import github_api


def test_buscar_avatar():
    resp_mock = Mock()
    resp_mock.json.return_value = {
        'login': 'marcellatorraca', 'id': 26558863,
        'avatar_url': 'https://avatars0.githubusercontent.com/u/26558863?v=4',
    }
    github_api.requests.get = Mock(return_value=resp_mock)
    url = github_api.buscar_avatar('marcellatorraca')
    assert 'https://avatars0.githubusercontent.com/u/26558863?v=4' == url
