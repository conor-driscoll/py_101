def greetings(name_list, title_occupation_dict):
    return (f"Top o' the morning to the top {title_occupation_dict['title']} "
            f"{title_occupation_dict['occupation']} on the Emerald Isle, "
            f"{' '.join(name_list)}!")


greeting = greetings(
    ["John", "Q", "Doe"],
    {"title": "Master", "occupation": "Plumber"},
)
print(greeting)
# Hello, John Q Doe! Nice to have a Master Plumber around.