Module geodata_harvester.write_logs
===================================

Functions
---------

    
`logging_addLevel(levelName, levelNum, methodName=None)`
:   Add new logging level to `logger`
    
    Credit to https://stackoverflow.com/a/35804945
    
    Args:
        levelName (_type_): Name of the logging level.
        levelNum (_type_): Numeric value of the logging level.
        methodName (_type_, optional): Name of the method to call. Defaults to None.
    
    Example:
    >>> addLoggingLevel('TRACE', logging.DEBUG - 5)
    >>> logging.getLogger(__name__).setLevel("TRACE")
    >>> logging.getLogger(__name__).trace('that worked')
    >>> logging.trace('so did this')
    >>> logging.TRACE
    5

    
`setup(path='data/debug', level='print')`
:   Set up the logging system for the AgReFed Data Harvester.
    
    Note that because this function is custom, 3 levels can be selected: "info", "print",
    "warning". Obviously, other levels are accessible, just not used (we assume that any level
    higher than WARNING should be in the log file, and not printed).
    
    Args:
        path (str, optional): path to log file. Defaults to "data/log".
        level (bool, optional): debug level. Defaults to "print". Valid options are "info", "print", and "warning".