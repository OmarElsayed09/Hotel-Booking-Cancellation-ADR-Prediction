"""FastAPI HTTP smoke tests that do not require trained model files."""
import unittest
from fastapi.testclient import TestClient
from api import app, app_state


class ApiSmokeTests(unittest.TestCase):
    def test_health_status_reflects_model_readiness(self):
        with TestClient(app) as client:
            resp = client.get("/api/health")
            self.assertEqual(resp.status_code, 200)
            data = resp.json()
            self.assertIn("classifier_ready", data)
            self.assertIn("regressor_ready", data)
            expected = "healthy" if data["classifier_ready"] and data["regressor_ready"] else "degraded"
            self.assertEqual(data["status"], expected)

    def test_metadata_endpoint(self):
        with TestClient(app) as client:
            resp = client.get("/api/metadata")
            self.assertEqual(resp.status_code, 200)
            self.assertIn("options", resp.json())

    def test_openapi_schema_contains_prediction_endpoint(self):
        with TestClient(app) as client:
            resp = client.get("/openapi.json")
            self.assertEqual(resp.status_code, 200)
            self.assertIn("/api/predict", resp.json()["paths"])


if __name__ == "__main__":
    unittest.main()
