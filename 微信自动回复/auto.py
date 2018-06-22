# 微信自动回复  QQ小兵

import itchat

itchat.auto_login (hotReload=True)

listfriends = itchat.get_friends ()[0:]

for friend in listfriends:
    img = itchat.get_head_img (userName=friend['UserName'])

    # 路径
    path = "E:\\python_study\\study_1\\wechat\\headimg\\" + friend['NickName'] + '.jpg'
    print ('正在下载头像%s' % friend['UserName'])

    try:
        # 下载头像
        with open (path, 'wb') as f:
            f.write (img)
    except Exception as e:
        print (repr (e))
