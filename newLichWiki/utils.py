from notifications.models import Notification


def add_notification(n_title, n_text, receiver_user_id, sender_user_id=0):
    Notification.objects.create(
        n_title=n_title,
        n_text=n_text,
        n_receiver_user_id=receiver_user_id,
        n_sender_user_id=sender_user_id,
    )
