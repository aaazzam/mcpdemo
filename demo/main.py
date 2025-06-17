# server.py
from fastmcp import FastMCP

mcp = FastMCP(
    "Demoff!fffffffffffsfffsffffffffffffffffkffffffffasfaffsfsfffffff!fffffffff!!! 🚀"
)


@mcp.tool()
def multiply(a: int, b: int) -> int:
    """Multiply two numbers"""
    return a * b


@mcp.tool()
def divide(a: int, b: int) -> int:
    """Divide two numbers"""
    return a / b


@mcp.tool()
def square(a: int) -> int:
    """Square a number"""
    return a * a


if __name__ == "__main__":
    mcp.run()
#
