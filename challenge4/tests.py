import unittest
from unittest.mock import patch, Mock, call
import duplicate


class TestDuplicate(unittest.TestCase):

    @patch("duplicate.os")
    @patch("duplicate.filecmp")
    def test_one_dir_duplicate(self, mock_filecmp: Mock, mock_os: Mock) -> None:
        # Setup Mocks
        mock_os.walk.return_value = [(".", [], ["test.txt", "test.txt"])]
        mock_filecmp.cmp.return_value = True

        # Run Removal
        duplicate.delete(".", interactive=False)

        # Test Mock Calls
        mock_os.walk.assert_called_once_with(".")
        mock_filecmp.cmp.assert_called_once_with(
            "./test.txt1", "./test.txt", shallow=False)
        mock_os.remove.assert_called_once_with("./test.txt")

    @patch("duplicate.os")
    @patch("duplicate.filecmp")
    def test_one_dir_no_matching_names(self, mock_filecmp: Mock, mock_os: Mock) -> None:
        # Setup Mocks
        mock_os.walk.return_value = [(".", [], ["test.txt", "test.csv"])]
        mock_filecmp.cmp.return_value = True  # Shouldn't Matter

        # Run Removal
        duplicate.delete(".", interactive=False)

        # Test Mock Calls
        mock_os.walk.assert_called_once_with(".")
        mock_filecmp.cmp.assert_not_called()
        mock_os.remove.assert_not_called()

    @patch("duplicate.os")
    @patch("duplicate.filecmp")
    def test_one_dir_different_contents(self, mock_filecmp: Mock, mock_os: Mock) -> None:
        # Setup Mocks
        mock_os.walk.return_value = [(".", [], ["test.txt", "test.txt"])]
        mock_filecmp.cmp.return_value = False

        # Run Removal
        duplicate.delete(".", interactive=False)

        # Test Mock Calls
        mock_os.walk.assert_called_once_with(".")
        mock_filecmp.cmp.assert_called_once_with(
            "./test.txt", "./test.txt", shallow=False)
        mock_os.remove.assert_not_called()

    @patch("duplicate.os")
    @patch("duplicate.filecmp")
    def test_nested_dir_duplicates(self, mock_filecmp: Mock, mock_os: Mock) -> None:
        # Setup Mocks
        mock_os.walk.return_value = [
            (".", ["dir1", "dir2"], ["test.txt"]),
            ("./dir1", [], ["test.txt"]),
            ("./dir2", ["dir3"], ["test.txt"]),
            ("./dir2/dir3", [], ["test.txt"])]
        mock_filecmp.cmp.return_value = True

        # Run Removal
        duplicate.delete(".", interactive=False)

        # Test Mock Calls
        mock_os.walk.assert_called_once_with(".")
        mock_filecmp.cmp.assert_has_calls([
            call("./test.txt", "./dir1/test.txt", shallow=False),
            call("./test.txt", "./dir2/test.txt", shallow=False),
            call("./test.txt", "./dir2/dir3/test.txt", shallow=False)
        ])
        mock_os.remove.assert_has_calls([
            call("./dir1/test.txt"),
            call("./dir2/test.txt"),
            call("./dir2/dir3/test.txt")
        ])

    @patch("duplicate.os")
    @patch("duplicate.filecmp")
    def test_nested_dir_no_duplicates(self, mock_filecmp: Mock, mock_os: Mock) -> None:
        # Setup Mocks
        mock_os.walk.return_value = [
            (".", ["dir1", "dir2"], ["test.txt"]),
            ("./dir1", [], ["test.csv"]),
            ("./dir2", ["dir3"], ["test.txt"]),
            ("./dir2/dir3", [], ["hello_world.txt"])]
        mock_filecmp.cmp.return_value = False

        # Run Removal
        duplicate.delete(".", interactive=False)

        # Test Mock Calls
        mock_os.walk.assert_called_once_with(".")
        mock_filecmp.cmp.assert_called_once_with(
            "./test.txt", "./dir2/test.txt", shallow=False)
        mock_os.remove.assert_not_called()

    @patch("duplicate.os")
    @patch("duplicate.filecmp")
    def test_dummy_desktop(self, mock_filecmp: Mock, mock_os: Mock) -> None:
        # Setup Mocks
        mock_os.walk.return_value = [
            ("dummy_desktop", ["f3", "f2", "f1"], ["info.txt", "test.txt"]),
            ("dummy_desktop/f3", [], ["xyz.txt", "abc.txt"]),
            ("dummy_desktop/f2", ["f4"], ["xyz.txt"]),
            ("dummy_desktop/f2/f4", ["f5"], ["mno.txt"]),
            ("dummy_desktop/f2/f4/f5", [], ["info.txt", "test.txt"]),
            ("dummy_desktop/f1", [], ["mno.txt", "do_not_delete.txt", "abc.txt"])]
        mock_filecmp.cmp.side_effect = fake_filecmp_cmp_for_dummy_desktop

        # Run Removal
        duplicate.delete("dummy_desktop", interactive=False)

        # Test Mock Calls
        mock_os.walk.assert_called_once_with("dummy_desktop")
        mock_filecmp.cmp.assert_has_calls([
            call("dummy_desktop/f3/xyz.txt",
                 "dummy_desktop/f2/xyz.txt", shallow=False),
            call("dummy_desktop/info.txt",
                 "dummy_desktop/f2/f4/f5/info.txt", shallow=False),
            call("dummy_desktop/test.txt",
                 "dummy_desktop/f2/f4/f5/test.txt", shallow=False),
            call("dummy_desktop/f2/f4/mno.txt",
                 "dummy_desktop/f1/mno.txt", shallow=False),
            call("dummy_desktop/f3/abc.txt",
                 "dummy_desktop/f1/abc.txt", shallow=False)
        ])
        mock_os.remove.assert_has_calls([
            call("dummy_desktop/f2/xyz.txt"),
            call("dummy_desktop/f2/f4/f5/test.txt"),
            call("dummy_desktop/f1/mno.txt"),
            call("dummy_desktop/f1/abc.txt"),
        ])


def fake_filecmp_cmp_for_dummy_desktop(file1: str, file2: str, shallow=True):
    # Every file evaluates to equal except info.txt
    return not ("info.txt" in file1 and "info.txt" in file2)


if __name__ == "__main__":
    unittest.main()
