from sys_path_hacks.warn import warn_deprecated_import

warn_deprecated_import('cms.djangoapps', 'contentstore.git_export_utils')

from cms.djangoapps.contentstore.git_export_utils import *
