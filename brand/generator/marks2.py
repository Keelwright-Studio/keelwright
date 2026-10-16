import math
from marks import INK, PAPER, ACC, colors
def badge_(bg): return f'<rect width="64" height="64" rx="15" fill="{bg}"/>'
def pt(cx,cy,r,a): return (cx+r*math.cos(math.radians(a)), cy+r*math.sin(math.radians(a)))

def wheel_full(size, ground, badge=True, accent=ACC):
    fg,bg=colors(ground); r=badge_(bg) if badge else ''
    cx=cy=32
    for i in range(8):
        a=i*45-90
        x1,y1=pt(cx,cy,5,a); x2,y2=pt(cx,cy,27,a)
        col=accent if i==0 else fg
        r+=f'<path d="M{x1:.1f} {y1:.1f} L{x2:.1f} {y2:.1f}" stroke="{col}" stroke-width="3.5" stroke-linecap="round"/>'
        hx,hy=pt(cx,cy,27.5,a); r+=f'<circle cx="{hx:.1f}" cy="{hy:.1f}" r="3" fill="{col}"/>'
    r+=f'<circle cx="32" cy="32" r="18" fill="none" stroke="{fg}" stroke-width="4"/>'
    r+=f'<circle cx="32" cy="32" r="6" fill="{fg}"/><circle cx="32" cy="32" r="2.2" fill="{bg}"/>'
    return f'<svg width="{size}" height="{size}" viewBox="0 0 64 64" role="img" aria-label="Keelwright mark, ship\'s wheel">{r}</svg>'

def wheel_king(size, ground, badge=True, accent=ACC):
    # six spokes, thick rim, the king spoke in accent, handles as rounded bars
    fg,bg=colors(ground); r=badge_(bg) if badge else ''
    cx=cy=32
    for i in range(6):
        a=i*60-90
        x1,y1=pt(cx,cy,0,a); x2,y2=pt(cx,cy,28.5,a)
        col=accent if i==0 else fg
        r+=f'<path d="M{x1:.1f} {y1:.1f} L{x2:.1f} {y2:.1f}" stroke="{col}" stroke-width="{5.5 if i==0 else 5}" stroke-linecap="round"/>'
    r+=f'<circle cx="32" cy="32" r="19" fill="none" stroke="{fg}" stroke-width="5.5"/>'
    r+=f'<circle cx="32" cy="32" r="7.5" fill="{bg}" stroke="{fg}" stroke-width="4"/>'
    return f'<svg width="{size}" height="{size}" viewBox="0 0 64 64" role="img" aria-label="Keelwright mark, wheel with king spoke">{r}</svg>'

def wheel_water(size, ground, badge=True, accent=ACC):
    # wheel rising from a waterline: upper part of an 8-spoke wheel, waterline across
    fg,bg=colors(ground); r=badge_(bg) if badge else ''
    cx,cy=32,38
    r+=f'<clipPath id="wclip{size}{ground}"><rect x="0" y="0" width="64" height="{cy}"/></clipPath><g clip-path="url(#wclip{size}{ground})">'
    for i in range(8):
        a=i*45-90
        x2,y2=pt(cx,cy,27,a)
        r+=f'<path d="M{cx} {cy} L{x2:.1f} {y2:.1f}" stroke="{fg}" stroke-width="3.5" stroke-linecap="round"/>'
        hx,hy=pt(cx,cy,27.5,a); r+=f'<circle cx="{hx:.1f}" cy="{hy:.1f}" r="3" fill="{fg}"/>'
    r+=f'<circle cx="{cx}" cy="{cy}" r="18" fill="none" stroke="{fg}" stroke-width="4"/>'
    r+=f'<circle cx="{cx}" cy="{cy}" r="6" fill="{fg}"/></g>'
    r+=f'<path d="M4 {cy} H60" stroke="{accent}" stroke-width="3.5" stroke-linecap="round"/>'
    return f'<svg width="{size}" height="{size}" viewBox="0 0 64 64" role="img" aria-label="Keelwright mark, wheel at the waterline">{r}</svg>'

def rose(size, ground, badge=True, accent=ACC):
    fg,bg=colors(ground); r=badge_(bg) if badge else ''
    r+=f'<circle cx="32" cy="32" r="25" fill="none" stroke="{fg}" stroke-width="2.5"/>'
    # four-point star: N in accent
    r+=f'<path d="M32 8 L36.5 27.5 L32 32 L27.5 27.5 Z" fill="{accent}"/>'
    r+=f'<path d="M32 56 L36.5 36.5 L32 32 L27.5 36.5 Z" fill="{fg}"/>'
    r+=f'<path d="M8 32 L27.5 27.5 L32 32 L27.5 36.5 Z" fill="{fg}"/>'
    r+=f'<path d="M56 32 L36.5 27.5 L32 32 L36.5 36.5 Z" fill="{fg}"/>'
    # small intercardinal ticks
    for a in (45,135,225,315):
        x1,y1=pt(32,32,20,a); x2,y2=pt(32,32,24,a)
        r+=f'<path d="M{x1:.1f} {y1:.1f} L{x2:.1f} {y2:.1f}" stroke="{fg}" stroke-width="2.5" stroke-linecap="round"/>'
    return f'<svg width="{size}" height="{size}" viewBox="0 0 64 64" role="img" aria-label="Keelwright mark, compass rose">{r}</svg>'

def needle(size, ground, badge=True, accent=ACC):
    fg,bg=colors(ground); r=badge_(bg) if badge else ''
    r+=f'<circle cx="32" cy="32" r="24" fill="none" stroke="{fg}" stroke-width="4"/>'
    for a in (-90,0,90,180):
        x1,y1=pt(32,32,19,a); x2,y2=pt(32,32,23,a)
        r+=f'<path d="M{x1:.1f} {y1:.1f} L{x2:.1f} {y2:.1f}" stroke="{fg}" stroke-width="3" stroke-linecap="round"/>'
    # needle pointing NE (-45deg)
    r+=f'<g transform="rotate(45 32 32)">'
    r+=f'<path d="M32 12 L37.5 32 L26.5 32 Z" fill="{accent}"/>'
    r+=f'<path d="M32 52 L37.5 32 L26.5 32 Z" fill="{fg}"/>'
    r+=f'</g><circle cx="32" cy="32" r="3.2" fill="{bg}"/>'
    return f'<svg width="{size}" height="{size}" viewBox="0 0 64 64" role="img" aria-label="Keelwright mark, compass needle">{r}</svg>'

def dividers(size, ground, badge=True, accent=ACC):
    # chart dividers: hinge at top, two legs, arc of the step in accent
    fg,bg=colors(ground); r=badge_(bg) if badge else ''
    r+=f'<path d="M32 14 L17 50" stroke="{fg}" stroke-width="4.5" stroke-linecap="round"/>'
    r+=f'<path d="M32 14 L47 50" stroke="{fg}" stroke-width="4.5" stroke-linecap="round"/>'
    r+=f'<circle cx="32" cy="13" r="5.5" fill="{fg}"/><circle cx="32" cy="13" r="2" fill="{bg}"/>'
    r+=f'<path d="M32 6 V13" stroke="{fg}" stroke-width="3" stroke-linecap="round"/>'
    r+=f'<path d="M14 52 C 20 56, 44 56, 50 52" fill="none" stroke="{accent}" stroke-width="3" stroke-linecap="round"/>'
    return f'<svg width="{size}" height="{size}" viewBox="0 0 64 64" role="img" aria-label="Keelwright mark, chart dividers">{r}</svg>'

WHEELS={'W1':('The wheel',wheel_full,'Eight spokes with turned handles, the king spoke picked out in cobalt — the one the helmsman feels for to know the rudder is centred. Literal and friendly; busiest at 16 px.'),
        'W2':('The king spoke',wheel_king,'Six heavy spokes, thick rim, open hub, no handles. Reads as a wheel and as a bold geometric badge; cleanest of the three small.'),
        'W3':('Wheel at the waterline',wheel_water,'The upper half of the wheel rising above the cobalt waterline. Keeps the studio\'s waterline motif; reads as a sunrise to some eyes.')}
COMPASSES={'N1':('The rose',rose,'A four-point compass rose in a thin ring, north in cobalt. Classic, balanced, trustworthy; the thin ring is the first thing lost at 16 px.'),
           'N2':('The needle',needle,'A heavy bezel with cardinal ticks and a needle swung to north-east, north half cobalt. More motion than the rose; strongest as a favicon.'),
           'N3':('The dividers',dividers,"Chart dividers stepping off a distance, the step arc in cobalt — the navigator's tool rather than the instrument. Says 'wright' and 'measure'; least compass-like.")}
