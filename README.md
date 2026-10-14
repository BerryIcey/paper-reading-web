<div align="center">

**简体中文 · [English](README.en.md)**

![paper-to-html — 阅读、理解、留下问题](docs/images/cover.svg)

### 把论文变成一份能跟着读的网页

连续读正文，逐图看证据，查完术语回到原处。

[![推荐 v2.1](https://img.shields.io/badge/推荐版本-v2.1-2f6354?style=flat-square)](https://github.com/BerryIcey/paper-to-html/releases/tag/v2.1)
[![MIT](https://img.shields.io/badge/License-MIT-657b72?style=flat-square)](LICENSE)

**[下载 v2.1](https://github.com/BerryIcey/paper-to-html/releases/download/v2.1/paper-to-html-v2-v2.1.zip) · [查看技能](https://github.com/BerryIcey/paper-to-html/tree/v2.1/skills/paper-to-html-v2/SKILL.md) · [更新说明](docs/v2.1-changes.md) · [反馈问题](https://github.com/BerryIcey/paper-to-html/issues)**

</div>

## 先看阅读体验

图和解释同步切换。先弄清“图里的一个点是什么”，再读它能支持什么结论。

![逐图阅读：原图与解释并排](docs/images/figure-reader.png)

<details>
<summary>展开查看全文入口和随手记</summary>

![正文阅读入口](docs/images/reader-overview.png)
![侧边随手记](docs/images/notes-bookmark.png)

</details>

[下载演示 HTML](https://raw.githubusercontent.com/BerryIcey/paper-to-html/main/demo/paper-reading.html)，保存后用浏览器打开。演示使用原创文字和模拟数据。GitHub 的 HTML 文件页显示源码，不会直接运行网页；保存项目笔记需要本地服务。

## 阅读时，你能得到什么

| 读正文 | 读图与证据 | 查阅与记录 |
|---|---|---|
| 连续原文与核心完整翻译 | 主图总览和逐面板讲解 | 彩色术语与知识卡 |
| 明确结论和连贯解释 | 当前问题、图例、实际观察与推理 | 查阅后返回原位置 |
| 全文论证链与文末评议 | 区分观察、推断和未解决问题 | 荧光笔、缩放、随手记 |

这是供 Codex 使用的 **Skill 与网页阅读组件**。生成内容需要核对来源；它不是脱离助手独立运行的自动论文分析器。

## 三步开始

### 1 · 安装推荐版

下载 [paper-to-html-v2-v2.1.zip](https://github.com/BerryIcey/paper-to-html/releases/download/v2.1/paper-to-html-v2-v2.1.zip)，解压后将其中完整的 `paper-to-html-v2` 文件夹放进当前设备的 Codex Skill 目录，通常是 `~/.codex/skills/`。已有旧安装时先在技能目录外备份。新开聊天确认技能可用。

下载包版本是 **v2.1**，技能调用名称仍是 **`$paper-to-html-v2`**。GitHub 更新不会自动更新电脑上的安装。

### 2 · 提供论文并调用

```text
$paper-to-html-v2
把这篇论文做成中文共读网页。
完整翻译核心正文，逐面板解释全部主图，并讲清全文论证。
```

提供有权使用的 PDF。默认包含核心正文、全部主图、必要知识卡与文末评议；独立方法细节、附图详解和复习内容可按需追加。缺少补充资料时，助手应说明实际覆盖范围。

### 3 · 阅读并留下问题

静态 HTML 可离线切图、放大、查卡和标记。要保存随手记，请打开该论文的本地阅读服务；问题保存到项目，供下一轮助手处理，**不会即时调用 GPT**。正文与笔记、浏览器草稿与项目文件是不同的保存内容。

<details>
<summary>只想体验组件？启动演示服务</summary>

不需要模型或 OpenAI API 密钥。需要 Python：

```sh
git clone https://github.com/BerryIcey/paper-to-html.git
cd paper-to-html
python skills/paper-to-html-v2/assets/reader-components/reading_server.py --root demo --port 18765
```

在同一台设备打开 `http://127.0.0.1:18765/paper-reading.html`。这只是临时演示服务；正式项目需要配置独立后台运行方式。

</details>

## 选择哪个版本

| 版本 | 状态 | 内容与入口 |
|---|---|---|
| **v2.1** | **最新推荐 · 已发布** | [下载](https://github.com/BerryIcey/paper-to-html/releases/tag/v2.1) · [更新报告](docs/v2.1-changes.md)：完整逐图讲解要求、自适应术语与知识卡、原文和图注查阅入口 |
| v2.0.2 | 历史版 | [查看快照](https://github.com/BerryIcey/paper-to-html/tree/v2.0.2) · [早期变更](docs/v2-changes.md) |
| v1.0.0 | 原始版 | [查看快照](https://github.com/BerryIcey/paper-to-html/tree/v1.0.0)，用于对照和回退 |

**v2.2 正在本地测试，尚未公开发布。** 它增加本科读者起点筛选及进一步跨领域适配；这些改动不包含在 v2.1 下载包中。Skill 版本与某篇论文网页自己的版本号分别管理。

[v2.1 校验文件](https://github.com/BerryIcey/paper-to-html/releases/download/v2.1/paper-to-html-v2-v2.1.sha256) · [版本差异](https://github.com/BerryIcey/paper-to-html/compare/v2.0.2...v2.1)。不要混用不同版本的参考文件。[个人 Skill 库](https://github.com/BerryIcey/my-skills)保留项目入口。

## 使用前需要知道

- **制作环境：** 支持 Skill 的助手和 PDF 读取能力；组件与服务使用 Python 标准库，PDF 裁图需要 PyMuPDF，脚本语法检查使用 Node.js。
- **核对范围：** 翻译、图例、数值与推理需要逐项核对。测试通过不证明解释全部正确，也不证明所有领域都已验证。
- **保存边界：** 正文可离线阅读；项目笔记依赖本地服务。目前没有断线自动补存、跨设备同步或即时问答。
- **设备访问：** `127.0.0.1` 只供本机使用。手机能读离线文件，不代表能连接电脑的本地地址提交笔记。
- **后台与历史：** 正式项目可保留 0/1/2 个历史备份，最新版另计；Windows 后台方案与其他系统不同，重启存活需另行验证。

## 一起改善阅读效果

[提交问题](https://github.com/BerryIcey/paper-to-html/issues)时请写明版本、浏览器、期望行为与实际情况。解释不清楚时，指出卡在哪个对象、比较或推理步骤，比只说“太简略”更有帮助。

当前关注：专门术语漏选与基础知识过选、长论文后半部分讲解质量、触控操作，以及不同论证方式的迁移。请勿上传私人笔记、凭据或未经许可的论文全文。

代码与通用说明使用 [MIT 许可](LICENSE)。论文及第三方图片沿用原有权利条件，仓库不分发用户论文。
