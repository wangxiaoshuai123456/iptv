import logging

cookie = {}
token = ''


def printCookieAndToken():
    print('api.cookie=%s, api.token=%s' % (cookie, token))


def get_info_by_cfg(file_name=''):
    info_list = []
    try:
        file = open(file_name, 'r')

        while True:
            line = file.readline()
            if line == '\n':
                break
            line = line[0:len(line) - 1]  # 去换行符
            data = {}
            print('line:', line)
            data_list = line.split(',')
            data['username'] = data_list[0]
            data['pwd'] = data_list[1]
            info_list.append(data)
    except IOError as err:
        print('读取配置文件失败...:Err ', err)
    finally:
        file.close()

    print('info_list:', info_list)

    return info_list


def log():
    logger = logging.getLogger('wsp')
    logger.setLevel(logging.DEBUG)

    if not logger.handlers:
        fileHander = logging.FileHandler('log.txt', encoding='utf-8')
        streamHandler = logging.StreamHandler()

        fmt = logging.Formatter('%(asctime)s %(name)s %(pathname)s %(lineno)s %(levelname)s %(message)s', \
                                '%Y-%m-%d %H:%M:%S')

        fileHander.setFormatter(fmt)
        streamHandler.setFormatter(fmt)

        logger.addHandler(fileHander)
        logger.addHandler(streamHandler)

    return logger

    # logger.removeHandler(fileHander)
    # logger.removeHandler(streamHandler)
