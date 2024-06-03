import pydicom
import matplotlib.pyplot as plt
import os

DIR_PATH = "dicom/series-000001/"
FILE_NAME = "image-000001.dcm"

def show_tags():
    # Load the DICOM file
    ds = pydicom.dcmread(DIR_PATH + FILE_NAME)

    # Print All
    print (ds)

    # Print some information about the image
    print('Patient Name:', ds.PatientName)
    print('Modality:', ds.Modality)
    print('Image Size:', ds.Rows, 'x', ds.Columns)

    # Show keywords
    print("ds[0x00100010].keyword = ", ds[0x00100010].keyword)
    print("ds[0x00180050].keyword = ", ds[0x00180050].keyword)

    # show single image
    img = ds.pixel_array
    plt.imshow(img)
    plt.show()

def show_tile():
    fig=plt.figure(figsize=(12, 12), facecolor="lightblue")
    fig.suptitle("DICOM FILES")
    columns = 6
    rows = 5
    files = os.listdir(DIR_PATH)
    index = 1
    for file in files:
        filename = DIR_PATH + "/" + file
        ds = pydicom.dcmread(filename)
        i_graph = fig.add_subplot(rows, columns, index)
        i_graph.set_title(index)
        i_graph.set_xticks([0, 500])
        i_graph.set_yticks([0, 500])
        plt.imshow(ds.pixel_array)
        index = index + 1
        if index > (columns * rows):
            break
    plt.show()

if __name__ == "__main__":
    show_tile()