from glob import glob 
import os 
from tqdm.auto import tqdm



if __name__ == "__main__":
    cur_dir = os.path.dirname(__file__)
    index_files_old = glob(os.path.join(cur_dir, "**/_index.md"), recursive=True)
    
    for index_file in tqdm(index_files_old):
        # change from _index.md to index.md
        new_index_file = index_file.replace("_index.md", "index.md")
        os.rename(index_file, new_index_file)
        