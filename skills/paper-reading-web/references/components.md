# 固定阅读组件与装配契约

用户已指定的组件是默认固定实现，不再为新论文从零重做。资源在assets/reader-components/：shell.html、reader.css、reader.js、reading_server.py、reader_supervisor.py。用scripts/build_reader.py将论文内容装入，生成无CDN依赖的单HTML。新论文修改内容和术语映射，保留这些组件。只有用户另有要求才调整行为；不把词汇/数据/论文图片烘焙进组件。

## 固定模块
- 返回：reader-return初始hidden。点击内部链接记录阅读位置后才出现，position:fixed固定在视口底部；不是段落旁永久按钮。可连续多次跳转/逐级回退，恢复原面板和每面板文本滚动。普通段落start对齐，data-reader-card卡片打开并居中；长卡标题居中。
- 左下笔与图例：笔默认收起，展开不自动开启标黄；额外开启/关闭按钮控制选择标黄，关闭保留标记；撤销上一批跨段标记。图例单独展开/收起，2列3行，记住开关。笔图标与图例按钮同一行；手机控件紧凑且返回按钮避开左下区域。标记支持正文、图解与术语行内标签，使用稳定block id恢复。
- 随手记：右侧可收起，文字＋文件选择/粘贴截图、草稿、更新、删除/撤销、回复和位置链接。提交默认仅经同源/api/notes写当前论文reading-notes.json，下轮助手读取。用户已明确选择此模式，不是即时GPT回复，也不是浏览器离线笔记替代。接口不可用时禁用提交、保留草稿、明确提示。不得把API密钥放前端。
- 图阅读器：总览及每小图都拥有独立data-reader-panel、图片和完整讲解；tab切换同时显示对应二者。桌面和iPad横向图左文右独立滚动；≤600px竖排但保持触摸tabs与原图/文本切换。标签最小44px，可水平滚动，键盘左右键也可用。
- 大图：点击当前图片打开模态框、滚轮/双指缩放、单指/鼠标平移、复位和关闭；关闭/取消指针时不继续拖动。
- 知识卡与导航：data-reader-card表示知识卡或其他解释卡；全部展开/收起。目录及笔记章节从main section[data-section]的DOM顺序生成，避免编号与跳转顺序分裂。

## 论文内容HTML契约
每篇使用唯一paper-id；所有id全局唯一且重生成稳定。不要用全部论文共用的localStorage键。

```html
<section id="results-1" data-section="03 Results第一单元">
  <h2>用实际对象、方法和发现命名</h2>
  <p class="source">原文页码与小节</p>
  <div class="original">连续完整原文（默认可见）</div>
  <div class="translation">完整翻译</div>
  <p class="unit-summary" id="summary-1" data-highlight-block>一个明确结论模块</p>
  <p id="analysis-1" data-highlight-block>详细解释；可含术语卡链接</p>
  <div id="fig-1" class="reader-figure" data-reader-figure>
    <div class="reader-tabs" role="tablist" aria-label="图1面板">
      <button data-reader-tab="overview" role="tab" aria-controls="fig1-overview">整图</button>
      <button data-reader-tab="a" role="tab" aria-controls="fig1-a">a</button>
    </div>
    <div id="fig1-overview" class="reader-panel" data-reader-panel="overview" role="tabpanel">
      <div class="reader-image"><img data-reader-zoom src="data:image/..." alt="本文图1整图"></div>
      <div id="fig1-overview-text" class="reader-text">完整图注、翻译、概括、整图逻辑</div>
    </div>
    <div id="fig1-a" class="reader-panel" data-reader-panel="a" role="tabpanel" hidden>
      <div class="reader-image"><img data-reader-zoom src="data:image/..." alt="本文图1a，保留对应图例"></div>
      <div id="fig1-a-text" class="reader-text"><p id="fig1-a-reading" data-highlight-block>该面板完整独立带读</p></div>
    </div>
  </div>
</section>
<section id="knowledge" data-section="知识卡">
  <details id="concept-x" class="reader-card" data-reader-card><summary>概念</summary><p id="concept-x-text" data-highlight-block>定义、本文用途与证据读法。</p></details>
</section>
```

这是结构示意，真实交付必须替换所有示意内容、全部主图面板及实际来源。data-highlight-block用于不嵌套的叶级文字块（p/li/td等），每个有唯一稳定id；不能把整section和内部p同时作为标记块。术语用a.term.term-category，href指向实际卡，覆盖正文及每面板。

## 装配与运行
`python scripts/build_reader.py --content content.html --paper-id unique-id --out outputs/paper-reading.html`

`python assets/reader-components/reading_server.py --root outputs --port <本项目端口>`

服务为标准库Python，默认只绑定127.0.0.1；HTML本地可阅读，但提问仅在项目服务可用时提交。按当前平台安排独立于聊天进程的稳定运行，不将此命令临时进程当永久方案。维护JSON遵循共享锁/确认停服后复读和原子保存。

手机/iPad打开离线HTML可以切图，不等于能够向电脑提交笔记。若用户要在移动端也提交，需要另行授权并配置能访问同一项目队列的安全网络服务（认证/TLS等），不能默认开放局域网端口，也不能把127.0.0.1当电脑的跨设备地址。当前资源不实现网络发布或即时GPT API。

## 验证边界
scripts/test_components.py测试队列真实创建/更新/附件/并发追加及拒绝非法来源，不代表浏览器交互实测。交付新网页还需按acceptance.md在390×844、768×1024、1024×768、1280×900等视口实测全部tabs图文切换、底部返回出现/回退、两个折叠控件、跨术语标黄/撤销、长卡及文本滚动恢复。必须标明未测试的真机触摸能力；静态CSS和脚本语法检查不能替代它。

## 2026-10-11范围与控件验收
默认只生成完整首次阅读核心；进阶模块列名称供后续选择，不预生成。已有进阶移入第二组保留。展开笔不自动标黄，显式开关才启用；纯净开关保留链接与用户高亮；折叠不代替开关。导航复用细竖线浅绿当前项模块。检查PDF原生图像类型与字迹；不要以放大插值宣称清晰提升。

2026-10-11最新：取消共读记录模块及生成要求。图例与侧栏共用左边界；两列三行按内容宽度布局，每项不换行，不裁字，不靠无限缩小字体塞入。桌面左侧控件与正文留间距，窄屏检查安全宽度及返回按钮重叠。验收需看实际文字是否单行、是否遮正文，不能只确认CSS生效。

术语卡片容器标记data-reader-card-group，容器内提供一键展开/收起；组件自动补齐按钮，操作只作用于本组术语卡，不误展开复习答案或全页其他details。全文论证链默认附简洁流程框图：研究问题→各阶段方法与关键发现，箭头写上一证据不足/下一问题；并行实验明确标并行，不把论证顺序当成发生时间或因果链。用离线可用HTML/CSS或SVG，不依赖CDN；手机可纵向阅读，保留后面的完整讲解。

术语组最新控件：标题与单个切换按钮同一行，按钮靠最右；全部展开时显示“一键收起”，否则显示“一键展开”，点击完成相反操作。监听单卡展开状态以同步文字，按钮只操作当前术语组；窄屏保持同一行并检查不溢出。此要求替代双按钮/另起一行。

## 最新四区及紧凑笔工具
顺序固定为基础文章内容→知识区→进阶内容→进阶知识区。知识区放基础概念、术语卡与论证链；复习自检、读者总结与评议放进阶知识区。分区表示归属，不自动改变生成权限：读者总结仍按此前要求首次默认必需、全文最后；复习仍需用户选择。更新导航、DOM和笔记下拉，保留锚点。
笔图标与图例按钮在同一行。笔图标一直可见、图标不变，点击展开或折叠；展开只出现“开启/关闭”同一切换按钮及“撤销”。开关文案表示点击动作，默认“开启”，开启后显示“关闭”；收起时关闭标记模式而保留已有标黄。不再使用独立收起笔按钮。按钮紧凑但可操作，手机及桌面展开后整行不溢出，图例内容在下方保持两列三行。


## 独立后台运行
将reading_server.py和reader_supervisor.py复制到当前论文输出目录。Windows当前用户任务运行reader_supervisor.py --root 当前输出目录 --port 当前端口，而不是直接运行服务子进程；守护程序在子进程退出后重启，锁避免重复实例。按maintenance.md配置与验证任务，不能只设置RestartCount便声称快速自动恢复。
/API契约：/api/health仅返回ok和port，用于启动入口的小型检查；/source-paper.pdf仅提供当前项目明确命名的源PDF。保留现有/api/notes安全限制与持久记录。脚本test_reader_routes.py检查PDF/健康/来源限制，test_reader_supervisor.py在独立临时目录模拟崩溃、重复启动和主动停止；不得向真实笔记写测试内容。
停止维护时先运行reader_supervisor.py --root 当前输出目录 --port 当前端口 --stop，确认子进程退出，再停止后台任务；恢复时重新启动任务。守护程序监控不依赖GPT连接，但实际Codex重启存活仍须单独验证。

## 临时查阅与浮层交互（2026-10-13）
返回按钮仅在正文名词链接跳到知识卡、或明确标记data-reader-return的临时查阅链接之后出现；目录与普通章节导航不建立返回记录，并清除过时记录。返回后恢复页位置、面板选择及独立文字滚动；栈用尽隐藏按钮。不可把所有页内锚点都作为临时查阅。
随手记入口为右边缘竖排“随手记”书签，面板不设收起按钮；点面板外自动收起，Escape亦可收起。内部填写、附件选择和图片预览不误关；草稿及附件保留。
图片预览为居中留白窗口，桌面宽约68%、高约78%；平板约80%、手机约90%宽以保障读图。右上角圆形×，缩放工具左上；点遮罩或Escape关闭。拖动图片结束到外部不误判为遮罩点击；保留滚轮/拖动/双指缩放。打开预览不清除笔记草稿。
验收含：目录跳转无返回、知识跳转有返回且精确还原；随手记内点击不关/外点击关/草稿保留；预览圆形关闭与遮罩关闭、内点击不关、窄屏无溢出。

## 正式交付版本与备份数量
首次打开询问：覆盖（0历史备份）/保留1个备份/保留2个备份；最新版另计。保存到项目reader-settings.json，离线选择仅在浏览器内有效，不能冒充项目文件已写入。允许稍后选择并从版本设置更改，未选择时不擅自清理历史。
每次正式交付前读项目设置，使用scripts/publish_reader.py保存简称_vN.0_YYYY-MM-DD_HHMMSS.html（北京时间），网页显示版本及时间。保留latest+指定历史数量，按交付序列清理manifest所管的历史HTML，只操作本项目versions目录；不清理论文、图片、附件、笔记、个人标黄或任意用户文件。改变备份数量在下次交付生效，版本号单调递增，不依赖剩余文件数。工作稿小改/测试不生成正式版。固定paper-reading.html为最新入口；历史快照须离线完整、自带图/样式/脚本与可用PDF入口。先检查来源和功能再发布，桌面分享同步并保留可辨认版本名。首次交付选择前不编造已实施的备份策略。

### 最新桌面与拖图规则（替代此前桌面版本命名建议）
桌面固定一份同名最新版HTML，每次正式交付完成后覆盖该文件，不在桌面堆历史。工作项目versions目录保存版本号+北京时间命名的最新版及0/1/2历史备份；固定最新入口继续可用。发布用--desktop传当前已约定桌面路径，不删除其他桌面文件；HTML中显示当前版本及更新时间。未选择备份策略不清理历史。
正文图与预览图均draggable=false并阻止dragstart，避免原生图片拖拽抢占左键平移；不拦截contextmenu，保留右键保存图片。此行为不影响浏览器滚轮缩放、触控双指缩放和关闭操作。

随手记书签支持鼠标/触控沿最右边上下拖动，仅改变纵向位置；上下各留8px，不越出视口。移动超过6px区分拖动与点击，拖后不误开面板；正常点击与键盘激活仍切换。按论文ID在浏览器保存相对位置，刷新/尺寸变化时恢复并限制范围。拖动不修改笔记内容。
