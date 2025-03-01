"""
Package for analyzing Nginx logs.

This package provides tools for parsing Nginx logs,
generating statistical reports, and running a FastAPI service.
"""

from .analyzer import generate_report
from .models import LogEntry
from .parser import parse_log_file

__all__ = ["generate_report", "LogEntry", "parse_log_file"]
