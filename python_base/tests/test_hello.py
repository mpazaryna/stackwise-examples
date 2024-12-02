import pytest

from src.hello import GreetingService


def test_greeting_with_name():
    """Test greeting generation with a specific name."""
    service = GreetingService()
    result = service.create_greeting("Alice")
    assert result == "Hello, Alice!"


def test_greeting_without_name():
    """Test default greeting generation."""
    service = GreetingService()
    result = service.create_greeting()
    assert result == "Hello, World!"


def test_greeting_with_custom_default():
    """Test greeting with custom default greeting."""
    service = GreetingService(default_greeting="Hi")
    result = service.create_greeting("Bob")
    assert result == "Hi, Bob!"
