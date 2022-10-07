
# to clean given phone number and normalize to the valid state like 38(067)147-41-18
def clean_phone_number(phone_number):
    cleaned = ''

    for i in str(phone_number):
        if i.isdigit():
            cleaned += i

    normalized_phone_number = f'{cleaned[0:2]}({cleaned[2:5]}){cleaned[5:8]}-{cleaned[8:10]}-{cleaned[10:]}'
    return normalized_phone_number
