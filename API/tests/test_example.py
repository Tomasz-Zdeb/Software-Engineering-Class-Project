def test_example_endpoint(client):
    response = client.get("/hello")
    assert {"hello": "world"} == response.json
