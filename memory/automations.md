# 自动化任务记忆

---

<!-- source: D:/360Downloads/2026-10-06-21-17-26/.workbuddy/memory/automations/d21bad42-a6a3-48f6-9e23-b1cbf9b1c937/memory.md -->

# 速卖通全托管商品优化 — 定时巡检记录

## 2026-10-07 15:30 巡检

### 结论
- **图片任务（result_img.json）：已完成 24/24，全部 ok=true。** 覆盖 6 个店铺（惠厨宠物1=4、焙亲美VIP=7、心乐缘自营转全托=3、心乐缘密斯=5、心乐缘科技=1、焙亲美=4）。
- **主任务（v2_result.json）：未完成，且当前被平台侧静默拦截，无法推进。** 累计 273 条记录，成功 121、失败 152。

### 环境状态
- 端口 9501 存活，HeadlessChrome/153（无头，未弹窗），daemon phase=holding 正常。
- node.exe 进程 6 个。
- 执行脚本（run_v2.js / run_img2.js）**均已停止**，非崩溃残留，而是无进程在跑；日志停更（v2 停在 12:06，img 停在 13:48）。
- 浏览器内残留 26 个泄漏标签页 → 已用自建 cleanup_tabs.js 清理，保留 1 个 productTask 主页面，登录态探测 200/hasData=true 正常。

### 关键发现：平台侧静默拦截（重要，复用价值高）
对 `879266987986088` 做保存链路诊断（diag_save.js）：
- 页面状态正常：更新按钮存在且未禁用，标题输入框有值，无任何提示弹窗。
- 制造标题改动后点击「更新」→ **新增 POST 请求数 = 0**，且无错误/成功提示，标题值未落库。
- 结论：**保存请求根本没发出去，平台静默丢弃**——与 run_v2.js 顶部注释记录的"受管控字段改动若无基础信息改动会被静默拦截"是同一类拦截。
- 小批量恢复探测（MODE=logi LIMIT=3）同样 0 成功，物流属性全部 0/N 未变。
- 按林老板约束：**不反复重试**，只说明现象。

### 待办（下次巡检可直接续跑）
- 剩余 **140 个产品**物流属性未填（心乐缘密斯26、惠厨30、心乐缘自营转全托23、焙亲美VIP22、金铭燕18、心乐缘科技12、焙亲美9）。
- 剩余 **71 个产品**SKU 编码需修（共 263 个 SKU，总 SKU 1174）。
- 41 个产品从未尝试过，但均不需物流属性（logFilled 已满），无额外收益。
- 清单已落盘 `remaining.json`（由 verify_now.js 生成，含 remainLogi / remainSku）。
- 恢复入口：`MODE=logi` 或 `MODE=sku` + `LIMIT` 控制批量，`DXM=id` 定位单产品试跑；脚本自带断点续跑（按 ok=true 跳过），勿重复处理已成功产品。

### 本次新增文件
- `cleanup_tabs.js` — 清理泄漏标签页 + 登录态探测，可重复执行。
- `diag_save.js` — 保存链路诊断（抓 POST 请求 + 弹窗提示），定位静默拦截用。
- `run_v2.js` 增加 `DXM` 环境变量支持（单产品/指定列表试跑）。

---

<!-- source: D:/360Downloads/2026-10-21-14-01-54/.workbuddy/memory/automations/da747ae2-952d-4693-be59-40f2d672094e/memory.md -->

# 自动化执行记录 · 周度记忆快照上传 GitHub

## 2026-10-26（首次执行）

**结果**：✅ 成功。46 文件上传全部成功、0 失败；远端 `main` 47 blob（含初始化遗留 `.gitkeep`）。
本地 commit `acc9b23 chore: 周度记忆快照`，6 文件 671 行**纯新增**。
仓库：https://github.com/v7g625qzqq-dotcom/ai-memory

### 本次踩坑（下次直接照抄）

1. **任务给的单根命令会丢历史** —— 只扫 `C:\Users\DELL\WorkBuddy` 会把 10-04/05/06/19/20
   和 MEMORY.md 覆盖成内容更少的版本，静默删掉 527 行。必须**同时扫 `D:\360Downloads` 下
   所有含 `.workbuddy/memory` 的工作区**（最新日志都在那边）。
2. **bash 传参禁用 `eval` + 字符串拼接** —— 反斜杠被转义吃掉，只扫到一半且覆盖了正确内容。
   改用数组 `ARGS+=(--root "$d")` 正常。
3. **提交前必须 `git diff --stat` 验纯增量** —— 只有 `+` 没有 `-` 才放行。

### 流程要点（沿用有效做法）

- `merge_memory.py --root` 可多次传（action=append），`--copy-identity` 拉身份三件套。
- 代理：`local_proxy.py --listen 127.0.0.1:8899 --upstream fan.596189.xyz:443` 后台跑，
  `netstat` 见 8899 LISTENING 再上传。沙箱会回收子进程，必须后台任务内自拉。
- 上传：Contents API 逐文件 PUT（**git push 在此环境代理下会挂起**），
  令牌从 Windows 凭据管理器自动读（`ghp_` 前缀 40 位）。
- 验证：`api.github.com/.../git/trees/main?recursive=1` 数 blob；
  `api.github.com/.../contents/{path}` base64 解码与本地逐字节比对
  （raw.githubusercontent.com 走代理超时，不可用）。
- 收尾：TaskStop 杀代理 → netstat 确认 8899 释放 → `switch_proxy.py restore` 还原注册表。
  本次系统代理本就未被改动（ProxyEnable 一直=0），restore 为无害兜底。

### 待改进

- 任务指令里的 `--root` 只有 C 盘一个，建议后续固定为「C 盘 + D 盘各工作区」双根。
- 可考虑在 `merge_memory.py` 内置 D 盘自动发现逻辑，避免每次手拼参数。
