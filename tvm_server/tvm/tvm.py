from dataclasses import dataclass
from tonpy.types import Cell, Stack
from tonpy.tvm import TVM, C7, method_name_to_id

from tvm_server.tvm.util import stack_to_json


@dataclass
class GetMethodResult:
    ok: bool
    exit_code: int
    stack: Stack

    def to_json(self):
        return {
            "ok": self.ok,
            "exit_code": self.exit_code,
            "stack": stack_to_json(self.stack)
        }


def run_get_method(code: Cell, data: Cell, method: str, stack: Stack | None = None, config: Cell | None = None) -> GetMethodResult:
    t = TVM(code=code, data=data)
    if config is not None:
        c7 = C7(global_config=config)
        t.set_c7(c7)
    ds = []
    if stack is not None:
        ds = stack.unpack_rec()
    t.set_stack([method_name_to_id(method), *ds])
    final_stack = t.run(unpack_stack=False)
    res = GetMethodResult(t.success, t.exit_code, final_stack)
    return res
