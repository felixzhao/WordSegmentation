
## need python 3

infile_path = "_Dict-SC2TC.Sort.V1_Simple_Chinese.txt"
outfile_path = "_Dict-SC2TC.Sort.V1_Simple_Chinese_UTF8"

## utf 8 to gbk2312
#open and encode the original content
file_source = open(infile_path, mode='r', encoding='gb18030')
file_content = file_source.read()
file_source.close

#write the UTF8 file with the encoded content
file_target = open(outfile_path, mode='w', encoding='utf_8')
file_target.write(file_content)
file_target.close