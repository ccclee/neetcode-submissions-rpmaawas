class PrefixTree:

    def __init__(self):
        self.prefixset = set()
        

    def insert(self, word: str) -> None:
        self.prefixset.add(word)


    def search(self, word: str) -> bool:
        return word in self.prefixset
        

    def startsWith(self, prefix: str) -> bool:
        prefixlist = list(self.prefixset)
        for word in prefixlist:
            if len(word)>= len(prefix) and word[:len(prefix)] == prefix:
                return True

        return False

        
        