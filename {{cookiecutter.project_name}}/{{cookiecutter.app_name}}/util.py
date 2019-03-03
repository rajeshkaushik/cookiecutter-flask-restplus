from typing import Any
from typing import Dict
from typing import Optional
from typing import no_type_check
from typing import List


class AttributeDict(dict):
    """A dictionary-like object allowing indexed and attribute access."""

    def __init__(self, *args, **kwargs):
        # type: (*Dict[str, str], **Any) -> None
        super(AttributeDict, self).__init__(*args, **kwargs)
        self.__dict__ = self


def pluck(data, *keys):
    """
    Returns `keys` values from a dict.
    Good for multi assigning variables straight from a dict.
    """
    return [data.get(k) for k in keys]


def filter_dict(data, *keys):
    """
    Returns a smaller dict with just `keys`.
    """
    d = {}
    for k in keys:
        val = data.get(k)
        if val:
            d[k] = val
    return d


@no_type_check
def deep_get(d, path):
    # type: (Dict[str, Any], str) -> Optional[str]
    # safe return deep path (dot separated) in dict
    # otherwise return None
    cur = d
    for p in path.split("."):
        cur = cur.get(p)
        if not cur:
            return None
    return cur


def delim_split(delim_str, delim=","):
    # type: (str, str) -> List[str]
    return [x.strip() for x in delim_str.split(delim)]
