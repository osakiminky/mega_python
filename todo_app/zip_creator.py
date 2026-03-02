#Import the zipfile and pathlib libraries to use their features
import zipfile
import pathlib

#Create a function that iterates over each file and creates a function for each
def make_archive(filepaths, dest_dir):

    #Use the pathlib library to create a destination path
    dest_path = pathlib.Path(dest_dir, "compressed.zip")

    #To create a new zip file specify the zipfile function and the dest_dir path
    #To extract an existing zipfile we specify 'r'
    with zipfile.ZipFile(dest_path, 'w') as archive:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            archive.write(filepath, arcname=filepath.name)

#To test the function i.e. if this script is executed as the main script then we want to call the function
if __name__ == '__main__':

    #Create a test dest directory and 2 test files to test if the function works
    make_archive(filepaths=["compress.py", "test2.py"], dest_dir="dest")