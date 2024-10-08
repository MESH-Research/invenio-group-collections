# -*- coding: utf-8 -*-
#
# This file is part of the invenio-group-collections-kcworks package.
# Copyright (C) 2024, MESH Research.
#
# invenio-group-collections-kcworks is free software; you can redistribute it
# and/or modify it under the terms of the MIT License; see
# LICENSE file for more details.

"""Proxy entities for invenio-group-collections-kcworks."""

from flask import current_app
from werkzeug.local import LocalProxy

current_group_collections = LocalProxy(
    lambda: current_app.extensions["invenio-group-collections-kcworks"]
)
"""Proxy to the extension."""

current_group_collections_service = LocalProxy(
    lambda: current_group_collections.collections_service
)
"""Proxy to the extension."""
