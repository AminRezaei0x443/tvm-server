
from tonpy.tvm.tvm import TVM, method_name_to_id
from tonpy.tvm.tvm import C7
from tvm_server.data.loader import load_data


def test_pool_data():
    # language=fift
    d = load_data()
    code = d["pool_code"]
    data = d["pool_data"]
    config = d["config"]
    c7 = C7(global_config=config)

    t = TVM(code=code, data=data, log_level=10)
    t.set_c7(c7)
    t.set_stack([method_name_to_id("get_pool_full_data")])
    final_stack = t.run(unpack_stack=True)
    print(final_stack)

    print(t.success, t.exit_code)
    assert t.success is True
    assert t.exit_code == -1
