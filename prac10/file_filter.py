
# Write a program that reads a file and "filters" it, writing only certain lines to another file

in_file = open("read_file_chess.txt", 'r')
out_file = open("write_file_chess.txt", 'w')
for line in in_file:
    if 'knight' in line or 'bishop' in line:
        out_file.write(line)
    else:
        pass
in_file.close()
out_file.close()
print("Done.")


# Extensions (Optional)

in_file2 = open("transcript.txt", 'r')
out_file2 = open("transcript_write.txt", 'w')
for line in in_file2:
    if line.startswith("So"):
        out_file2.write(line)
    else:
        pass
in_file2.close()
out_file2.close()
print("Done2.")