import PIL

def handler(event, context):
    print(event)
    print(context)
    print(PIL.VERSION)
    return PIL.VERSION


if __name__ == '__main__':
    print(handler({}, {}))
