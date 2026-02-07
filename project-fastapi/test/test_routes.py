def test_read_main(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


def test_create_hero(client):
    response = client.post(
        "/heroes/",
        json={"name": "Bruce Wayne", "secret_name": "Batman", "age": 35},
    )
    data = response.json()
    assert response.status_code == 200
    assert data["name"] == "Bruce Wayne"
    assert data["secret_name"] == "Batman"
    assert data["age"] == 35
    assert "id" in data


def test_read_heroes(client):
    # Primero crear un hero
    create_response = client.post(
        "/heroes/",
        json={"name": "Bruce Wayne", "secret_name": "Batman", "age": 35},
    )
    hero_id = create_response.json()["id"]

    # Luego leerlo por ID
    response = client.get(f"/heroes/{hero_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Bruce Wayne"
