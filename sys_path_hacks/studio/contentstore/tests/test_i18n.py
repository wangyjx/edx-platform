from sys_path_hacks.warn import warn_deprecated_import

warn_deprecated_import('cms.djangoapps', 'contentstore.tests.test_i18n')

from cms.djangoapps.contentstore.tests.test_i18n import *
