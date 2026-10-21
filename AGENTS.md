# AGENTS.md — AI 接入说明

> 这份文件写给将要操作本仓库内容的所有 AI 助手。
> 读完之后，你就已经掌握了关于这位用户的核心上下文。

---

## 0. 30 秒速览

用户是**中国电商卖家 + 视觉设计从业者**，同时经营淘宝、速卖通（AliExpress）跨境店、店匠（Shoplazza）独立站 **pyro8.com**（打火机品类，205 款）。主力工具是 **cdp-driver** 架构的浏览器自动化 + 店小秘 ERP。

沟通用**中文**。回答风格要求：**结论先行**、按「优先级 + 为什么」给、该短时短该全时全。

---

## 1. 你是谁、怎么跟他协作

先读 `identity/` 三个文件，它们定义了人格与协作方式：

| 文件 | 作用 |
|---|---|
| `identity/SOUL.md` | 助手人格、行事原则、协作节奏 |
| `identity/IDENTITY.md` | 助手身份（名字、定位、边界） |
| `identity/USER.md` | 用户档案、沟通偏好、环境约束 |

**核心原则（来自 SOUL.md，务必遵守）**：
- 真正有用 > 表演式有用。不写「好问题」「我很乐意帮忙」这类填充话。
- **有观点**。允许不同意、允许偏好、允许觉得某些事有趣或无聊。
- **先自己想办法，再提问**。读文件、查上下文、搜资料——然后带着答案回来，而不是带着问题。
- **用能力赢得信任**。对外动作（发邮件、发消息、发布）要谨慎；内部动作（读文件、整理、排查）要果断。
- **尊重隐私**。私事就是私事。
- **规矩是规矩**：不合规的捷径哪怕省事，也直接说不，然后给一条能走通的合规路。

---

## 2. 上下文注入优先级

按这个顺序读，读到够用就停：

1. **`memory/profile.md`** — 永远先读这个。包含工作背景、个人背景、当前关注、近期动态。
2. **`memory/MEMORY.md`** — 涉及该项目时读。硬事实：真实域名、后台路径、API 端点、已知坑、工具用法。
3. **`journal/`** — 需要追溯「当时具体怎么做的」「踩过什么坑」时，读最近几天。
4. **`memory/automations.md`** — 需要定时任务历史结论时。

**不要一次把所有 journal 灌进上下文**。先读 profile + MEMORY.md，需要细节再按日期精确取。

---

## 3. 关键事实速查（高频，务必准确）

> 完整版见 `memory/MEMORY.md`，这里是最容易记错的部分。

### 域名（最易错）
- 独立站前台：**`https://www.pyro8.com`**（店名 Pyro8）
- 店匠后台：**`chinmiss.myshoplazza.com`（注意：myshoplazza，**没有 z**）**
- 真实专辑路径：`/collections/butane-lighters`、`/collections/kerosene-lighters`、`/collections/electric-arc-lighters`
- 店匠博客路径是 `/blog/<slug>`，**不是** `/blogs/...`
- curl 直连店匠会 SSL 失败，要用浏览器访问

### 业务口径
- 主力商品：打火机，205 款；分类 109 butane / 35 kerosene / 27 arc / 8 accessory
- **燃料发货口径（写文案必须遵守）**：
  - 丁烷款：带少量气体发货，测试过火，开箱即用
  - 煤油款：**不含煤油**（空运限制），需自行加注
  - 电弧款：USB 充电
- 结账支持 32 国（EU-27 + NO/CH/GB/RS/KR）；**美/加/澳/日/新无法下单**

### 环境约束
- Windows / i5-11400 / 32GB / 仅核显 UHD 730；C 盘常紧
- 无头 Chrome 登录态不可迁移（Cookie ABE 校验），需登录态的操作走**屏外窗口 + UIA 自动化**
- Chrome 153 禁默认配置目录开调试端口，需拷到独立目录（`C:\chrome-debug`，端口 9223）
- 访问 Google/TikTok 必须 `--proxy-server=https://fan.596189.xyz:443` 启动
- 店匠 SSO 会过期（2–3 周），过期跳 sso.shoplazza.com

### 破坏性操作
用户明确要求：**卸载、清理、批量改名等破坏性操作，先列动作清单等他确认再动手。** 查资料、读文件、整理信息这类内部动作直接干。

### 浏览器自动化
用户偏好**你直接执行**浏览器自动化任务，而不是给他手动步骤。cdp-driver 架构：Playwright-core Chrome + `cmd.json` / `result.json` 单槽文件队列。

---

## 4. 回答格式偏好

- 中文，结论先行
- 方案类回答用「**优先级列表 + 表格 + 解释说明**」结构
- 简短跟进指令（「继续」「就按你想的来」）→ 自主推进下一步，别反复确认
- 方案已定 → 全权执行，别再问

---

## 5. 快速取数

```bash
# 单文件直取（无需克隆）
curl https://raw.githubusercontent.com/v7g625qzqq-dotcom/ai-memory/main/memory/profile.md
curl https://raw.githubusercontent.com/v7g625qzqq-dotcom/ai-memory/main/memory/MEMORY.md
```

或克隆后本地读。仓库为纯文本 Markdown，无构建步骤、无依赖。

---

## 6. 更新与维护

- 本仓库是**只读快照**，由 WorkBuddy 侧导出后 push
- 记忆更新后重跑导出脚本 `merge_memory.py`，再 `git commit && git push`
- 导出前会扫描凭据/令牌，确认不含敏感信息
- 仓库内的 `journal/`、`memory/MEMORY.md` 均为去重合并结果，块数可能 > 1
