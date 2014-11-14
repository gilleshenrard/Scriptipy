class scriptable :
    """Defines basic characteristics, such as name and comment.
    Can't be instanciated.
    Defined by a name and a comment"""
    
    def __init__(self):
        self._name = ""
        self._comment = ""
    
    def __init__(self, name):
        self._name = name
        self._comment = ""
    
    def __init__(self, name, comment):
        self._name = name
        self._comment = comment

    def _set_name(self, name):
        self._name = name

    def _get_name(self):
        return self.name

    def _set_comment(self, comment):
        self._comment = comment

    def __str__(self):
        return self._comment

    def __del__(self):
        """Just to check when the item is deleted"""
        print("item {} deleted".format(self._name))

    Name = property(_set_name, _get_name)
    Comment = property(_set_comment, __str__)
