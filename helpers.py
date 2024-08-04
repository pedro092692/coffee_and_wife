import bleach


def sanitize_iframe(iframe):
    allowed_attributes = ['src', 'width', 'height', 'frameborder', 'allowfullscreen']
    allowed_tags = ['iframe']

    # sanitize iframe using bleach
    cleaned_iframe = bleach.clean(iframe, tags=allowed_tags, attributes=allowed_attributes)

    # check src

    allowed_domains = ['googleusercontent.com', 'www.google.com']
    src_attribute = cleaned_iframe.split('src="')[1].split('"')[0]

    if not any(domain in src_attribute for domain in allowed_domains):
        return None  # Or handle invalid iframe

    return cleaned_iframe
