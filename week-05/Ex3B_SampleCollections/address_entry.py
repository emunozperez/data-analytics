name = "John Doe"
address = "123 Joe Smith St."
city = "Anytown"
state = "CA"
zip_code = "12345"
contact_info = {
    "name": name,
    "address": address,
    "city": city,
    "state": state,
    "zip_code": zip_code

}

print(f"{contact_info['name']} lives at {contact_info['address']}, {contact_info['city']}, {contact_info['state']} {contact_info['zip_code']}.")

contact_info.pop("name")

full_name = {
    "first_name": "John",
    "last_name": "Doe"  
}

full_name.update({"honorific": "Mr."})

contact_info.update({"full_name": full_name})

print(f"{contact_info['full_name']['honorific']} {contact_info['full_name']['first_name']} {contact_info['full_name']['last_name']} lives at {contact_info['address']}, {contact_info['city']}, {contact_info['state']} {contact_info['zip_code']}.")