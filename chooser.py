import wikipediaapi as wiki

with open("user.txt", "r") as file:
    email = file.readline().strip()

def choose_start_and_end():
    wik = wiki.Wikipedia(user_agent=f'Wikiracebot ({email})', language='en')
    random_pages = wik.random(limit=2)
    titles = list(random_pages.keys())

    start_page = wik.page(titles[0])
    end_page = wik.page(titles[1])

    return start_page, end_page