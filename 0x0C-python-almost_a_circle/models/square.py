from models.rectangle import Rectangle

class Square(Rectangle):
    """A Square class that inherits from Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square.

        Args:
            size (int): The size of the new Square.
            x (int): The x coordinate of the new Square.
            y (int): The y coordinate of the new Square.
            id (int): The identity of the new Square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get size of the Square."""
        return self.width

    @size.setter
    def size(self, value):
        """Set size of the Square."""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the Square attributes.

        Args:
            *args (ints): New attribute values.
                - 1st argument represents id attribute
                - 2nd // // size attribute
                - 3rd // // x attribute
                - 4th // // y attribute
            **kwargs (dict): New key/value pairs of attributes.
        """
        attrs = ["id", "size", "x", "y"]
        if args and len(args) != 0:
            for i, arg in enumerate(args):
                setattr(self, attrs[i], arg)
        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        """Return the dictionary rep of the Square."""
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}

    def __str__(self):
        """Return the string rep of the Square."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

