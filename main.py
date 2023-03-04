import requests

url = "https://www.zillow.com/graphql"

querystring = {"zpid":"41050423","contactFormRenderParameter":"","queryId":"5abd3e07a096148eec91b9198e81496a","operationName":"ForSaleShopperPlatformFullRenderQuery"}

payload = {
    "operationName": "ForSaleShopperPlatformFullRenderQuery",
    "variables": {
        "zpid": 41054502,
        "contactFormRenderParameter": {
            "zpid": 41050423,
            "platform": "desktop",
            "isDoubleScroll": True
        }
    },
    "clientVersion": "home-details/6.1.2166.master.09cd25e",
    "queryId": "5abd3e07a096148eec91b9198e81496a"
}
headers = {
    "cookie": "AWSALB=3xVnGpkhdL9%2FXj9wigdL5FQ3Ovqa7Y6JXe4JQm9l6sNxzwHYRz8kQvdJu8e1DQfewM6f4d%2FBIpi76RkzGSyRPKu8EGlL3l4FyqXR5BZsq5AXXpkOnS3Z9%2BVLrPee; AWSALBCORS=3xVnGpkhdL9%2FXj9wigdL5FQ3Ovqa7Y6JXe4JQm9l6sNxzwHYRz8kQvdJu8e1DQfewM6f4d%2FBIpi76RkzGSyRPKu8EGlL3l4FyqXR5BZsq5AXXpkOnS3Z9%2BVLrPee; JSESSIONID=DDD696794B7F13BEBD1436BFD4128DAD; zguid=24%7C%25244677af3a-1129-47f5-90e4-d1e6d7df3db9; zgsession=1%7C8e5b1072-ac09-4f4a-b33d-951b2bc85dc0",
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:97.0) Gecko/20100101 Firefox/97.0",
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Referer": "https://www.zillow.com/homedetails/7144-Bidwell-Rd-Joelton-TN-37080/41050423_zpid/",
    "content-type": "application/json",
    "client-id": "home-details_fs-sp_bootstrap",
    "Origin": "https://www.zillow.com",
    "DNT": "1",
    "Connection": "keep-alive",
    "Cookie": "AWSALB=5zQ5mHIoluTk8EpWQBOEal8uprYt57WBafar1Qmetlu8PWo/ESuHaZEddQ7MSVEaPQj7Ve3QzO/cHhOR9IOqOcSzddpAjRalfc2VTtfiIIc/HdGvbthuJyRBZ/dj; AWSALBCORS=5zQ5mHIoluTk8EpWQBOEal8uprYt57WBafar1Qmetlu8PWo/ESuHaZEddQ7MSVEaPQj7Ve3QzO/cHhOR9IOqOcSzddpAjRalfc2VTtfiIIc/HdGvbthuJyRBZ/dj; JSESSIONID=1BC46DCDFB20DA8AD441BEF277355602; search=6|1680488096306%7Crect%3D36.370720449610154%252C-85.98187025585938%252C36.002739876688615%252C-87.58862074414063%26rid%3D2243%26disp%3Dmap%26mdm%3Dauto%26p%3D2%26z%3D1%26days%3D30%26type%3Dhouse%26lt%3Dfsba%252Cfsbo%252Cfore%252Ccmsn%26price%3D0-600000%26mp%3D0-3083%26fs%3D1%26fr%3D0%26mmm%3D0%26rs%3D0%26ah%3D0%26singlestory%3D0%26housing-connector%3D0%26abo%3D0%26garage%3D0%26pool%3D0%26ac%3D0%26waterfront%3D0%26finished%3D0%26unfinished%3D0%26cityview%3D0%26mountainview%3D0%26parkview%3D0%26waterview%3D0%26hoadata%3D1%26zillow-owned%3D0%263dhome%3D0%26featuredMultiFamilyBuilding%3D0%26ageRestricted55Plus%3De%26commuteMode%3Ddriving%26commuteTimeOfDay%3Dnow%09%092243%09%09%09%09%09%09; zguid=24|%24425aeac0-5d78-4c9b-8bd2-ab3288f21658; zgsession=1|adf42daf-5f09-4cc0-b9e4-77557bed782e; zjs_anonymous_id=%22425aeac0-5d78-4c9b-8bd2-ab3288f21658%22; zjs_user_id=null; zg_anonymous_id=%22e1fae81c-f451-4ebe-8eed-7e94b4fc68a7%22; _pxff_cc=U2FtZVNpdGU9TGF4Ow==; pxcts=56f15b65-ba32-11ed-b46d-6d636c745961; _pxvid=56f0b6cf-ba32-11ed-b46d-6d636c745961; _pxff_bsco=1; x-amz-continuous-deployment-state=AYABeJt+bo2IIVT4Hgdd9MhC+ysAPgACAAFEAB1kM2Jsa2Q0azB3azlvai5jbG91ZGZyb250Lm5ldAABRwAVRzAxMTE2MjczQzlQQzdZU1JDTVBHAAEAAkNEABpDb29raWUAAACAAAAADFOSiL3BtsgKVGlcpgAwxeDBwu%2FT9V65hn+K5Dj8TVRleNoodFiTB1o2qYKwmTp5k6XHo7B0SWXqhns6fn88AgAAAAAMAAQAAAAAAAAAAAAAAAAAAESTWtxDjYM7RhlIG8H+QG%2F%2F%2F%2F%2F%2FAAAAAQAAAAAAAAAAAAAAAQAAAAyv+Lg5YubSYlRMNHRr2ZkTUzCRoShKZJM6cjmP; _px3=aa3d6a34a02c6375a17a67e808135f08052851f8ffdbcc0591472067543c4cc3:sG6D9jcx7v7qIifi9gqIXvuQ6Lhv38Ez80z5W9ab+hQu7yss8IDAHStjRVLTDjC0Dduwki3H73XT0KpFJzVugg==:1000:sgYGj0dGWGeDwGdoN6QBrgdJo4Lx6Oa7UCnAXLOdkEvguTqV1ph0k3IaPJ8vhSurWiVP3GQD9Nwcqf5+mPGP5RDUEzYmvMDh+tfE9edmSxko+7sdJQNRiXzoBAtZ7lp+DmhcYbr5NSxSD6OjUPJ897+fiLMUpwZtdPhT+TUTfVzrB6KBZF85OctBE2i06b5Cqsfm/0oJp8b+uYYx7neyYA==; _gcl_au=1.1.1321510869.1677896097; DoubleClickSession=true; _uetsid=5be42360ba3211ed8bb433a1277a32d6; _uetvid=5be43180ba3211eda95273912042a86f; __pdst=1999efa05efd4814b308c1695730f0c1; _pin_unauth=dWlkPU1qbG1aV0ptTkRjdFpEQXhPQzAwT0ROakxXRTNOamt0TlRkallqUmlPVGsyTVdJeA",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "TE": "trailers"
}

response = requests.request("POST", url, json=payload, headers=headers, params=querystring)

print(response.text)
