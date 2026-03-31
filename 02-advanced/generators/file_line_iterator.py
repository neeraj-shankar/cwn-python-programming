class FileLineIterator:
    """Iterator that reads file line by line with processing"""
    
    def __init__(self, filename):
        self.filename = filename
        self.file = None
    
    def __iter__(self):
        """Open file and return iterator"""
        self.file = open(self.filename, 'r')
        return self
    
    def __next__(self):
        """Get next line"""
        if self.file is None:
            raise StopIteration
        
        line = self.file.readline()
        
        if not line:  # End of file
            self.file.close()
            raise StopIteration
        
        return line.strip()  # Remove whitespace

# Usage
# for line in FileLineIterator('data.txt'):
#     print(line)