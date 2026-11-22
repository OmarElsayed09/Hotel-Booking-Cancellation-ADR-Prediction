"""Keep the uninitialized dashboard from presenting fictional model outputs."""
import unittest
from pathlib import Path

HTML = (Path(__file__).resolve().parents[1] / "static/index.html").read_text(encoding="utf-8")


class FrontendClaimsTests(unittest.TestCase):
    def test_no_fake_initial_predictions(self):
        self.assertNotIn("25.5%", HTML)
        self.assertNotIn("$133.61", HTML)
        self.assertNotIn("$400.84", HTML)
        self.assertIn("AWAITING PREDICTION", HTML)
        self.assertIn("Run a model prediction to display recommendations.", HTML)


if __name__ == "__main__":
    unittest.main()
