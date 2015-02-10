"""
Module with just two simply function to create default content for configuration files.

Used when configuration files can not be used for some reasons.
"""

def config():
    """
    Returns hardcoded tuple of strings with configuration data.

    Used when the configuration file doesn't exist.
    """
    t = tuple(  'fps_limit: 200;\r\n',
                'resolution: (400, 300);\r\n',
                'fullscreen: 0;\r\n',
                'debug: 0;\r\n',
    )
    return t

def keys():
    """
    Returns hardcoded tuple of strings with keys configuration.

    Used when the keys file doesn't exist.
    """
    t = tuple(  'K_p: pause;\r\n',
                'K_ESCAPE: quit;\r\n',
                'QUIT: quit;\r\n',
                'K_q: quit;\r\n',
    )
    return t