# AI Memory · 林老板的跨 AI 记忆库

> 这个仓库把 WorkBuddy 里的个人记忆（身份设定、用户画像、项目长期记忆、每日工作日志）导出成任何 AI 都能直接读取的纯文本 / Markdown。
>
> **给其他 AI 的用法**：直接拉这个仓库，或读 `AGENTS.md`。

---

## 快速开始

### 方式一：Git 克隆（完整）

```bash
git clone https://github.com/v7g625qzqq-dotcom/ai-memory.git
```

克隆后按下面的「文件地图」读取对应文件即可。

### 方式二：Raw 单文件直取（最省事，适合上下文注入）

不克隆，直接用 raw.githubusercontent.com 取单文件：

```bash
# 核心画像（工作背景 / 个人背景 / 当前关注 / 近期动态）—— 建议优先注入这个
curl https://raw.githubusercontent.com/v7g625qzqq-dotcom/ai-memory/main/memory/profile.md

# 项目长期记忆（店匠 / 速卖通 / SEO / 自动化 的硬事实）
curl https://raw.githubusercontent.com/v7g625qzqq-dotcom/ai-memory/main/memory/MEMORY.md

# 身份设定
curl https://raw.githubusercontent.com/v7g625qzqq-dotcom/ai-memory/main/identity/SOUL.md
curl https://raw.githubusercontent.com/v7g625qzqq-dotcom/ai-memory/main/identity/USER.md
curl https://raw.githubusercontent.com/v7g625qzqq-dotcom/ai-memory/main/identity/IDENTITY.md
```

### 方式三：作为系统提示注入

在别的 AI 里，把 `AGENTS.md` 的内容作为 system prompt 前缀，或把它放进项目根目录（多数 AI 工具会自动读取 `AGENTS.md` / `CLAUDE.md` / `.cursorrules`）。

### 方式四：MCP / 工具调用

若你的 AI 支持 MCP，本仓库可被包装成一个简易 MCP Server（提供 `get_profile` / `get_longterm_memory` / `search_journal` 三个只读工具）。需要时告诉我，可以直接生成。

---

## 文件地图

| 路径 | 内容 | 体积量级 | 该什么时候读 |
|---|---|---|---|
| `AGENTS.md` | 给 AI 的接入说明（先读这个） | 小 | 每次会话开始 |
| `memory/profile.md` | 云端生成的用户画像，含工作背景 / 个人背景 / 当前关注 / 近期动态 | ~7 KB | **最高频**，几乎每次都要 |
| `memory/MEMORY.md` | 项目长期硬事实：域名、API 路径、已知坑、工具用法 | ~7 KB | 涉及该项目时 |
| `memory/automations.md` | 定时巡检记录 | ~1.5 KB | 需要历史巡检结论时 |
| `identity/SOUL.md` | 助手人格与协作方式 | ~2 KB | 想要同样的语气和风格时 |
| `identity/USER.md` | 用户档案与沟通偏好 | ~1.3 KB | 调整沟通风格时 |
| `identity/IDENTITY.md` | 助手身份设定 | ~1 KB | 需要角色一致性时 |
| `journal/YYYY-MM-DD.md` | 每日工作日志，按时间倒序看最新 | 1–25 KB/天 | 追溯具体操作与踩坑时 |

---

## 数据来源

导出自 WorkBuddy 本地三层记忆：

| 层 | 来源 | 落地位置 |
|---|---|---|
| 云端画像 | `.workbuddy/memory/*_memory.md` | `memory/profile.md` |
| 身份层 | `.workbuddy/user-*/{SOUL,IDENTITY,USER}.md` | `identity/` |
| 工作区层 | 34 个项目的 `.workbuddy/memory/`（55 个文件） | `journal/` + `memory/MEMORY.md` |

同一天的日志若有多个工作区版本，按内容哈希去重后合并保留，因此 `journal/` 每天一个文件、块数可能 > 1。

---

## 更新方式

记忆更新后重新导出：

```bash
python merge_memory.py    # 需先编辑脚本内的 ROOTS / OUT 路径
```

或直接让 WorkBuddy 侧跑一次导出并 `git push`。

---

## 注意

- 本仓库是**只读记忆快照**，不含任何凭据、令牌或账号密码（导出前已扫描确认）。
- 涉及店铺后台、邮箱、社媒账号的具体操作细节，请以 `memory/MEMORY.md` 中的路径与经验为准，不要凭印象重造。
- 部分历史记录含环境相关细节（IP、端口、代理地址、调试目录），仅供本机环境使用，外泄前请自行判断。
