def get_cats_info(path: str) -> list[dict[str, str]] | str:
    """
    Read cat information from a text file and return a list of dictionaries.

    Each line contains a cat's ID, name, and age, separated by commas.
    Validates the data and removes extra whitespace from each field.

    Args:
        path (str): Path to the UTF-8 encoded text file.

    Returns:
        list[dict[str, str]] | str: A list of dictionaries containing
            each cat's ID, name, and age as strings.
            Returns an error message if the file is missing,
            incorrectly encoded, or contains invalid data.
    """

    result = []

    try:
        with open(path, 'r', encoding='utf-8') as file:
            for cat_line in file:
                parts = cat_line.strip().split(',')
                cleaned = list(map(str.strip, parts))
                cat_id, cat_name, cat_age = cleaned

                if not cat_id or not cat_name or not cat_age:
                    raise ValueError("Cat record contains empty fields.")

                cat = {"id": cat_id, "name": cat_name, "age": cat_age}

                result.append(cat)

    except FileNotFoundError:
        return "The file does not exist"
    except UnicodeDecodeError:
        return "Not UTF-8"
    except ValueError:
        return "Invalid file format."

    return result



print(get_cats_info("test.txt"))