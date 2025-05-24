import requests

cookies = {
    "csrfSecret": "ceC5KoXRBwt3_po9ssxiZL8K",
    "XSRF-TOKEN": "wjY9AHMa-CeVsXwQYUpWHXIgWJBelNQGBbHk.rxqrg7nLCPqNhAToEnsxgPs%2BUpS8Epyu4YYNZjhWY1U",
    "_ga_SFEHM3SCGE": "GS2.1.s1748065876$o1$g1$t1748065912$j0$l0$h0",
    "COOKIE_COACHMARK_PAS": "done",
}

headers = {
    "accept": "*/*",
    "accept-language": "en-US,en;q=0.9",
}

base_url = "https://gofood.co.id/_next/data/16.2.0/id"


def get_restaurant_info(area: str, id_restaurant: str) -> str:
    """Get restaurant detail by restaurant id"""
    params = {
        "service_area": area,
        "id": id_restaurant,
    }

    response = requests.get(
        f"{base_url}/{area}/restaurant/{id_restaurant}.json",
        params=params,
        cookies=cookies,
        headers=headers,
    )
    return response


def search_restaurant(area: str, keyword: str) -> str:
    """Search restaurant by food name"""
    params = {
        "keyword": keyword,
    }

    response = requests.get(
        f"{base_url}/search.json?keyword={keyword}",
        params=params,
        cookies=cookies,
        headers=headers,
    )
    return response
