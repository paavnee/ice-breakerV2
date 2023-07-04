import os
import requests


def scrape_linkedin_profile(linkedin_profile_url: str):
    """scrape information from LinkedIn profiles,
    Manually scrape the information from the LinkedIn profile"""
    api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"
    header_dic = {
        "Authorization": f'Bearer {os.environ.get("PROXYCURL_API_KEY")}'}

    # response = requests.get(
    #     api_endpoint, params={"url": linkedin_profile_url}, headers=header_dic
    # )
    response = requests.get(
        "https://gist.githubusercontent.com/paavnee/0cf94303b542d1b14c80047c4a6235d8/raw/863dd70c0e1bb8c5fa9f231aea2477fae4a36ba6/sample.json")

    data = response.json()
    data = {
        k: v
        for k, v in data.items()
        if v not in ([], "", "", None)
        and k not in ["people_also_viewed", "certifications"]
    }
    if data.get("groups"):
        for group_dict in data.get("groups"):
            group_dict.pop("profile_pic_url")

    return data
