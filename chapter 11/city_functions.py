def describe_location(city, country, *population):
    if population:
        population = population[:3]  # Why can I use 5 as my index value here even though the highest index is 1
        # when I use a colon?
        # Why can I not get rid of the parentheses by indexing unless there is only 1 number in the brackets?
        # I understand that"population=None"is the better option here but still want to understand what's happening here
        location_info = f"{city.title()}, {country.title()}, Population: {population}"
    else:
        location_info = f"{city.title()}, {country.title()}"
    return location_info


if __name__ == "__main__":
    print(describe_location("Shanghai", "China", 500_000, 5))
