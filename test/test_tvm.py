
from tvm_server.data.loader import load_data
from tvm_server.tvm import run_get_method


def test_pool_data():
    d = load_data()
    code = d["pool_code"]
    data = d["pool_data"]
    config = d["config"]

    r = run_get_method(code, data, "get_pool_full_data", config=config)
    assert r.ok
    assert r.exit_code == -1

    r = r.stack.unpack_rec()
    print(r)


def test_pool_data_fail():
    d = load_data()
    code = d["pool_code"]
    data = d["pool_data"]

    r = run_get_method(code, data, "get_pool_full_data")
    assert r.ok is False


def test_pool_data_json():
    d = load_data()
    code = d["pool_code"]
    data = d["pool_data"]
    config = d["config"]

    r = run_get_method(code, data, "get_pool_full_data", config=config)
    print(r.to_json())
