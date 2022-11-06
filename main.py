#from os import close
import drawSvg as draw
import random




d = draw.Drawing(300, 300, origin='center', displayInline=False)
def draw_circle():# Draw a circle
    # hexa_format = ['#' + ''.join([random.choice('ABCDEF0123456789') for i in range(6)])]
    # hexa_format = str(hexa_format).replace('[', '').replace(']', '')
    # print(hexa_format)
    # print(type(hexa_format))
    x1 = random.randrange (100)
    y1 = random.randrange (100)
    r = random.randrange (30)
    d.append(draw.Circle(x1, y1, r, fill='pink', stroke_width=random.randrange(5), stroke='red'))

for i in range (0, 10):
    draw_circle()

def draw_rectangle():# Draw a rectangle
    x1 = random.randint (-100, 100)
    y1 = random.randint (-100, 100)
    w = random.randrange (30)
    h = random.randrange (50)
    d.append(draw.Rectangle(x1, y1, w, h, fill='#1248ff'))

for i in range (0, 10):
    draw_rectangle()

def draw_line(n):
    x = []
    y = []
    for i in range (0, n):
        x.append(random.randint (-100, 100))
        y.append(random.randint (-100, 100))
    d.append(draw.Lines(x[0], y[0],
                      x[1], y[1],
                      x[2], y[2],
                     close=False,
                    fill='#8a2be2',
                   stroke='black' ))

def draw_arc(): #Draw an arc
    x1 = random.randint (-100, 100)
    y1 = random.randint (-100, 100)
    r = random.randrange (30)
    start = random.randint (0, 180)
    end = random.randrange (start, 360)
    d.append(draw.Arc(x1,y1,r,start,end,cw=False,stroke='green', stroke_width=3, fill='none'))

for i in range (0, 10):
    draw_arc()

# Draw an irregular polygon
d.append(draw.Lines(-80, -45,
                    70, -49,
                    95, 49,
                    -90, 40,
                    close=False,
            fill='#eeee00',
            stroke='black'))

# Draw a rectangle
#r = draw.Rectangle(-80,0,40,50, fill='#1248ff')
#r.appendTitle("Our first rectangle")  # Add a tooltip
#d.append(r)



# Draw an arbitrary path (a triangle in this case)
#p = draw.Path(stroke_width=2, stroke='lime',
 #             fill='black', fill_opacity=0.2)
#p.M(-10, 20)  # Start path at point (-10, 20)
#p.C(30, -10, 30, 50, 70, 20)  # Draw a curve to (70, 20)
#d.append(p)

# Draw text
#d.append(draw.Text('Basic text', 8, -10, 35, fill='blue'))  # Text with font size 8
#d.append(draw.Text('Path text', 8, path=p, text_anchor='start', valign='middle'))
#d.append(draw.Text(['Multi-line', 'text'], 8, path=p, text_anchor='end'))

# Draw multiple circular arcs
#d.append(draw.ArcLine(60,-20,20,60,270,
#            stroke='red', stroke_width=5, fill='red', fill_opacity=0.2))
#d.append(draw.Arc(60,-20,20,60,270,cw=False,
#            stroke='green', stroke_width=3, fill='none'))
#d.append(draw.Arc(60,-20,20,270,60,cw=True,
#            stroke='blue', stroke_width=1, fill='black', fill_opacity=0.3))

# Draw arrows
#arrow = draw.Marker(-0.1, -0.5, 0.9, 0.5, scale=4, orient='auto')
#arrow.append(draw.Lines(-0.1, -0.5, -0.1, 0.5, 0.9, 0, fill='red', close=True))
#p = draw.Path(stroke='red', stroke_width=2, fill='none',
#              marker_end=arrow)  # Add an arrow to the end of a path
#p.M(20, -40).L(20, -27).L(0, -20)  # Chain multiple path operations
#d.append(p)
#d.append(draw.Line(30, -20, 0, -10,
#            stroke='red', stroke_width=2, fill='none',
#            marker_end=arrow))  # Add an arrow to the end of a line
draw_line(3)
d.setPixelScale(2)  # Set number of pixels per geometry unit
#d.setRenderSize(400,200)  # Alternative to setPixelScale
d.saveSvg('example.svg')
#d.savePng('example.png')


# Display in Jupyter notebook
#d.rasterize()  # Display as PNG
d  # Display as SVG

