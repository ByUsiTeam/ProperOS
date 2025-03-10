# ProperOS

- 基于现在OpenJuOS**v3.5**开发

## 基础简介
1. 基于手机应用 `iApp` 开发的模拟操作系统应用。
2. ___ProperOS___ 的应用可以直接调用系统浏览器内核进行运行，并且调用库开放
3. 基于 **OpenJuOS** 二次开发，该版本会在原有的 **JuOS** 基础上继续进行美化，并且新增更多的可执行操作
4. 使用的是 **Apache-2.0** 开源协议你需要在你的项目中标注使用了该项目

## 安装运行方法
1. Git仓库
   ```bash
   git clone https://gitee.com/byusi/properos.git
   ```
2. 压缩所有文件
   ```bash
   cd properos
   zip -r 随便写.iApp .
   ```
3. 将 `随便写.iApp` 导入到手机，并且确保你手机上已经安装了 `iApp` 应用，使用 `MT管理器` 打开 `随便写.iApp` 在弹出的界面中选择 **类型** --> **全部** --> **iApp** 就可以正常的导入此项目。

4. 这样就可以修改此项目或更改此项目的部分内容并且分发，注意，在分发的过程中请注明原项目地址，原项目地址需要指定为该仓库：[https://gitee.com/byusi/properos](https://gitee.com/byusi/properos)