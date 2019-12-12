#自定义异常-----name 过长异常--继承
class NameTooLongError(Exception):
    err = 'name.long'
    print('自定义的NameTooLongError')
    def methFun(self):
        pass
#自定义异常-----name 过短异常--继承
class NameTooShortError(Exception):
    print('自定义的NameTooShortError')

def inputName():
    name = input('请输入用户名：')#5-10
    if len(name) > 10:
        raise NameTooLongError #自定义的异常要自行抛出
    elif len(name) < 5:
        raise NameTooShortError

if __name__ == '__main__':

    try:
        inputName()
    except NameTooShortError:
        print('您输入的用户名太短！')
    except NameTooLongError as e:
        print('您输入的用户名太长！',e.err)
        e.methFun()
    print('我在处理手机运营商操作')
    #--对手机号进行供应商鉴open