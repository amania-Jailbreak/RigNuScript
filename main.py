print("Loading....")
try:
    import os,sys,subprocess,configparser
except:
    print("モジュールの読み込みに失敗しました")
try:
    setting = configparser.ConfigParser()
    setting.read("config.ini")
except:
    print("設定ファイルを読み込めませんでした")

print("""
---------------------------------------------------------------------------
RigNuScript Ver 1.0

a = script_test
""")
c = input(">>>")
if c == "a":
    print("loading script")
    files = [file for file in os.listdir("./script") if file.endswith(".py")]
    names = []
    for file in files:
        with open(os.path.join("./script", file), 'r') as f:
            lines = f.readlines()
            for line in lines:
                if 'name:' in line:
                    name = line.split('name:')[1].strip()
                    names.append(name)
    for i in names:
        print(i)
