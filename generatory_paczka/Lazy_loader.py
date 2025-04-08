import os

def lazy_loader(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            path = os.path.join(folder_path, filename)
            with open(path, 'r', encoding='utf-8') as file:
                first_line = next(file, '').strip()
                yield first_line


for line in lazy_loader(r"C:\Users\USER\jpwp\generatory_paczka\teksty"):
    print (line)
    
    
    