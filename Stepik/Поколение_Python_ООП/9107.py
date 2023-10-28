class Pagination:
    def __init__(self, s, n):
        t = 1
        self.d = {}
        for i in s:

            self.d[t] = self.d.get(t, []) + [i]
            if len(self.d[t]) == n:
                t += 1
        self.total_pages = len(self.d)
        self.current_page = 1

    def prev_page(self):
        if self.current_page != 1:
            self.current_page -= 1
        return self

    def next_page(self):
        if self.current_page != self.total_pages:
            self.current_page += 1
        return self

    def first_page(self):
        self.current_page = 1
        return self

    def last_page(self):
        self.current_page = self.total_pages
        return self

    def go_to_page(self, n):
        if n < 1:
            self.current_page = 1
        elif n > self.total_pages:
            self.current_page = self.total_pages
        else:
            self.current_page = n
        return self

    def get_visible_items(self):
        return self.d[self.current_page]


alphabet = list('abcd')

pagination = Pagination(alphabet, 4)
pagination.next_page()
print(pagination.get_visible_items())
