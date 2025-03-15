import configparser
import os.path

file = os.path.abspath(os.path.curdir)+"\\configurations\\config.ini"
#file = os.path.abspath(os.path.curdir)+"/configurations/config.ini"
#file = "D:\\work\\worksapace_pycharm\\Nukri\\Nurkri.com\\configurations\\config.ini"
print(file)
config = configparser.RawConfigParser()
config.read(file)


def read_baseurl():
    url = config.get(section="applicationInfo",option="base_url")
    return url.replace('"',"")

def read_login_username():
    username = config.get(section="login",option="username")
    return username.replace('"',"")

def read_password():
    password = config.get(section="login",option="password")
    return password.replace('"',"")

def read_headline(number):
    username = config.get(section="data",option="headline"+str(number))
    return username.replace('"',"").strip()

def read_resume_path(number):
    username = config.get(section="resume_info",option="resume_path"+str(number))
    return username.replace('"',"").strip()
