import wikipediaapi as wiki

with open("user.txt", "r") as file:
    email = file.readline().strip()

def get_summary(page):
    return page.summary[:500] + "..." if page.summary else "No summary available."

def get_links(page):
    links = list(page.links.keys())

    bad_prefixes = (
        "Wikipedia:",
        "Template:",
        "Template talk:",
        "Help:",
        "File:",
        "Category:",
        "Portal:",
        "Talk:",
    )

    clean_links = []

    for link in links:
        if not link.startswith(bad_prefixes):
            clean_links.append(link)

    return clean_links

def choose_link(links):
    print("Choose a link to move to:")
    for i, link in enumerate(links):
        print(f"{i}. {link}")
    choice = int(input("Enter the number of your choice: "))
    return links[choice]

def move_to_link(link):
    wik = wiki.Wikipedia(user_agent=f'Wikiracebot ({email})', language='en')
    return wik.page(link)