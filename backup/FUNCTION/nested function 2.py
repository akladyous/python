def get_speak_func(volume):
    def inner1(text):
        return text.upper()
    def inner2(text):
        return text.lower()
    if volume > 0.5:
        return inner1
    else:
        return inner2
get_speak_func(0.3)
get_speak_func(0.7)
speak_func = get_speak_func(0.7)
speak_func('Hello')
