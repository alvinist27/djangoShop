from django.template.defaulttags import register


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)


@register.filter
def get_item_id(dictionary, key):
    return dictionary.get(key).id


@register.filter
def get_item_name(dictionary, key):
    return dictionary.get(key).name


@register.filter
def get_item_first_file_path(dictionary, key):
    return dictionary.get(key).images.first().file_path
