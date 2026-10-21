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
