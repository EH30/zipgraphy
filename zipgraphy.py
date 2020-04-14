import argparse
import zipfile


def check_zip(name):
    valid = ["zip", "rar"]
    try:
        if name[len(name)-3:] in valid:
            return True
    except TypeError:
        print("[-]ERROR Type python -h for help")
        print("[+]File hiding Example: python python zipgraphy.py -z Secret_files.zip -p NormalImage.jpg -o hidden_in_Image.jpg")
        print("[+]Extacting the hidden Files From Image Example: python zipgraphy.py -u hidden_in_Image -o /Desktop/Output_Folder")

    return False



def getData(filename):
    with zipfile.ZipFile(filename, "r") as zipped:
        zipped.extractall()
    


def hideFile(image, zipped, output):
    opnr_image = open(image, "rb")
    data_image = opnr_image.read()
    opnr_image.close()
    
    opnr_zip = open(zipped, "rb")
    data_zip = opnr_zip.read()
    opnr_zip.close()

    opnr_write = open(output, "ab+")
    opnr_write.write(data_image)
    opnr_write.write(data_zip)
    opnr_write.close()



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="""You're Files must be zipped    
    [+]File hiding Example: python python zipgraphy.py -z Secret_files.zip -p NormalImage.jpg -o hidden_in_Image.jpg    
    [+]Extacting the hidden Files From Image Example: python zipgraphy.py -u hidden_in_Image""")
    parser.add_argument("-z", type=str, help="Enter You're ZipFile Example: Secret_file.zip")
    parser.add_argument("-p", type=str, help="Enter You're Image Example: Image.jpg")
    parser.add_argument("-u", type=str, help="Enter You're the image that has hidden files Example: hidden_in_Image.jpg")
    parser.add_argument("-o", type=str, help="Enter You're OutPut File Name Example: hidden_in_Image.jpg")
    
    args = parser.parse_args()

    
    try:
        if args.u != None and args.z == None and args.p == None and args.o == None:
            getData(args.u, args.o) 
        elif args.z != None and args.p != None and args.o != None and check_zip(args.z):
            hideFile(args.p, args.z, args.o)
        else:
            print("[-]ERROR Type python -h for help")
            print("[+]File hiding Example: python python zipgraphy.py -z Secret_files.zip -p NormalImage.jpg -o hidden_in_Image.jpg")
            print("[+]Extacting the hidden Files From Image Example: python zipgraphy.py -u hidden_in_Image -o /Desktop/Output_Folder")
    
    except TabError:
        print("[-]ERROR Type python -h for help")
        print("[+]File hiding Example: python python zipgraphy.py -z Secret_files.zip -p NormalImage.jpg -o hidden_in_Image.jpg")
        print("[+]Extacting the hidden Files From Image Example: python zipgraphy.py -u hidden_in_Image -o /Desktop/Output_Folder")