
name = input('请输入要备份文件的名字')
p = name.rfind('.')
s = name[:p]
e = name[p:]
newname = s+'备份'+e
f = open('8.txt','r')
f1 = open(newname,'w')
while True:
	content = f.read(1024)
	f1.write(content)
	if len(content) == 0:
		break
#把8.txt内容写入到9.txt里


f1.close()

f.close()




















