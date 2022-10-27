
from sqlalchemy.orm import Session

import string
from ipaddress import ip_address

from app.db.models import Visitor


def add_visitor_repo(db:Session, ip_address: string, url: string):

    visitor = Visitor(ip_address=ip_address, url=url)

    db.add(visitor)
    db.commit()
    db.refresh(visitor)
    return visitor
