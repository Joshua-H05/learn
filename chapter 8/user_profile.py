def profile_maker(first_name, last_name, **info):
    info["first name"] = first_name
    info["last name"] = last_name
    return info


print(profile_maker("Joshua", "Hu", nationality="chinese"))  # does the variable "nationality" not have to be put in
# quotation marks?
