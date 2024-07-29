# -*- coding: UTF-8 -*-
"""
@Project :network_safe 
@File    :cad
@IDE     :PyCharm 
@Author  :方正
@Date    :2024/7/29 下午6:17 
"""
import os
import time
import uuid
from datetime import datetime

import ezdxf

from ezdxf.entities.acad_table import read_acad_table_content

import configparser
from cryptography.fernet import Fernet

# 生成一个密钥（请妥善保管此密钥）
key = b'fzrywy1998'
cipher_suite = Fernet(key)


# 检查当前日期是否小于2099年7月30日
def is_valid_date():
    current_date = datetime.now()
    target_date = datetime(2099, 12, 31)
    return current_date < target_date


# 获取用户的MAC地址
def get_mac_address():
    mac = uuid.getnode()
    return ':'.join(format(mac, '012x')[i:i + 2] for i in range(0, 12, 2))


# 加密MAC地址
def encrypt_mac(mac):
    return cipher_suite.encrypt(mac.encode()).decode()


# 解密MAC地址
def decrypt_mac(encrypted_mac):
    return cipher_suite.decrypt(encrypted_mac.encode()).decode()


# 写入INI文件
def write_ini(mac):
    config = configparser.ConfigParser()
    config['DEFAULT'] = {'EncryptedMAC': mac}
    with open('config.ini', 'w') as configfile:
        config.write(configfile)


# 读取INI文件
def read_ini():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config['DEFAULT']['EncryptedMAC']


def print_all_texts(dxf_file):
    # 加载DXF文件
    print(f"处理文件{dxf_file}")
    doc = ezdxf.readfile(dxf_file)
    msp = doc.modelspace()
    # 遍历模型空间中的所有实体
    for entity in msp:
        if entity.dxftype() == 'ACAD_TABLE':
            values = read_acad_table_content(entity)
            with open(f"{values[0][0]}.csv", "w") as f:
                f.write("\n".join(
                    [",".join([vv.replace(",", ";").split(";")[-1].split("}")[0] for vv in v]) for v in values]))


if __name__ == "__main__":
    try:
        print("本程序由方正开发,联系方式:11711153217@qq.com")
        mac = get_mac_address()
        if is_valid_date():
            encrypted_mac = encrypt_mac(mac)
            write_ini(encrypted_mac)
            print("INI文件已生成并加密MAC地址。")
        encrypted_mac = read_ini()
        decrypted_mac = decrypt_mac(encrypted_mac)
        if decrypted_mac == mac:
            current_directory = os.getcwd()
            for filename in os.listdir(current_directory):
                if filename.endswith('.dxf'):
                    dxf_file = os.path.join(current_directory, filename)
                    print_all_texts(filename)
        else:
            print("请联系1171153217@qq.com")
        print("处理完成")
    except Exception as e:
        print("错误",e)
    finally:
        time.sleep(100)
