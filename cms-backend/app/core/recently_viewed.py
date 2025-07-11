
import threading

class RecentViews:
    def __init__(self, max_items=10):
        self.data = {}
        self.lock = threading.Lock()
        self.max_items = max_items

    def add(self, user_id: int, article_id: int):
        with self.lock:
            lst = self.data.setdefault(user_id, [])
            if article_id in lst:
                lst.remove(article_id)
            lst.insert(0, article_id)
            if len(lst) > self.max_items:
                lst.pop()

    def get(self, user_id: int):
        return self.data.get(user_id, [])

recent_views = RecentViews()
