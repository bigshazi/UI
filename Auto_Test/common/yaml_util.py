
import os
import yaml

#获取项目根目录
def get_object_path():
    return os.path.dirname(__file__).split('common')[0]

#读取yaml文件
def read_yaml(yaml_path):
    with open(get_object_path()+yaml_path,mode='r',encoding='utf-8') as f:
        value = yaml.load(stream=f,Loader=yaml.FullLoader)
        return value

if __name__ == '__main__':
    print(read_yaml('Test_Case/user_manage/generate_QR_code.yaml'))