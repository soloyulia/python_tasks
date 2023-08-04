def get_formatted_name(first,last, midlle=''):
    if midlle:
        full_name = f"{first} {midlle} {last}"
    else:
        full_name = f"{first} {last}"

    return full_name.title()
