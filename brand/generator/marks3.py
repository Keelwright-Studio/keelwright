from marks import INK, PAPER, ACC, colors
def badge_(bg): return f'<rect width="64" height="64" rx="15" fill="{bg}"/>'
HX,HY=18,32
def legs(fg, tipcol=None, body=6, tip=3):
    tipcol=tipcol or fg
    r=f'<path d="M{HX} {HY} L39 17" stroke="{fg}" stroke-width="{body}" stroke-linecap="round"/>'
    r+=f'<path d="M{HX} {HY} L39 47" stroke="{fg}" stroke-width="{body}" stroke-linecap="round"/>'
    r+=f'<path d="M39 17 L47 9" stroke="{tipcol}" stroke-width="{tip}" stroke-linecap="round"/>'
    r+=f'<path d="M39 47 L47 55" stroke="{tipcol}" stroke-width="{tip}" stroke-linecap="round"/>'
    return r
def hinge(fg,bg): return f'<circle cx="{HX}" cy="{HY}" r="5" fill="{fg}"/><circle cx="{HX}" cy="{HY}" r="1.8" fill="{bg}"/>'

def k_dividers(size, ground, badge=True, accent=ACC):
    fg,bg=colors(ground); r=badge_(bg) if badge else ''
    r+=f'<path d="M{HX} 8 V56" stroke="{fg}" stroke-width="6" stroke-linecap="round"/>'
    r+=f'<path d="M47 9 A37 37 0 0 1 47 55" fill="none" stroke="{accent}" stroke-width="3" stroke-linecap="round"/>'
    r+=legs(fg)+hinge(fg,bg)
    return f'<svg width="{size}" height="{size}" viewBox="0 0 64 64" role="img" aria-label="Keelwright mark, K dividers">{r}</svg>'

def k_instrument(size, ground, badge=True, accent=ACC):
    fg,bg=colors(ground); r=badge_(bg) if badge else ''
    r+=f'<path d="M{HX} 14 V56" stroke="{fg}" stroke-width="6" stroke-linecap="round"/>'
    r+=f'<circle cx="{HX}" cy="10" r="4.5" fill="{fg}"/>'
    r+=legs(fg, tipcol=accent, body=6, tip=3.5)
    r+=f'<circle cx="{HX}" cy="{HY}" r="5.5" fill="{bg}" stroke="{fg}" stroke-width="3"/>'
    return f'<svg width="{size}" height="{size}" viewBox="0 0 64 64" role="img" aria-label="Keelwright mark, K instrument">{r}</svg>'

def k_course(size, ground, badge=True, accent=ACC):
    fg,bg=colors(ground); r=badge_(bg) if badge else ''
    r+=f'<path d="M{HX} 8 V56" stroke="{fg}" stroke-width="6" stroke-linecap="round"/>'
    r+=f'<path d="M47 9 A37 37 0 0 1 47 55" fill="none" stroke="{accent}" stroke-width="3" stroke-linecap="round" stroke-dasharray="1 6"/>'
    r+=legs(fg)+hinge(fg,bg)
    r+=f'<circle cx="47" cy="55" r="4" fill="{accent}"/>'
    return f'<svg width="{size}" height="{size}" viewBox="0 0 64 64" role="img" aria-label="Keelwright mark, K plotted course">{r}</svg>'

def k_solid(size, ground, badge=True, accent=ACC):
    # heavier, more letter-like: K whose arm and leg taper to points, hinge is a round joint, no arc; accent = the stem
    fg,bg=colors(ground); r=badge_(bg) if badge else ''
    r+=f'<path d="M{HX} 8 V56" stroke="{accent}" stroke-width="7" stroke-linecap="round"/>'
    r+=f'<path d="M{HX} {HY} L48 10" stroke="{fg}" stroke-width="7" stroke-linecap="round"/>'
    r+=f'<path d="M{HX} {HY} L48 54" stroke="{fg}" stroke-width="7" stroke-linecap="round"/>'
    r+=f'<circle cx="{HX}" cy="{HY}" r="6" fill="{fg}"/><circle cx="{HX}" cy="{HY}" r="2" fill="{bg}"/>'
    return f'<svg width="{size}" height="{size}" viewBox="0 0 64 64" role="img" aria-label="Keelwright mark, K joint">{r}</svg>'

KS={'K1':('The dividers K',k_dividers,'The K\'s arm and leg are the two legs of a pair of chart dividers, hinged on the stem; the cobalt arc is the distance they step off. Reads as a K first and an instrument second.'),
    'K2':('The instrument',k_instrument,'The same K drawn as the tool: a knurled knob on the stem, a screw hinge, needle points in cobalt. No arc, so the letter stays clean at 16 px.'),
    'K3':('The plotted course',k_course,'Dividers with a dotted cobalt course between the points and a fix at the end — a bearing laid off on a chart. The most storytelling; the dots go first when small.'),
    'K4':('The joint',k_solid,'Heaviest and most letter-like: cobalt stem, two ink legs on a round joint. Barely an instrument, but the strongest monogram of the set.')}

def k_final(size, ground, badge=True, accent=ACC, course=None):
    """K2 instrument; the dotted course appears at 48 px and above unless `course` forces it."""
    if course is None: course = size >= 48
    fg,bg=colors(ground); r=badge_(bg) if badge else ''
    r+=f'<path d="M{HX} 14 V56" stroke="{fg}" stroke-width="6" stroke-linecap="round"/>'
    r+=f'<circle cx="{HX}" cy="10" r="4.5" fill="{fg}"/>'
    if course:
        r+=f'<path d="M47 9 A37 37 0 0 1 47 55" fill="none" stroke="{accent}" stroke-width="3" stroke-linecap="round" stroke-dasharray="0.1 5.6"/>'
    r+=legs(fg, tipcol=accent, body=6, tip=3.5)
    r+=f'<circle cx="{HX}" cy="{HY}" r="5.5" fill="{bg}" stroke="{fg}" stroke-width="3"/>'
    body=r[len(badge_(bg)):] if badge else r
    r=(badge_(bg) if badge else '')+f'<g transform="translate(3 0)">{body}</g>'
    return f'<svg width="{size}" height="{size}" viewBox="0 0 64 64" role="img" aria-label="Keelwright mark">{r}</svg>'
