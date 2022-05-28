# copyfile() = copies contents of a file
# copy() = copyfile() + permission mode + destination can be a directory
# copy2() = copy() + copies metadata (file's creation and modification times)

import shutil

# copyfile(src,destination)
# copy(src,destination)
# copy2(src,destination)

shutil.copyfile('./assets/text2.txt','./assets/copy.txt')