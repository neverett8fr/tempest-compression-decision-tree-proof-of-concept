import os
import gzip
import lzma
import shutil
import csv


def calculate_compression_ratio(in_size, out_size):
    # could pass in file and do something like: `size = os.path.getsize(file)`
    ratio = (1 - (out_size / in_size))  # * 100

    return ratio


def append_to_csv(path, data):
    with open(path, mode='a', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(data)
        # new_data = ['John', 'Doe', '42']


def delete_file(path):
    os.remove(path)


def get_file_count(path):
    num_files = len([f for f in os.listdir(path)
                    if os.path.isfile(os.path.join(path, f))])
    return num_files


def get_file_size(path):
    return os.path.getsize(path) * 8


def get_file_as_bytes(path):
    with open(path, "rb") as f:
        file_data = f.read()
    return file_data


def compress_gzip(in_dir, out_dir, path):
    with open(in_dir+path, 'rb') as f_in, gzip.open(out_dir+path, 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)


def compress_lzw(in_path, out_path):
    with open(in_path, 'rb') as f_in, lzma.open(out_path, 'wb') as f_out:
        data = f_in.read()
        compressed = lzma.compress(data)
        f_out.write(compressed)


def compress_rle(file_in, file_out):
    with open(file_in, 'rb') as f_in:
        data = f_in.read()

    count = 1
    last_byte = data[0]
    compressed_data = bytearray()

    for byte in data[1:]:
        if byte == last_byte and count < 255:
            count += 1
        else:
            compressed_data.append(count)
            compressed_data.append(last_byte)
            count = 1
            last_byte = byte

    compressed_data.append(count)
    compressed_data.append(last_byte)

    with open(file_out, 'wb') as f_out:
        f_out.write(compressed_data)


png_count = get_file_count("files_to_compress/png")
jpg_count = get_file_count("files_to_compress/jpg")
txt_count = get_file_count("files_to_compress/txt")

for png in range(1, png_count - 1, 1):
    original_size = get_file_size("files_to_compress/png/"+str(png)+".png")
    compress_gzip("files_to_compress/png/",
                  "files_compressed/png/",
                  str(png)+".png")
    compressed_size = get_file_size("files_compressed/png/"+str(png)+".png")
    delete_file("files_compressed/png/"+str(png)+".png")
    ratio = calculate_compression_ratio(original_size, compressed_size)
    new_entry = [2, original_size, 1, compressed_size, ratio]
    append_to_csv("results/results.csv", new_entry)
    print(new_entry)

    original_size = get_file_size("files_to_compress/png/"+str(png)+".png")
    compress_rle("files_to_compress/png/"+str(png)+".png",
                 "files_compressed/png/"+str(png)+".png")
    compressed_size = get_file_size("files_compressed/png/"+str(png)+".png")
    delete_file("files_compressed/png/"+str(png)+".png")
    ratio = calculate_compression_ratio(original_size, compressed_size)
    new_entry = [2, original_size, 2, compressed_size, ratio]
    append_to_csv("results/results.csv", new_entry)
    print(new_entry)

    original_size = get_file_size("files_to_compress/png/"+str(png)+".png")
    compress_lzw("files_to_compress/png/"+str(png)+".png",
                 "files_compressed/png/"+str(png)+".png")
    compressed_size = get_file_size("files_compressed/png/"+str(png)+".png")
    delete_file("files_compressed/png/"+str(png)+".png")
    ratio = calculate_compression_ratio(original_size, compressed_size)
    new_entry = [2, original_size, 3, compressed_size, ratio]
    append_to_csv("results/results.csv", new_entry)
    print(new_entry)


for jpg in range(1, jpg_count - 1, 1):
    original_size = get_file_size("files_to_compress/jpg/"+str(jpg)+".jpg")
    compress_gzip("files_to_compress/jpg/",
                  "files_compressed/jpg/",
                  str(jpg)+".jpg")
    compressed_size = get_file_size("files_compressed/jpg/"+str(jpg)+".jpg")
    delete_file("files_compressed/jpg/"+str(jpg)+".jpg")
    ratio = calculate_compression_ratio(original_size, compressed_size)
    new_entry = [3, original_size, 1, compressed_size, ratio]
    append_to_csv("results/results.csv", new_entry)
    print(new_entry)

    original_size = get_file_size("files_to_compress/jpg/"+str(jpg)+".jpg")
    compress_rle("files_to_compress/jpg/"+str(jpg)+".jpg",
                 "files_compressed/jpg/"+str(jpg)+".jpg")
    compressed_size = get_file_size("files_compressed/jpg/"+str(jpg)+".jpg")
    delete_file("files_compressed/jpg/"+str(jpg)+".jpg")
    ratio = calculate_compression_ratio(original_size, compressed_size)
    new_entry = [3, original_size, 2, compressed_size, ratio]
    append_to_csv("results/results.csv", new_entry)
    print(new_entry)

    original_size = get_file_size("files_to_compress/jpg/"+str(jpg)+".jpg")
    compress_lzw("files_to_compress/jpg/"+str(jpg)+".jpg",
                 "files_compressed/jpg/"+str(jpg)+".jpg")
    compressed_size = get_file_size("files_compressed/jpg/"+str(jpg)+".jpg")
    delete_file("files_compressed/jpg/"+str(jpg)+".jpg")
    ratio = calculate_compression_ratio(original_size, compressed_size)
    new_entry = [3, original_size, 3, compressed_size, ratio]
    append_to_csv("results/results.csv", new_entry)
    print(new_entry)


for txt in range(1, txt_count - 1, 1):
    original_size = get_file_size("files_to_compress/txt/"+str(txt)+".txt")
    compress_gzip("files_to_compress/txt/",
                  "files_compressed/txt/",
                  str(txt)+".txt")
    compressed_size = get_file_size("files_compressed/txt/"+str(txt)+".txt")
    delete_file("files_compressed/txt/"+str(txt)+".txt")
    ratio = calculate_compression_ratio(original_size, compressed_size)
    new_entry = [1, original_size, 1, compressed_size, ratio]
    append_to_csv("results/results.csv", new_entry)
    print(new_entry)

    original_size = get_file_size("files_to_compress/txt/"+str(txt)+".txt")
    compress_rle("files_to_compress/txt/"+str(txt)+".txt",
                 "files_compressed/txt/"+str(txt)+".txt")
    compressed_size = get_file_size("files_compressed/txt/"+str(txt)+".txt")
    delete_file("files_compressed/txt/"+str(txt)+".txt")
    ratio = calculate_compression_ratio(original_size, compressed_size)
    new_entry = [1, original_size, 2, compressed_size, ratio]
    append_to_csv("results/results.csv", new_entry)
    print(new_entry)

    original_size = get_file_size("files_to_compress/txt/"+str(txt)+".txt")
    compress_lzw("files_to_compress/txt/"+str(txt)+".txt",
                 "files_compressed/txt/"+str(txt)+".txt")
    compressed_size = get_file_size("files_compressed/txt/"+str(txt)+".txt")
    delete_file("files_compressed/txt/"+str(txt)+".txt")
    ratio = calculate_compression_ratio(original_size, compressed_size)
    new_entry = [1, original_size, 3, compressed_size, ratio]
    append_to_csv("results/results.csv", new_entry)
    print(new_entry)
