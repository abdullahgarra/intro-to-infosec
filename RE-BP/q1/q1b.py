def fix_message_data(data: bytes) -> bytes:
    """
    Implement this function to return the "fixed" message content. This message
    should have minimal differences from the original message, but should pass
    the check of `msgcheck`.

    :param data: The source message data.
    :return: The fixed message data.
    """
    data = list(data)
    data[0] = 0
    data[1] = 141
    return bytes(data)


def fix_message(path):
    with open(path, 'rb') as reader:
        data = reader.read()
    fixed_data = fix_message_data(data)
    with open(path + '.fixed', 'wb') as writer:
        writer.write(fixed_data)


def main(argv):
    if len(argv) != 2:
        print('USAGE: python {} <msg-file>'.format(argv[0]))
        return -1
    path = argv[1]
    fix_message(path)
    print('done')


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
