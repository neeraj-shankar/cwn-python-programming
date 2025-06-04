class HashTableImplementation:

    def __init__(self, size=8):
        self.size = size
        self.table = [None] * self.size

    def _hash(self, key):

        return hash(key) % self.size

    def insert(self, key, value):
        print("I am being called..........")
        index = self._hash(key)
        start_index = index

        # Keep looking for empty index to place new bucket
        while self.table[index] is not None:

            # incase index is found, update the bucket with value
            k, _ = self.table[index]
            if k == key:
                self.table[index] = (key, value)
                return

            index = (index + 1) % self.size

        # finally add new key value pair to new index
        self.table[index] = (key, value)
        print(f"Inserted Key: {key} and Value: {value} at bucket: {index}")

    def display(self):

        for idx, item in enumerate(self.table):
            print(f"{idx}: {item}")



hti = HashTableImplementation()
print("Object create and its being called")
hti.insert("Name", "Neeraj")
hti.insert("Test", "Rajbhaan")
hti.display()
