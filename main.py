print("Loading....")
try:
    import os,sys,subprocess,configparser,sys
except:
    print("モジュールの読み込みに失敗しました")
try:
    setting = configparser.ConfigParser()
    setting.read("config.ini")
except:
    print("設定ファイルを読み込めませんでした")

def write_env_path_to_temp_ini(path):
    try:
        with open("temp.ini", "w") as temp_ini_file:
            temp_ini_file.write("[env]\npath = " + path)
    except Exception as e:
        print("temp.iniファイルにパスを書き込めませんでした")

write_env_path_to_temp_ini(sys.argv[1])

print("""
---------------------------------------------------------------------------
RigNuScript Ver 1.0
""")
print("loading script")
files = [file for file in os.listdir("./script") if file.endswith(".py")]
names = []
for file in files:
    names.append(file.split(".")[0])
for index, name in enumerate(names):
    print(f"{index} : {name}")
c = input(">>>")
if c.isdigit() and int(c) < len(names):
    selected_name = names[int(c)]
    selected_path = os.path.join("./script", f"{selected_name}.py")
    try:
        with open(selected_path, 'r', encoding="utf-8") as selected_file:
            selected_code = selected_file.read()
            exec(selected_code)
    except FileNotFoundError:
        print("選択されたスクリプトが見つかりません")
else:
    print("無効な番号が入力されました")

