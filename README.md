# ProperOS

- 基于 OpenJuOS **v3.5** 开发  
  [![ByUsi/OpenJuOS](https://gitee.com/byusi/openjuos/widgets/widget_card.svg?colors=4183c4,ffffff,ffffff,e3e9ed,666666,9b9b9b)](https://gitee.com/byusi/openjuos)

## 基础特性
1. 基于移动端应用 `iApp` 开发的模拟操作系统环境
2. **ProperOS** 应用可直接调用系统浏览器内核运行，并开放调用库
3. 在 **OpenJuOS** 基础上进行二次开发，优化界面设计并扩展功能模块
4. 采用 MIT 开源协议，分发时需注明原项目地址

## 部署指南

### 获取源码
- Gitee
  ```bash
  # Gitee 仓库
  git clone https://gitee.com/properos/properos.git
  ```

- GitHub
  ```bash
  # GitHub 镜像
  git clone https://github.com/ByUsiTeam/ProperOS.git
  ```

### 项目打包
```bash
# 进入目录
cd properos
# 签出分枝
git switch master
# 打包
zip -r ProperOS.iApp .
```

### 安装运行
1. 将生成的 `ProperOS.iApp` 文件传输至移动设备
2. 使用 **MT管理器** 打开文件
3. 选择打开方式：**类型** → **全部** → **iApp**
4. 完成导入后即可运行或二次开发

> JiYU.mtsx 为 MT管理器 的语法高亮文件

### 分发须知
修改或二次分发时，必须在项目中标注原始仓库地址：  
[https://gitee.com/properos/properos](https://gitee.com/properos/properos)  
或者  
[https://github.com/ByUsiTeam/ProperOS](https://github.com/ByUsiTeam/ProperOS)