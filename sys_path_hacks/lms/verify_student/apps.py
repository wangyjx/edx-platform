from sys_path_hacks.warn import warn_deprecated_import

warn_deprecated_import('lms.djangoapps', 'verify_student.apps')

from lms.djangoapps.verify_student.apps import *
