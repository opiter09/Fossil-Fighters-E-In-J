import os
import shutil
import subprocess
import sys

if (os.path.exists("NDS_UNPACK") == False):
    subprocess.run([ "dslazy.bat", "UNPACK", "america.nds" ])
    os.rename("NDS_UNPACK", "America")
    subprocess.run([ "dslazy.bat", "UNPACK", "japan.nds" ])
    shutil.rmtree("NDS_UNPACK/data/msg")
    shutil.rmtree("NDS_UNPACK/data/text")
    shutil.rmtree("NDS_UNPACK/data/font")
    os.rename("America/data/msg/", "NDS_UNPACK/data/msg/")
    os.rename("America/data/text/", "NDS_UNPACK/data/text/")
    os.rename("America/data/font/", "NDS_UNPACK/data/font/")
    subprocess.run([ "xdelta3-3.0.11-x86_64.exe", "-d", "-f", "-s", "NDS_UNPACK/data/text/japanese", "two.xdelta",
        "NDS_UNPACK/data/text/japanesex" ])
    os.remove("NDS_UNPACK/data/text/japanese")
    os.rename("NDS_UNPACK/data/text/japanesex", "NDS_UNPACK/data/text/japanese")
    subprocess.run([ "dslazy.bat", "PACK", "out.nds" ])
    