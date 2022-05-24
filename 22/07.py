from datetime import datetime
from math     import sin, pi
#==============================================================================
s_beg    = input( 'дата рождения ДД.ММ.ГГГГ: ' )
s_end    = input( 'дата расчета  ДД.ММ.ГГГГ: ' )
date_obj = lambda s_date: datetime.strptime( s_date, '%d.%m.%Y' )
T = ( date_obj(s_end) - date_obj(s_beg) ).days
for P in (23,28,33):
    print( sin( 2.0 * pi * T / P ) * 100 )