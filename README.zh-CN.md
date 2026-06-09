# Flow.Launcher.Plugin.SiYuanSearch - 思源笔记搜索插件

这是一个 Flow Launcher 插件，让你可以直接在 Flow Launcher 中搜索思源笔记并快速打开。

## 功能特性
- 使用 SQL 查询搜索思源笔记中的所有块
- 选中结果后直接通过 siyuan:// 协议在思源笔记中打开对应块
- 简单的 API 地址和令牌配置

## 安装方法
1. 下载插件包
2. 将其解压到 Flow Launcher 的插件目录中
3. 重启 Flow Launcher

## 配置步骤
1. 在思源笔记中开启 API 服务：
   - 打开思源笔记设置 -> API
   - 启用 API 服务
   - 复制你的 API 令牌

2. 在 Flow Launcher 中配置插件：
   - 打开 Flow Launcher 设置
   - 找到 SiYuan Search 插件
   - 设置思源 API 地址（默认：http://127.0.0.1:6806）
   - 粘贴你复制的 API 令牌

## 使用方法
输入 `sy` 加上你要搜索的关键词，即可搜索思源笔记中的内容。选中搜索结果后会自动在思源笔记中打开对应的块。

## 系统要求
- 已启用 API 服务的思源笔记
- Flow Launcher