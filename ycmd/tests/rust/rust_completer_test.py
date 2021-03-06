# Copyright (C) 2019 ycmd contributors
#
# This file is part of ycmd.
#
# ycmd is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# ycmd is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with ycmd.  If not, see <http://www.gnu.org/licenses/>.

from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
# Not installing aliases from python-future; it's unreliable and slow.
from builtins import *  # noqa

from mock import patch
from nose.tools import ok_, eq_

from ycmd import user_options_store
from ycmd.completers.rust.hook import GetCompleter


def GetCompleter_RlsFound_test():
  ok_( GetCompleter( user_options_store.GetAll() ) )


@patch( 'ycmd.completers.rust.rust_completer.RLS_EXECUTABLE', None )
def GetCompleter_RlsNotFound_test( *args ):
  ok_( not GetCompleter( user_options_store.GetAll() ) )


@patch( 'ycmd.completers.rust.rust_completer.GetExecutable',
        wraps = lambda x: x if x == 'rls' else None )
def GetCompleter_RlsFromUserOption_test( *args ):
  user_options = user_options_store.GetAll().copy( rls_binary_path = 'rls' )
  user_options = user_options.copy( rustc_binary_path = 'rustc' )
  eq_( 'rls', GetCompleter( user_options )._rls_binary_path )
  eq_( 'rustc', GetCompleter( user_options )._rustc_binary_path )


@patch( 'ycmd.completers.rust.rust_completer.RLS_EXECUTABLE', None )
def GetCompleter_RustcNotDefine_test( *args ):
  user_options = user_options_store.GetAll().copy( rls_binary_path = 'rls' )
  ok_( not GetCompleter( user_options ) )
