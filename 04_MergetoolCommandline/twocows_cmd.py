import cmd
import cowsay
import shlex

class numbername(cmd.Cmd):
    prompt = "cmd>> "

    def do_list_cows(self, arg):
        """print a list of the available cow names"""
        if arg == '':
            print(cowsay.list_cows())
    
    def do_make_bubble(self, arg):
        """print text inside a bubble"""
        print(cowsay.make_bubble(arg))
    
    def do_cowsay(self, arg):
        """print a cowsay dialog between two cows
            cowsay сообщение [название] [параметр=значение …] reply ответ [название] [параметр=значение …]
            сообщение и ответ — это реплики двух персонажей
            название — это название коровы (должно поддерживаться достраивание)
            параметр=значение — это eyes и tongue, а значение — строка"""
        lst = shlex.split(arg)
        message = lst[0]
        cow = ''
        eyes = ''
        tongue = ''
        idx = 1
        if lst[1] in cowsay.list_cows():
            cow = lst[1]
            idx = 2
        for i in range(idx, lst.index('reply')):
            param = lst[i].split('=')
            if len(param) == 2:
                if param[0] == 'eyes':
                    eyes = param[1]
                elif param[0] == 'tongue':
                    tongue = param[1]
                else:
                    return
            else:
                return
        if cow != '':
            if eyes != '':
                if tongue != '':
                    result = cowsay.cowsay(message, cow=cow, eyes=eyes, tongue=tongue)
                else:
                    result = cowsay.cowsay(message, cow=cow, eyes=eyes)
            else:
                if tongue != '':
                    result = cowsay.cowsay(message, cow=cow, tongue=tongue)
                else:
                    result = cowsay.cowsay(message, cow=cow)
        else:
            if eyes != '':
                if tongue != '':
                    result = cowsay.cowsay(message, eyes=eyes, tongue=tongue)
                else:
                    result = cowsay.cowsay(message, eyes=eyes)
            else:
                if tongue != '':
                    result = cowsay.cowsay(message, tongue=tongue)
                else:
                    result = cowsay.cowsay(message)
        m1 = result.split('\n')
        
        ind = lst.index('reply') + 1
        message = lst[ind]
        cow = ''
        eyes = ''
        tongue = ''
        for i in range(ind + 1, len(lst)):
            if lst[i] in cowsay.list_cows():
                cow = lst[i]
            else:
                param = lst[i].split('=')
                if len(param) == 2:
                    if param[0] == 'eyes':
                        eyes = param[1]
                    elif param[0] == 'tongue':
                        tongue = param[1]
                    else:
                        return
                else:
                    return
        if cow != '':
            if eyes != '':
                if tongue != '':
                    result = cowsay.cowsay(message, cow=cow, eyes=eyes, tongue=tongue)
                else:
                    result = cowsay.cowsay(message, cow=cow, eyes=eyes)
            else:
                if tongue != '':
                    result = cowsay.cowsay(message, cow=cow, tongue=tongue)
                else:
                    result = cowsay.cowsay(message, cow=cow)
        else:
            if eyes != '':
                if tongue != '':
                    result = cowsay.cowsay(message, eyes=eyes, tongue=tongue)
                else:
                    result = cowsay.cowsay(message, eyes=eyes)
            else:
                if tongue != '':
                    result = cowsay.cowsay(message, tongue=tongue)
                else:
                    result = cowsay.cowsay(message)
        m2 = result.split('\n')
        if len(m1) < len(m2):
            m1 = [''] * (len(m2) - len(m1)) + m1
        if len(m2) < len(m1):
            m2 = [''] * (len(m1) - len(m2)) + m2

        for i in range(len(m1)):
            print(m1[i].ljust(len(max(m1, key=len)), ' ') + m2[i])
    
    def do_cowthink(self, arg):
        """print a cowthink dialog between two cows
            cowthink сообщение [название] [параметр=значение …] reply ответ [название] [параметр=значение …]
            сообщение и ответ — это реплики двух персонажей
            название — это название коровы (должно поддерживаться достраивание)
            параметр=значение — это eyes и tongue, а значение — строка"""
        lst = shlex.split(arg)
        message = lst[0]
        cow = ''
        eyes = ''
        tongue = ''
        idx = 1
        if lst[1] in cowsay.list_cows():
            cow = lst[1]
            idx = 2
        for i in range(idx, lst.index('reply')):
            param = lst[i].split('=')
            if len(param) == 2:
                if param[0] == 'eyes':
                    eyes = param[1]
                elif param[0] == 'tongue':
                    tongue = param[1]
                else:
                    return
            else:
                return
        if cow != '':
            if eyes != '':
                if tongue != '':
                    result = cowsay.cowthink(message, cow=cow, eyes=eyes, tongue=tongue)
                else:
                    result = cowsay.cowthink(message, cow=cow, eyes=eyes)
            else:
                if tongue != '':
                    result = cowsay.cowthink(message, cow=cow, tongue=tongue)
                else:
                    result = cowsay.cowthink(message, cow=cow)
        else:
            if eyes != '':
                if tongue != '':
                    result = cowsay.cowthink(message, eyes=eyes, tongue=tongue)
                else:
                    result = cowsay.cowthink(message, eyes=eyes)
            else:
                if tongue != '':
                    result = cowsay.cowthink(message, tongue=tongue)
                else:
                    result = cowsay.cowthink(message)
        m1 = result.split('\n')
        
        ind = lst.index('reply') + 1
        message = lst[ind]
        cow = ''
        eyes = ''
        tongue = ''
        for i in range(ind + 1, len(lst)):
            if lst[i] in cowsay.list_cows():
                cow = lst[i]
            else:
                param = lst[i].split('=')
                if len(param) == 2:
                    if param[0] == 'eyes':
                        eyes = param[1]
                    elif param[0] == 'tongue':
                        tongue = param[1]
                    else:
                        return
                else:
                    return
        if cow != '':
            if eyes != '':
                if tongue != '':
                    result = cowsay.cowthink(message, cow=cow, eyes=eyes, tongue=tongue)
                else:
                    result = cowsay.cowthink(message, cow=cow, eyes=eyes)
            else:
                if tongue != '':
                    result = cowsay.cowthink(message, cow=cow, tongue=tongue)
                else:
                    result = cowsay.cowthink(message, cow=cow)
        else:
            if eyes != '':
                if tongue != '':
                    result = cowsay.cowthink(message, eyes=eyes, tongue=tongue)
                else:
                    result = cowsay.cowthink(message, eyes=eyes)
            else:
                if tongue != '':
                    result = cowsay.cowthink(message, tongue=tongue)
                else:
                    result = cowsay.cowthink(message)
        m2 = result.split('\n')
        if len(m1) < len(m2):
            m1 = [''] * (len(m2) - len(m1)) + m1
        if len(m2) < len(m1):
            m2 = [''] * (len(m1) - len(m2)) + m2

        for i in range(len(m1)):
            print(m1[i].ljust(len(max(m1, key=len)), ' ') + m2[i])
    
    def complete_cowsay(self, text, line, begidx, endidx):
        lst = shlex.split(line + '.')
        DICT = cowsay.list_cows()
        if len(lst) == 3:
            return [c for c in DICT if c.startswith(text)]
        if 'reply' in lst and len(lst) == lst.index('reply') + 3:
            return [c for c in DICT if c.startswith(text)]


if __name__ == '__main__':
    numbername().cmdloop() 
