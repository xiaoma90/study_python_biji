import itchat

# 登陆微信
from requests import post

itchat.auto_login (hotReload=True)
# 获取好友列表
friends = itchat.get_friends ()
# API调用
apiUrl = 'http://www.tuling123.com/openapi/api'


# 获取文本消息
def get_response(message):
    data = {
        'key': '15a6882d3e8c4425930ab4e57d9b051a',
        'info': message,
        'userid': 'robot',
    }
    # 处理错误
    try:
        # 发送请求，返回数据
        r = post (apiUrl, data=data).json ()
        # print (r.get ('text'))
        return r['text']
    except Exception as e:
        print (repr (e))


# get_response ('爱你哟')

# 设置回复消息  是文本 TEXT   装饰器  给函数新增功能
@itchat.msg_register (itchat.content.TEXT)
# 回复给微信好友
def auto_reply(msg):
    defaultReply = '我知道了'
    realFriends = itchat.search_friends ('雨薇')
    realFriendsName = realFriends[0]['UserName']
    # 好友回复的消息
    reply = get_response (msg['Text']) or defaultReply
    if msg['FromUserName'] == realFriendsName:
        itchat.send (reply, toUserName=realFriendsName)


itchat.run ()
