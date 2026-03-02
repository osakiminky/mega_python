#Import and install the zipfile module & libraries
import zipfile

#Create function
def extract_archive(archivepath, dest_dir):
    #To create a zipfile we use Write argument.
    #To read the contents of a zipfile we use Read argument
    with zipfile.ZipFile(archivepath, 'r') as archive:
        archive.extractall(dest_dir)

#To test the function, specify the absolute path of the compressed file & the test dest dir
if __name__ == "__main__":
    extract_archive("/Users/king/Desktop/PythonXYZ/archiveapp/compressed.zip",
                    "/Users/king/Desktop/PythonXYZ/archiveapp/files")