from graphics.rectangle import area as ra,perimeter as rp
from graphics.circle import area as ca,circumference as cp
from graphics.graphics_3d.cuboid import surface_area as cua,volume as cup
from graphics.graphics_3d.sphere import surface_area as sa,volume as sp

print("rectangle area:",ra(10,5))
print("rectangle perimeter:",rp(10,5))
print("\n circle area:",ca(7))
print("circle circumference:",cp(7))
print("\n cuboid surface_area:",cua(2,3,4))
print("cuboid volume:",cup(2,3,4))
print("\n sphere surface_area:",sa(5))
print("sphere volume:",sp(5))