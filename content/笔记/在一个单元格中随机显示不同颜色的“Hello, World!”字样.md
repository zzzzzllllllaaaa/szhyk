---
dg-publish: true
---
[[宏]]

以下是一个简单而有趣的宏示例，这个宏会在一个单元格中随机显示不同颜色的“Hello, World!”字样。

**注意**：使用宏前，请确保保存了工作，因为宏有可能会覆盖或者改变现有的数据。

1. 打开Excel，按下 `Alt + F11` 打开VBA编辑器。

2. 在VBA编辑器中，选择“插入” > “模块”来创建一个新模块。

3. 在新模块中，复制并粘贴以下代码：

```vb
Sub RandomHelloWorld()
    Dim targetCell As Range
    Set targetCell = Application.InputBox("Select a cell", Type:=8) ' 选择一个单元格
    If Not targetCell Is Nothing Then
        With targetCell
            .Value = "Hello, World!" ' 设置文本
            ' 随机生成RGB颜色
            .Font.Color = RGB(Int((255 + 1) * Rnd), Int((255 + 1) * Rnd), Int((255 + 1) * Rnd))
            .Interior.Color = RGB(Int((255 + 1) * Rnd), Int((255 + 1) * Rnd), Int((255 + 1) * Rnd))
        End With
    End If
End Sub
```

4. 按下 `F5` 或点击“运行”按钮来执行宏。

5. 当提示选择单元格时，点击你想要显示“Hello, World!”的单元格，然后点击“确定”。

这个宏会将你选中的单元格填充以“Hello, World!”文本，并且随机改变字体和背景颜色。每次运行宏时，它都会产生不同的颜色组合，使得单元格看起来既有趣又多彩。

记得在使用宏之前，需要在Excel中启用宏功能。这通常需要在“选项”中找到“信任中心”，随后在“宏设置”中选择“启用所有宏”和“信任对VBA项目对象模型的访问”。由于宏有可能包含恶意代码，因此只应该启用来自可信来源的宏。