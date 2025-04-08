class LogLineIterator:
    def __init__(self, filepath):
        self.file = open(filepath, 'r')

    def __iter__(self):
        return self

    def __next__(self):
        line = self.file.readline()
        if line == '':
            self.file.close()
            raise StopIteration
        return line.strip()

def process_logs(filepath):
    error_count = 0
    error_lines = []

    iterator = LogLineIterator(filepath)

    for line in iterator:
        if "ERROR" in line:  
            error_count += 1
            error_lines.append(line)

    print(f"Liczba błędów: {error_count}")
    print("Linie z błędami:")
    for error in error_lines:
        print(error)

if __name__ == "__main__":
    filepath = "log.txt"
    process_logs(filepath)

