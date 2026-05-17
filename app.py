import wikipediaapi as wiki
import chooser
import mover

try:
    with open("user.txt", "w") as file:
        email = input("Enter your email address to receive updates: ")
        if email.lower() == "anas":
            email = "codecrusader07@gmail.com"
        elif "@" not in email or "." not in email:
            raise ValueError("Invalid email address format.")
        elif len(email) > 254:
            raise ValueError("Email address is too long.")
        elif len(email) < 5:
            raise ValueError("Email address is too short.")
        wik = wiki.Wikipedia(user_agent=f'Wikiracebot ({email})', language='en')
        
        file.write(f"{email}\n")
except Exception as e:
    print(f"Something went wrong. : (\n{e}")
    exit(1)

start_page, end_page = chooser.choose_start_and_end()
print(f"Start page: {start_page.title}")
print(f"End page: {end_page.title}")

for _ in range(20):
    print(f"\nCurrent page: {start_page.title}")
    print(f"Summary: {mover.get_summary(start_page)}")
    

    command = input("\nEnter the link number to move to (or exit or summary or links): ")
    
    if command.lower() == "exit":
        print("\nExiting the game.")
        break
    
    elif command.lower() == "summary":
        print(f"\nSummary of {start_page.title}: {mover.get_summary(start_page)}")
        print(f"\nSummary of {end_page.title}: {mover.get_summary(end_page)}")
        continue
    
    elif command.lower() == "links":
        print("\nLoading links...")
        links = mover.get_links(start_page)
        if not links:
            print("No links available, cannot move further.")
            break
        shown_links = links[:]

        print(f"\nLinks from {start_page.title}:")
        for i, link_title in enumerate(shown_links):
            print(f"{i}. {link_title}")
        continue
    else:
        try:
            link_index = int(command)
            if 0 <= link_index < len(shown_links):
                start_page = mover.move_to_link(shown_links[link_index])
                if start_page.title == end_page.title:
                    print("\nCongratulations! You've reached the end page!")
                    break
            else:
                print("\nInvalid link number. Please try again.")
        except ValueError:
            print("\nInvalid input. Please enter a number, 'exit', 'summary', or 'links'.")
