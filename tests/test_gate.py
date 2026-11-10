import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "tools"))
import gate


class CheckTest(unittest.TestCase):
    def test_plain_text_passes(self):
        self.assertEqual(gate.check("docs/a.md", "plain text, café\n".encode()), [])
        self.assertEqual(gate.check("empty.txt", b""), [])

    def test_binary_is_refused(self):
        self.assertEqual(gate.check("a.png", b"\x89PNG\r\n\x1a\n\0\0"), ["binary file"])
        self.assertEqual(gate.check("a.txt", b"\xff\xfe"), ["binary file (not UTF-8 text)"])

    def test_long_line_is_refused_at_the_limit(self):
        self.assertEqual(gate.check("a.js", b"x" * gate.MAX_LINE), [])
        self.assertEqual(len(gate.check("a.js", b"ok\n" + b"x" * (gate.MAX_LINE + 1))), 1)

    def test_em_dash_is_refused_with_its_line(self):
        self.assertEqual(
            gate.check("a.md", f"one\ntwo {gate.EM_DASH} three\n".encode()),
            ["line 2 contains an em-dash"],
        )

    def test_secret_and_settings_names_are_refused(self):
        for path in (".env", "app/.env.production", "release.keystore", "k.pem",
                     "x/id.key", ".claude/settings.json", "a/.claude/b/c.md",
                     "CLAUDE.local.md", "settings.local.json"):
            self.assertTrue(gate.check(path, b"x\n"), path)
        for path in ("docs/environment.md", "keys.md", "claude.md", "src/.envoy"):
            self.assertEqual(gate.check(path, b"x\n"), [], path)

    def test_binary_with_secret_name_reports_both(self):
        self.assertEqual(len(gate.check("a.jks", b"\0")), 2)


if __name__ == "__main__":
    unittest.main()
