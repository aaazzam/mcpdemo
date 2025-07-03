# server.py
from fastmcp import FastMCP
import math
from dataclasses import dataclass
from datetime import datetime
from fastmcp.context import Context

mcp = FastMCP("Demo! 🚀", stateless_http=True)


@dataclass
class Person:
    name: str


@mcp.tool
async def ask_for_name(context: Context) -> str:
    """Ask for user's name using elicitation"""
    print("before elicit")
    result = await context.elicit(
        message="What is your name?",
        response_type=Person,
    )
    print("after elicit")
    if result.action == "accept":
        return f"Hello, {result.data.name}!"
    else:
        return "No name provided."


@mcp.tool()
def multiply(a: int, b: int) -> int:
    """Multiply two numbers"""
    return a * b


@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


@mcp.tool()
def square(a: int) -> int:
    """Square a number"""
    return a * a


@mcp.tool()
def cube(a: int) -> int:
    """Cube a number!"""
    return a * a * a


@mcp.tool()
def square_root(a: int) -> float:
    """Square root of a number"""
    return a ** (1 / 3)


@mcp.tool()
def cube_root(a: int) -> float:
    """Cube root of a number"""
    return a ** (1 / 3)


if __name__ == "__main__":
    mcp.run()
#
