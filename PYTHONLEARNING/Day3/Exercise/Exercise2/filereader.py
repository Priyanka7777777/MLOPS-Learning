class filereader:
    def read_file(self, file_path):
        with open(file_path, 'r') as file:
            return file.read()
        
print(filereader().read_file('sample.txt'))

def count_lines(file_path):
        with open(file_path, 'r') as file:
            return len(file.readlines())

print(count_lines('sample.txt'))
def count_words( file_path):
        with open(file_path, 'r') as file:
            content = file.read()
            return len(content.split())
print(count_words('sample.txt'))