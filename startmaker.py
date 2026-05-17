import requests
with open("user.txt", "r") as file:
    email = file.readline().strip()

URL = "https://en.wikipedia.org/w/api.php"

HEADERS = {
    "User-Agent": f"Wikiracebot/1.0 ({email})"
}

def get_random_titles(count):
    params = {
        "action": "query",
        "format": "json",
        "list": "random",
        "rnnamespace": 0,
        "rnlimit": count,
    }

    response = requests.get(URL, params=params, headers=HEADERS)
    response.raise_for_status()

    data = response.json()
    return [page["title"] for page in data["query"]["random"]]

titles = get_random_titles(20)

with open("start.txt", "a") as file:
    for title in titles:
        file.write(title + "\n")

print("Added random pages:")
for title in titles:
    print(title)