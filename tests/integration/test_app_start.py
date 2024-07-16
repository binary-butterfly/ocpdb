

def test_start_app(app):
    with app.test_client() as client:
        response = client.get('/api/public/v1/businesses/1')
        assert response
