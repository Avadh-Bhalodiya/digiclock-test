import weakref

from threading import currentThread

from django.core.paginator import Paginator
from django.conf import settings as dj_settings

from rest_framework.response import Response


def create_response(data, code, message=None, extra={}):
    extra["media_url"] = dj_settings.MEDIA_URL
    return Response(
        {"data": data, "message": message, "code": code, "extra": extra}, code
    )


def pagination_on_queryset(queryset, page, per_page_items):
    if not per_page_items:
        per_page_items = 10

    p = Paginator(queryset, per_page_items)

    try:
        page_instance = p.page(page)
    except Exception:  # noqa
        return {"page_count": p.num_pages}

    return {"page_count": p.num_pages, "data": page_instance.object_list}


class _ThreadContext(object):
    """
    Can be used to maintain a set of data required by application
    during a thread is running
    """

    def __init__(self):
        self.__context = weakref.WeakKeyDictionary()
        self.__block = weakref.WeakKeyDictionary()

    @property
    def _context(self):
        return self.__context.setdefault(currentThread(), {})

    @property
    def _block_data(self):
        return self.__block.setdefault(currentThread(), {})

    def set_data(self, **kwargs):
        self._context.update(kwargs)

    def unset_data(self, *args):
        for arg in args:
            self._context.pop(arg, None)

    def get_data(self, arg):
        return self._context.get(arg)

    def discard(self):
        return self.__context.pop(currentThread(), {})

    def __enter__(self):
        self._block_data.append(self.discard())
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.discard()
        if self._block_data:
            self.set_data(**self._block_data.pop())


ThreadContext = _ThreadContext()
