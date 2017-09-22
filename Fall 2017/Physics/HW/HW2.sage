var('x y z')
var('max')
max=0.5
disk = plot(((0.5*10^-9)/(2*(8.8*10^(-12))))*(1-(1+(0.3^2/z^2))^(-1)), (z, 0, max), gridlines=True)
sheet = plot(28.24858, (z, 0, max), color='red')
disk = disk + sheet
disk.save("Plots.png")
