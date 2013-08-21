#
# This file is part of Fidus Writer <http://www.fiduswriter.org>
#
# Copyright (C) 2013 Takuto Kojima, Johannes Wilm
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from avatar.util import get_primary_avatar, get_default_avatar_url

def get_user_avatar_url(user):
    the_avatar = get_primary_avatar(user, 80)
    if the_avatar :
        the_avatar = the_avatar.avatar_url(80)
    else:
        the_avatar = get_default_avatar_url()
    return the_avatar