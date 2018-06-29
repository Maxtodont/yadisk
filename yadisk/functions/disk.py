# -*- coding: utf-8 -*-

from ..api import DiskInfoRequest

__all__ = ["get_disk_info"]

def get_disk_info(session, **kwargs):
    """
        Get disk information.

        :param session: an instance of :any:`requests.Session` with prepared headers
        :param fields: list of keys to be included in the response

        :returns: :any:`DiskInfoObject`
    """

    request = DiskInfoRequest(session, **kwargs)
    request.send()

    return request.process()
