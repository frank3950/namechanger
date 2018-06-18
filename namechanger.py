import os
import shutil
import uuid
import config
import logging


class NameChanger:
    def __init__(self):
        logging.basicConfig(
            filename=config.LOG_FILE,
            level=logging.INFO
        )
        source_path = config.SOURCE_PATH

    @staticmethod
    def get_file():
        """获取要修改的文件名"""

        source_path = config.SOURCE_PATH
        logging.info('源目录：%s', source_path)
        match_file_list = []
        unmatch_file_list = []
        file_type = config.FILE_TYPE

        for file in os.listdir(source_path):
            file_fullname = os.path.join(source_path, file)
            if os.path.isfile(file_fullname):
                suffix = str(os.path.splitext(file)[-1]).lower()

                # 后缀与配置均转为小写进行匹配
                if suffix in (str.lower() for str in file_type):
                    match_file_list.append(file_fullname)
                else:
                    unmatch_file_list.append(file_fullname)

        logging.info('匹配的文件：')
        for match_file in match_file_list:
            logging.info(match_file)

        logging.info('未匹配的文件：')
        for unmatch_file in unmatch_file_list:
            logging.info(unmatch_file)

        return match_file_list

    @staticmethod
    def rename2uuid(file_list):
        """重命名为唯一字符串"""

        for file in file_list:
            suffix = str(os.path.splitext(file)[-1])
            new_name = str(uuid.uuid1()) + suffix
            new_path = config.TARGET_PATH
            new_filename = os.path.join(new_path, new_name)

            shutil.copyfile(file, new_filename)
            logging.info('Rename file %s to %s', file, new_filename)


if __name__ == '__main__':
    nc = NameChanger()
    file_list = nc.get_file()
    nc.rename2uuid(file_list)
