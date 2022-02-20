c.JupyterHub.port = 8000
# 指定暴露端口
c.PAMAuthenticator.encoding = 'utf8'
c.Authenticator.whitelist = {'admin', 'usr1', 'usr2', 'usr3'}
# 指定可使用用户
c.LocalAuthenticator.create_system_users = True
c.Authenticator.admin_users = {'admin'}
# 指定admin用户

c.JupyterHub.ssl_cert = '/jupyterhub_test/akkuma.net_bundle.pem'
c.JupyterHub.ssl_key = '/jupyterhub_test/akkuma.net.key'
#指定使用的证书
