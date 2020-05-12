from logbook import StreamHandler,Logger
import sys
StreamHandler(stream=sys.stdout).push_application()
log=Logger(name='Logbook')
log.info("Hello World")

