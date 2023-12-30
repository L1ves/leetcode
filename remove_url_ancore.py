def remove_url_anchor(url):
    # TODO: complete
    if '#' not in url:
        return url
    base_url, anchor = url.split('#', 1)
    #base_url = url[:url.find('#')]
    #base_url = url[0:find('#')]
    #return url.split('#')[0]
    # Return the base URL without the anchor fragment
    return base_url

