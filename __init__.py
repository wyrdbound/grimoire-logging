"""Grimoire Logging Package.

Flexible logging utilities with dependency injection support for the Grimoire engine.

This package provides a clean, dependency-injectable logging system that supports:
- Thread-safe logger injection and management
- Protocol-based design for easy extensibility
- Fallback to standard Python logging
- Zero-dependency core with optional integrations

Example usage:
    >>> from grimoire_logging import get_logger, inject_logger
    >>> 
    >>> # Use standard logging
    >>> logger = get_logger(__name__)
    >>> logger.info("Hello, world!")
    >>> 
    >>> # Inject custom logger
    >>> class MyLogger:
    ...     def info(self, msg: str) -> None:
    ...         print(f"INFO: {msg}")
    >>> 
    >>> inject_logger(MyLogger())
    >>> logger.info("Now using custom logger!")
"""

from .logging import (
    LoggerProtocol,
    clear_logger_injection,
    get_logger,
    inject_logger,
)

__version__ = "0.1.0"
__author__ = "The Wyrd One"
__email__ = "wyrdbound@proton.me"

__all__ = [
    # Main functions
    "get_logger",
    "inject_logger",
    "clear_logger_injection",
    # Protocols
    "LoggerProtocol",
    # Metadata
    "__version__",
]
