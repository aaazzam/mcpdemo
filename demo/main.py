# server.py
from fastmcp import FastMCP

mcp = FastMCP("Demofffffffffffff!fffffffffasfaffsfsfffffff!fffffffff!!! 🚀")


@mcp.tool()
def mod(a: int, b: int) -> int:
    """Modulo two numbers."""
    return a % b


@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers. Hi jake!"""
    return a + b


@mcp.tool()
def subtract(a: int, b: int) -> int:
    """Subtract two numbers"""
    return a - b


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


@mcp.tool()
def cube(a: int) -> int:
    """Cube a number"""
    return a * a * a


if __name__ == "__main__":
    mcp.run()
