"""
name:Resize
Author:amania
"""
print("-----------------------------------------------------------------")
print("Resize Script")
print("このモジュールでは現在の解像度を100%とし拡大と縮小を行うことができます")
print("警告:Configではデフォルトでバックアップが無効になっております バックアップを有効にするにはRNSのルートにあるconfigフォルダの中にあるResize.iniを編集してください")
print("-----------------------------------------------------------------")
try:
    import os
    import rns
    import cv2
except:
    print("モジュールの読み込みに失敗しました")
try:
    root = rns.RNS()
    path = root.env["path"]
except:
    print("RNSモジュールの初期化に失敗しました 実行環境とRNSの設定などを再確認しそれでもダメな場合は再インストールしてください")
try:
    config = rns.Config("Resize")
    if "setting" in config.config:
        if "backup" in config.config["setting"]:
            backup = config.config["setting"]["backup"]
        else:
            config.config["setting"]["backup"] = "False"
            backup = "False"
            config.save()
    else:
        config.config["setting"] = {}
        config.config["setting"]["backup"] = "False"
        config.save()
        backup = "False"
except Exception as e:
    print(e)
    print("設定を読み込めませんでした")
def resize_image(path, scale_factor, backup="False"):
    image = cv2.imread(path)
    if backup == "True":
        backup_path_t = path.split(".")
        backup_path = backup_path_t[0] + ".back." + backup_path_t[1]
        cv2.imwrite(backup_path, image)
    
    height, width = image.shape[:2]
    new_height = int(height * scale_factor)
    new_width = int(width * scale_factor)

    resized_image = cv2.resize(image, (new_width, new_height))
    print(path)
    cv2.imwrite(path, resized_image)
scale_factor = float(input("パーセントを入力してください: ")) / 100
resize_image(path, scale_factor, backup)


