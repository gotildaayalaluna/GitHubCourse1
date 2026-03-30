import unittest
import importlib.util
from pathlib import Path


def _load_exercise_module():
    module_path = Path(__file__).with_name("exercise.py")
    spec = importlib.util.spec_from_file_location("step04_exercise", module_path)
    module = importlib.util.module_from_spec(spec)
    assert spec is not None and spec.loader is not None
    spec.loader.exec_module(module)
    return module


exercise = _load_exercise_module()


class TestSanitizeTags(unittest.TestCase):
    def test_empty_input(self):
        """Test that empty list returns empty list."""
        self.assertEqual(exercise.sanitize_tags([]), [])

    def test_basic_tags(self):
        """Test basic tag normalization."""
        self.assertEqual(exercise.sanitize_tags(["Python", "JavaScript"]), ["python", "javascript"])

    def test_duplicate_tags_mixed_case(self):
        """Test that duplicate tags with mixed case are deduplicated."""
        self.assertEqual(exercise.sanitize_tags(["Python", "python", "PYTHON"]), ["python"])

    def test_tags_with_punctuation(self):
        """Test that punctuation is removed except hyphens."""
        self.assertEqual(exercise.sanitize_tags(["hello!", "world@", "foo-bar"]), ["hello", "world", "foo-bar"])

    def test_whitespace_trimming(self):
        """Test that whitespace is trimmed from tags."""
        self.assertEqual(exercise.sanitize_tags(["  python  ", "\tjs\n"]), ["python", "js"])

    def test_empty_tags_after_cleanup(self):
        """Test that tags that become empty after cleanup are removed."""
        self.assertEqual(exercise.sanitize_tags(["!!!", "   ", "@#$"]), [])

    def test_preserves_first_seen_order(self):
        """Test that first-seen order is preserved for duplicates."""
        self.assertEqual(exercise.sanitize_tags(["b", "a", "B", "A", "c"]), ["b", "a", "c"])

    def test_mixed_valid_and_invalid(self):
        """Test mix of valid, invalid, and duplicate tags."""
        result = exercise.sanitize_tags(["Valid", "!!!", "valid", "  test  ", "TEST"])
        self.assertEqual(result, ["valid", "test"])

    def test_hyphenated_tags(self):
        """Test that hyphens are preserved in tags."""
        self.assertEqual(exercise.sanitize_tags(["my-tag", "another-one"]), ["my-tag", "another-one"])


if __name__ == "__main__":
    unittest.main()