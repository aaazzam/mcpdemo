# server.py
from fastmcp import FastMCP

mcp = FastMCP("Demo!!!sfs!@!!! 🚀")


@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


if __name__ == "__main__":
    mcp.run()
