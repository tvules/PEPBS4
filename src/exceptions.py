class ParsingException(Exception):
    pass


class TagException(ParsingException):
    pass


class ParserFindTagException(TagException):
    pass


class TagAttributeException(TagException):
    pass
