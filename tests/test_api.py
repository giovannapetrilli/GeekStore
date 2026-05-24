def test_listar_produtos(client):

    response = client.get("/api/produtos")

    assert response.status_code == 200

    dados = response.json()

    assert len(dados) > 0


def test_compra_sucesso(client):

    response = client.post(
        "/api/comprar",
        json={
            "produto": "teclado",
            "cartao": "1234",
            "cupom": "GEEK20"
        }
    )

    assert response.status_code == 200

    dados = response.json()

    assert dados["status"] == "sucesso"


def test_produto_nao_existe(client):

    response = client.post(
        "/api/comprar",
        json={
            "produto": "monitor",
            "cartao": "1234",
            "cupom": ""
        }
    )

    assert response.status_code == 404