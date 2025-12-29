import requests

BASE_URL = "https://qa-internship.avito.com"
SELLER_ID = 111695


# POST создание объявления

def test_create_positive():
    # Arrange
    request_body = {
        "sellerID": SELLER_ID,
        "name": "комбинезон для собак",
        "price": 4500,
        "statistics": {
            "likes": 10,
            "viewCount": 45670,
            "contacts": 89999999999
        }
    }

    # Act
    response = requests.post(
        f"{BASE_URL}/api/1/item",
        json=request_body
    )

    body = response.json()
    print(body)

    # Assert
    try:
        assert response.status_code == 200
        assert "status" in body
        assert body["status"].startswith("Сохранили объявление - ")
        splits = body["status"].split(" - ")
        assert len(splits) == 2
        id = splits[1]
        assert len(id) > 0
    finally:
        # Clear
        requests.delete(f"{BASE_URL}/api/2/item/{id}")


def test_create_return_400_when_no_price():
    # Arrange
    request_body = {
        "sellerID": SELLER_ID,
        "name": "комбинезон для собак",
        "statistics": {
            "likes": 10,
            "viewCount": 45670,
            "contacts": 89999999999
        }
    }

    # Act
    response = requests.post(
        f"{BASE_URL}/api/1/item",
        json=request_body
    )

    body = response.json()

    # Assert
    assert response.status_code == 400
    assert "status" in body
    assert body["status"] == "400"
    assert "result" in body
    assert "message" in body["result"]
    assert "messages" in body["result"]
    assert body["result"]["message"] == "поле price обязательно"
    assert body["result"]["messages"] == {}


def test_create_return_400_when_price_0():
    # Arrange
    request_body = {
        "sellerID": SELLER_ID,
        "name": "комбинезон для собак",
        "price": 0,
        "statistics": {
            "likes": 10,
            "viewCount": 45670,
            "contacts": 89999999999
        }
    }

    # Act
    response = requests.post(
        f"{BASE_URL}/api/1/item",
        json=request_body
    )

    body = response.json()

    # Assert
    assert response.status_code == 400
    assert "status" in body
    assert body["status"] == "400"
    assert "result" in body
    assert "message" in body["result"]
    assert "messages" in body["result"]
    assert body["result"]["message"] == "поле price обязательно"
    assert body["result"]["messages"] == {}


def test_create_return_200_when_price_below_zero():
    # Arrange
    request_body = {
        "sellerID": SELLER_ID,
        "name": "комбинезон для собак",
        "price": -4500,
        "statistics": {
            "likes": 10,
            "viewCount": 45670,
            "contacts": 89999999999
        }
    }

    # Act
    response = requests.post(
        f"{BASE_URL}/api/1/item",
        json=request_body
    )

    body = response.json()

    # Assert
    try:
        assert response.status_code == 200
        assert "status" in body
        assert body["status"].startswith("Сохранили объявление - ")
        splits = body["status"].split(" - ")
        assert len(splits) == 2
        id = splits[1]
        assert len(id) > 0
    finally:
        # Clear
        requests.delete(f"{BASE_URL}/api/2/item/{id}")


def test_create_return_400_when_no_contact():
    # Arrange
    request_body = {
        "sellerID": SELLER_ID,
        "name": "комбинезон для собак",
        "price": -4500,
        "statistics": {
            "likes": 10,
            "viewCount": 45670,
        }
    }

    # Act
    response = requests.post(
        f"{BASE_URL}/api/1/item",
        json=request_body
    )

    body = response.json()

    # Assert
    assert response.status_code == 400
    assert "status" in body
    assert body["status"] == "400"
    assert "result" in body
    assert "message" in body["result"]
    assert "messages" in body["result"]
    assert body["result"]["message"] == "поле contacts обязательно"
    assert body["result"]["messages"] == {}

def test_create_return_400_when_no_likes():
    # Arrange
    request_body = {
        "sellerID": SELLER_ID,
        "name": "комбинезон для собак",
        "price": 4500,
        "statistics": {
            "viewCount": 45670,
            "contacts": 89999999999
        }
    }

    # Act
    response = requests.post(
        f"{BASE_URL}/api/1/item",
        json=request_body
    )

    body = response.json()

    # Assert
    assert response.status_code == 400
    assert "status" in body
    assert body["status"] == "400"
    assert "result" in body
    assert "message" in body["result"]
    assert "messages" in body["result"]
    assert body["result"]["message"] == "поле likes обязательно"
    assert body["result"]["messages"] == {}


def test_create_return_400_when_no_viewCount():
    # Arrange
    request_body = {
        "sellerID": SELLER_ID,
        "name": "комбинезон для собак",
        "price": 4500,
        "statistics": {
            "likes": 10,
            "contacts": 89999999999
        }
    }

    # Act
    response = requests.post(
        f"{BASE_URL}/api/1/item",
        json=request_body
    )

    body = response.json()

    # Assert
    assert response.status_code == 400
    assert "status" in body
    assert body["status"] == "400"
    assert "result" in body
    assert "message" in body["result"]
    assert "messages" in body["result"]
    assert body["result"]["message"] == "поле viewCount обязательно"
    assert body["result"]["messages"] == {}


def test_create_return_200_when_likes_below_zero():
    # Arrange
    request_body = {
        "sellerID": SELLER_ID,
        "name": "комбинезон для собак",
        "price": 4500,
        "statistics": {
            "likes": -10,
            "viewCount": 45670,
            "contacts": 89999999999
        }
    }

    # Act
    response = requests.post(
        f"{BASE_URL}/api/1/item",
        json=request_body
    )

    body = response.json()

    # Assert
    try:
        assert response.status_code == 200
        assert "status" in body
        assert body["status"].startswith("Сохранили объявление - ")
        splits = body["status"].split(" - ")
        assert len(splits) == 2
        id = splits[1]
        assert len(id) > 0
    finally:
        # Clear
        requests.delete(f"{BASE_URL}/api/2/item/{id}")


def test_create_return_200_when_viewCount_below_zero():
    # Arrange
    request_body = {
        "sellerID": SELLER_ID,
        "name": "комбинезон для собак",
        "price": 4500,
        "statistics": {
            "likes": 10,
            "viewCount": -45670,
            "contacts": 89999999999
        }
    }

    # Act
    response = requests.post(
        f"{BASE_URL}/api/1/item",
        json=request_body
    )

    body = response.json()

    # Assert
    try:
        assert response.status_code == 200
        assert "status" in body
        assert body["status"].startswith("Сохранили объявление - ")
        splits = body["status"].split(" - ")
        assert len(splits) == 2
        id = splits[1]
        assert len(id) > 0
    finally:
        # Clear
        requests.delete(f"{BASE_URL}/api/2/item/{id}")


def test_create_return_200_when_contact_8():
    # Arrange
    request_body = {
        "sellerID": SELLER_ID,
        "name": "комбинезон для собак",
        "price": 4500,
        "statistics": {
            "likes": 10,
            "viewCount": 45670,
            "contacts": 8
        }
    }

    # Act
    response = requests.post(
        f"{BASE_URL}/api/1/item",
        json=request_body
    )

    body = response.json()

    # Assert
    try:
        assert response.status_code == 200
        assert "status" in body
        assert body["status"].startswith("Сохранили объявление - ")
        splits = body["status"].split(" - ")
        assert len(splits) == 2
        id = splits[1]
        assert len(id) > 0
    finally:
        # Clear
        requests.delete(f"{BASE_URL}/api/2/item/{id}")

def test_create_return_200_when_contact_below_zero():
    # Arrange
    request_body = {
        "sellerID": SELLER_ID,
        "name": "комбинезон для собак",
        "price": 4500,
        "statistics": {
            "likes": 10,
            "viewCount": 45670,
            "contacts": -8
        }
    }

    # Act
    response = requests.post(
        f"{BASE_URL}/api/1/item",
        json=request_body
    )

    body = response.json()

    # Assert
    try:
        assert response.status_code == 200
        assert "status" in body
        assert body["status"].startswith("Сохранили объявление - ")
        splits = body["status"].split(" - ")
        assert len(splits) == 2
        id = splits[1]
        assert len(id) > 0
    finally:
        # Clear
        requests.delete(f"{BASE_URL}/api/2/item/{id}")


def test_create_return_400_when_name_with_numbers():
    # Arrange
    request_body = {
        "sellerID": SELLER_ID,
        "name": 4856,
        "price": 4500,
        "statistics": {
            "likes": 10,
            "viewCount": 45670,
            "contacts": 8
        }
    }

    # Act
    response = requests.post(
        f"{BASE_URL}/api/1/item",
        json=request_body
    )

    body = response.json()

    # Assert
    assert response.status_code == 400
    assert "status" in body
    assert body["status"] == "не передано тело объявления"
    assert "result" in body
    assert "message" in body["result"]
    assert "messages" in body["result"]
    assert body["result"]["message"] == ""
    assert body["result"]["messages"] == {}


def test_create_return_400_when_no_sellerID():
    # Arrange
    request_body = {
        "name": "комбинезон для собак",
        "price": 4500,
        "statistics": {
            "likes": 10,
            "viewCount": 45670,
            "contacts": 8
        }
    }

    # Act
    response = requests.post(
        f"{BASE_URL}/api/1/item",
        json=request_body
    )

    body = response.json()

    # Assert
    assert response.status_code == 400
    assert "status" in body
    assert body["status"] == "400"
    assert "result" in body
    assert "message" in body["result"]
    assert "messages" in body["result"]
    assert body["result"]["message"] == "поле sellerID обязательно"
    assert body["result"]["messages"] == {}


def test_create_return_400_when_sellerID_with_letters():
    # Arrange
    request_body = {
        "sellerID": "ggg",
        "name": "комбинезон для собак",
        "price": 4500,
        "statistics": {
            "likes": 10,
            "viewCount": 45670,
            "contacts": 8
        }
    }

    # Act
    response = requests.post(
        f"{BASE_URL}/api/1/item",
        json=request_body
    )

    body = response.json()

    # Assert
    assert response.status_code == 400
    assert "status" in body
    assert body["status"] == "не передано тело объявления"
    assert "result" in body
    assert "message" in body["result"]
    assert "messages" in body["result"]
    assert body["result"]["message"] == ""
    assert body["result"]["messages"] == {}


def test_create_return_200_when_sellerID_below_zero():
    # Arrange
    request_body = {
        "sellerID": -111693,
        "name": "комбинезон для собак",
        "price": 4500,
        "statistics": {
            "likes": 10,
            "viewCount": 45670,
            "contacts": 8
        }
    }

    # Act
    response = requests.post(
        f"{BASE_URL}/api/1/item",
        json=request_body
    )

    body = response.json()

    # Assert
    try:
        assert response.status_code == 200
        assert "status" in body
        assert body["status"].startswith("Сохранили объявление - ")
        splits = body["status"].split(" - ")
        assert len(splits) == 2
        id = splits[1]
        assert len(id) > 0
    finally:
        # Clear
        requests.delete(f"{BASE_URL}/api/2/item/{id}")

def test_create_return_400_when_sellerID_0():
    # Arrange
    request_body = {
        "sellerID": 0,
        "name": "комбинезон для собак",
        "price": 4500,
        "statistics": {
            "likes": 10,
            "viewCount": 45670,
            "contacts": 8
        }
    }

    # Act
    response = requests.post(
        f"{BASE_URL}/api/1/item",
        json=request_body
    )

    body = response.json()

    # Assert
    assert response.status_code == 400
    assert "status" in body
    assert body["status"] == "400"
    assert "result" in body
    assert "message" in body["result"]
    assert "messages" in body["result"]
    assert body["result"]["message"] == "поле sellerID обязательно"
    assert body["result"]["messages"] == {}


def test_create_return_400_when_likes_with_letters():
    # Arrange
    request_body = {
        "sellerID": SELLER_ID,
        "name": "комбинезон для собак",
        "price": 4500,
        "statistics": {
            "likes": "ooo",
            "viewCount": 45670,
            "contacts": 8
        }
    }

    # Act
    response = requests.post(
        f"{BASE_URL}/api/1/item",
        json=request_body
    )

    body = response.json()

    # Assert
    assert response.status_code == 400
    assert "status" in body
    assert body["status"] == "не передано тело объявления"
    assert "result" in body
    assert "message" in body["result"]
    assert "messages" in body["result"]
    assert body["result"]["message"] == ""
    assert body["result"]["messages"] == {}


def test_create_return_400_when_viewCount_with_letters():
    # Arrange
    request_body = {
        "sellerID": SELLER_ID,
        "name": "комбинезон для собак",
        "price": 4500,
        "statistics": {
            "likes": 10,
            "viewCount": "ppp",
            "contacts": 8
        }
    }

    # Act
    response = requests.post(
        f"{BASE_URL}/api/1/item",
        json=request_body
    )

    body = response.json()

    # Assert
    assert response.status_code == 400
    assert "status" in body
    assert body["status"] == "не передано тело объявления"
    assert "result" in body
    assert "message" in body["result"]
    assert "messages" in body["result"]
    assert body["result"]["message"] == ""
    assert body["result"]["messages"] == {}


def test_create_return_400_when_price_with_letters():
    # Arrange
    request_body = {
        "sellerID": SELLER_ID,
        "name": "комбинезон для собак",
        "price": "jjj",
        "statistics": {
            "likes": 10,
            "viewCount": 45670,
            "contacts": 8
        }
    }

    # Act
    response = requests.post(
        f"{BASE_URL}/api/1/item",
        json=request_body
    )

    body = response.json()

    # Assert
    assert response.status_code == 400
    assert "status" in body
    assert body["status"] == "не передано тело объявления"
    assert "result" in body
    assert "message" in body["result"]
    assert "messages" in body["result"]
    assert body["result"]["message"] == ""
    assert body["result"]["messages"] == {}


def test_create_return_400_when_contacts_with_letters():
    # Arrange
    request_body = {
            "sellerID": SELLER_ID,
            "name": "комбинезон для собак",
            "price": 4500,
            "statistics": {
                "likes": 10,
                "viewCount": 45670,
                "contacts": "lll"
            }
        }

    # Act
    response = requests.post(
        f"{BASE_URL}/api/1/item",
        json=request_body
    )

    body = response.json()

    # Assert
    assert response.status_code == 400
    assert "status" in body
    assert body["status"] == "не передано тело объявления"
    assert "result" in body
    assert "message" in body["result"]
    assert "messages" in body["result"]
    assert body["result"]["message"] == ""
    assert body["result"]["messages"] == {}


# GET получение всех объявлений пользователя

def test_get_return_200_when_id_with_items():
    # Arrange
    request_body = {
        "sellerID": SELLER_ID,
        "name": "комбинезон для собак",
        "price": 4500,
        "statistics": {
            "likes": 10,
            "viewCount": 45670,
            "contacts": 89999999999
        }
    }

    created_body = requests.post(
        f"{BASE_URL}/api/1/item",
        json=request_body
    ).json()
    created_id = created_body["status"].split(" - ")[1]

    # Act
    response = requests.get(f"{BASE_URL}/api/1/{SELLER_ID}/item")

    body = response.json()

    # Assert
    try:
        assert response.status_code == 200
        assert isinstance(body, list)
        assert len(body) == 1
        item = body[0]

        assert "createdAt" in item
        assert isinstance(item["createdAt"], str)
        assert len(item["createdAt"]) > 0

        assert "id" in item
        assert isinstance(item["id"], str)
        assert item["id"] == created_id

        assert "name" in item
        assert isinstance(item["name"], str)
        assert item["name"] == request_body["name"]

        assert "price" in item
        assert isinstance(item["price"], int)
        assert item["price"] == request_body["price"]

        assert "sellerId" in item
        assert isinstance(item["sellerId"], int)
        assert item["sellerId"] == request_body["sellerID"]

        assert "statistics" in item

        assert "likes" in item["statistics"]
        assert isinstance(item["statistics"]["likes"], int)
        assert item["statistics"]["likes"] == request_body["statistics"]["likes"]

        assert "viewCount" in item["statistics"]
        assert isinstance(item["statistics"]["viewCount"], int)
        assert item["statistics"]["viewCount"] == request_body["statistics"]["viewCount"]

        assert "contacts" in item["statistics"]
        assert isinstance(item["statistics"]["contacts"], int)
        assert item["statistics"]["contacts"] == request_body["statistics"]["contacts"]
    finally:
        # Clear
        requests.delete(f"{BASE_URL}/api/2/item/{created_id}")


def test_get_return_200_when_id_without_items():
    # Act
    response = requests.get(f"{BASE_URL}/api/1/{SELLER_ID}/item")
    body = response.json()

    # Assert
    assert response.status_code == 200
    assert isinstance(body, list)
    assert len(body) == 0


def test_get_return_405_when_no_id():
    response = requests.get(f"{BASE_URL}/api/1//item")

    assert response.status_code == 405


def test_get_return_400_when_id_with_letters():
    # Act
    response = requests.get(f"{BASE_URL}/api/1/ppp/item")
    body = response.json()

    # Assert
    assert response.status_code == 400
    assert "status" in body
    assert body["status"] == "400"
    assert "result" in body
    assert "message" in body["result"]
    assert "messages" in body["result"]
    assert body["result"]["message"] == "передан некорректный идентификатор продавца"
    assert body["result"]["messages"] == {}


# GET получение статистики по идентификатору

def test_get_return_200_when_id_exist():
    # Arrange
    request_body = {
        "sellerID": SELLER_ID,
        "name": "комбинезон для собак",
        "price": 4500,
        "statistics": {
            "likes": 10,
            "viewCount": 45670,
            "contacts": 89999999999
        }
    }

    created_body = requests.post(
        f"{BASE_URL}/api/1/item",
        json=request_body
    ).json()
    created_id = created_body["status"].split(" - ")[1]

    # Act
    response = requests.get(f"{BASE_URL}/api/1/statistic/{created_id}")
    body = response.json()

    # Assert
    try:
        assert response.status_code == 200
        assert isinstance(body, list)
        assert len(body) == 1
        item = body[0]

        assert "likes" in item
        assert isinstance(item["likes"], int)
        assert item["likes"] == request_body["statistics"]["likes"]

        assert "viewCount" in item
        assert isinstance(item["viewCount"], int)
        assert item["viewCount"] == request_body["statistics"]["viewCount"]
        assert "contacts" in item
        assert isinstance(item["contacts"], int)
        assert item["contacts"] == request_body["statistics"]["contacts"]
    finally:
        # Clear
        requests.delete(f"{BASE_URL}/api/2/item/{created_id}")


def test_get_return_404_when_no_id():
    # Act
    response = requests.get(f"{BASE_URL}/api/1/statistic/")

    # Assert
    assert response.status_code == 404


def test_get_return_400_when_id_0():
    # Act
    response = requests.get(f"{BASE_URL}/api/1/statistic/0")
    body = response.json()

    # Assert
    assert response.status_code == 400
    assert "status" in body
    assert body["status"] == "400"
    assert "result" in body
    assert "message" in body["result"]
    assert "messages" in body["result"]
    assert body["result"]["message"] == "передан некорректный идентификатор объявления"
    assert body["result"]["messages"] == {}


def test_get_return_400_when_id_below_zero():
    # Act
    response = requests.get(f"{BASE_URL}/api/1/statistic/-1")
    body = response.json()

    # Assert
    assert response.status_code == 400
    assert "status" in body
    assert body["status"] == "400"
    assert "result" in body
    assert "message" in body["result"]
    assert "messages" in body["result"]
    assert body["result"]["message"] == "передан некорректный идентификатор объявления"
    assert body["result"]["messages"] == {}


def test_get_return_400_when_id_numbers():
    # Act
    response = requests.get(f"{BASE_URL}/api/1/statistic/224263849557")
    body = response.json()

    # Assert
    assert response.status_code == 400
    assert "status" in body
    assert body["status"] == "400"
    assert "result" in body
    assert "message" in body["result"]
    assert "messages" in body["result"]
    assert body["result"]["message"] == "передан некорректный идентификатор объявления"
    assert body["result"]["messages"] == {}


def test_get_return_400_when_id_letters():
    # Act
    response = requests.get(f"{BASE_URL}/api/1/statistic/hhhhhhhh")
    body = response.json()

    # Assert
    assert response.status_code == 400
    assert "status" in body
    assert body["status"] == "400"
    assert "result" in body
    assert "message" in body["result"]
    assert "messages" in body["result"]
    assert body["result"]["message"] == "передан некорректный идентификатор объявления"
    assert body["result"]["messages"] == {}


# Get

def test_get_item_return_200_when_id_exist():
    # Arrange
    request_body = {
        "sellerID": SELLER_ID,
        "name": "комбинезон для собак",
        "price": 4500,
        "statistics": {
            "likes": 10,
            "viewCount": 45670,
            "contacts": 89999999999
        }
    }

    created_body = requests.post(
        f"{BASE_URL}/api/1/item",
        json=request_body
    ).json()
    created_id = created_body["status"].split(" - ")[1]

    # Act
    response = requests.get(f"{BASE_URL}/api/1/item/{created_id}")
    body = response.json()

    # Assert
    try:
        assert response.status_code == 200
        assert isinstance(body, list)
        assert len(body) == 1
        item = body[0]

        assert "createdAt" in item
        assert isinstance(item["createdAt"], str)
        assert len(item["createdAt"]) > 0

        assert "id" in item
        assert isinstance(item["id"], str)
        assert item["id"] == created_id

        assert "name" in item
        assert isinstance(item["name"], str)
        assert item["name"] == request_body["name"]

        assert "price" in item
        assert isinstance(item["price"], int)
        assert item["price"] == request_body["price"]

        assert "sellerId" in item
        assert isinstance(item["sellerId"], int)
        assert item["sellerId"] == request_body["sellerID"]

        assert "statistics" in item

        assert "likes" in item["statistics"]
        assert isinstance(item["statistics"]["likes"], int)
        assert item["statistics"]["likes"] == request_body["statistics"]["likes"]
        assert "viewCount" in item["statistics"]
        assert isinstance(item["statistics"]["viewCount"], int)
        assert item["statistics"]["viewCount"] == request_body["statistics"]["viewCount"]

        assert "contacts" in item["statistics"]
        assert isinstance(item["statistics"]["contacts"], int)
        assert item["statistics"]["contacts"] == request_body["statistics"]["contacts"]
    finally:
        # Clear
        requests.delete(f"{BASE_URL}/api/2/item/{created_id}")


def test_get_item_return_400_when_id_0():
    # Act
    response = requests.get(f"{BASE_URL}/api/1/item/0")
    body = response.json()

    # Assert
    assert response.status_code == 400
    assert "status" in body
    assert body["status"] == "400"
    assert "result" in body
    assert "message" in body["result"]
    assert "messages" in body["result"]
    assert body["result"]["message"] == "ID айтема не UUID: 0"
    assert body["result"]["messages"] == {}


def test_get_item_return_400_when_id_below_zero():
    # Act
    response = requests.get(f"{BASE_URL}/api/1/item/-4647484")
    body = response.json()

    # Assert
    assert response.status_code == 400
    assert "status" in body
    assert body["status"] == "400"
    assert "result" in body
    assert "message" in body["result"]
    assert "messages" in body["result"]
    assert body["result"]["message"] == "ID айтема не UUID: -4647484"
    assert body["result"]["messages"] == {}


def test_get_item_return_400_when_id_letters():
    # Act
    response = requests.get(f"{BASE_URL}/api/1/item/tyuhhj")
    body = response.json()

    # Assert
    assert response.status_code == 400
    assert "status" in body
    assert body["status"] == "400"
    assert "result" in body
    assert "message" in body["result"]
    assert "messages" in body["result"]
    assert body["result"]["message"] == "ID айтема не UUID: tyuhhj"
    assert body["result"]["messages"] == {}