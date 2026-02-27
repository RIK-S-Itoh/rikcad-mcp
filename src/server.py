from fastmcp import FastMCP
from tools import custom_tools, register_tapir

# --- RIKCAD 13 対応用モンキーパッチ ---
try:
    from archicad.commands import BasicCommands
    _original_GetProductInfo = BasicCommands.GetProductInfo

    def _patched_GetProductInfo(self):
        version, build, lang = _original_GetProductInfo(self)
        # RIKCAD 13 はバージョン 13 を返すため、Archicadライブラリの制限(24以上)を回避するため29に偽装する
        if version < 24:
            return 29, build, lang
        return version, build, lang

    BasicCommands.GetProductInfo = _patched_GetProductInfo
except ImportError:
    pass
# --------------------------------------

mcp = FastMCP("rikcad-mcp")

custom_tools.init_tools(mcp)
register_tapir.init_tapir(mcp)

if __name__ == "__main__":
    mcp.run()
