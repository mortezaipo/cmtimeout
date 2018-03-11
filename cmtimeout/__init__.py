"""ContextManager timeout handler library."""
import signal


class CMTimeOutException(Exception):
    """ContextManager timeout exception handler class."""

    pass


class CMTimeOut:
    """ContextManager timeout handler class."""

    def __init__(self, second, raise_error=False):
        """Initialize CMTimeOut class.

        :param second: timeout second
        :type second: int
        :param raise_error: raise error when timeout exceeded
        :type raise_error: bool
        """
        self._second = second
        self._raise_error = raise_error

    def __enter__(self):
        """Context manager enter action."""
        self._setup_handler()

    def __exit__(self, exception_class, exception_raised, tracebacak):
        """Context manager exit action.

        :param exception_class: main exception class
        :type exception_class: CMTimeOutException
        :param exception_raised: raised exception
        :type exception_raised: CMTimeOutException
        :param tracebacak: traceback object
        :type traceback: object
        """
        if exception_class is CMTimeOutException:
            if not self._raise_error:
                return True
            return False

    def _setup_handler(self):
        """Set related signals.

        :return: None
        :rtype: None
        """
        signal.signal(signal.SIGALRM, self._timeout_handler)
        signal.alarm(self._second)

    def _timeout_handler(self, signum, frame):
        """Handle timeout situation.

        :param signum: signal number
        :param signum: int
        :param frame: frame object
        :type frame: object

        :return: None
        :rtype: None
        """
        raise CMTimeOutException("ContextManager timeout exceeded.")
