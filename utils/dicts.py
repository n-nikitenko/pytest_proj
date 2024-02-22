def get_val(collection, key, default='git'):
    """
    Возвращает значение из словаря по переданному ключу, если ключ существует.
    В ином случае возвращается значение default.
    """
    if key in collection:
        return  collection[key]
    return default
