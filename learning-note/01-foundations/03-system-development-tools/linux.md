以下是对您提供的 Linux 入门笔记的优化版本，主要修正了若干技术细节、提升了结构清晰度、统一了命令格式，并补充了少量必要说明。内容保持原笔记的章节与核心信息，便于复习与查阅。

---

# 第一章 Linux 入门

## Linux 特点
- **一切皆文件**：硬件、进程、设备等均通过文件接口访问  
- **开源免费**：大多数发行版自由使用，社区驱动  
- **兼容 POSIX 标准**：实现良好的跨平台可移植性
- **图形界面**：可选择 GNOME、KDE 等桌面环境  
- **多用户 & 多任务**：真正的多用户操作系统，同时运行多进程  
- **支持多平台**：x86、ARM、RISC-V 等  

## 常用服务器组合
- **LAMP**：Linux + Apache + MySQL/MariaDB + PHP  
- **LNMP**：Linux + Nginx + MySQL/MariaDB + PHP  

## Linux 常见发行版
- **RedHat 家族**  
  - Red Hat Enterprise Linux（RHEL）：企业版，付费订阅  
  - CentOS：RHEL 的免费重建版本（CentOS 7 已停止维护，迁移至 CentOS Stream）  
- **Debian 家族**  
  - Debian：稳定、自由，适合服务器  
  - Ubuntu：基于 Debian，界面友好，社区活跃，适合新手  

---

# 第二章 Linux 安装

## 一、VMware 安装流程（简述）
1. 安装 VMware Workstation  
2. 创建虚拟机（CPU、内存、磁盘建议 2C/4G/40GB）  
3. 下载 Ubuntu 镜像（ **26.04 LTS** ）  
   - 清华镜像：https://mirrors.tuna.tsinghua.edu.cn/ubuntu-releases/24.04/  
4. 配置网络（NAT 或桥接）  
5. 启动并安装 Linux  
6. 登录系统  

## 二、Linux 目录结构

### 根目录 `/`
文件系统的最顶层，所有文件都挂载于此。

### 主要二级目录（分类整理）

#### 1. 命令相关目录
| 目录 | 说明 |
|------|------|
| `/bin` | 普通用户基础命令（如 ls、cp） |
| `/sbin` | 系统管理命令，常需 root 权限 |
| `/usr/bin` | 大部分应用程序及工具 |
| `/usr/sbin` | 后台服务、高阶管理命令 |

#### 2. 系统启动与内核
| 目录 | 说明 |
|------|------|
| `/boot` | 内核镜像、GRUB 引导配置 |
| `/proc` | 虚拟文件，存放进程与内核实时信息 |
| `/sys` | 硬件设备与内核对象的管理接口 |

#### 3. 硬件设备目录 `/dev`
- `/dev/sda`：第一块 SCSI/SATA 硬盘  
- `/dev/tty`：终端设备  
- `/dev/null`：数据黑洞  
- `/dev/zero`：无限零字节源  

#### 4. 全局配置目录 `/etc`
- `/etc/passwd`：用户账户信息  
- `/etc/group`：用户组信息  
- `/etc/profile`：全局环境变量  
- `/etc/hosts`：静态主机名解析  
- `/etc/systemd/`：systemd 服务配置  
- `/etc/init.d/`：传统 SysV 启动脚本  

#### 5. 用户家目录
- `/home/用户名`：普通用户家目录  
- `/root`：root 用户家目录  

#### 6. 动态库目录
- `/lib`：32 位系统基础库及内核模块  
- `/lib64`：64 位系统核心库  
- `/usr/lib`、`/usr/lib64`：应用程序专属库  

#### 7. 挂载点
- `/media`：自动挂载（U盘、光盘）  
- `/mnt`：手动临时挂载点  
- `/run`：运行时临时文件（重启清空）  

#### 8. 软件安装目录
- `/opt`：第三方大型软件  
- `/usr/local`：源码编译安装软件默认位置  

#### 9. 动态数据目录 `/var`
- `/var/log`：系统日志（故障排查关键）  
- `/var/spool`：打印、邮件队列  
- `/var/lib`：服务持久化数据  
- `/var/cache`：程序缓存  

#### 10. 临时文件目录
- `/tmp`：公共临时目录，所有用户可读写，**重启清空**  
- `/var/tmp`：清理周期更长的临时目录  

#### 11. `/usr` 下的其他资源
- `/usr/share`：共享数据（字体、图标、模板）  
- `/usr/include`：C/C++ 头文件  
- `/usr/src`：内核源码  
- `/usr/man` 或 `/usr/share/man`：手册页  

#### 12. 其他
- `/srv`：服务提供的数据目录（如网站、FTP）  
- `/lost+found`：文件系统修复后恢复的文件存放处  

### 目录分层归类
- **系统核心**：`/` `/bin` `/sbin` `/boot` `/dev` `/etc` `/lib` `/proc` `/sys`  
- **用户数据**：`/home` `/root`  
- **程序软件**：`/usr` `/opt` `/usr/local`  
- **动态数据**：`/var` `/tmp` `/run`  
- **挂载外设**：`/media` `/mnt` `/srv`  

## 三、虚拟机管理操作
- **快照**：保存当前状态，便于回滚  
- **克隆**：复制虚拟机（克隆后需修改 IP 避免冲突）  

## 四、远程连接工具（SSH 协议）
Windows 推荐：Xshell、FinalShell、MobaXterm  
新建会话：协议 SSH，端口 22，填写主机 IP 和用户名密码  

## 五、VIM 编辑器

### 普通模式（默认）
- 光标移动：`h`/`j`/`k`/`l` 或方向键  
- `gg`：文件首行  
- `G`：文件末行；`10G` 跳转到第 10 行  
- `0`：行首；`$`：行尾  
- `dd`：删除当前行；`5dd`：删除 5 行  
- `x`：删除光标后字符；`X`：删除光标前字符  
- `yy`：复制当前行；`p`：粘贴  
- `u`：撤销；`Ctrl+r`：重做  
- `i`：光标前插入；`a`：光标后插入；`o`：下一行插入  
- `ZZ`：保存并退出  

### 插入模式
按 `ESC` 返回普通模式  

### 命令模式（按 `:` 或 `/` 进入）
- `:w`：保存  
- `:q`：退出  
- `:wq` 或 `:x`：保存退出  
- `:q!`：强制退出不保存  
- `/关键字`：查找，按 `n` 下一个，`N` 上一个  
- `:set nu`：显示行号  
- `:set nonu`：隐藏行号  

---

# 第三章 Linux 基础命令

命令格式：  
`命令 [全局参数] [子命令] [局部参数] [操作对象]`

- **短参数**：`-a -b` 可合并为 `-ab`  
- **长参数**：`--all --help`  
- **通配符**：`*` 任意字符；`?` 单个字符  
- **管道** `|`：传递前一个命令的输出作为下一个命令的输入  

## 一、帮助命令
`man 命令或配置文件`  查看手册（按 `q` 退出）

## 二、开关机命令
| 命令 | 说明 |
|------|------|
| `poweroff` | 立即关机 |
| `reboot` | 立即重启 |
| `shutdown -h now` | 立即关机 |
| `shutdown -r +5` | 5 分钟后重启 |
| `shutdown -c` | 取消定时关机/重启 |

## 三、服务管理（systemctl）
```bash
systemctl start  服务名
systemctl stop   服务名
systemctl restart 服务名
systemctl status  服务名
systemctl enable  服务名   # 开机自启
systemctl disable 服务名
systemctl is-enabled 服务名
systemctl list-unit-files   # 查看所有自启配置
systemctl daemon-reload     # 重载服务配置
```

## 四、文件目录类命令
```bash
pwd                     # 当前绝对路径
ls -l -a                # 列表显示，包含隐藏文件
cd ~ / .. / -           # 家目录 / 上级 / 上一次目录
mkdir -p dir1/dir2      # 递归创建目录
rmdir empty_dir         # 删除空目录
touch file.txt          # 创建空文件/更新时间戳
cp -r source target     # 递归复制目录
rm -rf file_or_dir      # 强制递归删除（危险）
mv old new              # 移动或重命名
cat -n file             # 显示内容并编号
head -n 20 file         # 前20行
tail -n 20 -f file      # 后20行并持续跟踪
echo "hello" > file     # 覆盖写入
echo "world" >> file    # 追加写入
ln -s /abs/path link    # 创建软链接（建议绝对路径）
history                 # 查看命令历史
```

## 五、日期时间
```bash
date                        # 当前时间
date "+%Y-%m-%d %H:%M:%S"
date -d "+1 day"            # 一天后
```

## 六、用户管理（`/etc/passwd`）
```bash
useradd -m 用户名          # 创建用户并生成家目录
id 用户名
passwd 用户名
su - 用户名                # 切换用户并加载环境
userdel -r 用户名          # 删除用户及其家目录
sudo -l                    # 查看当前用户 sudo 权限
```

### sudo 配置（`/etc/sudoers`，使用 `visudo` 编辑）
```
alice   ALL=(ALL)       ALL      # 普通用户所有权限
%sudo   ALL=(ALL:ALL)   ALL      # sudo 组用户
charlie ALL=(ALL)       NOPASSWD: ALL   # 免密执行所有命令
```

## 七、组管理（`/etc/group`）
```bash
groupadd 组名
groupdel 组名
usermod -g 主组   用户名      # 修改主组
usermod -aG 附加组 用户名      # 追加附加组（保留原组）
usermod -G 组列表 用户名        # 重置附加组（覆盖）
usermod -l 新名 旧名            # 修改用户名
usermod -d /新家目录 -m 用户名   # 修改家目录并移动数据
```

## 八、文件权限
权限表示：`d rwx r-x r-x`  
- 第1位：`d`目录 / `-`文件 / `l`链接  
- 属主（u） / 属组（g） / 其他（o）  

### 修改权限 `chmod`
```bash
chmod u+x file                # 属主增加执行
chmod g-w,o=r file            # 属组去掉写，其他设为只读
chmod 755 file                # rwxr-xr-x
chmod -R 644 dir/             # 递归修改目录下所有文件
```

### 修改所有者 `chown`
```bash
chown alice:staff file        # 同时修改属主和属组
chown -R alice dir/           # 递归修改属主
```

## 九、搜索查找
```bash
find /home -name "*.txt"      # 按名字查找
find /var -size +10M          # 大于10M的文件
find / -user alice            # 属于alice的文件
grep -n "error" /var/log/syslog   # 在文件中搜索字符串
ls | grep ".conf"             # 过滤当前目录下的 .conf 文件
```

## 十、压缩与打包
```bash
gzip file.txt                 # 生成 file.txt.gz，原文件消失
gunzip file.txt.gz

zip -r archive.zip dir/       # 压缩目录
unzip archive.zip -d /target/

tar -zcvf archive.tar.gz dir/   # 打包并 gzip 压缩
tar -zxvf archive.tar.gz -C /dest/   # 解压到指定目录
```

## 十一、磁盘与挂载
```bash
df -h                         # 查看分区使用情况（人类可读）
fdisk -l                      # 列出磁盘分区
mount /dev/sdb1 /mnt/usb      
umount /mnt/usb               # 卸载
```

## 十二、进程管理
```bash
ps -ef                        # 显示所有进程（标准格式）
ps -aux                       # 显示 CPU/内存占用
kill -9 PID                   # 强制终止进程
```

## 十三、定时任务 `crontab`
```bash
crontab -e                    # 编辑当前用户的定时任务
crontab -l                    # 查看当前用户的定时任务
crontab -r                    # 删除所有任务
```
**时间格式**：  
`分 时 日 月 周 命令`  
- `*` 任意值  
- `*/5` 每5个单位  
- `1-5` 范围  
- `1,3,5` 多个值  

> 建议命令使用**绝对路径**，如 `/bin/echo` 而非 `echo`

---

# 第四章 生产开发扩展

## 一、软件安装

### RPM（RedHat 系）
```bash
rpm -qa                # 列出所有已安装包
rpm -ql 包名           # 查询包安装的文件列表
rpm -e 包名 --nodeps   # 强制卸载（不检查依赖）
rpm -ivh package.rpm   # 安装（i安装 v显示 h进度）
```

### YUM（基于 RPM，自动处理依赖）
```bash
yum install -y 包名
yum update 包名
yum remove 包名
yum list installed
yum clean all
yum deplist 包名
```

## 二、Docker

### Docker 架构
- **Client**：命令行工具  
- **Daemon**：后台服务，管理容器/镜像  
- **Registry**：镜像仓库（如 Docker Hub）  
- **Container**：运行中的实例  
- **Image**：只读模板  

### Docker 安装（CentOS/RHEL 示例）
```bash
# 卸载旧版
yum remove docker docker-common docker-engine
# 配置 yum 仓库（略，建议使用官方脚本）
curl -fsSL https://get.docker.com | bash -s docker
# 启动并设置自启
systemctl start docker
systemctl enable docker
```

### 常用命令
#### 镜像操作
```bash
docker search nginx
docker pull nginx:1.25
docker images
docker rmi 镜像ID
```

#### 容器操作
```bash
docker run -d --name web -p 80:80 nginx:1.25
docker ps -a
docker stop web
docker start web
docker rm -f web
docker logs web
```

#### 保存与加载镜像
```bash
docker commit container_id myimage:v1
docker save -o myimage.tar myimage:v1
docker load -i myimage.tar
```

#### 镜像仓库（Docker Hub）
```bash
docker login
docker tag myimage:v1 username/myimage:v1
docker push username/myimage:v1
```

### Docker 存储（持久化）
```bash
# 挂载宿主机目录
docker run -v /host/data:/app/data ...
# 使用 named volume
docker volume create mydata
docker run -v mydata:/app/data ...
docker volume ls
docker volume inspect mydata
```

### Docker 网络
```bash
docker network create mynet
docker run --network mynet --name app1 ...
docker network inspect mynet
```

## 三、Docker Compose（批量管理）

`compose.yaml` 示例：
```yaml
name: myproject
services:
  db:
    image: mysql:8.0
    container_name: mysql
    ports:
      - "3306:3306"
    environment:
      MYSQL_ROOT_PASSWORD: 123456
    volumes:
      - db-data:/var/lib/mysql
    restart: always
    networks:
      - back

volumes:
  db-data:

networks:
  back:
```

常用命令：
```bash
docker compose up -d          # 后台启动
docker compose down -v        # 停止并删除卷（数据会丢失）
docker compose ps             # 查看所有容器
docker compose logs           # 查看所有容器日志
```

## 四、Dockerfile 构建镜像

```dockerfile
# 基础镜像（推荐 alpine 或 slim 版本）
FROM ubuntu:22.04

# 更新并安装软件（合并 RUN 减少层数）
RUN apt-get update && apt-get install -y curl \
    && rm -rf /var/lib/apt/lists/*

# 复制文件（优先 COPY，ADD 仅在自动解压或远程 URL 时使用）
COPY ./app /usr/src/app
WORKDIR /usr/src/app

# 声明运行时端口（仅文档作用）
EXPOSE 8080

# 启动命令（CMD 可被覆盖，ENTRYPOINT 不易覆盖）
CMD ["python", "app.py"]
```

构建：
```bash
docker build -t myapp:1.0 .
docker build -f Dockerfile.dev -t myapp:dev .
```

