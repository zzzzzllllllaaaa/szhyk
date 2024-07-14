[[使用quartz部署Obsidian部署步骤]]

[Configuration (jzhao.xyz)](https://quartz.jzhao.xyz/configuration)

## 常规配置

这部分配置涉及可能影响整个站点的任何内容。以下是一个列表，分解了您可以配置的所有内容：

- `pageTitle`：网站的标题。在为您的网站生成 [RSS 源](https://quartz.jzhao.xyz/features/RSS-Feed)时，也会使用此功能。
- `enableSPA`：是否在您的站点上启用 [SPA 路由](https://quartz.jzhao.xyz/features/SPA-Routing)
- `enablePopovers`：是否在您的网站上启用[弹出式预览](https://quartz.jzhao.xyz/features/popover-previews)。
- `analytics`：用于您网站上的分析的内容。值可以是
    - `null`：不要使用分析;
    - `{ provider: 'google', tagId: '<your-google-tag>' }`：使用Google Analytics;
    - `{ provider: 'plausible' }`（托管）或（自托管）：使用 [Plausible](https://plausible.io/)`{ provider: 'plausible', host: '<your-plausible-host>' }`;
    - `{ provider: 'umami', host: '<your-umami-host>', websiteId: '<your-umami-website-id>' }`：使用[鲜味](https://umami.is/);
    - `{ provider: 'goatcounter', websiteId: 'my-goatcounter-id' }`（托管）或（自托管）使用 [GoatCounter](https://goatcounter.com/)`{ provider: 'goatcounter', websiteId: 'my-goatcounter-id', host: 'my-goatcounter-domain.com', scriptSrc: 'https://my-url.to/counter.js' }`;
    - `{ provider: 'posthog', apiKey: '<your-posthog-project-apiKey>', host: '<your-posthog-host>' }`：使用 [Posthog](https://posthog.com/);
    - `{ provider: 'tinylytics', siteId: '<your-site-id>' }`：使用[Tinylytics](https://tinylytics.app/);
    - `{ provider: 'cabin' }`或（自定义域）：使用 [Cabin](https://withcabin.com/)`{ provider: 'cabin', host: 'https://cabin.example.com' }`;
- `locale`：用于 [I18n](https://quartz.jzhao.xyz/features/i18n) 和日期格式
- `baseUrl`：这用于需要绝对 URL 才能知道您网站的规范“主页”所在的站点地图和 RSS 源。这通常是您网站的已部署 URL（例如 对于本网站）。不要包含协议 （即 ） 或任何前导或尾随斜杠。`quartz.jzhao.xyz``https://`
    - 如果您在没有自定义域的 GitHub 页面上[托管](https://quartz.jzhao.xyz/hosting)，这也应该包括子路径。例如，如果我的仓库是 ，GitHub 页面将部署到 ，而 将是 。`jackyzha0/quartz``https://jackyzha0.github.io/quartz``baseUrl``jackyzha0.github.io/quartz`
    - 请注意，Quartz 4 将尽可能避免使用它，并尽可能使用相对 URL，以确保您的网站无论您最终_实际_部署在哪里都能正常工作。
- `ignorePatterns`：Quartz 在查找文件夹内的文件时应忽略且不应搜索的 [glob](https://en.wikipedia.org/wiki/Glob_(programming)) 模式列表。有关更多详细信息，请参阅[私人页面](https://quartz.jzhao.xyz/features/private-pages)。`content`
- `defaultDateType`：是否使用“创建”、“修改”或“发布”作为默认日期在页面和页面列表上显示。
- `theme`：配置站点的外观。
    - `cdnCaching`：如果（默认），请使用 Google CDN 缓存字体。这通常会更快。如果您希望 Quartz 下载自包含的字体，请禁用 （） 此功能。`true``false`
    - `typography`：要使用的字体。[Google Fonts](https://fonts.google.com/) 上可用的任何字体都可以在这里使用。
        - `header`：用于标题的字体
        - `code`：内联引号和块引号的字体。
        - `body`：适用于一切的字体
    - `colors`：控制网站的主题设置。
        - `light`：页面背景
        - `lightgray`：边界
        - `gray`：图形链接，较重的边框
        - `darkgray`：正文文本
        - `dark`：标题文本和图标
        - `secondary`：链接颜色，当前[图形](https://quartz.jzhao.xyz/features/graph-view)节点
        - `tertiary`：悬停状态和访问[的图形](https://quartz.jzhao.xyz/features/graph-view)节点
        - `highlight`：内部链接背景、高亮显示的文本、[高亮化的代码行](https://quartz.jzhao.xyz/features/syntax-highlighting)
        - `textHighlight`：Markdown 高亮显示文本背景


