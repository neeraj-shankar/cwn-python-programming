##############################################################################
# + : add (plus).
# - : subtract (minus).
# x : multiply.
# / : divide.
# ** : power.
# % : modulo.
# << : left shift.
# >> : right shift.
# & : bit-wise AND.
# | : bit-wise OR.
# ^ : bit-wise XOR.
# ~ : bit-wise invert.
# < : less than.
# > : greater than.
# <= : less than or equal to.
# >= : greater than or equal to.
# == : equal to.
# != : not equal to.
# and : boolean AND.
# or : boolean OR.
# not : boolean NOT.
##############################################################################

##############################################################################
## Bitwise Operators:  used to perform operations at the bit-level. These
## operators work on integers and treat them as binary bit patterns.
##############################################################################

# bit-wise AND: Result bit 1,if both operand bits are 1;otherwise results bit 0.
a = 5
print(f"Binary of 5: {bin(a)}")
b = 3
res = a & b
print(f"Binary of 3: {bin(b)}")
print(f"Result of bit-wise AND: {res}")
