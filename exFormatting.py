# source: https://pyformat.info/
# --- Basic formatting

print '%s %s' % ('one', 'two')
# old % and new format(...) style formatting
print '{} {}'.format('one', 'two')
print '%d %d' % (1, 2)
print '{} {}'.format(1, 2)
# arguments re-arranging that is not available in the old format styling
print '{1} {0}'.format(1, 2)


# --- Value conversion

class Data(object):
    def __str__(self):
        return 'str'

    def __repr__(self):
        return 'repr'


# s renders str(...) function, r repr(...)
print '%s %r' % (Data(), Data())
print '{0!s} {0!r}'.format(Data())

# --- Padding and aligning strings

print '%10s' % ('test',)  # align right
print '{:>10}'.format('test')

print '%-10s' % ('test',)  # align left
print '{:10}'.format('test')

print '%*s' % (-8, 'test')
print '%*s' % ((- 8), 'test')
