# adafruit_hashlib
ljinux.api.var("argj", f"mkdir &/lib/adafruit_hashlib")
ljinux.based.command.fpexecc([None, "/bin/mkdir.py"])
for filee in [
    "__init__.mpy",
    "_md5.mpy",
    "_sha1.mpy",
    "_sha224.mpy",
    "_sha256.mpy",
    "_sha384.mpy",
    "_sha512.mpy",
]:
    ljinux.api.var("argj", f"cp {filee} &/lib/adafruit_hashlib/{filee}")
    ljinux.based.command.fpexecc([None, "/bin/cp.py"])
    del filee

# bins
for filee in [
    "md5sum.lja",
    "md5sum.py",
    "sha1sum.lja",
    "sha1sum.py",
    "sha224sum.lja",
    "sha224sum.py",
    "sha256sum.lja",
    "sha256sum.py",
    "sha384sum.lja",
    "sha384sum.py",
    "sha512sum.lja",
    "sha512sum.py",
]:
    ljinux.api.var("argj", f"cp {filee} /bin/{filee}")
    ljinux.based.command.fpexecc([None, "/bin/cp.py"])
    del filee

ljinux.api.var("return", "0")
