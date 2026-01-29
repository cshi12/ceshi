### 简单介绍：
- Linux命令使用：为了将来工作中与服务器设备进行交互而准备的技能
（远程连接/命令的使用）
- 数据库的使用：MySQL（增删改查），除了查询需要重点掌握，其他操作了解即可

---
### 操作系统：
- 是：所有硬件设备组装完成后的第一层软件，能够使用户使用硬件设备的软件即为操作系统。
- 常见分类：
	1. 桌面操作系统：Windows/macOS/Linux
	2. 移动端操作系统：Android(安卓)/iOS（苹果）
	3. 服务器操作系统：Linux/Windows Server
	4. 嵌入式操作系统：Android（底层是Linux）

Windows系统中，有多个顶级目录，即各个盘符，比如C盘等，路径之间的层级关系，使用：\来表示
	D:\data\work\hello.txt
Linux系统中，只有一个顶级目录，称之为根目录，用/表示，路径之间的层次关系，用:/来表示
	/user/local/hello.txt
练习题：请根据语言描述，写出对应的Linux路径
```
在根目录下有一个文件夹test，文件夹内有一个文件hello.txt，请描述文件的路径
/test/hello.txt
在根目录下有一个文件itheima.txt，请描述文件的路径
/itheima.txt
在根目录下有一个文件夹itcast，在itcast文件夹内有文件夹itheima，在itheima文件夹内有文件hello.txt，请描述文件的路径
/itcast/itheima/hello.txt
```
### Linux的文件和路径
![Pasted image 20250720093439.png](./images/Pasted%20image%2020250720093439.png)
### Linux命令的使用技巧
- Linux终端的放大缩小（在虚拟系统里面的终端）
ctrl+shift+=放大终端窗口显示
ctrl+-缩小终端窗口字体显示
- Linux命令的自动补全
在敲除文件/目标/命令的前几个字母之后。按下tab键
- 其他
使用上下方向键，快速获取之前输入过的命令
如果命令开始执行后停不下来，或者不想执行当前选中的命令，按住ctrl+c

#### 命令的基本内容
1. 终端命令格式
![Pasted image 20250719094355.png](./images/Pasted%20image%2020250719094355.png)
command：命令名，相应的功能的英文单词或者缩写，执行基本操作
【-options】：选项，选择命令可以显示更加丰富的数据
【parameter】：参数，命令的操作对象，一般文件，目录和进程等都可以显示更加丰富的数据
2. 查阅命令帮助信息,可以用来查看命令
方法一：--help
```
command--help
```
方法二：man
```
man command
```
#### 常见命令案例一
```
1.查看当前路径位置
	pwd
2.查看当前目录下有哪些文件和文件夹
	ls
3.创建adir,bdir,cdir三个文件夹（创建一个文件夹/创建多个文件夹）
mkdir(是make+directory)
	mkdir adir(可以单个)
	mkdir bdir cdir(也可以多个)
4.切换到adir目标下
	cd ./adir(表示同级，如果两个点表示上一级)，但是同级前面可省略，所以 cd adir
5.创建文件aa（创建文件）
	touch aa
6.切换到root目录下（绝对路径/相对路径）
（不太懂，101集15分钟之前）<--可以看上面文件路径部分理解
	绝对路径：cd /home/first/
	相对路径：cd
7.创建文件file重命名为aa
	创建：touch file
	重命名：mv file aa
8.复制文件aa到adir目录下（要求提示是否覆盖）
	cp -i aa adir(-i是是否覆盖)
9.复制文件夹bdir到cdir目录下
	cp -r bdir/ cdir/(涉及到文件夹的一般都有-r)
10.移动文件aa到bdir目录下(cdir下的bdir)
	mv aa ./cdir/bdir/(./可以省略)
11.创建 bb,cc 两个文件(创建多个文件)
	touch bb cc(空格即可，无需符号分割)
12.删除 bb 文件
	rm -i bb(防止误删，有-i，有提醒)
13.删除 adir 文件夹
	rm -ri adir/
14.删除当前目录下所有文件和文件夹
	rm -rf *
	(rm -rf /* 是删除根目录下所有，一般无权限)
```
ls(列出目录内容)
![Pasted image 20250720163826.png](./images/Pasted%20image%2020250720163826.png)
cd(路径切换)
cd:当前用户的根目录下
cd ~:当前用户的根目录下，特殊强调~：是当前用户家目录的路径信息，例如用户为root，~：/root，用户为admin，~：home/admin
![Pasted image 20250719102132.png](./images/Pasted%20image%2020250719102132.png)
mv（移动或者重命名）
![Pasted image 20250719152419.png](./images/Pasted%20image%2020250719152419.png)
cp(复制)
![Pasted image 20250719203301.png](./images/Pasted%20image%2020250719203301.png)
rm(删除)
![Pasted image 20250719205902.png](./images/Pasted%20image%2020250719205902.png)
### 一般命令，案例二
```
在桌面上打开终端窗口，执行如下操作:
01.将根目录下所有文件的详细信息输出到 demo 文件中(包含隐藏文件)
ls -a(查看所有的包括隐藏文件)
ls -l(以列表形式查看详细信息)
	 ls -al / > demo
02.直接查看 demo 文件的内容
	cat demo
03.将 /usr/bin 目录下所有文件的详细信息追加到 demo 文件中
	ls -al /user/demo >> demo
04.以分屏的形式查看 demo 文件的内容
	less demo
05.查找 demo 文件内容中包含 mysql 的信息
	ls -al /user/bin/ > demo
	grep mysql demo 
	
06.在 /usr/bin目录下所有文件的信息中查找包含mysql的信息
	方法一：(通过文件夹)
		1.ls -al /user/bin/ > demo
		2.grep mysql demo 
	方法二：（通过管道）
		1.ls -al /user/bin/ | grep mysql 
07.清空当前终端窗口中的内容
	clear
```

重定向>,>>
默认是覆盖
![Pasted image 20250720164459.png](./images/Pasted%20image%2020250720164459.png)

cat(查看内容)
![Pasted image 20250720164709.png](./images/Pasted%20image%2020250720164709.png)
cat 文件名1文件名2：将两个文件的额呢绒合并后并显示在终端窗口
注意：只是合并显示内容，并没有真正的合并两个文件

less(分屏查看)
![Pasted image 20250720171343.png](./images/Pasted%20image%2020250720171343.png)
续![Pasted image 20250720171948.png](./images/Pasted%20image%2020250720171948.png)
说明:less,more都常用于查看内容较多的文件信息，用分屏样式展示大量信息，文件内容信息至少能满屏

grep(根据关键词搜索文本内容)

![Pasted image 20250720173859.png](./images/Pasted%20image%2020250720173859.png)
管道 |
一般会和grep等混合使用
![Pasted image 20250720174401.png](./images/Pasted%20image%2020250720174401.png)
### 案例三：
 ```
 在桌面上打开终端窗口，执行如下操作:
01.将根目录下所有文件的详细信息输出到 demo 文件中
	ls -al / > demo
02.查看 demo 文件前 5 行内容
	head -5 demo
03.查看 demo 文件后 5行内容
	tail -5 demo
04.将 ping www.itheima.com 的信息输出到 ping_1og 文件中
	ping www.itheima.com >>ping_log(将不断出现ping结果信息追加写入特定文件中，用于模拟日志文件内容是不断变化的场景)
	cat ping_log
05.重新开启一个终端窗口，动态查看 ping_lpg 文件中的信息
	tail -f ping_log
```
head tail(查找特定位置)
![Pasted image 20250720180707.png](./images/Pasted%20image%2020250720180707.png)
说明：只要目标文件的内容是一直写入的状态，使用tail-f文件名，即可实时监控文件内容变化的操作。
补充：两者叠用：
head -5 demo | tail -2(前五个中的后两个)
### 案例四
```
01.查看当前系统内核版本信息
	cat /proc/vision(不同系统的版本信息查看都是通过查看特定文件内容来获取的，不同系统文件名可能不同)
02.查看当前系统发行版本信息
	cat /etc/redhat-release
03.重启当前系统
	reboot
04.关闭当前系统
	shutdown
	poweroff
```
shutdown关机选项
![Pasted image 20250721155731.png](./images/Pasted%20image%2020250721155731.png)
### 案例五ps/kil/top
```
01.查看当前系统下的进程信息
	ps -aux(PID是进程ID，command是软件程序名称)
2. 手动打开 nmon_x86_64_centos7
	./nmon_x86_64_centos7(在这之前应该先上传该软件)
		如果权限不足：chmod 755 +文件名
03.获取nmon_x86_64_centos7 的进程信息(进程ID)
	ps -aux | grep nmon
04.通过结束nmon_x86_64_centos7进程的方式关闭程序
	kill [-9] 进程id
05.打开当前系统的‘任务管理器'（动态查看进程信息）
	top
```
什么是进程
在任何系统中。运行软件程序时，都会有一个对应的进程存在，如果结束进程，就可以实现关闭对应软件程序的操作。
![Pasted image 20250721162601.png](./images/Pasted%20image%2020250721162601.png)
案例五具体：（我的nmon_x86_4_centos7放置在了/home/first/nmon）
![Pasted image 20250721173007.png](./images/Pasted%20image%2020250721173007.png)


#### 端口号：
- 说明：想要链接到服务器，需要使用ip地址，再想获取在服务器上运行的程序，需要通过端口号
- 注意：同一台服务器中不能有多个程序使用条哦那个一个端口号，因此在运行程序时，如果提示“端口号被占用”，那就需要先找到占用端口号的程序并结束掉，然后才能运行目标程序。
- 常见的端口号：
```
HTTP:80
HTTPS:443
SSH:22
MySQL:3306
```
### 案例六 netstat/lsof
```
01.查看当前系统中开放的端口有哪些
	netstat -anptu
02.查看哪个程序正在使用3306端口（需要root用户权限）
	netstat -anptu | grep mysql
	(配合grep命令过滤信息，获取占用某一端口号的程序名及对应的进程ID，再使用kill命令结束端口占用)
	lsof -i:3306(该命令使用时，-i后跟的信息中不能包含空格，否则报错)
```
netstat(先找到端口号，然后看后面的PID)
![Pasted image 20250721200416.png](./images/Pasted%20image%2020250721200416.png)![Pasted image 20250721200435.png](./images/Pasted%20image%2020250721200435.png)
lsof（通过已知的端口号，直接找信息）
![Pasted image 20250721202217.png](./images/Pasted%20image%2020250721202217.png)
lsof后面有空格，-i后没有
### 案例八which/su/passwd/exit/who
```
01.查看mysql程序的存放位置
	which mysql
		命令也是一个个的程序，也可以查找命令所存在位置，比如：which pwd
02.从普通用户切换至root用户，再从root用户切换回普通用户
	su - (需要输入root密码，直接回车，不会显示)，会到达root的根目录
	su 也会直接到root用户但是切换过来之后，到达的还是换之前的比如/home/first/
	su - admin
		注意：-前后都有空格
03，查看当前系统中所有登录用户的信息
	who -q
		扩展：查看当前用户名：whoami
04.退出当前终端窗口
	exit(会一层一层的退出)
```
su(切换用户)
![Pasted image 20250721203208.png](./images/Pasted%20image%2020250721203208.png)
### 案例七权限修改chmod
```
01.在当前目录下创建文件cm_demo
	touch cm_demo
02.查看文件当前权限状态
	ls -l(或者ll)
03，使用字母法将文件权限修改为：拥有者：可读/用户组：可写/其他用户：可执行
	chmod u=r,g=w,o=x cm_demo
04，使用数字法将文件权限修改为：拥有者：可读可写可执行/用户组：可读可写/其他用户：可写可执行
	chmod 763 cm_demo
```
查看文件详细信息（ls -l等价于ll）
![Pasted image 20250722095430.png](./images/Pasted%20image%2020250722095430.png)
-rwxr-xr-x
说明：
1. 信息中的第一位为文件类型：-（普通文件）或 d（文件夹）或L 是链接文件
2. 后续信息三段为1为部分依次为：用户/用户组/其他人
3. 每一组都会由r/w/x/-组成（r:读取 w:写入 x:执行 -：无权限）
rwx用户：可读可写可执行   r-x用户组：可读不可写可执行  r-x其他人：可读不可写可执行

对文件权限包括：
![Pasted image 20250722100609.png](./images/Pasted%20image%2020250722100609.png)
权限修改方法：
1. 数字法（重要，常用）
	需要根据需求，先行计算每个位置的权限结果（r:4/w:2/x:1/-:0）
	使用命令==chmod 权限数值 文件名== 修改文件权限
		注意：无论目标文件的权限作何修改，每一部分都必须有结果（数字一定是三位）
		如果某一部分没有任何权限，直接给0
		文件权限可以多次修
2. 字母法
![Pasted image 20250722181841.png](./images/Pasted%20image%2020250722181841.png)
![[Pasted image 20250722181855.png
字母法修改权限：
	1.先确定每一部分的权限，然后确认是增加/删减/赋予某个权限
	2.根据对应标识组织权限内容：
		u：拥有者/  g：用户组/  o：其他人/  a：以上全部
		+：增加权限/  -：删减权限/  =：赋予权限
		r:可读/  w：可写/  x：可执行/  -：无权限
	3.执行并验证权限结果即可
	注意：
		1.由于字母法需要考虑的内容组成较多，因此字母法的实现方式非常多样化
		2.如果需要同时变更多个部分的对应权限，需要使用逗点分隔每一个部分
		3.权限内容中不能添加空格
![Pasted image 20250809205353.png](./images/Pasted%20image%2020250809205353.png)
文件权限修改注意事项：
1.必须明确文件权限的含义
2.数字法和字母法都可以
3.尽量不要随意赋予文件最高权限（777）
4.适当修改文件权限：数字法（755），字母法（rwxr-xr-x）
### 案例九
```
01.在路径下创建adir,bdir两个文件夹
	mkdir adir bdir
02.在adir目录下创建文件f_demo
	touch adir/f_demo
03.切换路径到bdir目录下
	cd bdir
04.在当前目录下从用户目录中查找f_demo文件
	find home/first/ -name "*demo"
```
查找文件
![Pasted image 20250722184316.png](./images/Pasted%20image%2020250722184316.png)
引号仅仅表强调，没有也可以
*表示模糊，放在后面表示后面模糊
如果当前用户对目标路径没有访问权限，则无法执行查找文件动作

### 案例十ln -s
```
01.在当前路径下创建文件demo
	touch demo
02.给demo文件创建链接文件名为1demo
	ln -s demo ldemo(ldemo-->demo)
03.修改1demo链接文件的内容
	ls > ldemo(通过重定向修改ldemo)
04.查看demo文件的内容是否同样变化
	cat demo
05.修改demo文件内容，查看1demo链接文件内容是否同样变化
	ls -l > demo
	cat ldemo
如果删除原文件，链接文件会失效
```
链接文件相当于快捷方式，包括硬链接和软链接，软链接=快捷方式
链接文件
	软链接 ln -s 原文件名 链接文件名：类似于windows下的快捷方式
	硬链接 ln 原文件名 链接文件名：类似于复制文件（听不懂跳过了）
	![Pasted image 20250723083032.png](./images/Pasted%20image%2020250723083032.png)

区分：find主要用于按文件名_和_文件属性查找文件，而grep则用于搜索文本内容。

### 案例11: tar/gzip/bzip2/zip/unzip
```
1.在当前路径下创建atdir，btdir两个文件夹
	mkdir atdir btdir
2. 在atdir目录下创建aa,bb,cc三个文件
	 cd atdir
	 touch aa bb cc
3.分别用三种压缩方法对atdir目录进行压缩
	cd ../(不要再目标文件夹内部进行打包压缩文件操作，需要返回上一级目录，在需要打包的文件上一个目录进行)
	法1：tar -zcvf ctdir.tar.gz atdir/
	法2：zip -r ctdir atdir（如果目标文件是文件夹，需要用-r选项来处理内部所有文件）
4.分别解压上一步产生的压缩包文件内容至btdir目录下
	法1：tar -zxvf ctdir.tar.gz -C btdir/
	法2：unzip -d btdir/ ctdir
```
![Pasted image 20250723085335.png](./images/Pasted%20image%2020250723085335.png)
打包压缩的合并（增加了一个z选项，指打包再压缩）
方法一：
![Pasted image 20250723084034.png](./images/Pasted%20image%2020250723084034.png)
	打包文件.tar.gz中的打包文件指的是打算打包之后的命名，而后面的被压缩文件/路径指的就是打算进行打包的文件
		-z:gzip压缩 -c:打包 -v:显示过程 -f:指定文件
		-z:gzip解压 -x:解包 -v:显示过程 -f:指定文件 -C：用于指定解压目录
方法2：136集
![Pasted image 20250723090846.png](./images/Pasted%20image%2020250723090846.png)
压缩包名的后缀.zip可以省略

vi模式
![Pasted image 20250723092050.png](./images/Pasted%20image%2020250723092050.png)
i a o 按哪一个都可以

yum
yum（YellowdogUpdater,Modified）是一个在Linux系统中常用的软件包管理器。
yum提供了查找、安装、删除某一个、一组甚至全部软件包的命令，而且命令简洁而又好记。
![Pasted image 20250723094731.png](./images/Pasted%20image%2020250723094731.png)
