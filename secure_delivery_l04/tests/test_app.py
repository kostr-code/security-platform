import unittest
from service.app import response_for


class RoutingTests(unittest.TestCase):
    def test_health_returns_success(self):
        status, payload = response_for("/healthz")
        self.assertEqual(status, 200)
        self.assertEqual(payload["status"], "ok")

    def test_unknown_route_returns_404(self):
        status, payload = response_for("/not-found")
        self.assertEqual(status, 404)
        self.assertEqual(payload["error"], "not_found")

    def test_health_with_query_string(self):
        status, _ = response_for("/healthz?source=ci")
        self.assertEqual(status, 200)


if __name__ == "__main__":
    unittest.main()
