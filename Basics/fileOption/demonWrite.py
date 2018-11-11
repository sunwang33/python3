# #!/usr/bin/env python
# #-*- coding：utf-8 -*-
# # @Time    ：2018/11/11 14:24
# # @Author  ：SunWang
# # @File    ：demonWrite.py
# if __name__ == '__main__':
#     filename = input("Please input the name of file: ")
#     f = open(filename, "w")
#     while 1:  #此处写1的话，效率最高。
#         context =  input("please input context('EOF' will close file.): ")
#         if  context == "EOF":
#             f.close()
#             #exit(1)
#             break
#         else:
#             f.write(context)
#             f.write("\n")
#
#     fRead = open(filename)
#     readContext = fRead.read()
#     print("####################start################")
#     print(readContext)
#     print("#####################end#################")
#     fRead.close()
filename = input("please input the name of file: ")
fWrite = open(filename , "w")
while 1:
    filecontext = input("Please input the context of this file('EOF' is exit.): ")
    if filecontext == "EOF":
        break
    else:
        fWrite.write(filecontext)
        fWrite.write("\n")
fWrite.close()

fRead = open(filename, "r")
readcontext=fRead.read()
print("###################start######################")
print(readcontext)
print("####################end#######################")
fRead.close()