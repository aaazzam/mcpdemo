# server.py
from fastmcp import FastMCP, Context
import math
from dataclasses import dataclass
from datetime import datetime

mcp = FastMCP("Demo!!!!!s?!! 🚀")


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
def subtract(a: int, b: int) -> int:
    """Subtract two numbers"""
    return a - b


@mcp.tool()
def divide(a: int, b: int) -> int:
    """Divide two numbers"""
    return a / b


@mcp.tool()
def get_current_time() -> str:
    """Get the current time"""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
