#!/usr/bin/env python

"""
  @package: TODO describe
   @script: ${app.py}
  @purpose: ${purpose}
  @created: Mon DD, YYYY
   @author: <B>H</B>ugo <B>S</B>aporetti <B>J</B>unior
   @mailto: yorevs@hotmail.com
"""
import signal
import sys

if len(sys.argv) > 1 and sys.argv[1].upper() == 'QT':
    from ui.qt.car_rental_qt import CarRentalQt as CarRental
else:
    from ui.shell.views.car_rental import CarRental as CarRental


def exit_app(sig=None, frame=None):
    print(frame)
    print('\033[2J\033[H')
    print('Bye.')
    print('')
    exit(sig)


# Application entry point
if __name__ == "__main__":
    signal.signal(signal.SIGINT, exit_app)
    CarRental().run()
    exit_app(0)
