'''
This is a PEB file rotation code. Which writes its output to a (input_file)_output.peb file.
'''
import os
import re

def file_2_datastream(file_path):
    """
        Function to read peb image file and get image stream from it.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"{file_path} was not found or is a directory")
    with open(file_path,"r") as FH:
        data_list = re.sub(r"#.*","",FH.read()).split("\n") # Reading file & removing comments.
        data = [d.strip() for d in data_list if d != ""] # filtering empty lines and wide spaces.
    if len(data)>=2:
        if data[0].lower() != "p1":
            raise Exception("File format is incorrect!\n(Hint : file format not found to be P1)")
        xy = data[1].split(" ")
        if len(xy) != 2 :
            raise Exception("File format is incorrect!\n(Hint : dimension not found)")
        else:
            try:
                x= int(xy[0])
                y= int(xy[1])
            except:
                raise Exception("File format is incorrect!\n(Hint : dimension are not integers)")
    else:
        raise Exception("File format is incorrect!")
    if len(data) == 2:
        return data
    data_stream = [a for a in ' '.join(data[2:]) if a !=' ']
    if len(data_stream) != x*y:
         raise Exception("File format is incorrect!\n(Hint : dimension mismatch)")
    else:
        print("File validated successfully..!")
    
    return data_stream, x, y

def split_data_stream(data_stream, x):
    """
        Function to split image stream data list into multiple sub lists.
    """
    op = []
    for i in range(0, len(data_stream), x):
        op.append(data_stream[i:i + x])
    return op

def apply_rotation(data_2d, n):
    """
        Function to rotate 2d array by any number of times.
    """
    new_x = len(data_2d)-1 # new number of columns 
    new_y = len(data_2d[0])-1 # new number of rows
    if n == 0:
        return data_2d
    elif n<0: # counterclockwise rotation
        op = [[0 for x in range(new_x+1)] for y in range(new_y+1)] 
        for row_idx,row in enumerate(data_2d):
            for column_idx,value in enumerate(row[::-1]):
                op[column_idx][row_idx]=value
        n = n+1
    elif n>0: # clockwise rotation
        op = [[0 for x in range(new_x+1)] for y in range(new_y+1)] 
        for row_idx,row in enumerate(data_2d):
            for column_idx,value in enumerate(row):
                op[column_idx][new_x-row_idx]=value
        n = n-1
    return apply_rotation(op, n)

def store_to_file(file_path,data_stream_2d):
    """
        Function to write output file
    """
    new_path_dir = os.path.split(file_path)[0]
    new_name = os.path.split(file_path)[1].split(".")[0]+"_output."+os.path.split(file_path)[1].split(".")[-1]
    to_write_str = f"P1\n{len(data_stream_2d[0])} {len(data_stream_2d)}\n"
    for row in data_stream_2d:
        to_write_str += " ".join(row)+"\n"
    with open(os.path.join(new_path_dir,new_name),"w") as FH:
        FH.write(to_write_str)

def main():

    # getting user inputs
    path = input("Please enter path to peb file : ")
    degrees_of_rotation = input('''please enter degrees of rotation 
    (Degrees of rotation are rounded off to closest multiple of 90 
    eg 45degrees~=90 and 44degrees~=0) -ve means counterclockwise & +ve means clockwise : ''')

    # calculating number of rotations
    n = round(float(degrees_of_rotation)/90)
    data_stream, x, y = file_2_datastream(path) # x-> number of columns and y -> number of rows

    # generating 2d array for image
    data_2d = split_data_stream(data_stream,x)
    print("Input Image ",*data_2d,sep="\n")

    # applying rotation
    new_data_stream = apply_rotation(data_2d, n)
    print("output Image ",*new_data_stream,sep="\n")

    # Storing output data to new peb file
    store_to_file(path,new_data_stream)

if __name__ == "__main__":
    main()
