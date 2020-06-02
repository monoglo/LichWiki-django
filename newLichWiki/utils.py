from notifications.models import Notification


# TODO 自己的个人中心被评论
# TODO 自己的评论被评论
# TODO 自己创建的页面被修改
# TODO 自己的修改被修改
# TODO 私信 （前端）
def add_notification(n_title, n_text, receiver_user_id, sender_user_id=0):
    Notification.objects.create(
        n_title=n_title,
        n_text=n_text,
        n_receiver_user_id=receiver_user_id,
        n_sender_user_id=sender_user_id,
    )
