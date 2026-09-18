#!/usr/bin/env python3
"""Interactive tools (vanilla JS, no dependencies). Rates mirror the price tables in data_core.SERVICES."""
import json

# material -> (label, low, high) installed $/sq ft — same ranges as the service price tables
RATES = [
    ("lvp_std", "Vinyl plank — standard LVP (12-mil)", 1.75, 3.25),
    ("lvp_mid", "Vinyl plank — mid-range SPC (20-mil)", 2.75, 5.50),
    ("lvp_prem", "Vinyl plank — premium SPC (22+ mil)", 4.25, 7.50),
    ("lam_mid", "Laminate — mid-range (10–12 mm, AC4)", 3.25, 5.00),
    ("lam_wr", "Laminate — water-resistant", 4.75, 7.00),
    ("eng_5", "Engineered hardwood — 5″ plank", 9.00, 12.00),
    ("eng_wide", "Engineered hardwood — 7–9″ wide plank", 11.00, 15.00),
    ("solid", "Solid hardwood — 3/4″ nail-down", 10.00, 14.00),
    ("tile_std", "Porcelain / ceramic tile — 12–18″", 6.00, 10.00),
    ("tile_lf", "Large-format porcelain — 24″+", 9.00, 15.00),
    ("tile_wood", "Wood-look porcelain plank", 8.00, 13.00),
    ("refinish", "Sand & refinish existing hardwood", 4.50, 7.00),
]
REMOVAL = [("none", "No removal (bare slab / new build)", 0, 0), ("soft", "Carpet, laminate or floating vinyl", 1.75, 3.25), ("tile", "Glued-down tile with thinset chip-out", 2.50, 4.50)]


def TOOLS(SERVICES, SERVICE_ORDER, YEAR):
    rates_js = json.dumps({k: [lo, hi] for k, _, lo, hi in RATES})
    rem_js = json.dumps({k: [lo, hi] for k, _, lo, hi in REMOVAL})
    mat_opts = "".join(f'<option value="{k}">{l} — ${lo:.2f}–${hi:.2f}/sq ft</option>' for k, l, lo, hi in RATES)
    rem_opts = "".join(f'<option value="{k}">{l}</option>' for k, l, _, _ in REMOVAL)

    calc = f"""<div class="tool" id="calc">
<div class="fg">
<label for="c-sf">Floor area (sq ft)<input id="c-sf" type="number" min="20" max="20000" value="1000" inputmode="numeric"></label>
<label for="c-w">Waste / cuts allowance<select id="c-w"><option value="0.07">7% — straight lay, simple rooms</option><option value="0.10" selected>10% — typical home</option><option value="0.15">15% — diagonal, herringbone, many angles</option></select></label>
<label class="full" for="c-m">Floor type<select id="c-m">{mat_opts}</select></label>
<label class="full" for="c-r">Old floor removal<select id="c-r">{rem_opts}</select></label>
<label for="c-l">Rooms needing slab leveling<input id="c-l" type="number" min="0" max="20" value="0" inputmode="numeric"></label>
<label for="c-b">New baseboard / quarter-round (linear ft)<input id="c-b" type="number" min="0" max="3000" value="0" inputmode="numeric"></label>
</div>
<div class="out" aria-live="polite"><div>Estimated installed total</div><b id="c-out">—</b><div id="c-break" style="font-size:.95rem;margin-top:.5rem"></div></div>
<p style="font-size:.86rem;color:var(--gray);margin:.9rem 0 0">Ranges use our {YEAR} Sarasota-area installed prices (material + labor). Slab leveling is figured at $250–$700 per room and trim at $2.50–$5.00 per linear foot. This is a planning range, not a quote.</p>
</div>
<script>
(function(){{var R={rates_js},X={rem_js},$=function(i){{return document.getElementById(i)}};
function f(n){{return '$'+Math.round(n).toLocaleString('en-US')}}
function go(){{var sf=Math.max(0,+$('c-sf').value||0),w=+$('c-w').value,m=R[$('c-m').value],r=X[$('c-r').value],lv=+$('c-l').value||0,bb=+$('c-b').value||0;
var a=sf*(1+w),lo=a*m[0]+sf*r[0]+lv*250+bb*2.5,hi=a*m[1]+sf*r[1]+lv*700+bb*5;
$('c-out').textContent=f(lo)+' – '+f(hi);
$('c-break').innerHTML='Flooring with '+Math.round(w*100)+'% waste: <strong>'+f(a*m[0])+' – '+f(a*m[1])+'</strong>'+(r[1]?' · Removal: <strong>'+f(sf*r[0])+' – '+f(sf*r[1])+'</strong>':'')+(lv?' · Leveling: <strong>'+f(lv*250)+' – '+f(lv*700)+'</strong>':'')+(bb?' · Trim: <strong>'+f(bb*2.5)+' – '+f(bb*5)+'</strong>':'')+'<br>That is about <strong>$'+(lo/Math.max(sf,1)).toFixed(2)+' – $'+(hi/Math.max(sf,1)).toFixed(2)+'</strong> per square foot, all in.'}}
['c-sf','c-w','c-m','c-r','c-l','c-b'].forEach(function(i){{$(i).addEventListener('input',go)}});go()}})();
</script>"""

    finder = """<div class="tool" id="finder">
<form id="fq">
<p><strong>1. Which rooms?</strong></p><div class="opt"><label><input type="radio" name="room" value="living" checked><span>Living areas / bedrooms</span></label><label><input type="radio" name="room" value="wet"><span>Kitchen, bath or laundry</span></label><label><input type="radio" name="room" value="whole"><span>Whole house</span></label></div>
<p><strong>2. What is under the floor?</strong></p><div class="opt"><label><input type="radio" name="sub" value="slab" checked><span>Concrete slab (most Florida homes)</span></label><label><input type="radio" name="sub" value="ply"><span>Plywood / second story</span></label><label><input type="radio" name="sub" value="condo"><span>Condo above the ground floor</span></label></div>
<p><strong>3. Pets or kids?</strong></p><div class="opt"><label><input type="radio" name="pets" value="no" checked><span>No</span></label><label><input type="radio" name="pets" value="yes"><span>Yes — claws, spills, accidents</span></label></div>
<p><strong>4. Flood zone or barrier island?</strong></p><div class="opt"><label><input type="radio" name="flood" value="no" checked><span>No</span></label><label><input type="radio" name="flood" value="yes"><span>Yes / not sure</span></label></div>
<p><strong>5. Is the home empty part of the year with the A/C turned up?</strong></p><div class="opt"><label><input type="radio" name="vac" value="no" checked><span>No, lived in year-round</span></label><label><input type="radio" name="vac" value="yes"><span>Yes — seasonal / snowbird</span></label></div>
<p><strong>6. Is it a rental?</strong></p><div class="opt"><label><input type="radio" name="str" value="no" checked><span>No</span></label><label><input type="radio" name="str" value="yes"><span>Yes — vacation or long-term rental</span></label></div>
<p><strong>7. Budget, installed?</strong></p><div class="opt"><label><input type="radio" name="bud" value="low"><span>Under $5 / sq ft</span></label><label><input type="radio" name="bud" value="mid" checked><span>$5–$10 / sq ft</span></label><label><input type="radio" name="bud" value="high"><span>$10+ / sq ft</span></label></div>
</form>
<div class="out" aria-live="polite" id="fq-out"></div></div>
<script>
(function(){var F={lvp:{n:'Luxury vinyl plank (SPC core)',u:'/vinyl-plank-flooring/'},tile:{n:'Porcelain tile',u:'/tile-installation/'},eng:{n:'Engineered hardwood',u:'/hardwood-flooring/'},lam:{n:'Water-resistant laminate',u:'/laminate-flooring/'}};
function v(n){return document.querySelector('#fq input[name='+n+']:checked').value}
function go(){var s={lvp:0,tile:0,eng:0,lam:0},why={lvp:[],tile:[],eng:[],lam:[]};
function add(k,p,t){s[k]+=p;if(t)why[k].push(t)}
var room=v('room'),sub=v('sub'),pets=v('pets'),fl=v('flood'),vac=v('vac'),st=v('str'),bud=v('bud');
if(room=='wet'){add('tile',4,'handles standing water in kitchens and baths');add('lvp',3,'waterproof core for wet rooms');add('eng',-3);add('lam',-2)}
if(room=='whole'){add('lvp',2,'one continuous floor through wet and dry rooms');add('tile',2,'runs through every room without transitions')}
if(room=='living'){add('eng',2,'real wood where water is not a daily risk');add('lvp',1);add('lam',1)}
if(sub=='slab'){add('lvp',2,'floats over a slab once moisture is tested');add('tile',2,'bonds directly to concrete');add('eng',1,'engineered planks can be glued to a tested slab')}
if(sub=='ply'){add('eng',2,'plywood subfloors take nail-down wood well');add('lam',1)}
if(sub=='condo'){add('lvp',3,'pairs with sound-rated underlayment most associations accept');add('eng',1,'works over an approved acoustic mat');add('tile',-1)}
if(pets=='yes'){add('lvp',3,'scratch- and accident-resistant');add('tile',3,'claws cannot mark porcelain');add('eng',-2);add('lam',1)}
if(fl=='yes'){add('tile',4,'porcelain is the flood-damage-resistant choice');add('lvp',1,'planks can sometimes be lifted, dried and relaid');add('eng',-3);add('lam',-3)}
if(vac=='yes'){add('tile',2,'indifferent to humidity swings in a closed-up house');add('lvp',2,'rigid core stays stable when the A/C is set high');add('eng',-2)}
if(st=='yes'){add('lvp',3,'cheap to repair between guests');add('tile',2,'survives sand, luggage and heavy turnover');add('eng',-2)}
if(bud=='low'){add('lvp',3,'fits an under-$5 installed budget');add('lam',3,'lowest cost wood look');add('eng',-4);add('tile',-1)}
if(bud=='mid'){add('lvp',1);add('tile',2,'mid-range porcelain fits $5–$10 installed')}
if(bud=='high'){add('eng',4,'wide-plank oak sits in the $10+ range');add('tile',1)}
var r=Object.keys(s).sort(function(a,b){return s[b]-s[a]}).slice(0,2);
document.getElementById('fq-out').innerHTML='<div>Best fit for your answers</div>'+r.map(function(k,i){return '<p style="margin:.6rem 0 0"><b style="font-size:1.2rem">'+(i+1)+'. '+F[k].n+'</b><br>'+(why[k].length?'Why: '+why[k].slice(0,3).join('; ')+'.':'A solid all-round fit.')+' <a href="'+F[k].u+'">See '+F[k].n.toLowerCase()+' in Sarasota →</a></p>'}).join('')+'<p style="font-size:.86rem;color:var(--gray);margin:.9rem 0 0">A slab moisture reading and a look at the subfloor can change the answer. That check is part of our free estimate.</p>'}
document.getElementById('fq').addEventListener('change',go);go()})();
</script>"""

    items = [
        ("Association name, unit number and floor level", "Rules differ by floor: ground-floor units on slab are often exempt from sound underlayment."),
        ("Current governing documents — declaration, rules and the architectural / alteration form", "Ask the manager for the newest version; flooring rules are often amended."),
        ("Required impact sound rating (IIC) and airborne rating (STC)", "Florida Building Code sets a baseline of 50 for both between dwelling units (45 if field tested); many associations write a higher number into their documents."),
        ("Underlayment product data sheet and the lab test report for the full floor assembly", "The report should name the slab thickness and floor type tested, not just the pad."),
        ("Flooring product specification sheet", "Thickness, core type, wear layer, and whether a pad is pre-attached."),
        ("Contractor certificate of insurance naming the association as certificate holder", "General liability and workers' compensation or exemption."),
        ("Contractor business tax receipt / local registration", "Some buildings also want a W-9."),
        ("Scope drawing or marked floor plan", "Which rooms change, where transitions land, and whether kitchens and baths are included."),
        ("Work schedule within the building's permitted hours", "Many Gulf-front buildings restrict noisy work to weekdays and ban it during season."),
        ("Elevator reservation, floor protection and debris plan", "Pads in the cab, corridor runners, and how tear-out leaves the building."),
        ("Refundable damage deposit, if required", "Get the amount and the refund conditions in writing."),
        ("Written approval letter before material is ordered", "Do not rely on a verbal OK from the front desk."),
        ("Post-install inspection or field sound test, if the documents call for one", "Know before you start who pays if a field test is required."),
    ]
    chk = "".join(f'<li style="list-style:none;margin:0 0 .7rem"><label style="display:flex;gap:.7rem;align-items:flex-start;cursor:pointer"><input type="checkbox" style="width:20px;height:20px;margin-top:.2rem;flex:none"><span><strong>{a}</strong><br><span style="color:var(--gray);font-size:.95rem">{b}</span></span></label></li>' for a, b in items)
    condo = f"""<div class="tool" id="condo"><p style="margin-top:0"><strong>Tick each item as you collect it.</strong> Your progress stays in this browser only.</p><ul style="padding:0;margin:0">{chk}</ul>
<div class="out"><b id="cd-n">0</b> of {len(items)} items ready · <a href="javascript:window.print()">Print this checklist</a></div></div>
<script>(function(){{var b=[].slice.call(document.querySelectorAll('#condo input')),K='sfc-condo';try{{var s=JSON.parse(localStorage.getItem(K)||'[]');b.forEach(function(x,i){{x.checked=!!s[i]}})}}catch(e){{}}
function u(){{document.getElementById('cd-n').textContent=b.filter(function(x){{return x.checked}}).length;try{{localStorage.setItem(K,JSON.stringify(b.map(function(x){{return x.checked}})))}}catch(e){{}}}}
b.forEach(function(x){{x.addEventListener('change',u)}});u()}})();</script>"""

    return [
        dict(slug="flooring-cost-calculator", crumb="Cost calculator", h1="Flooring Cost Calculator — Sarasota, FL",
             title=f"Flooring Cost Calculator Sarasota FL ({YEAR}) | Free Tool",
             description="Enter square footage, floor type, removal and slab prep to get a realistic installed price range for a Sarasota-area flooring project.",
             lede="Square footage in, realistic installed price range out — with removal, slab leveling and trim on their own lines.",
             capsule=f"This calculator multiplies your floor area (plus a waste allowance) by our {YEAR} installed price ranges for Sarasota and Manatee counties, then adds old-floor removal, slab leveling and baseboard. A 1,000 sq ft mid-range vinyl plank job with carpet removal lands around $4,900 to $9,600.",
             html=calc,
             notes_html="""<h2>How to read the result</h2><p>The low end assumes a flat, dry slab, a straight lay and an entry-level product in that category. The high end assumes a premium product and normal surprises. Three things push a Gulf Coast job past the high end: a slab that fails its moisture test and needs a mitigation coating, glued-down tile that needs grinding after removal, and furniture-heavy homes where rooms have to be done in phases.</p>
<h2>What the calculator leaves out</h2><ul><li>Moisture mitigation (epoxy or urethane barrier) when the slab reads above the flooring manufacturer's limit</li><li>Stairs — priced per tread, see <a href="/stair-treads/">stair treads</a></li><li>Showers and backsplashes — priced per project, see <a href="/tile-installation/">tile installation</a></li><li>Condo association fees, deposits and sound testing — see the <a href="/tools/condo-flooring-approval-checklist/">condo approval checklist</a></li></ul>
<p>For the reasoning behind each range, read the <a href="/cost/">flooring cost guides</a>.</p>"""),
        dict(slug="florida-flooring-finder", crumb="Flooring finder", h1="Florida Flooring Finder — Which Floor Fits Your Home?",
             title="Best Flooring for Florida Homes Quiz | Free Flooring Finder",
             description="Seven questions about rooms, slab, pets, flood risk, seasonal vacancy and budget. Get the two floor types that fit a Gulf Coast home, with reasons.",
             lede="Seven questions. Two recommendations. The reasoning shown, so you can argue with it.",
             capsule="The finder scores luxury vinyl plank, porcelain tile, engineered hardwood and water-resistant laminate against seven conditions that matter on the Gulf Coast: wet rooms, concrete slab or condo, pets, flood exposure, seasonal vacancy, rental use and budget. It returns the top two with the reasons that drove the score.",
             html=finder,
             notes_html="""<h2>Why these seven questions</h2><p>Most flooring quizzes ask about style. In coastal Florida the floor usually fails for other reasons: moisture coming up through a slab, a closed-up house in August, storm water, or a condo association that rejects the underlayment. The scoring weights those first and looks second.</p>
<p>Read more: <a href="/blog/">flooring answers</a> · <a href="/cost/">cost guides</a>.</p>"""),
        dict(slug="condo-flooring-approval-checklist", crumb="Condo approval checklist", h1="Condo Flooring Approval Checklist — Sarasota, Siesta Key &amp; Longboat Key",
             title="Condo Flooring Approval Checklist | Sarasota FL",
             description="The 13 items most Sarasota-area condo associations ask for before hard flooring goes in: IIC/STC ratings, underlayment test reports, insurance, schedule and more.",
             lede="What most associations want in the packet before tile, wood or vinyl plank replaces carpet above the ground floor.",
             capsule="Most Sarasota-area condo associations require written approval before hard flooring is installed above the ground floor. The packet usually includes the underlayment's impact sound (IIC) test report, the flooring specification, the contractor's certificate of insurance, a marked floor plan, a work schedule inside permitted hours and an elevator reservation. Requirements vary by building — your documents control.",
             html=condo,
             notes_html="""<h2>How we help</h2><p>We put the packet together for you: product data sheets, the assembly test report that matches your slab, our insurance certificate naming the association, and a schedule that respects the building's work hours. You sign the form; we do the paperwork.</p>
<p>Related: <a href="/vinyl-plank-flooring/">vinyl plank flooring</a> · <a href="/tile-installation/">tile installation</a> · <a href="/longboat-key/">Longboat Key</a> · <a href="/siesta-key/">Siesta Key</a>.</p>"""),
    ]
