from character_copier_kata.copier import ISource, IDestination, Copier


class TestCopier:

    def test_given_single_char_should_copy_char(self, mocker):
        source = mocker.Mock(spec=ISource)
        destination = mocker.Mock(spec=IDestination)
        source.get_char.side_effect = ["a", "\n"]
        copier = Copier(source, destination)

        copier.copy_character()

        assert source.get_char.call_count == 1
        assert destination.set_char.call_count == 1
        destination.set_char.assert_called_once_with("a")
