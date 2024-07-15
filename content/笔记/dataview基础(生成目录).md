[[obsidian插件]]

简介::可以用来索引属性进行数据整合。

[官方网站](https://blacksmithgu.github.io/obsidian-dataview/)
[dataview入门教程](https://zhuanlan.zhihu.com/p/409253101)
[高级进阶版](https://zhuanlan.zhihu.com/p/373623264)，真的是牛逼。让我想学js了。
[少数派介绍，这个看起来好酷](https://sspai.com/post/73958)，[[倒计时]]
**基本语法:**
```
```dataview
list（列表）/table（表格）/task    (表现形式)
from""（文件夹）/#(标签)      (检索范围，留空表示不筛选)
where contains(file.name(支持的元数据),"习惯")  (聚合条件)
sort(顺序排序) file.ctime(支持的元数据)/+desc(表示倒叙)
limit 5（数字可更改，限制显示条数）
```

- 可以显示的属性用```::```来表示。
- 可以改别名，author AS 作者。

**简单模板**
```dataview
list
from #
sort file.mtime desc
```


**元数据:**
- file.name:文件标题。
- file.folder:该文件所属文件夹的路径。
- file.path:完整的文件路径。
- file.link:文件的链接。
- file.size:文件的大小。
- file.ctime:文件创建日期(日期+时间)。
- file.cday:文件创建的日期(一个日期)。
- file.mtime: 文件上次修改的时间(日期+时间)。
- file.mday:文件上次修改的日期(一个日期)。
- file.tags: 笔记中所有标签的数组，子标签按每个级别细分，因此`# tag/1/2`将储存在数组中，作为`[# tag,# tag/1,# tag/1/2]`。
- file.etags:
- file.inlinks:指向此文件的所有传入链接的数组。
- file.outlinks:此文件所有的出站链接的数组。
- file.aliases:注释的所有别名数组。

form后面可以使用和(and)、或(or)进行条件筛选。

**显示当前页面所有元数据**
```
```dataview
TABLE this
WHERE file = this.file
```


**表格**
这样写（必须要有英文逗号）:
```text
table author,from,tags
```

