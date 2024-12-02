from typing import Optional


class GreetingService:
    """Service for generating personalized greetings."""

    def __init__(self, default_greeting: str = "Hello") -> None:
        """
        Initialize the greeting service.

        Args:
            default_greeting: The default greeting to use when none is specified
        """
        self.default_greeting = default_greeting

    def create_greeting(self, name: Optional[str] = None) -> str:
        """
        Create a personalized greeting message.

        Args:
            name: Optional name to personalize the greeting

        Returns:
            A formatted greeting string
        """
        if name:
            return f"{self.default_greeting}, {name}!"
        return f"{self.default_greeting}, World!"
