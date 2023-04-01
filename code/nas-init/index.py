# coding=utf-8
import os


def handler(event, context):
    if not os.path.exists("/mnt/auto/halo2"):
        os.system(
            "mkdir -p /mnt/auto/halo2 && pwd")
    return "nas init"
