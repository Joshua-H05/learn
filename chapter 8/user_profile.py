def profile_maker(first_name, last_name, **info):
    info["first name"] = first_name
    info["last name"] = last_name
    return info


print(profile_maker("Joshua", "Hu", nationality="chinese"))  # does the variable "nationality" not have to be put in
# quotation marks? Is it because it's a parameter? If so, does Python just automatically convert the parameters and
# their arguments into key value pairs in the dictionary?
# keyword parameter--> passing the value "chinese" to keyword parameter "nationality"
# kwarg = keyword argument
