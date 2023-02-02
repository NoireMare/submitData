import pytest
import random
import requests
from config import API_URL


def test_create_pass_get_pass():
    pass_add = create_pass()
    new_pass, title, other_titles = pass_add[0], pass_add[1], pass_add[2]

    assert new_pass.status_code == 200

    pass_id = new_pass.json()["id"]
    get_pass_by_id = get_pass(pass_id)

    assert get_pass_by_id.status_code == 200
    assert get_pass_by_id.json() == {
                        "pass_": {
                            "id": pass_id,
                            "add_time": "2023-01-30T19:10:32.853000",
                            "beauty_title": "beauty_title",
                            "title": title,
                            "other_titles": other_titles,
                            "connect": "connect_test",
                            "status": "new"
                            },
                        "coordinate": {
                            "height": 1200,
                            "latitude": 120.45,
                            "longitude": 120.45
                            },
                        "level": {
                            "winter": "wi",
                            "summer": "su",
                            "autumn": "au",
                            "spring": "sp"
                            },
                        "image": {
                            "title_1": "t1_test",
                            "title_2": "t2_test",
                            "title_3": "t3_test",
                            "image_1": "img1_test",
                            "image_2": "img2_test",
                            "image_3": "img3_test"
                            },
                        "user": {
                            "fam": "fam_test",
                            "name": "name_test",
                            "otc": "otc_test",
                            "phone": "9999999",
                            "email": "user@example.com"
                            }
                        }


def test_change_pass_get_passes_by_user_email():
    pass_add = create_pass()
    new_pass, title, other_titles = pass_add[0], pass_add[1], pass_add[2]
    pass_id = new_pass.json()["id"]
    payload = {
        "pass_": {
            "add_time": "2023-01-30T19:10:32.853Z",
            "beauty_title": f"changing_test",
            "title": title,
            "other_titles": other_titles,
            "connect": "changing_connect_test",
            "status": "accepted"
        },
        "level": {
            "winter": "1A",
            "summer": "1A",
            "autumn": "1B",
            "spring": "1A"
        },
        "image": {
            "title_1": "t1_changing",
            "image_1": "img1_changing",
            "title_2": "t2_changing",
            "image_2": "img2_changing",
            "title_3": "t3_changing",
            "image_3": "img3_changing"
        },
        "coordinate": {
            "latitude": 240.45,
            "longitude": 2320.15,
            "height": 930
        }
    }
    changed_pass = requests.patch(API_URL + f'/passes/{pass_id}/edit', json=payload)

    assert changed_pass.status_code == 200

    get_changed_pass = get_pass(pass_id)
    assert get_changed_pass.json() == {
                    "pass_": {
                        "id": pass_id,
                        "add_time": "2023-01-30T19:10:32.853000",
                        "beauty_title": f"changing_test",
                        "title": title,
                        "other_titles": other_titles,
                        "connect": "changing_connect_test",
                        "status": "accepted"
                    },
                    "user": {
                        "fam": "fam_test",
                        "name": "name_test",
                        "otc": "otc_test",
                        "phone": "9999999",
                        "email": "user@example.com"
                    },
                    "level": {
                        "winter": "1A",
                        "summer": "1A",
                        "autumn": "1B",
                        "spring": "1A"
                    },
                    "image": {
                        "title_1": "t1_changing",
                        "image_1": "img1_changing",
                        "title_2": "t2_changing",
                        "image_2": "img2_changing",
                        "title_3": "t3_changing",
                        "image_3": "img3_changing"
                    },
                    "coordinate": {
                        "latitude": 240.45,
                        "longitude": 2320.15,
                        "height": 930
                    }
                }

    email = get_changed_pass.json()['user']['email']
    get_passes_by_email = requests.get(API_URL + f'/passes/user/{email}')

    assert get_passes_by_email.status_code == 200

    previous_pass = get_pass(pass_id-1).json()
    title_previous_pass = previous_pass["pass_"]["title"]
    other_titles_previous_pass = previous_pass["pass_"]["other_titles"]

    assert get_passes_by_email.json() == [
        {
            "pass_": {
                "id": pass_id-1,
                "add_time": "2023-01-30T19:10:32.853000",
                "beauty_title": "beauty_title",
                "title": title_previous_pass,
                "other_titles": other_titles_previous_pass,
                "connect": "connect_test",
                "status": "new"
            },
            "level": {
                "winter": "wi",
                "summer": "su",
                "autumn": "au",
                "spring": "sp"
            },
            "image": {
                "title_1": "t1_test",
                "title_2": "t2_test",
                "title_3": "t3_test",
                "image_1": "img1_test",
                "image_2": "img2_test",
                "image_3": "img3_test"
            },
            "coordinate": {
                "height": 1200,
                "latitude": 120.45,
                "longitude": 120.45
            }
        },
        {
            "pass_": {
                "id": pass_id,
                "add_time": "2023-01-30T19:10:32.853000",
                "beauty_title": f"changing_test",
                "title": title,
                "other_titles": other_titles,
                "connect": "changing_connect_test",
                "status": "accepted"
            },
            "level": {
                "winter": "1A",
                "summer": "1A",
                "autumn": "1B",
                "spring": "1A"
            },
            "image": {
                "title_1": "t1_changing",
                "image_1": "img1_changing",
                "title_2": "t2_changing",
                "image_2": "img2_changing",
                "title_3": "t3_changing",
                "image_3": "img3_changing"
            },
            "coordinate": {
                "latitude": 240.45,
                "longitude": 2320.15,
                "height": 930
            }
        }
    ]


def create_pass():
    payload = {
        "pass_": {
            "add_time": "2023-01-30T19:10:32.853Z",
            "beauty_title": f"beauty_title",
            "title": f"title_test_{random.randint(1, 10000)}",
            "other_titles": f"other_titles_test_{random.randint(1, 10000)}",
            "connect": "connect_test",
            "status": "new"
        },
        "user": {
            "fam": "fam_test",
            "name": "name_test",
            "otc": "otc_test",
            "phone": "9999999",
            "email": "user@example.com"
        },
        "level": {
            "winter": "wi",
            "summer": "su",
            "autumn": "au",
            "spring": "sp"
        },
        "image": {
            "title_1": "t1_test",
            "image_1": "img1_test",
            "title_2": "t2_test",
            "image_2": "img2_test",
            "title_3": "t3_test",
            "image_3": "img3_test"
        },
        "coordinate": {
            "latitude": 120.45,
            "longitude": 120.45,
            "height": 1200
        }
    }
    return (requests.post(API_URL + "/passes/create", json=payload),
            payload['pass_']['title'], payload['pass_']['other_titles'])


def get_pass(pass_id):
    return requests.get(API_URL + f"/passes/{pass_id}")






