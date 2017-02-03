class DownMenuObject(object):

    def __init__(self, request, data):
        self.request = request
        self.id = data['id']
        self.name = data['name']
        self.url = data['url']

    @property
    def is_active(self):
        menu_id = getattr(self.request, 'menu_id', None)
        return self.id == menu_id


class TopMenuObject(object):

    def __init__(self, request, data, elements):
        self.request = request
        self.id = data['id']
        self.name = data['name']
        self.icon = data.get('icon', '')
        self.elements = elements

    @property
    def is_active(self):
        for element in self.elements:
            if element.is_active:
                return True
        return False


class MenuParser(object):
    TOP_MENU_CLS = TopMenuObject
    DOWN_MENU_CLS = DownMenuObject

    def __init__(self, elements):
        self.elements = elements

    def parse(self, request):
        self.request = request
        for top in self.elements:
            yield self._parse_top(top)

    def _parse_top(self, top):
        elements = [
            self.DOWN_MENU_CLS(self.request, element)
            for element in top.get('elements', [])]
        return TopMenuObject(self.request, top, elements)
