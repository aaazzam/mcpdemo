# server.py
from fastmcp import FastMCP, Context
import math
from dataclasses import dataclass
from datetime import datetime

mcp = FastMCP("Demo!!!!!! 🚀")


@mcp.tool()
def multiply(a: int, b: int) -> int:
    """Multiply two numbers"""
    return a * b
