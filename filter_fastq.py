import sys


def is_a_number(input):
    try:
        float(input)
        return True
    except ValueError:
        return False


keep_filtered = False
min_length = 0
gc_low = 0
gc_high = 100
output_base_name = ''
if len(sys.argv) == 2:
    file_name = sys.argv[1]
else:
    i = 1
    while i < len(sys.argv) - 1:
        if sys.argv[i] == '--min_length':
            min_length = sys.argv[i+1]
            i += 2
        elif sys.argv[i] == '--keep_filtered':
            keep_filtered = True
            i += 1
        elif sys.argv[i] == '--gc_bounds':
            if is_a_number(sys.argv[i+1]):
                gc_low = float(sys.argv[i+1])
                if is_a_number(sys.argv[i+2]):
                    gc_high = float(sys.argv[i+2])
                    i += 3
                else:
                    i += 2
            else:
                i += 1
        elif sys.argv[i] == '--output_base_name':
            output_base_name = sys.argv[i+1]
            i += 2
    file_name = sys.argv[len(sys.argv) - 1]
if output_base_name == '':
    file_name_list = [x for x in file_name]
    output_base_name = ''.join(file_name_list[0: len(file_name_list) - 6])
print(f"Launch status: File name: {file_name}, keep filtered: {keep_filtered}, min length = {min_length}, GC min = {gc_low}, GC max = {gc_high}, output base name: {output_base_name}")
