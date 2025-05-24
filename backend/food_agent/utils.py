import requests

cookies = {
    "COOKIE_COACHMARK_PAS": "done",
    "nc": "1",
    "sID": "eyJhbGciOiJSUzI1NiIsImtpZCI6IiJ9.eyJhdWQiOlsiZ29qZWsiXSwiYnJvd3Nlcl9mYW1pbHkiOiJjaHJvbWUiLCJkYXQiOnsiYWN0aXZlIjoidHJ1ZSIsImJsYWNrbGlzdGVkIjoiZmFsc2UiLCJjb3VudHJ5X2NvZGUiOiIrNjIiLCJjcmVhdGVkX2F0IjoiMjAxNy0wNy0yN1QwOTo1MjoyOFoiLCJlbWFpbCI6Im11aGFtbWFkYWJkdWxheml6YWxnaG9mYXJpQGdtYWlsLmNvbSIsImVtYWlsX3ZlcmlmaWVkIjoidHJ1ZSIsImdvcGF5X2FjY291bnRfaWQiOiIwMS1mZDZhZGViNzQwOGM0NDFiODg4YTAyMDM4Y2M3YTRmYi0yNCIsIm5hbWUiOiJNdWF6IiwibnVtYmVyIjoiODUxNTYzNzU3ODMiLCJwaG9uZSI6Iis2Mjg1MTU2Mzc1NzgzIiwic2lnbmVkX3VwX2NvdW50cnkiOiJJRCIsIndhbGxldF9pZCI6IjE3MjA4MDU5MjM0MzEwMjQzMiJ9LCJleHAiOjE3NDgxNTk5NzgsImlhdCI6MTc0ODA2MzYyNywiaXNzIjoiZ29pZCIsImp0aSI6IjMyNjIzMDcxLTkzZjktNDk5YS04OWVmLWQ4NmI3M2QxMGU3MiIsInBsYXRmb3JtIjoiZ29mb29kLXdlYiIsInNjb3BlcyI6W10sInNpZCI6IjcyMTY0ZTRiLTAzMjQtNDk0YS1iY2M1LTM3MWYxYzlhZjhmZCIsInN1YiI6IjJkY2RkNmVkLTViY2QtNGJhZS1hOGUzLTIyYmU4ODU0MWUwOCIsInRva2VuX3ZlcnNpb24iOiIxLjEiLCJ1aWQiOiI1NzAwMTc0NTUiLCJ1dHlwZSI6ImN1c3RvbWVyIn0.O4KvKmxOLyC3tdkwIxIELRMzZ-rR6AjUu52dtOLzl9ryQkcOybWYriGH13jtkYG7bubC2BlJeywv0dXJTCj4a2LfZDKWlWLE3rzyBzPwtEBiCuhJQxtfBNqO1h6luSPSvIEV4eP0RX8w85rQwVv_1muFhx0GDqvFJSMj02HGM9s",
    "gf_chosen_loc": "%7B%22locality%22%3A%22jakarta-timur%22%2C%22name%22%3A%22Jakarta%20Timur%2C%20Jakarta%22%2C%22serviceArea%22%3A%22jakarta%22%2C%22serviceAreaId%22%3A%221%22%2C%22latitude%22%3A-6.2250138%2C%22longitude%22%3A106.9004472%2C%22category%22%3A%22%22%2C%22timezone%22%3A%22Asia%2FJakarta%22%2C%22found%22%3Atrue%7D",
    "csrfSecret": "wt2wd2iYZJQUW20Eemu6mUkP",
    "XSRF-TOKEN": "khhQ8Lgz-csg6ZfXSSmWaqE7DWzzX7Qro49g.ant49Ey1rduLlfQKBCJToEq3K74i7VS6V5zzF%2B9%2BFok",
}

headers = {
    "accept": "*/*",
    "accept-language": "en-US,en;q=0.7",
    "newrelic": "eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjIwNjcyMzgiLCJhcCI6IjE4MzQ4NzYwOTEiLCJpZCI6IjU3NDIyYjFiN2JjYzJkMjkiLCJ0ciI6IjMxMGMxMTMzNTNhYzExYTNhYTEzNTdlMTI5Mjg2NWQwIiwidGkiOjE3NDgwOTA3ODE4NTgsInRrIjoiMjE5MDI2MiJ9fQ==",
    "priority": "u=1, i",
    "sec-ch-ua": '"Brave";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"macOS"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "sec-gpc": "1",
    "traceparent": "00-310c113353ac11a3aa1357e1292865d0-57422b1b7bcc2d29-01",
    "tracestate": "2190262@nr=0-1-2067238-1834876091-57422b1b7bcc2d29----1748090781858",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
    "x-nextjs-data": "1",
    # 'cookie': 'COOKIE_COACHMARK_PAS=done; nc=1; sID=eyJhbGciOiJSUzI1NiIsImtpZCI6IiJ9.eyJhdWQiOlsiZ29qZWsiXSwiYnJvd3Nlcl9mYW1pbHkiOiJjaHJvbWUiLCJkYXQiOnsiYWN0aXZlIjoidHJ1ZSIsImJsYWNrbGlzdGVkIjoiZmFsc2UiLCJjb3VudHJ5X2NvZGUiOiIrNjIiLCJjcmVhdGVkX2F0IjoiMjAxNy0wNy0yN1QwOTo1MjoyOFoiLCJlbWFpbCI6Im11aGFtbWFkYWJkdWxheml6YWxnaG9mYXJpQGdtYWlsLmNvbSIsImVtYWlsX3ZlcmlmaWVkIjoidHJ1ZSIsImdvcGF5X2FjY291bnRfaWQiOiIwMS1mZDZhZGViNzQwOGM0NDFiODg4YTAyMDM4Y2M3YTRmYi0yNCIsIm5hbWUiOiJNdWF6IiwibnVtYmVyIjoiODUxNTYzNzU3ODMiLCJwaG9uZSI6Iis2Mjg1MTU2Mzc1NzgzIiwic2lnbmVkX3VwX2NvdW50cnkiOiJJRCIsIndhbGxldF9pZCI6IjE3MjA4MDU5MjM0MzEwMjQzMiJ9LCJleHAiOjE3NDgxNTk5NzgsImlhdCI6MTc0ODA2MzYyNywiaXNzIjoiZ29pZCIsImp0aSI6IjMyNjIzMDcxLTkzZjktNDk5YS04OWVmLWQ4NmI3M2QxMGU3MiIsInBsYXRmb3JtIjoiZ29mb29kLXdlYiIsInNjb3BlcyI6W10sInNpZCI6IjcyMTY0ZTRiLTAzMjQtNDk0YS1iY2M1LTM3MWYxYzlhZjhmZCIsInN1YiI6IjJkY2RkNmVkLTViY2QtNGJhZS1hOGUzLTIyYmU4ODU0MWUwOCIsInRva2VuX3ZlcnNpb24iOiIxLjEiLCJ1aWQiOiI1NzAwMTc0NTUiLCJ1dHlwZSI6ImN1c3RvbWVyIn0.O4KvKmxOLyC3tdkwIxIELRMzZ-rR6AjUu52dtOLzl9ryQkcOybWYriGH13jtkYG7bubC2BlJeywv0dXJTCj4a2LfZDKWlWLE3rzyBzPwtEBiCuhJQxtfBNqO1h6luSPSvIEV4eP0RX8w85rQwVv_1muFhx0GDqvFJSMj02HGM9s; gf_chosen_loc=%7B%22locality%22%3A%22jakarta-timur%22%2C%22name%22%3A%22Jakarta%20Timur%2C%20Jakarta%22%2C%22serviceArea%22%3A%22jakarta%22%2C%22serviceAreaId%22%3A%221%22%2C%22latitude%22%3A-6.2250138%2C%22longitude%22%3A106.9004472%2C%22category%22%3A%22%22%2C%22timezone%22%3A%22Asia%2FJakarta%22%2C%22found%22%3Atrue%7D; csrfSecret=wt2wd2iYZJQUW20Eemu6mUkP; XSRF-TOKEN=khhQ8Lgz-csg6ZfXSSmWaqE7DWzzX7Qro49g.ant49Ey1rduLlfQKBCJToEq3K74i7VS6V5zzF%2B9%2BFok',
}

base_url = "https://gofood.co.id/_next/data/16.2.0/en"

base_url_gofood = "https://gofood.co.id/gofood/web/v2"


def search_restaurant_near_me(kota: str, kecamatan: str) -> dict:
    """
    Get restaurants near me

    Args:
        kota(str): area name on map e.g "jakarta" all on lowercase
        kecamatan(str): area name on map e.g "jakarta-pusat" all on lowercase and space is replaced with "-"

    Returns:
        dict: json response from gofood api
    """

    params = {
        "service_area": kota,
        "locality": f"{kecamatan}-restaurants",
        "category": "near_me",
    }

    response = requests.get(
        f"{base_url}/{kota}/{kecamatan}-restaurants/near_me.json",
        params=params,
        cookies=cookies,
        headers=headers,
    )
    print(response)
    return response.json()


def get_restaurant_details(kota: str, restaurant_name: str, id_restaurant: str) -> dict:
    """
    Get detail of restauran by id_restaurant

    Args:
        kota(str): area name on map e.g "jakarta" all on lowercase
        restaurant_name(str): restaurant name on map e.g "ayam-kremes-kraton-pahlawan-revolusi" all on lowercase and space is replaced with "-"
        id_restaurant(str): restaurant uid on anthor api to retrieve restaurant list, usually in uid tag e.g "2f5f6bd9-598f-46a9-9408-c84e812e90a6"

    Returns:
        dict: restaurant detail data in json format
    """

    url = f"{base_url}/{kota}/restaurant/{restaurant_name}-{id_restaurant}.json?service_area={kota}&id={restaurant_name}-{id_restaurant}"

    response = requests.get(
        url,
        cookies=cookies,
        headers=headers,
    )

    return response.json()


def get_merchant_promo(id_restaurant: str) -> dict:
    """
    Get merchant promo by id_restaurant, this endpoint also returned if merchant is on Gojek Plus promo or not.

    Args:
        id_restaurant(str): restaurant uid on anthor api to retrieve restaurant list, usually in uid tag e.g "2f5f6bd9-598f-46a9-9408-c84e812e90a6"

    Returns:
        dict: merchant promo data in json format, this return if the restaurant on Gojek Plus promo or not.
    """
    url = f"{base_url_gofood}/deals/profile?cart_amount=0&merchant_id={id_restaurant}&service_type=5&offeringToken=&distance=130&gf_plus_two_exp_enabled=true&tenant=gofood&picked_loc=-6.2250138,106.9004472&fulfillment_modes=regular&allowed_payment_types=0,4,15,16"

    response = requests.get(
        url,
        cookies=cookies,
        headers=headers,
    )

    return response.json()


def search_restaurant_by_food_name(food_name: str) -> dict:
    """
    Search restaurant by food name

    Args:
        food_name(str): food name to search e.g "ayam goreng"

    Returns:
        dict: restaurant data in json format with some details such as priceLevel, rating and distance
    """
    url = f"{base_url}/search.json?q={food_name}"

    response = requests.get(
        url,
        cookies=cookies,
        headers=headers,
    )

    return response.json()


def get_restaurant_review(kota: str, restaurant_name: str, restaurant_id: str) -> dict:
    """
    Get restaurant review by restaurant_id and restaurant_name. But, you must specify the kota

    Args:
        kota(str): kota to search e.g "jakarta" all in lower case, space is replaced by -
        restaurant_name(str): restaurant name to search e.g "mcdonalds"
        restaurant_id(str): restaurant uid on anthor api to retrieve restaurant list, usually in uid tag e.g "2f5f6bd9-598f-46a9-9408-c84e812e90a6"

    Returns:
        dict: restaurant data in json format with some details such as reviews, rating, menu rating, value for money, etc.
    """

    url = f"{base_url}/{kota}/restaurant/{restaurant_name}-{restaurant_id}/reviews.json?service_area={kota}&id={restaurant_name}-{restaurant_id}"

    response = requests.get(
        url,
        cookies=cookies,
        headers=headers,
    )

    return response.json()
