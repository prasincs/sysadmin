#!/usr/bin/env python
import os,stat
with open ("android_vendors_list") as f:
    g = open("51-android.rules","w")
    for line in f.readlines():
        name, id = line.strip().split(",")
        g.write("#%s\n"%name)
        g.write('SUBSYSTEM=="usb", ATTR{idVendor}=="%s", MODE="0666"\n'%id)
    os.chmod("51-android.rules",stat.S_IXOTH|stat.S_IROTH|stat.S_IRWXU|stat.S_IRWXG)
    g.close()
