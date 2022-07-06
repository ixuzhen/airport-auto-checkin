# （金坷垃）机场自动登录

`
bash envs.sh
# 修改config文件，换成自己的网站，用户名，密码
# 每天6点10分执行一次main.py
crontab -e
10 6 * * * python /home/user_name/airport_autocheckin/main.py
`