""" Utility methods for Organization Attributes """


def generate_key_for_field(data):
    """
    Method used to generate key for the attribute of organizations
    :param data: existing attributes with keys
    :return: next key to be placed against attribute
    """
    keys = [int(value['order']) for key, value in data.items()]
    return max(keys) + 1 if keys else 1


def generate_random_key_for_field(name, order):
    """
    Method used to generate random key for the attribute of organizations
    :param name: name of the attribute
    :param order: order of the attribute
    :return: next key to be placed against attribute
    """
    return "{}_{}".format(name.lower(), order)


def is_label_exists(name, data):
    """
    Method used to check whether label exists for the attribute of organizations
    :param name: name of the attribute
    :param data: existing attributes with keys
    :return: boolean value
    """
    return name in [value['label'] for key, value in data.items()]


def is_key_exists(key, data):
    """
    Method used to check whether key exists for the attribute of organizations
    :param key: key of the attribute
    :param data: existing attributes with keys
    :return: boolean value
    """
    return key in list(data.keys())


def generate_key_for_main_user(user_id):
    """
    Method used to generate key for the user organization
    :param user_id: id of the user
    :return: key to be placed against user main organization
    """
    return 'ORGANIZATION-USER-{user_id}'.format(
        user_id=user_id
    )
