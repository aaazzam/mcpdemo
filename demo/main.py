# server.py
from fastmcp import FastMCP

mcp = FastMCP("ffffDemo!!!!sf@!!! 🚀")


@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


if __name__ == "__main__":
    mcp.run()
