main_dict = {
    "key1": "50",
    "key2": "Hello",
    "key3": {
        "subkey1": "3.14",
        "subkey2": 100,
        "subkey3": False,
        "subkey4": [1, 2, 3],
        "subkey5": None
    },
    "key4": True
}

types_dict = {
    key: type(value) for key, value in main_dict.items()
}

nested_types_dict = {
    subkey: type(subvalue) for subkey, subvalue in main_dict["key3"].items()
}

print("Словник з типами даних основного словника:", types_dict)
print("Словник з типами даних вкладеного словника:", nested_types_dict)