import os
import time
import zipfile

content = {
    "pack": {
        "pack_format": 1,
        "description": f"§r汉化资源包，§c§n推荐加载！\n§r作者:§6§oGinsway§2|§r版本：§6§ov{time.strftime('%y.%m.%d', time.localtime())}"
    }
}

if __name__ == '__main__':
    with open("pack.mcmeta", "w", encoding="utf-8") as mcmeta:
        mcmeta.write(repr(content))
    with zipfile.ZipFile(f"./TLSAftermath-Language-Package-v{time.strftime('%y.%m.%d', time.localtime())}.zip",
                         mode="w") as package:
        for i in os.listdir("./assets"):
            package.write(f"./assets/{i}/lang/zh_CN.lang", f"assets/{i}/lang/zh_CN.lang")
        package.write("./pack.mcmeta", "pack.mcmeta")
        package.write("./pack.png", "pack.png")
        print("finish!")
