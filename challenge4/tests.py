import unittest
from unittest import mock
import duplicate


class TestDuplicate(unittest.TestCase):

    @mock.patch("duplicate.os")
    @mock.patch("duplicate.filecmp")
    def test_most_basic_duplicate(self, mock_filecmp: mock.Mock, mock_os: mock.Mock) -> None:
        # Setup Mocks
        mock_os.walk.return_value = [(".", [], ["test.txt", "test.txt"])]
        mock_filecmp.cmp.return_value = True

        # Run Removal
        duplicate.delete(".", interactive=False)

        # Test Removal Calls
        mock_os.remove.assert_called_once_with("./test.txt")

    @mock.patch("duplicate.os")
    @mock.patch("duplicate.filecmp")
    def test_no_matching_names(self, mock_filecmp: mock.Mock, mock_os: mock.Mock) -> None:
        # Setup Mocks
        mock_os.walk.return_value = [(".", [], ["test.txt", "test.csv"])]
        mock_filecmp.cmp.return_value = True  # Shouldn't Matter

        # Run Removal
        duplicate.delete(".", interactive=False)

        # Test Removal Calls
        mock_os.remove.assert_not_called()

    @mock.patch("duplicate.os")
    @mock.patch("duplicate.filecmp")
    def test_different_contents(self, mock_filecmp: mock.Mock, mock_os: mock.Mock) -> None:
        # Setup Mocks
        mock_os.walk.return_value = [(".", [], ["test.txt", "test.txt"])]
        mock_filecmp.cmp.return_value = False

        # Run Removal
        duplicate.delete(".", interactive=False)

        # Test Removal Calls
        mock_os.remove.assert_not_called()


if __name__ == "__main__":
    unittest.main()
