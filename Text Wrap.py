
def wrap(string, max_width):
    s = textwrap.wrap(string, max_width)
    x = ''
    for a in s:
        x += a + '\n'
    return x.strip()
