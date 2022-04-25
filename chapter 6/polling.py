favorite_languages = {
    "Jen": "python",
    "Sarah": "c",
    "Edward": "ruby",
    "Phil": "python"
}
should_take_poll = ["Jen", "Edward", "Phil", "Tom"]
for person in favorite_languages.keys():
    print(f"Hi, {person}")
    if person in should_take_poll:
        language = favorite_languages[person]
        print(f"{person}, I see you like {language}!\n")
for person in should_take_poll:
    if person not in favorite_languages.keys():
        print(f"{person}, you should take the poll!")
