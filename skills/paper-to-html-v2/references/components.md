# 固定组件与页面装配要求
复用assets/reader-components中的shell.html、reader.css、reader.js、reading_server.py和reader_supervisor.py。论文专属文字、图片、术语映射与路径不烘焙进通用组件。交互和排版的唯一规范见page-and-navigation.md，数据/发布见maintenance.md；不要重新设计或从历史附录挑旧规则。

## 教学内容装配
术语发现和卡片解释遵循adaptive-concepts.md；审核后保存本文概念清单。可用build_reader.py的`--concepts 本文清单.json --concept-report 内部匹配报告.json`调用concept_markup.py，或用其mark_concepts函数处理正文。匹配器只链接文本节点，不发现概念、不生成卡片、不证明覆盖/理解；卡片目标必须先存在。作用于原文、译文、图注及解释的自然段，不把入口限制到解释段。语境歧义用scope_ids或人工标注解决，不套固定全篇词库。卡内关系链接由写作者明确组织，不自动密集标色。

新面板的正文讲解按[逐图讲解要求](panel-teaching-contract.md)保存，调用`scripts/teaching_contract.py`的`render_teaching`。`data-reader-teaching`内部包含`data-teaching-role="question"/"legend"/"reasoning"/"next"`，题注、译文和唯一结论仍放在之前。两个自然解释区域均须展开为自然段，局部图例用表格；不是把短explain切成几个空标题。新面板缺块时build/publish拒绝交付。旧版已认可布局保留，维护时核对同等语义内容。

## HTML结构说明
每篇唯一稳定data-paper-id；所有id全局唯一且续改稳定。主章节section[data-section]和data-reading-tier使用core/knowledge/advanced/advanced-knowledge，顺序对应四区，目录及笔记选项从实际DOM生成。
每主图data-reader-figure有整图与所有子图tab，每面板data-reader-panel有独立图片和reader-text。tab同时切图/文；reader-text有稳定id保存滚动。知识卡data-reader-card；整组data-reader-card-group。临时跳非卡片目的地须在链接加data-reader-return，普通章节链接不加。
data-highlight-block放不嵌套叶级块（p/li/td），每块稳定id；不要同时标section和内部p。术语a.term.term-category链接实际卡，不加角标。模板仅结构示意，真实网页不得保留占位图、示意内容或缺面板。

```html
<section id="results-1" data-section="03 Results第一单元" data-reading-tier="core">
  <h2>用实际对象、方法和发现命名</h2>
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
      <div id="fig1-a-text" class="reader-text">
        <!-- 原图注、完整翻译、唯一结论后，插入render_teaching输出；此处不以一个p代替完整教学 -->
      </div>
    </div>
  </div>
</section>
<section id="knowledge" data-section="知识卡" data-reading-tier="knowledge" data-reader-card-group>
  <details id="concept-x" class="reader-card" data-reader-card><summary>概念</summary><!-- 按adaptive-concepts.md写自足连贯解释，不以三个短提示代替认识建立。 --></details>
</section>
```

## 装配
`python scripts/build_reader.py --content content.html --paper-id unique-id --out outputs/paper-reading-working.html --reader-url http://127.0.0.1:当前端口/paper-reading.html`
reader-url只填当前项目经验证的loopback入口，便于桌面版打开项目设置；端口不跨设备通用。工作稿装配不等于正式交付，后续用publish_reader.py，见maintenance.md。
装配生成单HTML，图片由内容提供完整嵌入资源；工具不自动核对科学语义，不自动创建任务或启动服务。将两个服务脚本复制到论文输出目录，独立后台任务运行supervisor，工作稿更新不必重启服务。

## 能力边界
笔记仅通过同源/api/notes写项目；支持内容、截图、编辑历史、删除恢复和处理回复。断线草稿留浏览器，但当前组件没有自动补存/独立附件库功能，不能声称已做。移动端离线可读/切图，不等于能访问电脑loopback；跨设备项目提交须另行配置安全服务。
本地API：/api/health快速检查；/source-paper.pdf限定原PDF；/api/settings读写备份数量；/api/notes读写笔记。Origin/Host及输入限制保持；不默认公开端口，不放模型API密钥。
模板与脚本实际行为须按acceptance.md验证，CSS生效或面板计数不等于操作通过或用户理解。
