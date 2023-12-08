import base64
from tonpy.types import Cell
from os import path
import pathlib


def load_data():
    return {
        "config": _read("config", True),
        "pool_data": _read("pool_data"),
        "pool_code": _read("pool_code")
    }


def _read(k, b64: bool = True):
    dir_ = pathlib.Path(__file__).parent.resolve()
    with open(path.join(dir_, k)) as f:
        d = f.read()
        if not b64:
            d = base64.b64encode(bytes.fromhex(d)).decode("utf8")
        return Cell(d)
