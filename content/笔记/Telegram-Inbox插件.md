[[obsidian插件]]

这是一个电报信息收集插件，可以将发送给自定义机器人的信息同步到obsidian的自定义页面。

## 模板元数据
### 可用数据

以下数据字段可用于自定义消息模板。请注意，某些字段可能并非所有邮件都存在：

- `message_id`：消息的唯一标识符。
- `origin_name`：与转发邮件的来源关联的名称（如果适用）。
- `origin_username`：与转发邮件的来源关联的用户名（如果适用）。
- `text`：消息的主要内容。
- `date`：发送消息的日期，格式为“YYYY-MM-DD”。
- `time`：发送消息的时间，格式为“HH：mm”。
- `name`：消息发件人的姓名。
- `username`：邮件发件人的用户名（如果可用）。
- `user_id`：邮件发件人的唯一标识符。
- `origin_link`：表示与转发邮件的来源关联的链接（如果适用）。

> 因为你应该使用或避免逃脱。`text``origin_link``{{{text}}}``{{&text}}`

### 基本


```
{{{text}}} - {{time}}
```

### 条件语句



```
{{#origin_link}}
[link]({{&origin_link}})
{{/origin_link}}
```