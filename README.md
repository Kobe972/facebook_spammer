# facebook_spammer
如果你的facebook账户被无故封禁，给官方发邮件又得不到回复，可以用此仓库进行邮件轰炸，直到得到官方的回复。这个项目无需本地部署，会自动在每天凌晨给官方发一封邮件，邮件内容见content.txt
使用方法：
1. fork本仓库
2. 在Settings->Secrets and variables->Actions->Repository secrets中新建三个secret，名为FROM, TO, PASSWORD，分别为你的邮箱、facebook官方邮箱（比如disabled@fb.com）、你的邮箱密码
3. 在Actions中启动workflow
4. 如果想修改邮件内容，可以编辑content.txt

注意：如果你的邮箱不是outlook邮箱，需要更改代码中的smtp服务器地址。

希望facebook官方能解决因为使用代理被封禁的问题
