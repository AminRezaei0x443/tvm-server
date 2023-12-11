from tonpy.types import Stack, CellSlice, Cell

Entry = int | CellSlice | Cell | list["Entry"] | None


def entry_to_json(entry: Entry):
    if isinstance(entry, list):
        d = []
        for e in entry:
            d.append(entry_to_json(e))
        return {"type": "tuple", "tuple": d}
    if isinstance(entry, int):
        return {"type": "int", "num": str(entry)}
    if isinstance(entry, Cell):
        return {"type": "cell", "cell": entry.to_boc()}
    if isinstance(entry, CellSlice):
        return {"type": "cell", "cell": entry.to_boc()}
    if entry is None:
        return {"type": "null"}
    raise NotImplementedError("entry_to_json:", type(entry))


def stack_to_json(stack: Stack) -> list:
    sl = stack.unpack_rec()
    return entry_to_json(sl)["tuple"]
