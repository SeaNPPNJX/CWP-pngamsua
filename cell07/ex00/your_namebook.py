#!/usr/bin/env python3

def array_of_names(my_dict):
    return [f"{i.capitalize()} {my_dict[i].capitalize()}" for i in my_dict]



persons = {
"jean": "valjean",
"grace": "hopper",
"xavier": "niel",
"fifi": "brindacier"
}
print(array_of_names(persons))
