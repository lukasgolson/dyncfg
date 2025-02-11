import logging
from pathlib import Path

logger = logging.getLogger(__name__)


class ConfigValue(str):
    """A subclass of str that provides additional methods for type conversion and default handling.

    Attributes:
        parent (DynamicConfig): The parent configuration instance.
        section (str): The section name in the configuration.
        key (str): The key name in the section.
    """

    def __new__(cls, value: str, parent=None, section: str = None, key: str = None):
        obj = super(ConfigValue, cls).__new__(cls, value)
        obj.parent = parent
        obj.section = section
        obj.key = key
        return obj

    def or_default(self, default_value, update: bool = True) -> "ConfigValue":
        """Return the value if non-empty; otherwise, return and optionally update with default_value."""
        if self:
            return self  # Return current non-empty value.

        if update and self.parent and self.section and self.key:
            with self.parent._lock:
                self.parent.config.set(self.section, self.key, str(default_value))
                if self.parent.auto_write:
                    self.parent._write_config()
        return ConfigValue(str(default_value), self.parent, self.section, self.key)

    def log(self) -> "ConfigValue":
        """Log the configuration value."""
        logger.info(f"[{self.section}] {self.key} = {self}")
        return self

    def as_int(self, default: int = 0) -> int:
        """Convert the value to an integer, or return a default value if conversion fails."""
        try:
            return int(self)
        except ValueError:
            return default

    def as_float(self, default: float = 0.0) -> float:
        """Convert the value to a float, or return a default value if conversion fails."""
        try:
            return float(self)
        except ValueError:
            return default

    def as_bool(self, default: bool = False) -> bool:
        """Convert the value to a boolean, or return a default value if conversion fails."""
        val = self.lower()
        if val in ("true", "yes", "1"):
            return True
        elif val in ("false", "no", "0"):
            return False
        return default

    def as_path(self) -> Path:
        """Convert the value to a path"""
        val = Path(self)

        return val

    def as_list(self, separator: str = ",") -> "ConfigValueList":
        """
        Convert the string value into a ConfigValueList by splitting on the given separator.

        Args:
            separator (str): The delimiter to use for splitting the string. Defaults to a comma.

        Returns:
            ConfigValueList: A list-like wrapper of ConfigValue objects.
        """
        from config_value_list import ConfigValueList

        values = [
            ConfigValue(item.strip(), self.parent, self.section, self.key)
            for item in self.split(separator)
        ]
        return ConfigValueList(values)
