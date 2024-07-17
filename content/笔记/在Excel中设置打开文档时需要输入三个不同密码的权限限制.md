---
dg-publish: true
---
[[宏]]

在Excel中，你不能直接设置一个工作簿在打开时需要输入三个不同的密码。Excel的保护机制只允许设置一个打开密码（Open Password）和一个修改密码（Modify Password）。

在这个宏中，我们将创建一个自动运行的宏，当工作簿被打开时，用户需要依次输入三个预设的密码。只有当所有的密码都正确时，用户才能访问工作簿的内容。

```vba
Private Sub Workbook_Open()
    Dim inputPassword As String
    Dim correctPasswords As Variant
    correctPasswords = Array("Password1", "Password2", "Password3") '将密码修改为你需要的密码
    
    Dim i As Integer
    For i = LBound(correctPasswords) To UBound(correctPasswords)
        inputPassword = InputBox("请输入密码 " & i + 1 & " 来解锁工作簿:", "安全验证")
        
        If inputPassword <> correctPasswords(i) Then
            MsgBox "密码错误，无法访问工作簿。"
            ThisWorkbook.Close False
            Exit Sub
        End If
    Next i
    
    MsgBox "所有密码正确，欢迎使用工作簿。"
End Sub
```

将上述代码复制到工作簿中的`ThisWorkbook`对象的VBA编辑器中。然后，保存工作簿并重新打开，你会发现每次打开工作簿时都会依次要求输入三个密码。

**请注意以下几点：**
- 这段代码仅在打开工作簿时运行，一旦你关闭了VBA编辑器并保存了工作簿，你将无法访问VBA编辑器来删除或更改这个宏，除非你知道所有的密码。
- 这种保护方式并不是特别安全，对于懂得VBA的用户来说，这些密码可以被绕过。
- 在使用这个宏之前，请确保宏已经被启用。
- 在分发含有这种宏的工作簿前，请确保接收者了解如何输入密码，并告知他们密码，以免造成数据无法访问的困扰。

如果需要更为复杂和安全的解决方案，你可能需要考虑使用其他的软件或服务来实现多重验证。