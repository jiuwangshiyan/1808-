name = input('请输入要备份文件的名字')

f = open('8.txt','r')
content = f.read()#content 是读取f.read
print(content)
f.close()


#把8.txt内容写入到9.txt里
p = name.rfind('.')
s = name[ :p]
e = name[p:]
newname = s+'备份'+e


f1 = open(newname,'w')
f1.write(content)
f1.close()





















