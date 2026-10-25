# 项目长期记忆（合并自各工作区 MEMORY.md）
> 本文件由多个工作区的 `MEMORY.md` 去重合并而成，内容按来源块保留。

---

<!-- source: C:/Users/DELL/WorkBuddy/2026-09-28-14-43-09/.workbuddy/memory/MEMORY.md -->

# 项目长期备注（chinmiss 店匠独立站）

## 必须记住的事实
- **店铺域名：`https://chinmiss.myshoplaza.com`**（myshoplaza，**没有 z**；带 z 的域名不存在）。curl 直连该站会 SSL 失败，要用浏览器访问。
- 真实前台专辑：`/collections/butane-lighters`、`/collections/kerosene-lighters`、`/collections/electric-arc-lighters`。
- 2026-10-19 时首页已装修上线（Jet Flame 轮播 + 三分类板块）；Electric Arc 板块曾有灰图待排查。
- 店匠 SSO 登录会话会过期（约 2-3 周），过期后进 /admin 跳 sso.shoplazza.com。

## 资产位置
- 产品图池：`cdp-driver/imgs_all/`（文件名 = 产品 uuid 前 8 位 + _序号，AVIF/WEBP/JPEG 混合）
- IG 素材包：工作区 `ig_pack/`（30 张 4:5 成图 + 头像 + manifest），文案 `ig_captions.csv`，手册 `Instagram启动包-2026-10-19.md`
- TikTok 包：工作区 `tt_videos/`（30 条 9:16 mp4）、`tt_captions.csv`、上传脚本 `tt_upload.js`（跑法：NODE_PATH 指向 node workspace 的 node_modules）

## Instagram 账号（2026-10-20 设）
- 账号 **@linshijin3**（林仕金），简介已设好（4 行英文 + www.pyro8.com）。
- **pyro8.com 是用户自己的域名**，TikTok 和 IG 简介都挂它；但 TikTok 30 条文案引导的还是 chinmiss.myshoplaza.com，两域名未统一。
- IG 网页版「网站」字段锁死，只能手机 App 设置（待用户手机操作）；简介里的 URL 纯文本不可点。
- 无调试端口操控用户 Chrome 的路线：UIA omnibox SetValue 写 `javascript:` + SetForegroundWindow + SendKeys Enter，PrintWindow 后台截图，title 写 IGX: 标记回传。**中文常量经地址栏会损坏，必须 \uXXXX 转义**。

## TikTok 账号与接管方式（2026-10-19 建）
- 账号 **@www.pyro8.com**（用户名=网址），昵称 "Tariff-free lighters"，简介挂 www.pyro8.com；30 条产品视频已全部发出。
- 接管浏览器：调试实例跑在 `C:\chrome-debug`（用户 Chrome 配置的完整拷贝，含 FanVPN 已连美国节点），端口 **9223**，用 Playwright connectOverCDP 接管。原 Chrome 配置在 `C:\Users\DELL\AppData\Local\Google\Chrome\User Data`（无调试端口）。
- Chrome 136+ 不允许默认配置目录开调试端口，必须拷配置到独立目录再启动；扩展目录用 fs.cpSync 会拷成空壳，要用 cp -r。
- 上传页三大坑：file input 直接 setInputFiles 无效（要点「选择视频」触发 filechooser）；文案框在视口外（scrollIntoView+focus 后键盘输入）；偶发整页「出错了」点重试即可。

## 收款渠道（2026-10-20 起）
- 店匠收款路径：设置→收款 = /admin/smart_apps/coral/payment/pay；PayPal 管理页 = /admin/smart_apps/coral/payment/providers/paypal；改动需点顶部「保存」。
- PayPal 方案已全开：PayPal/信用卡(跳转+Basic站内表单)/Apple Pay/Google Pay/Pay Later + 12种欧洲本地支付；ACDC 未解锁（需PayPal审批）；Shoplazza Payments 未申请（2%佣金，Pro 0%）；Stripe等卡通道未接。

## SEO 现状（2026-10-20 诊断）
- 域名 2026-09-30 注册，尚未被任何搜索引擎收录；无 GSC 验证。
- 已修：默认域名重定向开启（apex 301→www）；4 个专辑 SEO 标题/描述已写入。
- 未修：首页 title/desc 仍是 chinmiss；全站无 JSON-LD/hreflang；首页无 H1；图片 alt 大量为空；About/Contact/博客均 404。
- 专辑 SEO 入口：商品→商品专辑→点专辑→SEO 铅笔→勾「独立编辑」（否则禁用）→填→确定→保存。

## SEO 首页已优化（2026-10-20）
- 店铺名已改 Pyro8；已装官方 Website SEO App（/admin/smart_apps/shrew/website_seo），首页 title/desc/keywords 已配置并前台验证；appstore.shoplazza.com 国内可达（apps 子域不可达）。

## 无头自动化限制（2026-10-20 实测）
- Chrome 153：默认配置目录禁 --remote-debugging-port；拷贝/联接目录 Cookie 全丢（ABE 校验），登录态不可迁移 → 无头模式做不了任何需登录的操作。
- 屏外窗口方案可行：SetWindowPos 移到 (-2600,-1800) + UIA Invoke + omnibox javascript: 注入；--proxy-server=https://fan.596189.xyz:443 可替代 FanVPN 扩展（节点列表解密脚本 vpn_decrypt.js）。
- robots.txt 已自带 Sitemap: /sitemap.xml.gz；sitemap=180 产品+4 专辑，全部有效 → GSC 手动提交非必需。
- GSC sitemap 已于 2026-10-20 提交成功（UIA 自动化，回执"已成功提交"）；Google 网页登录已恢复（账号 林仕金 ls634063666@gmail.com）；店匠 SSO 仍需重新登录。
- "请求编入索引"入口 = GSC 每页顶部搜索框"检查...中的任何网址"→ 输 URL → 请求编入索引；2026-10-21 已执行：首页/butane/electric-arc 均已收录，kerosene 已提交索引请求。GSC 及 Google 全系必须用 --proxy-server=https://fan.596189.xyz:443 启动 Chrome，否则直连超时。
- 博客 2026-10-21 已上线首篇文章 /blog/butane-vs-kerosene-vs-electric-arc-lighters（选购指南，含三分类内链）；audit 里 /blogs/company 是主题配置字符串非真实死链。店匠博客 URL 结构 /blog/<slug>。
- FanVPN 扩展已从 Chrome 消失，联网一律用 --proxy-server=https://fan.596189.xyz:443（节点解密 cdp-driver/vpn_decrypt.js）；Chrome 无障碍树仅启动后约 1 分钟可用，UIA 自动化须趁新启动窗口完成。

## 店匠后台 UIA 自动化工具（2026-10-20 建，可复用）
- 工作区 `adm.js` + `adm.ps1`：通用后台操作器，动作 nav/dump/click/invoke/type/editlist/edittype/keysto/pasteto/keys/scroll/shot/read/move/clickwin/winrect。命令经 adm_cmd*.json（UTF-8）传入，node adm.js '{json}' 调用；手工 PowerShell 跑时勿用 adm.js 同名 cmd 文件（会互踩）。
- 关键经验：ValuePattern.SetValue 对 React 输入框有效；TinyMCE 走 Source code 对话框（Edit 无名按 AutomationId）；SEO 弹窗字段无名用 editlist 索引；SEO/专辑「独立编辑」必须先勾选；Focus-Verify 防止输入串到用户窗口（用户在用电脑时返回 FOREGROUND_BLOCKED）；窗口 resize/白屏后控件树错位必须 F5；rc-select 下拉选项鼠标点不中（未解决），键盘 {DOWN}+{ENTER} 会误触别的控件。
- 2026-10-20 已完成：JSON-LD 全站注入（Custom Code，前台已验证）；About Us (/pages/about-us) 与 Contact Us (/pages/contact-us) 两页已建+SEO。用户手动在页尾菜单挂好 About/Contact（已验证前台生效）。用户确认真实联系邮箱为 **lsj63@qq.com**，Contact 页正文已改为 mailto:lsj63@qq.com 并前台验证。页脚 Pyro8 栏文案 ✅ 深夜已发布并前台验证（"Premium butane, kerosene & electric arc lighters shipped tariff-free worldwide."，占位文案消失）。遗留：博客页 404。
- sitemap 只含产品+专辑，不含 pages → 页脚挂链是 pages 被爬取的主要入口。

## 商品描述重写完成（2026-10-21 深夜）
- **179/179 全量重写成功**（rewrite_desc.js，0 失败），前台验证通过；149 个视频块完整保留，图片重排保留。
- 分类分布：109 butane / 35 kerosene / 27 arc / 8 accessory（无 lighter 关键词=烟盒/雪茄剪/水烟，走中性模板）。
- **燃料发货口径（用户定）**：丁烷款带少量气体发货、测试过火、开箱即用；煤油款不含煤油（空运限制）需自行加注；电弧 USB 充电。写文案以此为准。
- 结构：hook 池（id 种子随机）+ 特征句（标题提取）+ 规格表（不编造尺寸）+ 燃料运输 + 保养 + 内链（3 专辑 + 2 博客）。翻译 app 自动本地化前台文案。
- adm2.ps1 已加 winTitle 窗口锁定（必须带，否则可能选错用户窗口）；GSC 5 篇博客待用户登录 Google 后提交（深链 inspect?resource_id=sc-domain%3Apyro8.com&id=...）。

## Chrome 联网代理架构定版（2026-10-22 实测定版）
- **`C:\chrome-debug` profile 里 FanVPN 扩展残留会覆盖 `--proxy-server`**（Chrome 出口变移动直连）→ Chrome 启动必须带 `--disable-extensions`，之后 `--proxy-server` 才生效。
- 节点 `fan.596189.xyz:443` 只支持 https 代理协议；且**到 *.gstatic.com / fonts.googleapis.com / google-analytics 阻断**（google.com/search/accounts 正常），Google 登录页会渲染但 JS 不加载、按钮无响应。
- 定版方案：Chrome `--proxy-server=http://127.0.0.1:8899` + `local_proxy.py` 分流（gstatic 等被断域名**直连 Google 中国边缘 IP 203.208.41.2**，其余走上游 TLS CONNECT）。live.js 已固化此配置。
- Google 登录页点击要 trusted 事件：JS click/坐标都无效时用 Playwright locator click。
- 不要用 Windows 系统代理方案：注册表 `https=` 前缀含义是"用 TLS 连代理"，与明文本地转发层冲突。

## 欧盟下单能力（2026-10-23 实测通过）
- **欧盟 27/27 国全部可下单**，运费 €7.54–23.36（均值 €10.27，测试商品 €10.14）。GB/NO/CH 也可，IS 冰岛无配送方案（本来就没上）。
- 结账国家下拉 69 国，欧盟 27 国全在；付款方式 = **Credit & debit card（Visa/MC/AMEX/Discover/JCB）+ PayPal**；无追加税费（含税 DDP 一致）。
- 语言前缀 /fr /de /es /it /nl /pl /pt = 200；/sv /da /el = 404；后台 `language_selector_enabled=false`（前台无语言切换器）。
- 最大转化隐患：**运费≈货值**，建议满额免运/阶梯运费；CY/MT 运费 €23.36 畸高。
- **代理节点 fan.365747.xyz 访问不了 `static.staticdj.com`（店匠支付脚本 CDN）→ 付款页「Network error/转圈」**。该 CDN 直连 200/0.84s。验支付方式必须用直连浏览器（host-resolver-rules + profile `C:\chrome-direct` + 端口 9226）。
- 结账自动化坑：结算按钮被翻译成「查看」（选 `button.cart__checkout`）；token 含连字符（`271326-00000012`）；地址必填是 `input#address`（`#address1` 只是门牌可选）；配送方式是可点 div 不是 radio；步骤链 contact_information→shipping_method→payment_method。

## GSC 资源 ID 与博客收录（2026-10-22）
- GSC 有效资源 ID 是 **`https://www.pyro8.com/`（网址前缀属性）**，不是 `sc-domain:pyro8.com`（网域属性会 not-verified）。裸进 `search.google.com/search-console` 自动落到正确资源。
- 5 篇博客已全部被 Google 收录（10-22 确认）：butane-vs-kerosene-vs-electric-arc-lighters / how-to-choose-windproof-lighter / lighter-gift-guide / how-to-refill-butane-lighter / electric-arc-lighter-guide。

## 店匠后台 API 速查（2026-10-23 实战验证，比 UI 稳 10 倍）
- **后台域是 `chinmiss.myshoplaza.com/admin/...`**（不是 pyro8.com）。**API 必须在该域调用**，在前台域调 `/admin/api/*` 会 401。
- 页面：`GET /admin/api/pages?page=0&limit=50`（**page 从 0 起**）／`GET|PUT|DELETE /admin/api/pages/{id}`／`POST /admin/api/pages`（`content` 是 HTML 字符串；handle 会按 title 重生成，建完回读 url）
- 菜单：`GET /admin/api/menus/detail?id=footer|header`／**保存只有 `POST /admin/api/menus/save`**（`PUT .../detail?id=` 一律 404；UI「添加」只改内存，「保存」才提交）。自定义 URL 项：`{id:0,origin_type:-1,type:'web',source_id:'0',url,url_obj:{type:'web',source_id:'0',url,title:''}}`
- 自定义代码：`POST /admin/api/admin/script-tag`（`{name, device:'all', display_scope:'online', event_type:'custom', src:'<script>..</script>'}`）；入口 `/admin/micro_apps/plugin-scripttag/custom`，表单要 React native setter 写 textarea
- 路径对照：页面管理 `/admin/smart_apps/store/page`（**不存在 /admin/pages**）｜菜单 `/admin/smart_apps/store/menus` → 点行进 `/admin/smart_apps/store/menu/footer`｜应用商店 `/admin/smart_apps/angora/app_store`
- 驱动：`live.js`（自拉 Chrome 9223 + 代理，已改绝对路径 require）+ `live_send.py`（通用命令发送器）；`ev.py` 只能发 eval。SPA 内点菜单不刷新、hook 保留；goto 会重置 hook。

## 欧盟合规状态（2026-10-23）
- 已完成：5 个政策页（privacy/terms/refund-returns/shipping-delivery/legal-notice）＋页脚挂链＋Cookie 同意横幅＋产品页 GPSR 合规块＋Contact 页 WhatsApp 18664598280 与二维码。
- 站点基础已达标：含税 DDP 价、欧元结算、50+ 国家（含全欧盟）与本地货币。
- **待办**：欧盟负责人（EU RP，约 €199/年，用户称办好再弄）→ 办好后更新 legal-notice 与 gpsr_block；EN 13869 儿童防护报告；新奇打火机排查；电弧款电池 EPR 注册。

## 无头自动化定版（2026-10-23 推翻旧结论）
- **能无头做店匠后台**：`HEADLESS=1` + 同一 `C:/chrome-debug` profile + **直连**（`LIVE_PROXY=none`）。cookie 在 headful/headless 间通用；旧结论「无头做不了登录」只对拷到新目录成立。
- 店匠 SSO 必须直连（走美国代理表单不渲染）；登录=点 `634063666@qq.com` 账户行。
- 前台 www.pyro8.com 必须 headful（headless 被 Cloudflare 拦）。
- 工具：`run_once.js <task.js> <json>` 单进程跑（spawn Chrome→CDP→执行→关闭），解决沙箱回收；`lib_login/lib_shot/lib_click`。
- 营销模块路径：rebate/serval/coupon/sales_pop(+ /setting)/subscription_popups/flashsale/micro_apps/micro-loyalty。
- 弹窗文案编辑器 = about:blank iframe 里的 TinyMCE（`body.mce-content-body`），只有首行能稳定改。满减活动金额框 React 受控改不动，需手动配。
- 已上线获客组件：WELCOME10/FRIEND5/THANKS5 三码 + 订阅弹窗（前台已验证）+ 浮窗通知。

## 获客组件现状（2026-10-23 晚）
- **订阅弹窗已删除**（用户明确讨厌弹窗，看到就关站）→ 以后不要再给用户装弹窗类组件，改内联/页脚表单。
- 优惠码 3 个在线：WELCOME10（首单10%）/ FRIEND5 / THANKS5；浮窗通知已开。
- **Omnisend 已完整打通并授权**（2026-10-23 17:00）：账号 `ls634063666@gmail.com` / 密码 `Pyro8Omni2026!` / Brand ID `6adb21a13589fec01408176a`（显示名 Pyro8）/ FREE 套餐 500 封·250 联系人；店匠后台 `/admin/micro_apps/omnisend/home` 显示「已授权」。
- Omnisend 反自动化三个坑（已全部解决，别再重试旧路）：① 它用 `www.recaptcha.net`，**只有直连通、走任何代理都 20s 超时** → `local_proxy.py` 已加 recaptcha.net 直连分支；② 邮箱确认只标记注册记录，**user 账号在 onboarding 第 3 步 Get started 后才创建**；③ onboarding 的 session **不跨浏览器进程**，必须同一个 run 里跑完 confirm→step1→step2→step3（`t_omni_finish.js`）。
- 店匠→Omnisend 授权：店匠后台**直连**点「前往授权」→ Omnisend `apps/consent` 点 Authorize access；headless 回调会被 Cloudflare 拦但**授权其实已生效**。
- 店小秘的速卖通买家邮箱**不可直接群发**（GDPR/AUP/发信域信誉）→ 只能做广告自定义受众 + 包裹卡扫码换同意。

---

<!-- source: D:/360Downloads/2026-10-05-11-29-16/.workbuddy/memory/MEMORY.md -->

# 项目长期记忆（店匠独立站 + 速卖通）

## 店铺与链路
- 店匠独立站：www.pyro8.com（店名 chinmiss），后台域名 chinmiss.myshoplaza.com；语言路由 /fr /de /es /it /nl /pl /pt /ko（主市场=美国，默认 en-US/USD）。
- 主力商品：打火机（约 205 款），货源/管理走店小秘 ERP；速卖通【个体户】打火机店铺约 90 款。
- 浏览器自动化：cdp-driver（Playwright-core Chrome + cmd.json/result.json 单槽队列），目录 `C:/Users/DELL/.workbuddy/binaries/node/workspace/cdp-driver`，Chrome 在 `C:/Users/DELL/.agent-browser/browsers/chrome-153.0.8010.36/chrome.exe`，profile 已登录店小秘+店匠后台。

## 独立站下单能力（2026-10-06 实测）
- 结账仅支持 32 国：EU-27 + NO/CH/GB/RS/KR。**美/加/澳/日/新等无法下单**（无运费方案）→ P0 待修。
- 8 语言路由全通，但前台无语言切换入口（language_selector_enabled=false），地区选择器只切货币。
- 支付仅 PayPal；欧洲本地支付(iDEAL/BLIK/EPS…)被 disable_local_funding 关闭。
- 单件($10.14)运费：欧 $7.99–9.03，韩 $3.50；约 $5.5–6/kg。首页横幅"Free Shipping Worldwide"与实际不符。
- 结账报价 API（不产生真实订单）：POST /api/checkout/price {order_token, calculate_shipping_line:true, step:"shipping_method", shipping_address:{country,country_code,province:"ALL",city,zip,...}} → data.shipping_info.shipping_lines。

## 关键坑
- 本机路由器 DNS(192.168.1.1) 污染 www.pyro8.com（假 IP 跳百度、证书报错假象）；权威 DNS 正确。浏览器验证需加 `--host-resolver-rules=MAP www.pyro8.com 104.17.247.119,MAP pyro8.com 216.120.131.66`。
- cdp-driver 单槽队列：批次运行期间绝不能另发指令；改脚本要改源模板 ui_one.js（run_B 是生成物会被覆盖）。
- 批次并发会成片误判 browser-crash；脚本已加原子锁+崩溃延后（defer_pids.txt）不拉黑。

## 视频补注入批次（终态）
- 865/875 完成；剩 10 个为店小秘硬校验失败（海关监管属性需人工刷新重设、自定义属性重名），需人工处理。

## 后台配送修复路径（2026-10-06 实测）
- 设置→物流 `/admin/smart_apps/loriot/shipping`；自定义方案「欧洲专线包税带电」悬浮→铅笔→「创建区域方案」加国家；点大洲名=整洲全选（北美=177 地区），需展开单选。确定才落库，Esc 不保存。
- 费率模型：首重 + 每克附加（500g 打火机欧洲运费 $8-9）。
- 技能：shoplazza-order-capability-audit（下单能力验证全流程）。

## 主题编辑器（装修自动化）
- 入口：/admin/smart_apps/store/theme →「编辑」→ /admin/card?theme_id=3fc49b61-39fd-4814-9510-f7c7d54704fb（Life Style）。编辑器加载慢，入口按钮需轮询重试。
- 公告栏文案：左栏「导航」→公告栏（contenteditable div，必须真实键入）；改完点顶栏 common.to_publish 发布+弹窗确认。
- 首页模板数据：GET /admin/api/theme-edit/{ose}/temp-template-datas/4df98411-4ae5-40c5-aab4-1113f7dcc3ee（ose 每次会话变，来自 create-oseid）；header/页尾是独立模板不在其中。
- 横幅文案已改 "Duties & Taxes Included. No Extra Fees."（2026-10-06，替代 Free Shipping）。

---

<!-- source: D:/360Downloads/2026-10-21-14-01-54/.workbuddy/memory/MEMORY.md -->

# 项目长期记忆 · 2026-10-21-14-01-54 工作区

## 记忆导出到 GitHub 的固定做法

**仓库**：https://github.com/v7g625qzqq-dotcom/ai-memory（Public，v7g625qzqq-dotcom/ai-memory）

### 铁律一：导出必须双根目录

`merge_memory.py` 的 `--root` 是 `action="append"`，可传多次。**只传一个根会静默丢历史**：

| 根目录 | 覆盖范围 |
|---|---|
| `C:\Users\DELL\WorkBuddy` | 08-07 ~ 10-23 的工作区日志（21 个 memory 目录） |
| `D:\360Downloads\2026-10-XX-XX-XX` | **10-04 ~ 10-25 的最新日志（18 个工作区）** |

只扫 C 盘会把 10-04/05/06/19/20 与 MEMORY.md 覆盖成更少内容的版本，git diff 显示 527 行删除。
→ 每次导出都用 `find D:/360Downloads -maxdepth 3 -type d -name memory -path "*.workbuddy*"`
   逐个追加为 `--root`。

### 铁律二：bash 传参禁用 eval

用 `eval` 拼 `--root "C:\\Users\\DELL\\WorkBuddy"` 会被反斜杠转义吃掉，只扫到一半。
必须用数组：

```bash
ARGS=(--out . --root "C:\Users\DELL\WorkBuddy" --copy-identity "<personal目录>")
while IFS= read -r d; do ARGS+=(--root "$d"); done < <(find ... )
"$PY" merge_memory.py "${ARGS[@]}"
```

### 铁律三：提交前验纯增量

`git diff --stat` 必须只有 `+` 没有 `-`，才允许提交。

### 上传链路（不要改）

- **必须用 Contents API 逐文件 PUT，`git push` 在此环境代理下会挂起**。
- 代理：`local_proxy.py --listen 127.0.0.1:8899 --upstream fan.596189.xyz:443`，
  后台任务启动（沙箱会回收子进程），netstat 确认 8899 LISTENING 再上传。
- 令牌在 Windows 凭据管理器，`upload_contents.py` 自动读取（`ghp_` 前缀 40 位）。
- 验证用 `api.github.com/.../git/trees/main?recursive=1` 数 blob +
  `api.github.com/.../contents/{path}` base64 比对；**raw.githubusercontent.com 走代理超时，不可用**。
- 收尾必做：TaskStop 杀代理 → netstat 确认 8899 释放 → `switch_proxy.py restore`。
- 辅助脚本 `verify_upload.py`（工作区根目录）做远端/本地逐字节一致性校验。

### 自动化任务

- 周度快照：`.workbuddy/memory/automations/da747ae2-952d-4693-be59-40f2d672094e/memory.md`
