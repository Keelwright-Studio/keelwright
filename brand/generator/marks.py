# shared SVG mark definitions; ground = 'light'|'dark'
INK="#14213D"; PAPER="#FBF8F3"; ACC="#2D6AE3"
def colors(ground):
    return (INK, PAPER) if ground=='light' else (PAPER, INK)
def hull(size, ground, badge=True, accent=ACC):
    fg,bg=colors(ground)
    r=''
    if badge: r+=f'<rect width="64" height="64" rx="15" fill="{bg}"/>'
    r+=f'<path d="M6 21 L58 16 C 57 28, 48 37, 34 37 C 20 37, 8 33, 6 21 Z" fill="{fg}"/>'
    r+=f'<path d="M27 36 L30 54 H34 L36 36 Z" fill="{fg}"/>'
    r+=f'<path d="M13 34 V45" stroke="{fg}" stroke-width="3" stroke-linecap="round"/>'
    r+=f'<path d="M3 28 H61" stroke="{accent}" stroke-width="3" stroke-linecap="round"/>'
    return f'<svg width="{size}" height="{size}" viewBox="0 0 64 64" role="img" aria-label="Keelwright mark, hull">{r}</svg>'
def section(size, ground, badge=True, accent=ACC):
    fg,bg=colors(ground)
    r=''
    if badge: r+=f'<rect width="64" height="64" rx="15" fill="{bg}"/>'
    r+=f'<rect x="7" y="13" width="50" height="38" rx="4" fill="none" stroke="{fg}" stroke-width="3"/>'
    r+=f'<path d="M14 25 L50 22 C 49 31, 42 37, 33 37 C 23 37, 15 33, 14 25 Z" fill="{fg}"/>'
    r+=f'<path d="M11 29 H53" stroke="{accent}" stroke-width="3" stroke-linecap="round"/>'
    return f'<svg width="{size}" height="{size}" viewBox="0 0 64 64" role="img" aria-label="Keelwright mark, half-hull">{r}</svg>'
def kmono(size, ground, badge=True, accent=ACC):
    fg,bg=colors(ground)
    r=''
    if badge: r+=f'<rect width="64" height="64" rx="15" fill="{bg}"/>'
    r+=f'<path d="M22 8 V46" stroke="{fg}" stroke-width="6" stroke-linecap="round"/>'
    r+=f'<path d="M24 32 L44 12 M24 32 L44 52" fill="none" stroke="{fg}" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/>'
    r+=f'<path d="M19 44 L22 58 L25 44 Z" fill="{fg}"/>'
    r+=f'<path d="M10 44 H54" stroke="{accent}" stroke-width="3" stroke-linecap="round"/>'
    return f'<svg width="{size}" height="{size}" viewBox="0 0 64 64" role="img" aria-label="Keelwright mark, K monogram">{r}</svg>'
def keelline(size, ground, badge=True, accent=ACC):
    # D: a single keel line — long baseline with a fin, a hull "ghost" as a thin arc above
    fg,bg=colors(ground)
    r=''
    if badge: r+=f'<rect width="64" height="64" rx="15" fill="{bg}"/>'
    r+=f'<path d="M8 36 H56" stroke="{fg}" stroke-width="5" stroke-linecap="round"/>'
    r+=f'<path d="M29 36 L31 50 H33 L35 36 Z" fill="{fg}"/>'
    r+=f'<path d="M14 36 C 20 20, 44 20, 50 36" fill="none" stroke="{accent}" stroke-width="3" stroke-linecap="round"/>'
    return f'<svg width="{size}" height="{size}" viewBox="0 0 64 64" role="img" aria-label="Keelwright mark, keel line">{r}</svg>'
MARKS={'A':('The hull',hull,'A sailboat hull in profile, solid ink, with fin keel and rudder below a cobalt waterline. The most literal; reads as a boat at every size.'),
       'B':('The half-hull',section,"A half-hull model on its plaque — the thing a boatbuilder carves before building. Says 'wright' and 'craft'; the frame costs it some presence at 16 px."),
       'C':('The K',kmono,'A K whose stem runs below the waterline and ends in a keel. Works as a monogram and favicon; least nautical at small sizes.')}
