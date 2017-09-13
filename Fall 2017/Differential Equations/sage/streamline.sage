var('x y')
p1 = streamline_plot((y, -x), (x, -2, 2), (y, -2, 2), color=(0,0,0))
p2 = plot_vector_field((y, -x), (x, -2, 2), (y, -2, 2), color=(0,1,1))
P = p1 + p2
P.save('streamline.png')


