def find_admin(lst, lang):
    return [dev for dev in lst if dev['language'] == lang and dev['githubAdmin'] == 'yes']