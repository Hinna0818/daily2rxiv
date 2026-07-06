import contextlib
import io
import unittest

from daily2rxiv.cli import main


class CliTests(unittest.TestCase):
    def test_invalid_source_exits_cleanly(self):
        with contextlib.redirect_stderr(io.StringIO()):
            with self.assertRaises(SystemExit) as raised:
                main(["fetch", "--sources", "unknown", "--no-llm"])
        self.assertEqual(raised.exception.code, 2)

    def test_invalid_limit_exits_cleanly(self):
        with contextlib.redirect_stderr(io.StringIO()):
            with self.assertRaises(SystemExit) as raised:
                main(["fetch", "--limit", "0", "--no-llm"])
        self.assertEqual(raised.exception.code, 2)


if __name__ == "__main__":
    unittest.main()
