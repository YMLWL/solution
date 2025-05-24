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

    response = requests.get(
        f"{base_url}/{kota}/{kecamatan}-restaurants/near_me.json?service_area={kota}&locality={kecamatan}-restaurant&category=near_me",
        cookies=cookies,
        headers=headers,
    )

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
