class AttrDisplay:
    """
    Provides an inheritable print overload method that displays
    instances with their class names and a name=value pair for
    each attribute stored on the instance itself (but not attrs
    inherited from its classes). Can be mixed into any class,
    and will work on any instance.
    """

    def gatherAttr(self):
        """ Gathers all attributes of the passed instance"""
        attrs = []

        for key, val in sorted(self.__dict__.items()):
            attrs.append(f'{key} = {val}')
        # for key in sorted(self.__dict__):
        #     #'__dict__' contains all attributes of object
        #     attrs.append(f'{key} = {getattr(self, key)}')
        return ', '.join(attrs)

    def __str__(self):
        return f'[{self.__class__.__name__} : {self.gatherAttr()}]'

