import requests
import json

cookies = {
    'ezoadgid_479514': '-1',
    'ezoref_479514': '',
    'ezosuibasgeneris-1': '0b6a8236-47e7-4f39-6202-fb717add07ba',
    'ezoab_479514': 'mod170',
    'active_template::479514': 'pub_site.1697885038',
    'ezopvc_479514': '1',
    'ezepvv': '1017',
    'lp_479514': 'https://chataigpt.org/',
    'ezovuuidtime_479514': '1697885039',
    'ezovuuid_479514': 'c6a6294b-eec3-4a90-4b65-aa2a6f6e6184',
    'ezouspvv': '0',
    'ezouspva': '0',
    '_gid': 'GA1.2.255934549.1697885048',
    '_ga_LZVDZ7FGS6': 'GS1.1.1697885048.1.0.1697885048.0.0.0',
    '_ga_596EQ86CZJ': 'GS1.1.1697885048.1.0.1697885048.0.0.0',
    'ntvSession': '{}',
    '_cc_id': '61d57d5baa95a9e892239a92ba75b359',
    'panoramaId_expiry': '1698489849725',
    'panoramaId': 'f6bc90063dabac57411c78033fbe16d53938abc3f7cd1782970ec5f4c55568fd',
    'panoramaIdType': 'panoIndiv',
    '__gads': 'ID=eb57bf963e17eec8:T=1697885050:RT=1697885050:S=ALNI_MZlORuSHHIzj3bf-mFrNgTi0WDfrg',
    '__gpi': 'UID=00000cbe0cb01511:T=1697885050:RT=1697885050:S=ALNI_MaJPbtsxNW27C9Azx5zMnW-wV6abQ',
    '_au_1d': 'AU1D-0100-001697885054-628AE3KQ-T67N',
    '_au_last_seen_pixels': 'eyJhcG4iOjE2OTc4ODUwNTQsInR0ZCI6MTY5Nzg4NTA1NCwicHViIjoxNjk3ODg1MDU0LCJydWIiOjE2OTc4ODUwNTQsInRhcGFkIjoxNjk3ODg1MDU0LCJhZHgiOjE2OTc4ODUwNTQsImdvbyI6MTY5Nzg4NTA1NCwiYW1vIjoxNjk3ODg1MDU0LCJ1bnJ1bHkiOjE2OTc4ODUwNTQsImFkbyI6MTY5Nzg4NTA1NH0%3D',
    'ezds': 'ffid%3D1%2Cw%3D1920%2Ch%3D1200',
    'ezohw': 'w%3D779%2Ch%3D1036',
    'wpaicg_chat_client_id': 't_cdfa9e8fb431b05c8c638cea01a603',
    'wpaicg_conversation_url_shortcode': 'e64db9995f8ab0b5bc0e6f2e7f792c4d',
    'e64db9995f8ab0b5bc0e6f2e7f792c4d': 'a%3A2%3A%7Bi%3A0%3Bs%3A14%3A%22Human%3A%20hi%0AAI%3A%20%22%3Bi%3A1%3Bs%3A34%3A%22Hello%21%20How%20can%20I%20assist%20you%20today%3F%22%3B%7D',
    '_ga': 'GA1.2.172051785.1697885048',
    'cf_clearance': '6xJxKF2hcDTKFo25mg3LnB5G38sv6dh_a4H90vca.78-1697885062-0-1-db600938.33d7179c.12e01e96-0.2.1697885062',
    '_pbjs_userid_consent_data': '3524755945110770',
    'ezux_lpl_479514': '1697885110629|e8adb35d-d5c7-4b18-49c3-852e4bd6b729|false',
    'cto_bundle': 'Ac51j19OanVsQUlFbGh0WURhaDlIRFhaVVE3MmxXWDQ0dEVhMmVoZk03eXRrSDVlUU5YNERPdldaVEhmTFJQOGslMkZuR3I5MmhkOWdoOXRNWW01aWp6dDE0ZHJUSTcwNVh3aExwWnVuZnQ5JTJGb2VyZ0tlSnZaUWJPbUlwaXMzUzhMSThNaCUyQg',
    'cto_bundle': '',
    '__qca': 'P0-1920689361-1697885121301',
    'ezux_et_479514': '3',
    'ezux_tos_479514': '72',
}

headers = {
    'authority': 'chataigpt.org',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryzXTDcCzUdk8tI9g8',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'ezoadgid_479514=-1; ezoref_479514=; ezosuibasgeneris-1=0b6a8236-47e7-4f39-6202-fb717add07ba; ezoab_479514=mod170; active_template::479514=pub_site.1697885038; ezopvc_479514=1; ezepvv=1017; lp_479514=https://chataigpt.org/; ezovuuidtime_479514=1697885039; ezovuuid_479514=c6a6294b-eec3-4a90-4b65-aa2a6f6e6184; ezouspvv=0; ezouspva=0; _gid=GA1.2.255934549.1697885048; _ga_LZVDZ7FGS6=GS1.1.1697885048.1.0.1697885048.0.0.0; _ga_596EQ86CZJ=GS1.1.1697885048.1.0.1697885048.0.0.0; ntvSession={}; _cc_id=61d57d5baa95a9e892239a92ba75b359; panoramaId_expiry=1698489849725; panoramaId=f6bc90063dabac57411c78033fbe16d53938abc3f7cd1782970ec5f4c55568fd; panoramaIdType=panoIndiv; __gads=ID=eb57bf963e17eec8:T=1697885050:RT=1697885050:S=ALNI_MZlORuSHHIzj3bf-mFrNgTi0WDfrg; __gpi=UID=00000cbe0cb01511:T=1697885050:RT=1697885050:S=ALNI_MaJPbtsxNW27C9Azx5zMnW-wV6abQ; _au_1d=AU1D-0100-001697885054-628AE3KQ-T67N; _au_last_seen_pixels=eyJhcG4iOjE2OTc4ODUwNTQsInR0ZCI6MTY5Nzg4NTA1NCwicHViIjoxNjk3ODg1MDU0LCJydWIiOjE2OTc4ODUwNTQsInRhcGFkIjoxNjk3ODg1MDU0LCJhZHgiOjE2OTc4ODUwNTQsImdvbyI6MTY5Nzg4NTA1NCwiYW1vIjoxNjk3ODg1MDU0LCJ1bnJ1bHkiOjE2OTc4ODUwNTQsImFkbyI6MTY5Nzg4NTA1NH0%3D; ezds=ffid%3D1%2Cw%3D1920%2Ch%3D1200; ezohw=w%3D779%2Ch%3D1036; wpaicg_chat_client_id=t_cdfa9e8fb431b05c8c638cea01a603; wpaicg_conversation_url_shortcode=e64db9995f8ab0b5bc0e6f2e7f792c4d; e64db9995f8ab0b5bc0e6f2e7f792c4d=a%3A2%3A%7Bi%3A0%3Bs%3A14%3A%22Human%3A%20hi%0AAI%3A%20%22%3Bi%3A1%3Bs%3A34%3A%22Hello%21%20How%20can%20I%20assist%20you%20today%3F%22%3B%7D; _ga=GA1.2.172051785.1697885048; cf_clearance=6xJxKF2hcDTKFo25mg3LnB5G38sv6dh_a4H90vca.78-1697885062-0-1-db600938.33d7179c.12e01e96-0.2.1697885062; _pbjs_userid_consent_data=3524755945110770; ezux_lpl_479514=1697885110629|e8adb35d-d5c7-4b18-49c3-852e4bd6b729|false; cto_bundle=Ac51j19OanVsQUlFbGh0WURhaDlIRFhaVVE3MmxXWDQ0dEVhMmVoZk03eXRrSDVlUU5YNERPdldaVEhmTFJQOGslMkZuR3I5MmhkOWdoOXRNWW01aWp6dDE0ZHJUSTcwNVh3aExwWnVuZnQ5JTJGb2VyZ0tlSnZaUWJPbUlwaXMzUzhMSThNaCUyQg; cto_bundle=; __qca=P0-1920689361-1697885121301; ezux_et_479514=3; ezux_tos_479514=72',
    'origin': 'https://chataigpt.org',
    'referer': 'https://chataigpt.org/',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
}
msg="your message "
data = f'------WebKitFormBoundaryzXTDcCzUdk8tI9g8\r\nContent-Disposition: form-data; name="_wpnonce"\r\n\r\n85b0e18a5d\r\n------WebKitFormBoundaryzXTDcCzUdk8tI9g8\r\nContent-Disposition: form-data; name="post_id"\r\n\r\n7\r\n------WebKitFormBoundaryzXTDcCzUdk8tI9g8\r\nContent-Disposition: form-data; name="url"\r\n\r\nhttps://chataigpt.org\r\n------WebKitFormBoundaryzXTDcCzUdk8tI9g8\r\nContent-Disposition: form-data; name="action"\r\n\r\nwpaicg_chat_shortcode_message\r\n------WebKitFormBoundaryzXTDcCzUdk8tI9g8\r\nContent-Disposition: form-data; name="message"\r\n\r\n{msg}\r\n\r\n------WebKitFormBoundaryzXTDcCzUdk8tI9g8\r\nContent-Disposition: form-data; name="bot_id"\r\n\r\n0\r\n------WebKitFormBoundaryzXTDcCzUdk8tI9g8--\r\n'

response = requests.post('https://chataigpt.org/wp-admin/admin-ajax.php', cookies=cookies, headers=headers, data=data)
data_get=json.loads(response.text)
print(data_get['data'])

