from pathlib import Path

path = Path("cats_file.txt")
path.write_text("60b90c1c13067a15887e1ae1,Tayson,3\n60b90c2413067a15887e1ae2,Vika,1\n60b90c2e13067a15887e1ae3,Barsik,2\n60b90c3b13067a15887e1ae4,Simon,12\n60b90c4613067a15887e1ae5,Tessi,5")


def get_cats_info(path):
    cats_info = []
    try:
        with open(path, "r", encoding="utf_8") as file:
            for line in file:
                cat_id, name, age = line.split(',')
                cat_info = {"id": cat_id,"name": name,"age": int(age)}
                cats_info.append(cat_info)    
    except FileNotFoundError:
        print(f"File '{path}' not found.")
        return None            
    return cats_info 

    
cats_info = get_cats_info(path)
print(cats_info)
