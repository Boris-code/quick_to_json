import spider.utils.tools as tools


def main():
    contents = tools.read_file('to_json.txt', readlines=True)

    json = {}
    for content in contents:
        content = content.strip()
        if not content or content.startswith(':'):
            continue

        regex = "([^:\s]*)[:|\s]*(.*)"

        result = tools.get_info(content, regex, fetch_one=True)
        if result[0] in json:
            json[result[0]] = json[result[0]] + '&' + result[1]
        else:
            json[result[0]] = result[1].strip()

    print(tools.dumps_json(json))


if __name__ == '__main__':
    main()
