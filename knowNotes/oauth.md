# What is oauth?
是一种不需要账户密码而直接通过第三方授权完成注册登陆的验证方式。

# What problem does oauth solve?
每次登陆都需要一个账户和密码的组合。若没有则需要注册。

# How does the oauth work?
比如用户在第三方S已经有了注册好的账户。当用户在登陆网站W的时候，W可以用过用户向S申请一个token，让W可以使用部分用户在S上的注册信息，来直接认证用户的身份并且直接登陆。S负责提供认证并且负责控制W所使用的token的访问权限。而用户也可以随时更改token的权限。
