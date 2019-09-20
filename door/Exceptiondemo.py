"""
异常的处理
异常是指程序中的例外，违例情况；
在Python3中，BaseException是所以异常的基类，所以的内置异常都是它的派生类；
Exception是除了SystemExit，GeneratorExit和KeyboardInterrupt之外的所有内置异常的基类，用户自定义的异常也要继承它；
Python内的异常使用继承结构创建，可以在异常处理程序中捕获基类异常，也可以捕获子类异常；
*StopItertion 当迭代器中没有数据项时触发，由内置函数next()和迭代器的__next__()方法触发
*ArithmeticError 算法异常基类，包括OverflowError(溢出异常)，ZeroDivisionError(零除异常)，FloatingPointError(失败的浮点数操作)
*AssertionError assert语句失败时触发
*AttributeError 属性引用和属性赋值异常
*BufferError 缓存异常，当一个缓存相关的操作不能进行时触发
*EOFError 未见末尾，使用内置函数input()生成，标识到达文件末尾。但是如read()和readline()等大多数I/O操作将返回一个空字符串来表示EOF而不是引发异常
*ImportError 导入异常，当import语句或者from语句无法在模块中找到相应文件名称时触发
*LookupError 当使用映射或者序列时，如果键值或者索引无法找到的时候触发——(KeyError和IndexError的基类)
*MemoryError 内存错误，当操作超出内存范围时触发
*NameError 名称异常，在局部或者全局空间中无法找到文件名称时触发
*OSError 当一个系统函数返回一个系统相关的错误时触发
*ReferenceError 引用异常，当底层的对象呗销毁后访问弱引用是触发
*RuntimeError 包含其他分类中没有被包括进去的一般错误
*SyntaxError 语法错误
*SystemError 编译器的内部错误
*TypeError 类型异常，当操作或者函数应用到不合适的类型时触发
*ValueError 值异常，当操作或者函数的类型正确，但是值不正确时触发
"""