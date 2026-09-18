# 02 - Real questions people ask about residential flooring (Sarasota / Florida Gulf Coast)

Site: **sarasotaflooringcompany.com** - Date: **2026-09-18** - Companion file: `02-questions.json`

## How this was researched (and what 'evidence' means here)

Live WebSearch + WebFetch on 2026-09-18. Important limits of the tooling, so the labels are read honestly:

- **Reddit was not reachable** (the search backend refuses `reddit.com` and `site:reddit.com` returns nothing). No question below is labelled REDDIT. This is the main sourcing gap - see the end of the file.
- The Google **People-also-ask widget and autocomplete dropdown cannot be rendered** by the tool. `PAA` here means: the question was seen verbatim or near-verbatim as a SERP title or as an FAQ entry on a publisher cost guide (This Old House, Angi, HomeGuide, HomeAdvisor) - those FAQ blocks are built from PAA data. No question is labelled AUTOCOMPLETE.
- `HOUZZ` / `QUORA` = a real thread with that question (URL given). `COMPETITOR-FAQ` = FAQ on a Florida flooring/removal company site. `MANUFACTURER-FAQ` = TCNA, NWFA, Shaw, COREtec, Mohawk, Pergo material. `AI-PROMPT` = conversational phrasing people give ChatGPT/Perplexity/Gemini. `EXPERT-GAP` = a question the sources imply but nobody answers well (opportunity).
- Angi, HomeGuide and acousticalsolutions.com block direct fetching (HTTP 403); their numbers come from search-index snippets and are marked for on-page verification where it matters. This Old House, HomeAdvisor, homeyou, Remove Right, TCNA, UF/IFAS, Yext, SOCi were fetched directly.
- Any number that could not be tied to a source says **needs source**. Nothing was filled in from memory without that flag, except the high-humidity wood EMC values which are flagged 'verify'.

Priority: **P1** = deserves its own post; **P2** = answer inside a service/FAQ page; **P3** = nice to have. `FL` = Florida / Gulf Coast / Sarasota angle.

## Totals

- Questions: **129** - P1: **79** - Florida-angle: **72** - questions containing at least one 'needs source' fact: **23**

| Cluster | Questions | P1 |
|---|---|---|
| cost | 9 | 6 |
| material-choice/comparison | 9 | 4 |
| florida-humidity-moisture | 8 | 6 |
| concrete-slab-subfloor | 8 | 6 |
| condo-hoa-sound | 10 | 7 |
| installation-process-timeline | 8 | 5 |
| hardwood | 7 | 2 |
| lvp-vinyl | 7 | 5 |
| tile | 7 | 4 |
| laminate | 6 | 3 |
| stairs | 5 | 3 |
| repair-refinish | 7 | 5 |
| pets-kids | 5 | 2 |
| water-flood-hurricane | 7 | 6 |
| maintenance-cleaning | 5 | 2 |
| hiring-a-contractor | 6 | 3 |
| permits-licensing | 5 | 3 |
| vacation-rental-investor | 5 | 4 |
| resale-value | 5 | 3 |

| Evidence type | Count |
|---|---|
| PAA | 48 |
| COMPETITOR-FAQ | 25 |
| EXPERT-GAP | 17 |
| HOUZZ | 14 |
| AI-PROMPT | 11 |
| MANUFACTURER-FAQ | 8 |
| QUORA | 6 |

## Questions by cluster

### cost

**1. How much does it cost to install vinyl plank flooring in Sarasota, FL?**
- cluster: `cost` | intent: `cost` | priority: **P1** | FL
- evidence: AI-PROMPT - https://www.homeyou.com/fl/flooring-installation-sarasota-costs
- short_answer_facts:
  - This Old House (updated 06/05/2026): vinyl plank materials $2-$7/sq ft, LVP materials $3-$10/sq ft, labor $3-$10/sq ft; combined $5-$17/sq ft (standard plank) and $6-$20/sq ft (LVP) (https://www.thisoldhouse.com/flooring/cost-to-install-vinyl-plank-flooring)
  - homeyou Sarasota page (dated Aug 12, 2026): typical Sarasota flooring installation project $799-$6,002; vinyl/linoleum $2.50-$4/sq ft, laminate $5.50-$6/sq ft, wood about $8/sq ft (https://www.homeyou.com/fl/flooring-installation-sarasota-costs)
  - Remove Right SW Florida guide (Feb 18, 2026): ceramic/porcelain tile removal $2.50-$4.50/sq ft, $4.00-$6.50+/sq ft on a thick mortar bed; light thinset grinding adds $0.75-$1.25/sq ft (https://removeright.com/floor-removal-cost-guide-southwest-florida/)

**2. How much does it cost to install 1,000 square feet of vinyl flooring?**
- cluster: `cost` | intent: `cost` | priority: **P1**
- evidence: PAA - https://www.thisoldhouse.com/flooring/cost-to-install-vinyl-plank-flooring
- short_answer_facts:
  - This Old House (updated 06/05/2026): vinyl plank materials $2-$7/sq ft, LVP materials $3-$10/sq ft, labor $3-$10/sq ft; combined $5-$17/sq ft (standard plank) and $6-$20/sq ft (LVP) (https://www.thisoldhouse.com/flooring/cost-to-install-vinyl-plank-flooring)
  - At $6-$20/sq ft installed (TOH LVP range) 1,000 sq ft is roughly $6,000-$20,000 before demo and slab prep (https://www.thisoldhouse.com/flooring/cost-to-install-vinyl-plank-flooring)
  - Remove Right SW Florida guide (Feb 18, 2026): click LVP removal $1.00-$2.50/sq ft, glue-down hardwood $3.00-$4.50/sq ft, stretch-in carpet $0.50-$1.25/sq ft (https://removeright.com/floor-removal-cost-guide-southwest-florida/)

**3. How much does hardwood flooring cost per square foot installed?**
- cluster: `cost` | intent: `cost` | priority: **P1**
- evidence: PAA - https://homeguide.com/costs/hardwood-flooring-cost
- short_answer_facts:
  - HomeGuide (2026): hardwood $9-$25/sq ft installed; solid $11-$25, engineered $9-$20; a 2,000 sq ft home runs $14,000-$50,000 (https://homeguide.com/costs/hardwood-flooring-cost)
  - Angi (2026 data, 10,984 projects): average hardwood install project $4,723, typical range $2,469-$7,034; $6-$12/sq ft installed, $13-$25/sq ft for premium species (https://www.angi.com/articles/how-much-does-hardwood-flooring-cost.htm)
  - Glue-down engineered on slab adds moisture mitigation/adhesive cost - dollar figure: needs source

**4. How much does porcelain tile installation cost per square foot?**
- cluster: `cost` | intent: `cost` | priority: **P1**
- evidence: PAA - https://homeguide.com/costs/porcelain-tile-flooring-installation-cost
- short_answer_facts:
  - HomeGuide (2026): porcelain tile floor installation $15-$50/sq ft installed; labor alone $12-$30/sq ft (verify range on page - fetch was blocked, figures from search snippet) (https://homeguide.com/costs/porcelain-tile-flooring-installation-cost)
  - ANSI A108.02: for tile with any edge 15 in. or longer the substrate may vary no more than 1/8 in. in 10 ft and 1/16 in. in 24 in. (https://www.ceramictilefoundation.org/blog/floor-or-wall-flat-enough-for-large-format-tile)
  - Remove Right SW Florida guide (Feb 18, 2026): ceramic/porcelain tile removal $2.50-$4.50/sq ft, $4.00-$6.50+/sq ft on a thick mortar bed; light thinset grinding adds $0.75-$1.25/sq ft (https://removeright.com/floor-removal-cost-guide-southwest-florida/)

**5. How much does it cost to remove tile flooring in Southwest Florida?**
- cluster: `cost` | intent: `cost` | priority: **P1** | FL
- evidence: COMPETITOR-FAQ - https://removeright.com/floor-removal-cost-guide-southwest-florida/
- short_answer_facts:
  - Remove Right SW Florida guide (Feb 18, 2026): ceramic/porcelain tile removal $2.50-$4.50/sq ft, $4.00-$6.50+/sq ft on a thick mortar bed; light thinset grinding adds $0.75-$1.25/sq ft (https://removeright.com/floor-removal-cost-guide-southwest-florida/)
  - Angi (2026): tile removal $2-$7/sq ft nationally, about $3.50 average (https://www.angi.com/articles/whats-average-cost-remove-ceramic-tile.htm)
  - Saltillo $3.50-$6.00 and terrazzo $3.00-$5.50/sq ft to remove in SW Florida (Remove Right, Feb 2026) (https://removeright.com/floor-removal-cost-guide-southwest-florida/)

**6. Does a flooring removal quote include thinset and mortar removal?**
- cluster: `cost` | intent: `commercial` | priority: **P2** | FL
- evidence: COMPETITOR-FAQ - https://removeright.com/floor-removal-cost-guide-southwest-florida/
- short_answer_facts:
  - SW Florida pricing lists surface prep separately: light thinset grinding $0.75-$1.25/sq ft, heavy mortar bed $1.50-$2.50, mastic/adhesive $0.75-$1.50 (https://removeright.com/floor-removal-cost-guide-southwest-florida/)
  - Shaw SPC guide: concrete must be flat within 3/16 in. in 10 ft (1/8 in. in 6 ft) (https://www.cfiu.org/wp-content/uploads/2022/01/Shaw-Floors-Floorte-Pro-6-7-10-Installation-pdf-generated-on-12_30_2021.pdf)

**7. Is it less expensive to install carpet or laminate flooring?**
- cluster: `cost` | intent: `comparison` | priority: **P3**
- evidence: PAA - https://www.thisoldhouse.com/flooring/laminate-flooring-installation-cost
- short_answer_facts:
  - This Old House (updated 04/01/2026): laminate materials $1-$4/sq ft, labor $4-$8/sq ft, total $5-$12/sq ft; 1,000 sq ft = $5,000-$12,000 (https://www.thisoldhouse.com/flooring/laminate-flooring-installation-cost)
  - HomeAdvisor: carpet $3.50-$11/sq ft installed (https://www.homeadvisor.com/cost/flooring/)

**8. What's the average markup on flooring, and how do I get the best flooring prices?**
- cluster: `cost` | intent: `informational` | priority: **P3**
- evidence: PAA - https://www.homeadvisor.com/cost/flooring/
- short_answer_facts:
  - HomeAdvisor lists both as FAQ entries on its flooring cost guide; specific markup percentage: needs source (https://www.homeadvisor.com/cost/flooring/)
  - HomeAdvisor: old-floor removal commonly $1-$1.50/sq ft nationally (page dated 2022 - Florida tile demo is higher, see Remove Right) (https://www.homeadvisor.com/cost/flooring/)

**9. Why are flooring quotes in Sarasota so different from each other?**
- cluster: `cost` | intent: `cost` | priority: **P1** | FL
- evidence: EXPERT-GAP
- short_answer_facts:
  - Remove Right SW Florida guide (Feb 18, 2026): ceramic/porcelain tile removal $2.50-$4.50/sq ft, $4.00-$6.50+/sq ft on a thick mortar bed; light thinset grinding adds $0.75-$1.25/sq ft (https://removeright.com/floor-removal-cost-guide-southwest-florida/)
  - Professional self-leveling underlayment runs about $3-$9/sq ft; a 50 lb bag covers ~50 sq ft at 1/8 in. or 12-15 sq ft at 1/2 in. (https://engineerfix.com/how-much-does-it-cost-to-self-level-a-concrete-floor/)
  - Line items that swing a quote: demo type, thinset grinding, slab moisture testing/mitigation, leveling, baseboards, transitions, furniture moving, condo acoustic underlayment (https://floorboys.com/buying-guide/questions-to-ask-before-hiring-flooring-contractor/)

### material-choice/comparison

**10. What is the best flooring for a Florida home?**
- cluster: `material-choice/comparison` | intent: `comparison` | priority: **P1** | FL
- evidence: HOUZZ - https://www.houzz.com/discussions/5354690/choosing-flooring-for-florida-home
- short_answer_facts:
  - Sarasota outdoor relative humidity averages about 74% for the year, from ~69% in April to ~78% in August (https://weather-and-climate.com/average-monthly-Humidity-perc,sarasota-florida-us,United-States-of-America)
  - ANSI A137.1: porcelain is tile with water absorption of 0.5% or less (ASTM C373); only such tile can carry PTCA certification (https://tcnatile.com/resource-center/porcelain-tile-certification/)
  - NWFA: wood floors perform best at 30-50% relative humidity and 60-80 F; most flooring is manufactured at 6-9% moisture content (https://www.hursthardwoods.com/moisture-control/)
  - Rigid-core LVP and porcelain are the low-risk picks on slab; engineered (not solid) wood is the way to get real wood (https://www.houzz.com/discussions/5840417/humid-fla-concrete-slab-best-floor-choice-type-don-t-want-tile)

**11. Why do Florida homes have tile floors?**
- cluster: `material-choice/comparison` | intent: `informational` | priority: **P2** | FL
- evidence: QUORA - https://www.quora.com/Why-do-Florida-homes-have-tile-floors
- short_answer_facts:
  - Quora answers: tile stays cool on a slab, shrugs off sand and humidity, and is easy to clean (https://www.quora.com/Why-do-Florida-homes-have-tile-floors)
  - ANSI A137.1: porcelain is tile with water absorption of 0.5% or less (ASTM C373); only such tile can carry PTCA certification (https://tcnatile.com/resource-center/porcelain-tile-certification/)

**12. LVP vs porcelain tile: which is better for a Florida house?**
- cluster: `material-choice/comparison` | intent: `comparison` | priority: **P1** | FL
- evidence: AI-PROMPT
- short_answer_facts:
  - This Old House (updated 06/05/2026): vinyl plank materials $2-$7/sq ft, LVP materials $3-$10/sq ft, labor $3-$10/sq ft; combined $5-$17/sq ft (standard plank) and $6-$20/sq ft (LVP) (https://www.thisoldhouse.com/flooring/cost-to-install-vinyl-plank-flooring)
  - HomeGuide (2026): porcelain tile floor installation $15-$50/sq ft installed; labor alone $12-$30/sq ft (verify range on page - fetch was blocked, figures from search snippet) (https://homeguide.com/costs/porcelain-tile-flooring-installation-cost)
  - A two-person crew lays about 1,000 sq ft of click LVP in 1-2 days on a flat, prepped slab; tile and glue-down wood take several times longer because of cure times (https://tampaflooringgallery.com/quick-step-estimating-the-duration-of-your-flooring-installation-project/)
  - COREtec: avoid prolonged direct sunlight, use drapes or blinds at peak hours to prevent discoloration and thermal expansion (https://www.georgiacarpet.com/pages/installation-guides/coretec-scratchless-installation-guide.html)

**13. SPC vs WPC vinyl plank: which core is better for Florida heat?**
- cluster: `material-choice/comparison` | intent: `comparison` | priority: **P1** | FL
- evidence: EXPERT-GAP - https://www.georgiacarpet.com/pages/installation-guides/coretec-scratchless-installation-guide.html
- short_answer_facts:
  - COREtec: three-season (no climate control) rooms allowed only for floating installs - SPC lines rated -25 F to 155 F after installation, WPC lines only 32 F to 100 F (https://www.georgiacarpet.com/pages/installation-guides/coretec-scratchless-installation-guide.html)
  - COREtec: avoid prolonged direct sunlight, use drapes or blinds at peak hours to prevent discoloration and thermal expansion (https://www.georgiacarpet.com/pages/installation-guides/coretec-scratchless-installation-guide.html)
  - Density/dent-resistance numbers for SPC vs WPC: needs source

**14. Are bamboo floors a good choice in Florida?**
- cluster: `material-choice/comparison` | intent: `informational` | priority: **P2** | FL
- evidence: QUORA - https://www.quora.com/Are-bamboo-floors-a-good-choice-in-Florida
- short_answer_facts:
  - Quora consensus: bamboo is still a moisture-reactive product - it can swell or warp with high humidity or standing water (https://www.quora.com/Are-bamboo-floors-a-good-choice-in-Florida)
  - NWFA: wood floors perform best at 30-50% relative humidity and 60-80 F; most flooring is manufactured at 6-9% moisture content (https://www.hursthardwoods.com/moisture-control/)

**15. What's the best flooring option for a house by the water?**
- cluster: `material-choice/comparison` | intent: `comparison` | priority: **P1** | FL
- evidence: QUORA - https://www.quora.com/Whats-the-best-flooring-option-for-a-house-by-the-water
- short_answer_facts:
  - FEMA Technical Bulletin 2 (Jan 2025) ranks materials Class 1-5; only Class 4 and 5 are acceptable below the base flood elevation - per-material flooring classes: needs source (Table 2 of the PDF could not be parsed in this session) (https://www.fema.gov/sites/default/files/documents/fema_tb_2_flood_damage-resistant_materials_requirements_01-22-2025.pdf)
  - ANSI A137.1: porcelain is tile with water absorption of 0.5% or less (ASTM C373); only such tile can carry PTCA certification (https://tcnatile.com/resource-center/porcelain-tile-certification/)
  - Houzz beach-house thread: pros steer owners to tile because sand, wet guests and open windows defeat wood, and direct sun stresses vinyl (https://www.houzz.com/discussions/4913977/beach-house-flooring-luxury-vinyl-tile-sunlight-or-other-options)

**16. What type of flooring should I choose for the high-traffic areas of my home?**
- cluster: `material-choice/comparison` | intent: `comparison` | priority: **P2**
- evidence: QUORA - https://www.quora.com/What-type-of-flooring-should-I-choose-for-the-high-traffic-areas-of-my-home
- short_answer_facts:
  - PEI wear scale runs 0-5: PEI 2 light traffic (baths, bedrooms), PEI 3 all residential floors, PEI 4 heavy residential/medium commercial, PEI 5 heavy commercial (https://www.angi.com/articles/what-is-pei-rating.htm)
  - Wear layer: 12 mil = 0.012 in. (standard residential); 20 mil = 0.020 in. and is the usual commercial minimum - recommended for large dogs, kids and rentals (https://riosfloor.com/blog/12-mil-vs-20-mil-wear-layer-spc-vinyl-florida/)
  - Laminate AC (abrasion class) ratings run AC1-AC5: AC3 suits every room of a home plus light commercial, AC4-AC5 are commercial grades (https://www.flooring101.com/understanding-laminate-flooring-grades-and-ac-ratings-what-do-they-mean/)
  - Janka hardness (lbf): red oak 1,290; white oak 1,360; hard maple 1,450; hickory 1,820; Brazilian cherry 2,350 (https://www.bruce.com/en-us/hardwood-flooring-understanding-the-janka-rating.html)

**17. Tropical climate flooring: ceramic tile vs laminate vs hardwood - which should I pick?**
- cluster: `material-choice/comparison` | intent: `comparison` | priority: **P2** | FL
- evidence: HOUZZ - https://www.houzz.com/discussions/5179891/tropical-climate-flooring-ceramic-tile-vs-laminate-vs-hardwood
- short_answer_facts:
  - ANSI A137.1: porcelain is tile with water absorption of 0.5% or less (ASTM C373); only such tile can carry PTCA certification (https://tcnatile.com/resource-center/porcelain-tile-certification/)
  - Pergo WetProtect warranty covers household spills, pet accidents and wet mopping, but excludes flooding, standing water, leaking pipes and appliance leaks (http://pdf.lowes.com/warrantyguides/604743160023_warranty.pdf)
  - NWFA: wood floors perform best at 30-50% relative humidity and 60-80 F; most flooring is manufactured at 6-9% moisture content (https://www.hursthardwoods.com/moisture-control/)

**18. Does wood-look porcelain tile or vinyl plank look more realistic and last longer?**
- cluster: `material-choice/comparison` | intent: `comparison` | priority: **P2**
- evidence: EXPERT-GAP
- short_answer_facts:
  - PEI wear scale runs 0-5: PEI 2 light traffic (baths, bedrooms), PEI 3 all residential floors, PEI 4 heavy residential/medium commercial, PEI 5 heavy commercial (https://www.angi.com/articles/what-is-pei-rating.htm)
  - Wear layer: 12 mil = 0.012 in. (standard residential); 20 mil = 0.020 in. and is the usual commercial minimum - recommended for large dogs, kids and rentals (https://riosfloor.com/blog/12-mil-vs-20-mil-wear-layer-spc-vinyl-florida/)
  - Expected service life in years for each: needs source

### florida-humidity-moisture

**19. Can you have real hardwood floors in Florida?**
- cluster: `florida-humidity-moisture` | intent: `informational` | priority: **P1** | FL
- evidence: HOUZZ - https://www.houzz.com/discussions/2394557/locals-telling-me-no-real-wood-in-fl
- short_answer_facts:
  - NWFA: wood floors perform best at 30-50% relative humidity and 60-80 F; most flooring is manufactured at 6-9% moisture content (https://www.hursthardwoods.com/moisture-control/)
  - Wood at 70 F and 40% RH stabilises near 7.7% moisture content; at the 75-80% RH of un-air-conditioned Florida air it would climb to roughly 14-16% (FPL Wood Handbook EMC table - high-RH values: verify) (https://en.wikipedia.org/wiki/Equilibrium_moisture_content)
  - NWFA concrete-subfloor guidance: slab must test at or below 75% RH (ASTM F2170) or 3 lbs/1,000 sq ft/24 hr (ASTM F1869) unless a rated vapor-retarder system is used; solid wood should not go below grade (https://nwfa.org/wp-content/uploads/2020/03/Concrete-Subfloors_Updated.pdf)

**20. Am I stupid to want engineered wood in Florida?**
- cluster: `florida-humidity-moisture` | intent: `informational` | priority: **P1** | FL
- evidence: HOUZZ - https://www.houzz.com/discussions/6120603/am-i-stupid-to-want-engineered-wood-in-florida
- short_answer_facts:
  - NWFA concrete-subfloor guidance: slab must test at or below 75% RH (ASTM F2170) or 3 lbs/1,000 sq ft/24 hr (ASTM F1869) unless a rated vapor-retarder system is used; solid wood should not go below grade (https://nwfa.org/wp-content/uploads/2020/03/Concrete-Subfloors_Updated.pdf)
  - Engineered hardwood wear layer: 2 mm allows 1-2 sandings, 3 mm 2-3, 4 mm 3-4; each full sanding removes roughly 0.5-1 mm (https://www.woodandbeyond.com/blog/what-is-a-good-wear-layer-for-engineered-wood-flooring/)
  - Houzz thread: replacing 1.5 in. of solid wood + plywood with a thin floor changes heights at doors, cabinets and adjacent floors (https://www.houzz.com/discussions/6120603/am-i-stupid-to-want-engineered-wood-in-florida)

**21. What indoor humidity should I keep for wood floors in Florida?**
- cluster: `florida-humidity-moisture` | intent: `informational` | priority: **P1** | FL
- evidence: MANUFACTURER-FAQ - https://www.hursthardwoods.com/moisture-control/
- short_answer_facts:
  - NWFA: wood floors perform best at 30-50% relative humidity and 60-80 F; most flooring is manufactured at 6-9% moisture content (https://www.hursthardwoods.com/moisture-control/)
  - Sarasota outdoor relative humidity averages about 74% for the year, from ~69% in April to ~78% in August (https://weather-and-climate.com/average-monthly-Humidity-perc,sarasota-florida-us,United-States-of-America)
  - EPA: dry water-damaged areas and materials within 24-48 hours to prevent mold; keep indoor RH below 60% (ideally 30-50%) (https://www.epa.gov/mold/brief-guide-mold-moisture-and-your-home)

**22. What should I set my AC and humidistat to when I leave my Florida home for the summer so the floors aren't damaged?**
- cluster: `florida-humidity-moisture` | intent: `informational` | priority: **P1** | FL
- evidence: AI-PROMPT - https://ask.ifas.ufl.edu/publication/HE887
- short_answer_facts:
  - UF/IFAS 'Closing Your Seasonal Home': leave the AC on, set no higher than 85 F, because above that indoor RH passes 55-60% and mold can grow; have the humidistat calibrated before leaving (SW Florida HVAC firms commonly advise 78-80 F with the humidistat at 55-60%) (https://ask.ifas.ufl.edu/publication/HE887)
  - SW Florida HVAC guidance: thermostat 78-80 F and humidistat about 55-60% while away; never switch the system off (https://getbest.com/where-do-i-set-the-thermostat-humidistat-when-i-leave-home/)
  - NWFA: wood floors perform best at 30-50% relative humidity and 60-80 F; most flooring is manufactured at 6-9% moisture content (https://www.hursthardwoods.com/moisture-control/)
  - Wood at 70 F and 40% RH stabilises near 7.7% moisture content; at the 75-80% RH of un-air-conditioned Florida air it would climb to roughly 14-16% (FPL Wood Handbook EMC table - high-RH values: verify) (https://en.wikipedia.org/wiki/Equilibrium_moisture_content)

**23. How long does flooring need to acclimate in Florida before installation?**
- cluster: `florida-humidity-moisture` | intent: `informational` | priority: **P1** | FL
- evidence: PAA - https://nwfa.org/wp-content/uploads/2026/02/NWFA-Installation-Guidelines.pdf
- short_answer_facts:
  - NWFA: acclimation only counts once the HVAC has been running at least 48 hours at normal living conditions; acclimation is judged by moisture-meter readings, not a fixed number of days (https://nwfa.org/wp-content/uploads/2026/02/NWFA-Installation-Guidelines.pdf)
  - NWFA: wood flooring should be within 4% moisture content of the subfloor for strip under 3 in. wide, within 2% for plank 3 in. or wider (https://www.hursthardwoods.com/moisture-control/)
  - COREtec install guide: acclimation not required, but install at 55-85 F; keep a 1/4 in. expansion gap at all walls (https://www.georgiacarpet.com/pages/installation-guides/coretec-scratchless-installation-guide.html)

**24. What happens long-term if wood flooring wasn't acclimated before it was installed?**
- cluster: `florida-humidity-moisture` | intent: `informational` | priority: **P2**
- evidence: HOUZZ - https://www.houzz.com/discussions/4467708/long-term-impact-of-not-letting-wood-acclimate
- short_answer_facts:
  - NWFA: wood flooring should be within 4% moisture content of the subfloor for strip under 3 in. wide, within 2% for plank 3 in. or wider (https://www.hursthardwoods.com/moisture-control/)
  - NWFA/Wagner: never sand a cupped floor until the moisture source is fixed and moisture-meter readings are back to normal - sanding early causes crowning; mild cupping can flatten on its own over weeks to months (https://www.wagnermeters.com/moisture-meters/wood-info/can-wood-floor-cupping-be-fixed/)

**25. Can mold grow under vinyl plank flooring on a Florida slab?**
- cluster: `florida-humidity-moisture` | intent: `informational` | priority: **P1** | FL
- evidence: EXPERT-GAP - https://ifti.com/acceptable-moisture-content-concrete-vinyl-flooring/
- short_answer_facts:
  - IFTI: most floating LVP/LVT makers still cap in-slab RH at 75-85%; floating does not remove the moisture limit, it changes the failure from adhesive bond loss to dimensional and hygiene problems (https://ifti.com/acceptable-moisture-content-concrete-vinyl-flooring/)
  - EPA: dry water-damaged areas and materials within 24-48 hours to prevent mold; keep indoor RH below 60% (ideally 30-50%) (https://www.epa.gov/mold/brief-guide-mold-moisture-and-your-home)
  - ASTM F710/F2170 default: in-slab relative humidity must not exceed 75% unless the flooring or adhesive manufacturer specifies otherwise; probes are set at 40% of slab depth for slabs drying from one side (https://ifti.com/astm-f2170-vs-f1869-which-moisture-test-fits-your-project/)

**26. Why do my hardwood floors cup every summer in Florida?**
- cluster: `florida-humidity-moisture` | intent: `informational` | priority: **P2** | FL
- evidence: PAA - https://woodfloors.org/problem-prevention/
- short_answer_facts:
  - NWFA/Wagner: never sand a cupped floor until the moisture source is fixed and moisture-meter readings are back to normal - sanding early causes crowning; mild cupping can flatten on its own over weeks to months (https://www.wagnermeters.com/moisture-meters/wood-info/can-wood-floor-cupping-be-fixed/)
  - NWFA: wood floors perform best at 30-50% relative humidity and 60-80 F; most flooring is manufactured at 6-9% moisture content (https://www.hursthardwoods.com/moisture-control/)
  - Sarasota outdoor relative humidity averages about 74% for the year, from ~69% in April to ~78% in August (https://weather-and-climate.com/average-monthly-Humidity-perc,sarasota-florida-us,United-States-of-America)

### concrete-slab-subfloor

**27. Do I need a moisture barrier under vinyl plank flooring on a concrete slab?**
- cluster: `concrete-slab-subfloor` | intent: `informational` | priority: **P1** | FL
- evidence: PAA - https://ifti.com/acceptable-moisture-content-concrete-vinyl-flooring/
- short_answer_facts:
  - IFTI: most floating LVP/LVT makers still cap in-slab RH at 75-85%; floating does not remove the moisture limit, it changes the failure from adhesive bond loss to dimensional and hygiene problems (https://ifti.com/acceptable-moisture-content-concrete-vinyl-flooring/)
  - Mohawk laminate FAQ: a moisture barrier is required over concrete; 6-mil polyethylene film with 8 in. overlapped seams for floating floors (https://content.syndigo.com/legacy/sp/a/mohklamFAQ.pdf.pdf?spworld_assetname=4YV9qpwo.pdf&spworld_download=1&spworld_filename=mohklamFAQ.pdf.pdf)
  - Shaw Floorte Pro SPC install guide: allows up to 8 lbs (F1869) or 90% RH (F2170; some Shaw documents say 85%); pH must not exceed 9-10; three tests per first 1,000 sq ft (https://www.cfiu.org/wp-content/uploads/2022/01/Shaw-Floors-Floorte-Pro-6-7-10-Installation-pdf-generated-on-12_30_2021.pdf)

**28. How do you test a concrete slab for moisture before installing flooring?**
- cluster: `concrete-slab-subfloor` | intent: `informational` | priority: **P1** | FL
- evidence: PAA - https://ifti.com/astm-f2170-vs-f1869-which-moisture-test-fits-your-project/
- short_answer_facts:
  - ASTM F710/F2170 default: in-slab relative humidity must not exceed 75% unless the flooring or adhesive manufacturer specifies otherwise; probes are set at 40% of slab depth for slabs drying from one side (https://ifti.com/astm-f2170-vs-f1869-which-moisture-test-fits-your-project/)
  - ASTM F1869 calcium chloride default: moisture vapor emission no more than 3 lbs per 1,000 sq ft per 24 hours unless the manufacturer allows more (https://ifti.com/astm-f2170-vs-f1869-which-moisture-test-fits-your-project/)
  - Shaw requires three tests for the first 1,000 sq ft; F2170 results are required for its warranty (https://www.cfiu.org/wp-content/uploads/2022/01/Shaw-Floors-Floorte-Pro-6-7-10-Installation-pdf-generated-on-12_30_2021.pdf)

**29. What is an acceptable moisture level in a concrete slab for flooring?**
- cluster: `concrete-slab-subfloor` | intent: `informational` | priority: **P1**
- evidence: PAA - https://ifti.com/acceptable-moisture-content-concrete-vinyl-flooring/
- short_answer_facts:
  - ASTM F710/F2170 default: in-slab relative humidity must not exceed 75% unless the flooring or adhesive manufacturer specifies otherwise; probes are set at 40% of slab depth for slabs drying from one side (https://ifti.com/astm-f2170-vs-f1869-which-moisture-test-fits-your-project/)
  - ASTM F1869 calcium chloride default: moisture vapor emission no more than 3 lbs per 1,000 sq ft per 24 hours unless the manufacturer allows more (https://ifti.com/astm-f2170-vs-f1869-which-moisture-test-fits-your-project/)
  - Shaw Floorte Pro SPC install guide: allows up to 8 lbs (F1869) or 90% RH (F2170; some Shaw documents say 85%); pH must not exceed 9-10; three tests per first 1,000 sq ft (https://www.cfiu.org/wp-content/uploads/2022/01/Shaw-Floors-Floorte-Pro-6-7-10-Installation-pdf-generated-on-12_30_2021.pdf)
  - NWFA concrete-subfloor guidance: slab must test at or below 75% RH (ASTM F2170) or 3 lbs/1,000 sq ft/24 hr (ASTM F1869) unless a rated vapor-retarder system is used; solid wood should not go below grade (https://nwfa.org/wp-content/uploads/2020/03/Concrete-Subfloors_Updated.pdf)

**30. Can you install hardwood flooring directly on a concrete slab?**
- cluster: `concrete-slab-subfloor` | intent: `informational` | priority: **P1** | FL
- evidence: PAA - https://nwfa.org/wp-content/uploads/2020/03/Concrete-Subfloors_Updated.pdf
- short_answer_facts:
  - NWFA concrete-subfloor guidance: slab must test at or below 75% RH (ASTM F2170) or 3 lbs/1,000 sq ft/24 hr (ASTM F1869) unless a rated vapor-retarder system is used; solid wood should not go below grade (https://nwfa.org/wp-content/uploads/2020/03/Concrete-Subfloors_Updated.pdf)
  - Houzz pros: solid wood over slab traditionally needs a built-up plywood subfloor; engineered is made to glue direct (https://www.houzz.com/discussions/5840417/humid-fla-concrete-slab-best-floor-choice-type-don-t-want-tile)
  - NWFA: wood flooring should be within 4% moisture content of the subfloor for strip under 3 in. wide, within 2% for plank 3 in. or wider (https://www.hursthardwoods.com/moisture-control/)

**31. Is glue-down or floating better for floors on a Florida concrete slab?**
- cluster: `concrete-slab-subfloor` | intent: `comparison` | priority: **P1** | FL
- evidence: HOUZZ - https://www.houzz.com/discussions/5844482/engineered-wood-floors-in-a-condo-what-underlayment-floating-glue
- short_answer_facts:
  - IFTI: most floating LVP/LVT makers still cap in-slab RH at 75-85%; floating does not remove the moisture limit, it changes the failure from adhesive bond loss to dimensional and hygiene problems (https://ifti.com/acceptable-moisture-content-concrete-vinyl-flooring/)
  - Siesta Dunes (Siesta Key) rules: units above the first floor need an underlayment with minimum IIC 50 under carpet AND hard floors, management must inspect it before flooring goes down, and floating floors are prohibited above the first floor (https://www.siestadunes.com/terms-conditions/)
  - Houzz: the wrong adhesive over a damp Florida slab is a common cause of lifting and bubbling - adhesive must be rated for the measured RH (https://www.houzz.com/discussions/5840417/humid-fla-concrete-slab-best-floor-choice-type-don-t-want-tile)

**32. How flat does a concrete floor need to be for vinyl plank flooring?**
- cluster: `concrete-slab-subfloor` | intent: `informational` | priority: **P1**
- evidence: PAA - https://www.cfiu.org/wp-content/uploads/2022/01/Shaw-Floors-Floorte-Pro-6-7-10-Installation-pdf-generated-on-12_30_2021.pdf
- short_answer_facts:
  - Shaw SPC guide: concrete must be flat within 3/16 in. in 10 ft (1/8 in. in 6 ft) (https://www.cfiu.org/wp-content/uploads/2022/01/Shaw-Floors-Floorte-Pro-6-7-10-Installation-pdf-generated-on-12_30_2021.pdf)
  - Professional self-leveling underlayment runs about $3-$9/sq ft; a 50 lb bag covers ~50 sq ft at 1/8 in. or 12-15 sq ft at 1/2 in. (https://engineerfix.com/how-much-does-it-cost-to-self-level-a-concrete-floor/)

**33. How much does it cost to level a concrete floor before new flooring?**
- cluster: `concrete-slab-subfloor` | intent: `cost` | priority: **P2**
- evidence: PAA - https://engineerfix.com/how-much-does-it-cost-to-self-level-a-concrete-floor/
- short_answer_facts:
  - Professional self-leveling underlayment runs about $3-$9/sq ft; a 50 lb bag covers ~50 sq ft at 1/8 in. or 12-15 sq ft at 1/2 in. (https://engineerfix.com/how-much-does-it-cost-to-self-level-a-concrete-floor/)
  - ANSI A108.02: for tile with any edge 15 in. or longer the substrate may vary no more than 1/8 in. in 10 ft and 1/16 in. in 24 in. (https://www.ceramictilefoundation.org/blog/floor-or-wall-flat-enough-for-large-format-tile)

**34. Moisture in my slab ruined my engineered wood floor - now what?**
- cluster: `concrete-slab-subfloor` | intent: `informational` | priority: **P2** | FL
- evidence: HOUZZ - https://www.houzz.com/discussions/2371243/mystery-moisture-in-slab-ruined-engineered-wood-floor-now-what
- short_answer_facts:
  - NWFA concrete-subfloor guidance: slab must test at or below 75% RH (ASTM F2170) or 3 lbs/1,000 sq ft/24 hr (ASTM F1869) unless a rated vapor-retarder system is used; solid wood should not go below grade (https://nwfa.org/wp-content/uploads/2020/03/Concrete-Subfloors_Updated.pdf)
  - ASTM F710/F2170 default: in-slab relative humidity must not exceed 75% unless the flooring or adhesive manufacturer specifies otherwise; probes are set at 40% of slab depth for slabs drying from one side (https://ifti.com/astm-f2170-vs-f1869-which-moisture-test-fits-your-project/)
  - NWFA/Wagner: never sand a cupped floor until the moisture source is fixed and moisture-meter readings are back to normal - sanding early causes crowning; mild cupping can flatten on its own over weeks to months (https://www.wagnermeters.com/moisture-meters/wood-info/can-wood-floor-cupping-be-fixed/)

### condo-hoa-sound

**35. What IIC rating do I need for condo flooring in Florida?**
- cluster: `condo-hoa-sound` | intent: `informational` | priority: **P1** | FL
- evidence: COMPETITOR-FAQ - https://eastcoastfl.com/blog/condo-flooring-requirements/
- short_answer_facts:
  - Florida Building Code (Building, sound transmission section 1206/1207 depending on edition): floor-ceiling assemblies between dwelling units need IIC 50 and STC 50 (45 if field tested) (https://acousticalsolutions.com/florida-building-code-floor-soundproofing)
  - Floor Coverings International Sarasota: most Sarasota condos want IIC/STC 50+, luxury buildings often 60+; cork, rubber or dense recycled-foam underlayments are the usual route (https://floorcoveringsinternational.com/locations/us/fl/sarasota/tips/guide-condo-flooring-soundproofing/)
  - Commercial Acoustics: tile on a bare concrete slab tests in the high 20s IIC, so an acoustic underlayment is needed to reach 50; many HOAs demand IIC 55-60 (https://commercial-acoustics.com/soundproofing/flooring-permit/)

**36. What is the best flooring for a Florida condo on an upper floor?**
- cluster: `condo-hoa-sound` | intent: `comparison` | priority: **P1** | FL
- evidence: AI-PROMPT
- short_answer_facts:
  - Florida Building Code (Building, sound transmission section 1206/1207 depending on edition): floor-ceiling assemblies between dwelling units need IIC 50 and STC 50 (45 if field tested) (https://acousticalsolutions.com/florida-building-code-floor-soundproofing)
  - Siesta Dunes (Siesta Key) rules: units above the first floor need an underlayment with minimum IIC 50 under carpet AND hard floors, management must inspect it before flooring goes down, and floating floors are prohibited above the first floor (https://www.siestadunes.com/terms-conditions/)
  - Houzz pro answer: most rigid-core LVP has an attached pad and adding a second underlayment (beyond ~1.5-2 mm) can void the warranty - get the acoustic test report for the exact assembly before buying (https://www.houzz.com/discussions/5922442/lvp-in-condo-with-concrete-floors-sound-barrier-underlayment)

**37. Can I put vinyl plank flooring in my second-floor condo?**
- cluster: `condo-hoa-sound` | intent: `informational` | priority: **P1** | FL
- evidence: HOUZZ - https://www.houzz.com/discussions/5922442/lvp-in-condo-with-concrete-floors-sound-barrier-underlayment
- short_answer_facts:
  - Houzz pro answer: most rigid-core LVP has an attached pad and adding a second underlayment (beyond ~1.5-2 mm) can void the warranty - get the acoustic test report for the exact assembly before buying (https://www.houzz.com/discussions/5922442/lvp-in-condo-with-concrete-floors-sound-barrier-underlayment)
  - Houzz: one HOA policy demanded IIC/STC 70+, far above code; vinyl's thin pad alone rarely documents that (https://www.houzz.com/discussions/5447919/luxury-vinyl-plank-acoustic-ratings-for-condos)
  - Commercial Acoustics: tile on a bare concrete slab tests in the high 20s IIC, so an acoustic underlayment is needed to reach 50; many HOAs demand IIC 55-60 (https://commercial-acoustics.com/soundproofing/flooring-permit/)

**38. Can I replace the carpet in my Florida condo with tile or hardwood?**
- cluster: `condo-hoa-sound` | intent: `informational` | priority: **P1** | FL
- evidence: COMPETITOR-FAQ - https://eastcoastfl.com/blog/condo-flooring-requirements/
- short_answer_facts:
  - Florida Statute 718.113 governs unit-owner alterations; the condo declaration/rules (not the statute) set the actual IIC number - read them first (https://www.leg.state.fl.us/statutes/index.cfm?App_mode=Display_Statute&URL=0700-0799/0718/Sections/0718.113.html)
  - DBPR condo arbitration orders show associations enforcing declarations that require board approval and sound-absorbent underlayment under hard flooring - owners can be ordered to fix or remove the floor (https://www2.myfloridalicense.com/lsc/arbitration/allorders/2010036113.pdf)
  - Florida Building Code (Building, sound transmission section 1206/1207 depending on edition): floor-ceiling assemblies between dwelling units need IIC 50 and STC 50 (45 if field tested) (https://acousticalsolutions.com/florida-building-code-floor-soundproofing)

**39. What is the best soundproof underlayment for condo floors?**
- cluster: `condo-hoa-sound` | intent: `comparison` | priority: **P1** | FL
- evidence: COMPETITOR-FAQ - https://floorcoveringsinternational.com/locations/us/fl/sarasota/tips/guide-condo-flooring-soundproofing/
- short_answer_facts:
  - Floor Coverings International Sarasota: most Sarasota condos want IIC/STC 50+, luxury buildings often 60+; cork, rubber or dense recycled-foam underlayments are the usual route (https://floorcoveringsinternational.com/locations/us/fl/sarasota/tips/guide-condo-flooring-soundproofing/)
  - Cork flooring can reach IIC 55-60 by itself per FCI Sarasota (https://floorcoveringsinternational.com/locations/us/fl/sarasota/tips/guide-condo-flooring-soundproofing/)
  - Houzz pro answer: most rigid-core LVP has an attached pad and adding a second underlayment (beyond ~1.5-2 mm) can void the warranty - get the acoustic test report for the exact assembly before buying (https://www.houzz.com/discussions/5922442/lvp-in-condo-with-concrete-floors-sound-barrier-underlayment)
  - Delta-IIC values for specific underlayments: needs source (use each product's ASTM E2179 report)

**40. How do I get HOA approval for new flooring in my Sarasota condo?**
- cluster: `condo-hoa-sound` | intent: `local` | priority: **P1** | FL
- evidence: COMPETITOR-FAQ - https://eastcoastfl.com/blog/condo-flooring-requirements/
- short_answer_facts:
  - Typical package: renovation application with flooring + underlayment spec sheets and acoustic test report, installer insurance certificates, dates; some buildings take a refundable construction deposit (https://www.jasonscarpetandtile.com/about-us/blog/what-south-florida-condo-owners-need-to-know-before-replacing-their-floors)
  - Siesta Dunes (Siesta Key) rules: units above the first floor need an underlayment with minimum IIC 50 under carpet AND hard floors, management must inspect it before flooring goes down, and floating floors are prohibited above the first floor (https://www.siestadunes.com/terms-conditions/)
  - Town of Longboat Key Building FAQ: owners cannot pull owner-builder permits in multi-family (condo) buildings - a contractor must (URL returned 404 on fetch; text from search index - verify) (https://www.longboatkey.org/town-government/departments/planning-zoning-building/building-division/frequently-asked-questions)

**41. Are floating floors allowed in Siesta Key and Longboat Key condos?**
- cluster: `condo-hoa-sound` | intent: `local` | priority: **P1** | FL
- evidence: EXPERT-GAP - https://www.siestadunes.com/terms-conditions/
- short_answer_facts:
  - Siesta Dunes (Siesta Key) rules: units above the first floor need an underlayment with minimum IIC 50 under carpet AND hard floors, management must inspect it before flooring goes down, and floating floors are prohibited above the first floor (https://www.siestadunes.com/terms-conditions/)
  - Rules differ building by building - Longboat Key associations commonly require IIC/STC 50+ underlayment; individual LBK documents: needs source

**42. What happens if I install hard flooring without the soundproofing my condo requires?**
- cluster: `condo-hoa-sound` | intent: `informational` | priority: **P2** | FL
- evidence: COMPETITOR-FAQ - https://eastcoastfl.com/blog/condo-flooring-requirements/
- short_answer_facts:
  - DBPR condo arbitration orders show associations enforcing declarations that require board approval and sound-absorbent underlayment under hard flooring - owners can be ordered to fix or remove the floor (https://www2.myfloridalicense.com/lsc/arbitration/allorders/2010036113.pdf)
  - Floor Coverings International Sarasota: most Sarasota condos want IIC/STC 50+, luxury buildings often 60+; cork, rubber or dense recycled-foam underlayments are the usual route (https://floorcoveringsinternational.com/locations/us/fl/sarasota/tips/guide-condo-flooring-soundproofing/)

**43. Do I need soundproofing if I'm installing carpet in a condo?**
- cluster: `condo-hoa-sound` | intent: `informational` | priority: **P3** | FL
- evidence: COMPETITOR-FAQ - https://eastcoastfl.com/blog/condo-flooring-requirements/
- short_answer_facts:
  - Siesta Dunes (Siesta Key) rules: units above the first floor need an underlayment with minimum IIC 50 under carpet AND hard floors, management must inspect it before flooring goes down, and floating floors are prohibited above the first floor (https://www.siestadunes.com/terms-conditions/)

**44. What's the difference between IIC and STC ratings for floors?**
- cluster: `condo-hoa-sound` | intent: `informational` | priority: **P2**
- evidence: COMPETITOR-FAQ - https://www.jasonscarpetandtile.com/about-us/blog/what-south-florida-condo-owners-need-to-know-before-replacing-their-floors
- short_answer_facts:
  - IIC rates impact noise (footsteps, dropped objects) through a floor-ceiling assembly; STC rates airborne sound (voices, TV) (https://floorcoveringsinternational.com/locations/us/fl/sarasota/tips/guide-condo-flooring-soundproofing/)
  - Florida Building Code (Building, sound transmission section 1206/1207 depending on edition): floor-ceiling assemblies between dwelling units need IIC 50 and STC 50 (45 if field tested) (https://acousticalsolutions.com/florida-building-code-floor-soundproofing)

### installation-process-timeline

**45. How long does it take to replace the floors in a whole house?**
- cluster: `installation-process-timeline` | intent: `informational` | priority: **P1**
- evidence: PAA - https://tampaflooringgallery.com/quick-step-estimating-the-duration-of-your-flooring-installation-project/
- short_answer_facts:
  - A two-person crew lays about 1,000 sq ft of click LVP in 1-2 days on a flat, prepped slab; tile and glue-down wood take several times longer because of cure times (https://tampaflooringgallery.com/quick-step-estimating-the-duration-of-your-flooring-installation-project/)
  - MAPEI: most tile can be grouted 24 hours after setting; wait at least 24 hours after grouting for foot traffic and 72 hours for heavy loads/appliances (rapid-set products are faster) (https://www.mapei.com/us/en-us/training-and-technical-service/tech-talk-blog/detail/mapei-blog/2018/07/02/tile-installation-basics)
  - A full sand-and-refinish takes 3-5 working days; oil-based polyurethane needs up to 30 days to fully cure before rugs go back (https://bigbrohardwood.com/how-long-to-refinish-hardwood-floors/)

**46. Can I live in my house during floor removal and installation?**
- cluster: `installation-process-timeline` | intent: `informational` | priority: **P1**
- evidence: COMPETITOR-FAQ - https://removeright.com/floor-removal-cost-guide-southwest-florida/
- short_answer_facts:
  - A two-person crew lays about 1,000 sq ft of click LVP in 1-2 days on a flat, prepped slab; tile and glue-down wood take several times longer because of cure times (https://tampaflooringgallery.com/quick-step-estimating-the-duration-of-your-flooring-installation-project/)
  - MAPEI: most tile can be grouted 24 hours after setting; wait at least 24 hours after grouting for foot traffic and 72 hours for heavy loads/appliances (rapid-set products are faster) (https://www.mapei.com/us/en-us/training-and-technical-service/tech-talk-blog/detail/mapei-blog/2018/07/02/tile-installation-basics)
  - Silica-dust exposure figures for tile demo: needs source

**47. Do flooring installers move furniture?**
- cluster: `installation-process-timeline` | intent: `commercial` | priority: **P2** | FL
- evidence: COMPETITOR-FAQ - https://maynardfloors.com/flooring-in-sarasota-fl/
- short_answer_facts:
  - Sarasota competitors state it both ways - some include furniture moving, others ask owners to clear rooms, valuables and pets first; ask for it as a line item (https://maynardfloors.com/flooring-in-sarasota-fl/)

**48. What is the best time of year for flooring installation in Sarasota?**
- cluster: `installation-process-timeline` | intent: `local` | priority: **P1** | FL
- evidence: COMPETITOR-FAQ - https://www.homeyou.com/fl/flooring-installation-sarasota-costs
- short_answer_facts:
  - Sarasota outdoor relative humidity averages about 74% for the year, from ~69% in April to ~78% in August (https://weather-and-climate.com/average-monthly-Humidity-perc,sarasota-florida-us,United-States-of-America)
  - NWFA: acclimation only counts once the HVAC has been running at least 48 hours at normal living conditions; acclimation is judged by moisture-meter readings, not a fixed number of days (https://nwfa.org/wp-content/uploads/2026/02/NWFA-Installation-Guidelines.pdf)
  - Many condo associations restrict construction during season (roughly Nov-Apr) - specific Sarasota/LBK rules: needs source

**49. Can you install new flooring over existing tile?**
- cluster: `installation-process-timeline` | intent: `informational` | priority: **P1** | FL
- evidence: MANUFACTURER-FAQ - https://coretecfloors.com/en-eu/flooring-faqs
- short_answer_facts:
  - COREtec: can go over most existing hard surfaces if fully adhered, clean, flat, dry and structurally sound (https://www.georgiacarpet.com/pages/installation-guides/coretec-scratchless-installation-guide.html)
  - Shaw SPC guide: concrete must be flat within 3/16 in. in 10 ft (1/8 in. in 6 ft) (https://www.cfiu.org/wp-content/uploads/2022/01/Shaw-Floors-Floorte-Pro-6-7-10-Installation-pdf-generated-on-12_30_2021.pdf)
  - Remove Right SW Florida guide (Feb 18, 2026): ceramic/porcelain tile removal $2.50-$4.50/sq ft, $4.00-$6.50+/sq ft on a thick mortar bed; light thinset grinding adds $0.75-$1.25/sq ft (https://removeright.com/floor-removal-cost-guide-southwest-florida/)

**50. Is dustless tile removal worth the extra cost?**
- cluster: `installation-process-timeline` | intent: `commercial` | priority: **P1** | FL
- evidence: COMPETITOR-FAQ - https://removeright.com/floor-removal-cost-guide-southwest-florida/
- short_answer_facts:
  - Remove Right SW Florida guide (Feb 18, 2026): ceramic/porcelain tile removal $2.50-$4.50/sq ft, $4.00-$6.50+/sq ft on a thick mortar bed; light thinset grinding adds $0.75-$1.25/sq ft (https://removeright.com/floor-removal-cost-guide-southwest-florida/)
  - Price premium for dustless vs conventional removal: needs source

**51. How long after tile installation can you walk on it?**
- cluster: `installation-process-timeline` | intent: `informational` | priority: **P2**
- evidence: PAA - https://www.mapei.com/us/en-us/training-and-technical-service/tech-talk-blog/detail/mapei-blog/2018/07/02/tile-installation-basics
- short_answer_facts:
  - MAPEI: most tile can be grouted 24 hours after setting; wait at least 24 hours after grouting for foot traffic and 72 hours for heavy loads/appliances (rapid-set products are faster) (https://www.mapei.com/us/en-us/training-and-technical-service/tech-talk-blog/detail/mapei-blog/2018/07/02/tile-installation-basics)

**52. How much extra flooring should I order for waste?**
- cluster: `installation-process-timeline` | intent: `informational` | priority: **P3**
- evidence: PAA - https://tileshoppes.com/blogs/posts/the-10-waste-rule-for-flooring
- short_answer_facts:
  - Order 5% extra for simple square rooms, 10% for typical homes, 15-20% for diagonal or herringbone layouts (https://tileshoppes.com/blogs/posts/the-10-waste-rule-for-flooring)

### hardwood

**53. What type of wood is best for floors?**
- cluster: `hardwood` | intent: `comparison` | priority: **P2**
- evidence: COMPETITOR-FAQ - https://footprintsfloors.com/sarasota/services/flooring-installation/hardwood
- short_answer_facts:
  - Janka hardness (lbf): red oak 1,290; white oak 1,360; hard maple 1,450; hickory 1,820; Brazilian cherry 2,350 (https://www.bruce.com/en-us/hardwood-flooring-understanding-the-janka-rating.html)
  - HomeGuide (2026): hardwood $9-$25/sq ft installed; solid $11-$25, engineered $9-$20; a 2,000 sq ft home runs $14,000-$50,000 (https://homeguide.com/costs/hardwood-flooring-cost)

**54. Where should you not put hardwood floors?**
- cluster: `hardwood` | intent: `informational` | priority: **P2**
- evidence: COMPETITOR-FAQ - https://footprintsfloors.com/sarasota/services/flooring-installation/hardwood
- short_answer_facts:
  - Footprints Floors Sarasota: not recommended in bathrooms, laundry rooms or other high-moisture rooms - warping, cupping, swelling (https://footprintsfloors.com/sarasota/services/flooring-installation/hardwood)
  - NWFA concrete-subfloor guidance: slab must test at or below 75% RH (ASTM F2170) or 3 lbs/1,000 sq ft/24 hr (ASTM F1869) unless a rated vapor-retarder system is used; solid wood should not go below grade (https://nwfa.org/wp-content/uploads/2020/03/Concrete-Subfloors_Updated.pdf)

**55. Solid vs engineered hardwood: which is better on a concrete slab?**
- cluster: `hardwood` | intent: `comparison` | priority: **P1** | FL
- evidence: PAA - https://nwfa.org/wp-content/uploads/2020/03/Concrete-Subfloors_Updated.pdf
- short_answer_facts:
  - NWFA concrete-subfloor guidance: slab must test at or below 75% RH (ASTM F2170) or 3 lbs/1,000 sq ft/24 hr (ASTM F1869) unless a rated vapor-retarder system is used; solid wood should not go below grade (https://nwfa.org/wp-content/uploads/2020/03/Concrete-Subfloors_Updated.pdf)
  - HomeGuide (2026): hardwood $9-$25/sq ft installed; solid $11-$25, engineered $9-$20; a 2,000 sq ft home runs $14,000-$50,000 (https://homeguide.com/costs/hardwood-flooring-cost)
  - Engineered hardwood wear layer: 2 mm allows 1-2 sandings, 3 mm 2-3, 4 mm 3-4; each full sanding removes roughly 0.5-1 mm (https://www.woodandbeyond.com/blog/what-is-a-good-wear-layer-for-engineered-wood-flooring/)

**56. Is it safe to use hardwood flooring in a Sarasota kitchen?**
- cluster: `hardwood` | intent: `local` | priority: **P2** | FL
- evidence: COMPETITOR-FAQ - https://www.homeyou.com/fl/flooring-installation-sarasota-costs
- short_answer_facts:
  - NWFA: wood floors perform best at 30-50% relative humidity and 60-80 F; most flooring is manufactured at 6-9% moisture content (https://www.hursthardwoods.com/moisture-control/)
  - Footprints Floors: kitchens can have hardwood but need extra care because wood is porous (https://footprintsfloors.com/sarasota/services/flooring-installation/hardwood)

**57. How long do hardwood floors last?**
- cluster: `hardwood` | intent: `informational` | priority: **P3**
- evidence: COMPETITOR-FAQ - https://footprintsfloors.com/sarasota/services/flooring-installation/hardwood
- short_answer_facts:
  - Footprints Floors: 50+ years with maintenance because solid wood can be re-sanded (https://footprintsfloors.com/sarasota/services/flooring-installation/hardwood)
  - A 3/4 in. solid board can take roughly 4 full sandings (up to ~10 light ones) over its life; many engineered floors only 1-2 (https://50floor.com/blog/how-many-times-can-you-refinish-wood-floor/)

**58. How thick should the wear layer be on engineered hardwood?**
- cluster: `hardwood` | intent: `informational` | priority: **P1**
- evidence: PAA - https://www.woodandbeyond.com/blog/what-is-a-good-wear-layer-for-engineered-wood-flooring/
- short_answer_facts:
  - Engineered hardwood wear layer: 2 mm allows 1-2 sandings, 3 mm 2-3, 4 mm 3-4; each full sanding removes roughly 0.5-1 mm (https://www.woodandbeyond.com/blog/what-is-a-good-wear-layer-for-engineered-wood-flooring/)
  - A 3/4 in. solid board can take roughly 4 full sandings (up to ~10 light ones) over its life; many engineered floors only 1-2 (https://50floor.com/blog/how-many-times-can-you-refinish-wood-floor/)

**59. What is the best layout or direction for hardwood flooring?**
- cluster: `hardwood` | intent: `informational` | priority: **P3**
- evidence: COMPETITOR-FAQ - https://footprintsfloors.com/sarasota/services/flooring-installation/hardwood
- short_answer_facts:
  - Order 5% extra for simple square rooms, 10% for typical homes, 15-20% for diagonal or herringbone layouts (https://tileshoppes.com/blogs/posts/the-10-waste-rule-for-flooring)

### lvp-vinyl

**60. Why is my vinyl plank floor buckling?**
- cluster: `lvp-vinyl` | intent: `informational` | priority: **P1** | FL
- evidence: QUORA - https://www.quora.com/Why-is-my-vinyl-plank-floor-buckling
- short_answer_facts:
  - COREtec install guide: acclimation not required, but install at 55-85 F; keep a 1/4 in. expansion gap at all walls (https://www.georgiacarpet.com/pages/installation-guides/coretec-scratchless-installation-guide.html)
  - Quora/Houzz: planks pinned by tight trim, door jambs or glued transitions have nowhere to expand and peak; sun-heated areas bow first (https://www.quora.com/Why-is-my-vinyl-plank-floor-buckling)
  - Shaw SPC guide: concrete must be flat within 3/16 in. in 10 ft (1/8 in. in 6 ft) (https://www.cfiu.org/wp-content/uploads/2022/01/Shaw-Floors-Floorte-Pro-6-7-10-Installation-pdf-generated-on-12_30_2021.pdf)

**61. Does sunlight damage vinyl plank flooring?**
- cluster: `lvp-vinyl` | intent: `informational` | priority: **P1** | FL
- evidence: HOUZZ - https://www.houzz.com/discussions/4066423/vinyl-plank-floor-problems
- short_answer_facts:
  - COREtec: avoid prolonged direct sunlight, use drapes or blinds at peak hours to prevent discoloration and thermal expansion (https://www.georgiacarpet.com/pages/installation-guides/coretec-scratchless-installation-guide.html)
  - Shaw vinyl care also says to avoid prolonged direct sunlight (https://shawfloors.com/flooring/how-to/vinyl/care-maintenance)
  - Houzz: window film/UV-blocking treatments quoted at roughly $200-$500 per window (https://www.houzz.com/discussions/4066423/vinyl-plank-floor-problems)

**62. Should I get a 12 mil or 20 mil wear layer on vinyl plank?**
- cluster: `lvp-vinyl` | intent: `comparison` | priority: **P1**
- evidence: PAA - https://riosfloor.com/blog/12-mil-vs-20-mil-wear-layer-spc-vinyl-florida/
- short_answer_facts:
  - Wear layer: 12 mil = 0.012 in. (standard residential); 20 mil = 0.020 in. and is the usual commercial minimum - recommended for large dogs, kids and rentals (https://riosfloor.com/blog/12-mil-vs-20-mil-wear-layer-spc-vinyl-florida/)

**63. Is vinyl plank flooring really waterproof?**
- cluster: `lvp-vinyl` | intent: `informational` | priority: **P1**
- evidence: PAA - https://ifti.com/acceptable-moisture-content-concrete-vinyl-flooring/
- short_answer_facts:
  - IFTI: most floating LVP/LVT makers still cap in-slab RH at 75-85%; floating does not remove the moisture limit, it changes the failure from adhesive bond loss to dimensional and hygiene problems (https://ifti.com/acceptable-moisture-content-concrete-vinyl-flooring/)
  - Click vinyl planks can sometimes be lifted, cleaned, dried and re-laid after clean-water events; pads/cork underlayment should be discarded and the slab dried and tested first; contaminated (surge/sewage) water usually means replacement (https://ogdensflooring.com/can-you-save-flooring-after-a-flood/)
  - EPA: dry water-damaged areas and materials within 24-48 hours to prevent mold; keep indoor RH below 60% (ideally 30-50%) (https://www.epa.gov/mold/brief-guide-mold-moisture-and-your-home)

**64. Can you put vinyl plank flooring on a lanai or in a Florida room with no AC?**
- cluster: `lvp-vinyl` | intent: `informational` | priority: **P1** | FL
- evidence: EXPERT-GAP - https://www.georgiacarpet.com/pages/installation-guides/coretec-scratchless-installation-guide.html
- short_answer_facts:
  - COREtec: three-season (no climate control) rooms allowed only for floating installs - SPC lines rated -25 F to 155 F after installation, WPC lines only 32 F to 100 F (https://www.georgiacarpet.com/pages/installation-guides/coretec-scratchless-installation-guide.html)
  - COREtec: avoid prolonged direct sunlight, use drapes or blinds at peak hours to prevent discoloration and thermal expansion (https://www.georgiacarpet.com/pages/installation-guides/coretec-scratchless-installation-guide.html)
  - TCNA EJ171: movement joints every 20-25 ft in each direction for interior tile; every 8-12 ft where tile gets direct sunlight or moisture, and outdoors (https://www.tileletter.com/movement-joints/)

**65. Can I place appliances on top of vinyl flooring?**
- cluster: `lvp-vinyl` | intent: `informational` | priority: **P3**
- evidence: PAA - https://www.thisoldhouse.com/flooring/cost-to-install-vinyl-plank-flooring
- short_answer_facts:
  - Shaw: use wide load-bearing bases/rollers and felt protectors to avoid indentation (https://shawfloors.com/flooring/how-to/vinyl/care-maintenance)
  - Floating-floor rule about not pinning planks under cabinets/islands: needs source

**66. Does vinyl plank flooring need to acclimate?**
- cluster: `lvp-vinyl` | intent: `informational` | priority: **P2**
- evidence: PAA - https://www.georgiacarpet.com/pages/installation-guides/coretec-scratchless-installation-guide.html
- short_answer_facts:
  - COREtec install guide: acclimation not required, but install at 55-85 F; keep a 1/4 in. expansion gap at all walls (https://www.georgiacarpet.com/pages/installation-guides/coretec-scratchless-installation-guide.html)
  - Many other brands ask for 24-48 hours in the conditioned room - follow the specific install guide or risk the warranty (https://www.flooringclarity.com/does-vinyl-plank-flooring-need-to-acclimate/)

### tile

**67. Why are my floor tiles popping up or sounding hollow?**
- cluster: `tile` | intent: `informational` | priority: **P1** | FL
- evidence: MANUFACTURER-FAQ - https://www.tcnatile.com/resource-center/faq/
- short_answer_facts:
  - CTaSC: tenting/hollow tile is almost always compounding defects - missing movement joints plus poor mortar bond or contamination; hollow sound means the tile has lost bond (https://ctasc.com/expert-answers/tile-tenting-and-hollow-sounding-tile/)
  - TCNA EJ171: movement joints every 20-25 ft in each direction for interior tile; every 8-12 ft where tile gets direct sunlight or moisture, and outdoors (https://www.tileletter.com/movement-joints/)

**68. Do tile floors need expansion joints?**
- cluster: `tile` | intent: `informational` | priority: **P1** | FL
- evidence: MANUFACTURER-FAQ - https://tcnatile.com/resource-center/faq/placement/
- short_answer_facts:
  - TCNA FAQ: every tile installation needs room to move; in small rooms a perimeter gap hidden by baseboard is sufficient, larger areas need visible joints per EJ171 (https://tcnatile.com/resource-center/faq/placement/)
  - TCNA EJ171: movement joints every 20-25 ft in each direction for interior tile; every 8-12 ft where tile gets direct sunlight or moisture, and outdoors (https://www.tileletter.com/movement-joints/)

**69. What floor tile is not slippery when wet?**
- cluster: `tile` | intent: `informational` | priority: **P1** | FL
- evidence: PAA - https://www.daltile.com/why-daltile/industry-standards/dcof-slip-resistance-testing-reading-test-results
- short_answer_facts:
  - ANSI A137.1 / A326.3: tile for level interior floors expected to be walked on wet must have a wet DCOF of 0.42 or greater (a minimum, not a guarantee for every condition) (https://www.daltile.com/why-daltile/industry-standards/dcof-slip-resistance-testing-reading-test-results)
  - Pool decks, lanais and ramps need more than the 0.42 interior minimum - exterior thresholds: needs source (ANSI A326.3-2021 product-use categories)

**70. What PEI rating do I need for floor tile?**
- cluster: `tile` | intent: `informational` | priority: **P2**
- evidence: PAA - https://www.angi.com/articles/what-is-pei-rating.htm
- short_answer_facts:
  - PEI wear scale runs 0-5: PEI 2 light traffic (baths, bedrooms), PEI 3 all residential floors, PEI 4 heavy residential/medium commercial, PEI 5 heavy commercial (https://www.angi.com/articles/what-is-pei-rating.htm)

**71. What's the difference between porcelain and ceramic tile?**
- cluster: `tile` | intent: `comparison` | priority: **P2**
- evidence: MANUFACTURER-FAQ - https://www.tcnatile.com/resource-center/faq/
- short_answer_facts:
  - ANSI A137.1: porcelain is tile with water absorption of 0.5% or less (ASTM C373); only such tile can carry PTCA certification (https://tcnatile.com/resource-center/porcelain-tile-certification/)
  - HomeGuide (2026): porcelain tile floor installation $15-$50/sq ft installed; labor alone $12-$30/sq ft (verify range on page - fetch was blocked, figures from search snippet) (https://homeguide.com/costs/porcelain-tile-flooring-installation-cost)

**72. How flat does the floor have to be for large-format tile?**
- cluster: `tile` | intent: `informational` | priority: **P1**
- evidence: EXPERT-GAP - https://www.ceramictilefoundation.org/blog/floor-or-wall-flat-enough-for-large-format-tile
- short_answer_facts:
  - ANSI A108.02: for tile with any edge 15 in. or longer the substrate may vary no more than 1/8 in. in 10 ft and 1/16 in. in 24 in. (https://www.ceramictilefoundation.org/blog/floor-or-wall-flat-enough-for-large-format-tile)
  - ANSI A108.02 lippage: 1/32 in. allowable with grout joints 1/16 in. or less (plus tile warpage) (https://nationaltileauthority.com/tile-lippage-standards-and-prevention/)
  - Professional self-leveling underlayment runs about $3-$9/sq ft; a 50 lb bag covers ~50 sq ft at 1/8 in. or 12-15 sq ft at 1/2 in. (https://engineerfix.com/how-much-does-it-cost-to-self-level-a-concrete-floor/)

**73. Can I run the same wood-look tile from the living room out onto the lanai?**
- cluster: `tile` | intent: `informational` | priority: **P2** | FL
- evidence: HOUZZ - https://www.houzz.com/discussions/6246235/flooring-advice-florida-condo
- short_answer_facts:
  - TCNA EJ171: movement joints every 20-25 ft in each direction for interior tile; every 8-12 ft where tile gets direct sunlight or moisture, and outdoors (https://www.tileletter.com/movement-joints/)
  - ANSI A137.1 / A326.3: tile for level interior floors expected to be walked on wet must have a wet DCOF of 0.42 or greater (a minimum, not a guarantee for every condition) (https://www.daltile.com/why-daltile/industry-standards/dcof-slip-resistance-testing-reading-test-results)
  - ANSI A137.1: porcelain is tile with water absorption of 0.5% or less (ASTM C373); only such tile can carry PTCA certification (https://tcnatile.com/resource-center/porcelain-tile-certification/)

### laminate

**74. Is laminate flooring a bad idea in Florida?**
- cluster: `laminate` | intent: `informational` | priority: **P1** | FL
- evidence: AI-PROMPT
- short_answer_facts:
  - Pergo WetProtect warranty covers household spills, pet accidents and wet mopping, but excludes flooding, standing water, leaking pipes and appliance leaks (http://pdf.lowes.com/warrantyguides/604743160023_warranty.pdf)
  - Mohawk laminate FAQ: a moisture barrier is required over concrete; 6-mil polyethylene film with 8 in. overlapped seams for floating floors (https://content.syndigo.com/legacy/sp/a/mohklamFAQ.pdf.pdf?spworld_assetname=4YV9qpwo.pdf&spworld_download=1&spworld_filename=mohklamFAQ.pdf.pdf)
  - Sarasota outdoor relative humidity averages about 74% for the year, from ~69% in April to ~78% in August (https://weather-and-climate.com/average-monthly-Humidity-perc,sarasota-florida-us,United-States-of-America)

**75. Waterproof laminate vs luxury vinyl plank: which is better in Florida humidity?**
- cluster: `laminate` | intent: `comparison` | priority: **P1** | FL
- evidence: PAA - http://pdf.lowes.com/warrantyguides/604743160023_warranty.pdf
- short_answer_facts:
  - Pergo WetProtect warranty covers household spills, pet accidents and wet mopping, but excludes flooding, standing water, leaking pipes and appliance leaks (http://pdf.lowes.com/warrantyguides/604743160023_warranty.pdf)
  - This Old House (updated 04/01/2026): laminate materials $1-$4/sq ft, labor $4-$8/sq ft, total $5-$12/sq ft; 1,000 sq ft = $5,000-$12,000 (https://www.thisoldhouse.com/flooring/laminate-flooring-installation-cost)
  - This Old House (updated 06/05/2026): vinyl plank materials $2-$7/sq ft, LVP materials $3-$10/sq ft, labor $3-$10/sq ft; combined $5-$17/sq ft (standard plank) and $6-$20/sq ft (LVP) (https://www.thisoldhouse.com/flooring/cost-to-install-vinyl-plank-flooring)

**76. What is the abrasion (AC) rating on laminate flooring and which do I need?**
- cluster: `laminate` | intent: `informational` | priority: **P2**
- evidence: PAA - https://www.thisoldhouse.com/flooring/laminate-flooring-installation-cost
- short_answer_facts:
  - Laminate AC (abrasion class) ratings run AC1-AC5: AC3 suits every room of a home plus light commercial, AC4-AC5 are commercial grades (https://www.flooring101.com/understanding-laminate-flooring-grades-and-ac-ratings-what-do-they-mean/)

**77. Can I install laminate flooring over other types of flooring?**
- cluster: `laminate` | intent: `informational` | priority: **P2**
- evidence: PAA - https://www.thisoldhouse.com/flooring/laminate-flooring-installation-cost
- short_answer_facts:
  - Mohawk laminate FAQ: a moisture barrier is required over concrete; 6-mil polyethylene film with 8 in. overlapped seams for floating floors (https://content.syndigo.com/legacy/sp/a/mohklamFAQ.pdf.pdf?spworld_assetname=4YV9qpwo.pdf&spworld_download=1&spworld_filename=mohklamFAQ.pdf.pdf)
  - Shaw SPC guide: concrete must be flat within 3/16 in. in 10 ft (1/8 in. in 6 ft) (https://www.cfiu.org/wp-content/uploads/2022/01/Shaw-Floors-Floorte-Pro-6-7-10-Installation-pdf-generated-on-12_30_2021.pdf)

**78. Do you need a moisture barrier under laminate on a concrete floor?**
- cluster: `laminate` | intent: `informational` | priority: **P1** | FL
- evidence: MANUFACTURER-FAQ - https://content.syndigo.com/legacy/sp/a/mohklamFAQ.pdf.pdf?spworld_assetname=4YV9qpwo.pdf&spworld_download=1&spworld_filename=mohklamFAQ.pdf.pdf
- short_answer_facts:
  - Mohawk laminate FAQ: a moisture barrier is required over concrete; 6-mil polyethylene film with 8 in. overlapped seams for floating floors (https://content.syndigo.com/legacy/sp/a/mohklamFAQ.pdf.pdf?spworld_assetname=4YV9qpwo.pdf&spworld_download=1&spworld_filename=mohklamFAQ.pdf.pdf)
  - ASTM F1869 calcium chloride default: moisture vapor emission no more than 3 lbs per 1,000 sq ft per 24 hours unless the manufacturer allows more (https://ifti.com/astm-f2170-vs-f1869-which-moisture-test-fits-your-project/)

**79. How much does it cost to install 1,000 square feet of laminate flooring?**
- cluster: `laminate` | intent: `cost` | priority: **P2**
- evidence: PAA - https://www.thisoldhouse.com/flooring/laminate-flooring-installation-cost
- short_answer_facts:
  - This Old House (updated 04/01/2026): laminate materials $1-$4/sq ft, labor $4-$8/sq ft, total $5-$12/sq ft; 1,000 sq ft = $5,000-$12,000 (https://www.thisoldhouse.com/flooring/laminate-flooring-installation-cost)
  - Angi (2026, 10,975 projects): average laminate install $2,998, typical range $1,471-$4,657, $3-$13/sq ft (https://www.angi.com/articles/how-much-does-laminate-flooring-cost.htm)
  - HomeGuide: $4-$14/sq ft installed, labor $3-$8/sq ft (https://homeguide.com/costs/cost-to-install-laminate-flooring)

### stairs

**80. How much does it cost to install hardwood stair treads?**
- cluster: `stairs` | intent: `cost` | priority: **P1**
- evidence: PAA - https://homeguide.com/costs/hardwood-stairs-cost
- short_answer_facts:
  - HomeGuide (2026): hardwood stairs $100-$250 per step installed; installers charge $50-$80/hour (https://homeguide.com/costs/hardwood-stairs-cost)
  - Angi (2026): about $160 per step, roughly $1,600-$1,920 for a 10-12 step flight with labor (https://www.angi.com/articles/hardwood-stairs-cost.htm)

**81. What do I do with the stairs when the whole house is getting laminate or vinyl?**
- cluster: `stairs` | intent: `informational` | priority: **P1**
- evidence: HOUZZ - https://www.houzz.com/discussions/2503108/what-to-do-with-stairs-when-using-laminate-or-vinyl-whole-house
- short_answer_facts:
  - Houzz threads: many LVP lines have no matching stair nose, and glued-on vinyl nosings come loose - hardwood treads stained to coordinate are the common fix (https://www.houzz.com/discussions/4349600/stair-noses-on-vinyl-plank-floors)
  - HomeGuide (2026): hardwood stairs $100-$250 per step installed; installers charge $50-$80/hour (https://homeguide.com/costs/hardwood-stairs-cost)

**82. Can you put vinyl plank flooring on stairs?**
- cluster: `stairs` | intent: `informational` | priority: **P1**
- evidence: HOUZZ - https://www.houzz.com/discussions/4349600/stair-noses-on-vinyl-plank-floors
- short_answer_facts:
  - Florida Residential Code R311.7.5: nosing 3/4 in. to 1-1/4 in. on stairs with solid risers (https://codes.iccsafe.org/s/FLRC2020P1/part-iii-building-planning-and-construction/FLRC2020P1-Pt03-Ch03-SecR311.7.5.1)
  - Planks on stairs are fully glued, not floated - per-brand instructions: needs source

**83. How do we make wood or laminate stairs less slippery?**
- cluster: `stairs` | intent: `informational` | priority: **P2**
- evidence: QUORA - https://www.quora.com/How-do-we-make-laminate-wood-stairs-less-slippery-without-damage
- short_answer_facts:
  - Quora answers: textured/brushed finishes, runners or clear anti-slip treads rather than high-gloss finish (https://www.quora.com/How-do-we-make-laminate-wood-stairs-less-slippery-without-damage)

**84. Will new, thicker flooring throw my stair riser heights out of code?**
- cluster: `stairs` | intent: `informational` | priority: **P2** | FL
- evidence: EXPERT-GAP - https://codes.iccsafe.org/s/FLRC2020P1/part-iii-building-planning-and-construction/FLRC2020P1-Pt03-Ch03-SecR311.7.5.1
- short_answer_facts:
  - Florida Residential Code R311.7.5: max riser 7-3/4 in., min tread 10 in., and the tallest riser may not exceed the shortest by more than 3/8 in. (https://codes.iccsafe.org/s/FLRC2020P1/part-iii-building-planning-and-construction/FLRC2020P1-Pt03-Ch03-SecR311.7.5.1)

### repair-refinish

**85. How much does it cost to refinish hardwood floors?**
- cluster: `repair-refinish` | intent: `cost` | priority: **P1**
- evidence: PAA - https://homeguide.com/costs/cost-to-refinish-hardwood-floors
- short_answer_facts:
  - HomeGuide (2026): refinishing hardwood costs $2-$8/sq ft, $800-$3,200 for a typical job (https://homeguide.com/costs/cost-to-refinish-hardwood-floors)
  - Angi (2026, via search snippet - verify on page): $3-$8/sq ft, average about $1,891 (range $1,107-$2,680); dustless refinishing $5-$8/sq ft (https://www.angi.com/articles/hardwood-floor-refinishing-cost-and-other-factors.htm)

**86. How long does it take to refinish hardwood floors?**
- cluster: `repair-refinish` | intent: `informational` | priority: **P1**
- evidence: PAA - https://bigbrohardwood.com/how-long-to-refinish-hardwood-floors/
- short_answer_facts:
  - A full sand-and-refinish takes 3-5 working days; oil-based polyurethane needs up to 30 days to fully cure before rugs go back (https://bigbrohardwood.com/how-long-to-refinish-hardwood-floors/)
  - High humidity slows finish drying - Florida-specific dry-time data: needs source

**87. How many times can you refinish hardwood or engineered floors?**
- cluster: `repair-refinish` | intent: `informational` | priority: **P1**
- evidence: PAA - https://50floor.com/blog/how-many-times-can-you-refinish-wood-floor/
- short_answer_facts:
  - A 3/4 in. solid board can take roughly 4 full sandings (up to ~10 light ones) over its life; many engineered floors only 1-2 (https://50floor.com/blog/how-many-times-can-you-refinish-wood-floor/)
  - Engineered hardwood wear layer: 2 mm allows 1-2 sandings, 3 mm 2-3, 4 mm 3-4; each full sanding removes roughly 0.5-1 mm (https://www.woodandbeyond.com/blog/what-is-a-good-wear-layer-for-engineered-wood-flooring/)

**88. Can cupped hardwood floors be fixed without replacing them?**
- cluster: `repair-refinish` | intent: `informational` | priority: **P1** | FL
- evidence: PAA - https://www.wagnermeters.com/moisture-meters/wood-info/can-wood-floor-cupping-be-fixed/
- short_answer_facts:
  - NWFA/Wagner: never sand a cupped floor until the moisture source is fixed and moisture-meter readings are back to normal - sanding early causes crowning; mild cupping can flatten on its own over weeks to months (https://www.wagnermeters.com/moisture-meters/wood-info/can-wood-floor-cupping-be-fixed/)
  - NWFA: wood floors perform best at 30-50% relative humidity and 60-80 F; most flooring is manufactured at 6-9% moisture content (https://www.hursthardwoods.com/moisture-control/)

**89. Is it better to refinish or replace hardwood floors?**
- cluster: `repair-refinish` | intent: `comparison` | priority: **P1**
- evidence: PAA - https://homeguide.com/costs/cost-to-refinish-hardwood-floors
- short_answer_facts:
  - HomeGuide (2026): refinishing hardwood costs $2-$8/sq ft, $800-$3,200 for a typical job (https://homeguide.com/costs/cost-to-refinish-hardwood-floors)
  - HomeGuide (2026): hardwood $9-$25/sq ft installed; solid $11-$25, engineered $9-$20; a 2,000 sq ft home runs $14,000-$50,000 (https://homeguide.com/costs/hardwood-flooring-cost)
  - NAR/NARI 2022 Remodeling Impact Report: hardwood refinishing recovered 147% of cost, new wood flooring 118% (the 2025 edition does not list flooring projects) (https://www.floortrendsmag.com/articles/110579-nar-nari-releases-2022-remodeling-impact-report)

**90. How much does hardwood floor repair cost?**
- cluster: `repair-refinish` | intent: `cost` | priority: **P2**
- evidence: PAA - https://www.angi.com/articles/hardwood-floor-repair-cost.htm
- short_answer_facts:
  - Angi (2026): average hardwood floor repair $1,078, typical range $482-$1,707 (https://www.angi.com/articles/hardwood-floor-repair-cost.htm)

**91. Can you replace just a few damaged vinyl planks or tiles instead of the whole floor?**
- cluster: `repair-refinish` | intent: `informational` | priority: **P2**
- evidence: EXPERT-GAP
- short_answer_facts:
  - Dye-lot/discontinued-pattern risk and keeping a spare box: needs source
  - Order 5% extra for simple square rooms, 10% for typical homes, 15-20% for diagonal or herringbone layouts (https://tileshoppes.com/blogs/posts/the-10-waste-rule-for-flooring)

### pets-kids

**92. What is the best flooring for dogs?**
- cluster: `pets-kids` | intent: `comparison` | priority: **P1**
- evidence: PAA - https://www.angi.com/articles/luxury-vinyl-flooring-good-choice-pets.htm
- short_answer_facts:
  - Angi/HomeGuide: waterproof LVP and porcelain/ceramic tile rank first for scratch, stain and urine resistance (https://www.angi.com/articles/luxury-vinyl-flooring-good-choice-pets.htm)
  - Wear layer: 12 mil = 0.012 in. (standard residential); 20 mil = 0.020 in. and is the usual commercial minimum - recommended for large dogs, kids and rentals (https://riosfloor.com/blog/12-mil-vs-20-mil-wear-layer-spc-vinyl-florida/)
  - PEI wear scale runs 0-5: PEI 2 light traffic (baths, bedrooms), PEI 3 all residential floors, PEI 4 heavy residential/medium commercial, PEI 5 heavy commercial (https://www.angi.com/articles/what-is-pei-rating.htm)

**93. What flooring holds up to dog urine?**
- cluster: `pets-kids` | intent: `informational` | priority: **P1**
- evidence: PAA - https://homeguide.com/costs/best-flooring-for-dogs
- short_answer_facts:
  - Urine is acidic and seeps into seams; if it reaches a wood core or subfloor the stain/odor is hard to reverse - tile and waterproof LVP are not permanently damaged (https://homeguide.com/costs/best-flooring-for-dogs)
  - Pergo WetProtect warranty covers household spills, pet accidents and wet mopping, but excludes flooding, standing water, leaking pipes and appliance leaks (http://pdf.lowes.com/warrantyguides/604743160023_warranty.pdf)

**94. What is the hardest hardwood floor for a house with big dogs?**
- cluster: `pets-kids` | intent: `comparison` | priority: **P2**
- evidence: PAA - https://www.bruce.com/en-us/hardwood-flooring-understanding-the-janka-rating.html
- short_answer_facts:
  - Janka hardness (lbf): red oak 1,290; white oak 1,360; hard maple 1,450; hickory 1,820; Brazilian cherry 2,350 (https://www.bruce.com/en-us/hardwood-flooring-understanding-the-janka-rating.html)

**95. Do dog nails scratch vinyl plank flooring?**
- cluster: `pets-kids` | intent: `informational` | priority: **P2**
- evidence: PAA - https://riosfloor.com/blog/12-mil-vs-20-mil-wear-layer-spc-vinyl-florida/
- short_answer_facts:
  - Wear layer: 12 mil = 0.012 in. (standard residential); 20 mil = 0.020 in. and is the usual commercial minimum - recommended for large dogs, kids and rentals (https://riosfloor.com/blog/12-mil-vs-20-mil-wear-layer-spc-vinyl-florida/)

**96. What is the safest non-slip flooring for seniors and kids?**
- cluster: `pets-kids` | intent: `informational` | priority: **P2** | FL
- evidence: EXPERT-GAP - https://www.daltile.com/why-daltile/industry-standards/dcof-slip-resistance-testing-reading-test-results
- short_answer_facts:
  - ANSI A137.1 / A326.3: tile for level interior floors expected to be walked on wet must have a wet DCOF of 0.42 or greater (a minimum, not a guarantee for every condition) (https://www.daltile.com/why-daltile/industry-standards/dcof-slip-resistance-testing-reading-test-results)
  - Fall-injury statistics for older adults (CDC): needs source

### water-flood-hurricane

**97. What flooring survives a hurricane flood in Florida?**
- cluster: `water-flood-hurricane` | intent: `informational` | priority: **P1** | FL
- evidence: AI-PROMPT - https://www.fema.gov/sites/default/files/documents/fema_tb_2_flood_damage-resistant_materials_requirements_01-22-2025.pdf
- short_answer_facts:
  - FEMA Technical Bulletin 2 (Jan 2025) ranks materials Class 1-5; only Class 4 and 5 are acceptable below the base flood elevation - per-material flooring classes: needs source (Table 2 of the PDF could not be parsed in this session) (https://www.fema.gov/sites/default/files/documents/fema_tb_2_flood_damage-resistant_materials_requirements_01-22-2025.pdf)
  - ANSI A137.1: porcelain is tile with water absorption of 0.5% or less (ASTM C373); only such tile can carry PTCA certification (https://tcnatile.com/resource-center/porcelain-tile-certification/)
  - Hurricane Milton made landfall at Siesta Key on Oct 9, 2024 as a Category 3; Helene's surge two weeks earlier damaged about 7,600 residences in unincorporated Sarasota County (>$1.1B) and 2,200 structures on Longboat Key ($176M) - verify figures against county release (https://www.scgov.net/Home/Components/News/News/8261/23)

**98. Can vinyl plank flooring be saved after a flood?**
- cluster: `water-flood-hurricane` | intent: `informational` | priority: **P1** | FL
- evidence: PAA - https://ogdensflooring.com/can-you-save-flooring-after-a-flood/
- short_answer_facts:
  - Click vinyl planks can sometimes be lifted, cleaned, dried and re-laid after clean-water events; pads/cork underlayment should be discarded and the slab dried and tested first; contaminated (surge/sewage) water usually means replacement (https://ogdensflooring.com/can-you-save-flooring-after-a-flood/)
  - EPA: dry water-damaged areas and materials within 24-48 hours to prevent mold; keep indoor RH below 60% (ideally 30-50%) (https://www.epa.gov/mold/brief-guide-mold-moisture-and-your-home)

**99. How soon do I have to pull up wet flooring after storm surge?**
- cluster: `water-flood-hurricane` | intent: `informational` | priority: **P1** | FL
- evidence: EXPERT-GAP - https://www.epa.gov/mold/brief-guide-mold-moisture-and-your-home
- short_answer_facts:
  - EPA: dry water-damaged areas and materials within 24-48 hours to prevent mold; keep indoor RH below 60% (ideally 30-50%) (https://www.epa.gov/mold/brief-guide-mold-moisture-and-your-home)
  - Hurricane Milton made landfall at Siesta Key on Oct 9, 2024 as a Category 3; Helene's surge two weeks earlier damaged about 7,600 residences in unincorporated Sarasota County (>$1.1B) and 2,200 structures on Longboat Key ($176M) - verify figures against county release (https://www.scgov.net/Home/Components/News/News/8261/23)
  - ASTM F710/F2170 default: in-slab relative humidity must not exceed 75% unless the flooring or adhesive manufacturer specifies otherwise; probes are set at 40% of slab depth for slabs drying from one side (https://ifti.com/astm-f2170-vs-f1869-which-moisture-test-fits-your-project/)

**100. Does homeowners insurance cover flood-damaged floors in Florida?**
- cluster: `water-flood-hurricane` | intent: `informational` | priority: **P1** | FL
- evidence: PAA - https://www.fema.gov/flood-insurance
- short_answer_facts:
  - FEMA: standard homeowners policies do not cover flood; NFIP building coverage goes up to $250,000 (contents $100,000) and new policies usually have a 30-day waiting period (https://www.fema.gov/flood-insurance)

**101. Can water-damaged hardwood floors be saved?**
- cluster: `water-flood-hurricane` | intent: `informational` | priority: **P1**
- evidence: PAA - https://www.angi.com/articles/flooded-flooring-what-know-when-replace.htm
- short_answer_facts:
  - NWFA/Wagner: never sand a cupped floor until the moisture source is fixed and moisture-meter readings are back to normal - sanding early causes crowning; mild cupping can flatten on its own over weeks to months (https://www.wagnermeters.com/moisture-meters/wood-info/can-wood-floor-cupping-be-fixed/)
  - Angi (2026): average hardwood floor repair $1,078, typical range $482-$1,707 (https://www.angi.com/articles/hardwood-floor-repair-cost.htm)
  - EPA: dry water-damaged areas and materials within 24-48 hours to prevent mold; keep indoor RH below 60% (ideally 30-50%) (https://www.epa.gov/mold/brief-guide-mold-moisture-and-your-home)

**102. What are the signs of water damage under vinyl or laminate floors?**
- cluster: `water-flood-hurricane` | intent: `informational` | priority: **P2**
- evidence: PAA - https://ctr-nw.com/blog/signs-of-water-damage-under-vinyl-floors/
- short_answer_facts:
  - EPA: dry water-damaged areas and materials within 24-48 hours to prevent mold; keep indoor RH below 60% (ideally 30-50%) (https://www.epa.gov/mold/brief-guide-mold-moisture-and-your-home)
  - IFTI: most floating LVP/LVT makers still cap in-slab RH at 75-85%; floating does not remove the moisture limit, it changes the failure from adhesive bond loss to dimensional and hygiene problems (https://ifti.com/acceptable-moisture-content-concrete-vinyl-flooring/)

**103. How long does a slab need to dry after flooding before new floors go in?**
- cluster: `water-flood-hurricane` | intent: `informational` | priority: **P1** | FL
- evidence: EXPERT-GAP - https://ifti.com/astm-f2170-vs-f1869-which-moisture-test-fits-your-project/
- short_answer_facts:
  - ASTM F710/F2170 default: in-slab relative humidity must not exceed 75% unless the flooring or adhesive manufacturer specifies otherwise; probes are set at 40% of slab depth for slabs drying from one side (https://ifti.com/astm-f2170-vs-f1869-which-moisture-test-fits-your-project/)
  - Shaw Floorte Pro SPC install guide: allows up to 8 lbs (F1869) or 90% RH (F2170; some Shaw documents say 85%); pH must not exceed 9-10; three tests per first 1,000 sq ft (https://www.cfiu.org/wp-content/uploads/2022/01/Shaw-Floors-Floorte-Pro-6-7-10-Installation-pdf-generated-on-12_30_2021.pdf)
  - Typical drying time in days for a flooded slab-on-grade: needs source - test, don't guess

### maintenance-cleaning

**104. Can you use a steam mop on vinyl plank or hardwood floors?**
- cluster: `maintenance-cleaning` | intent: `informational` | priority: **P1**
- evidence: PAA - https://lighthouse.shawinc.com/SiteFiles/Lighthouse/pdf/SBF-ResilientVinylWarranty-Care-and-Maintenance.pdf
- short_answer_facts:
  - Shaw resilient warranty/care guide: 'Do not use steam cleaners on resilient flooring' (https://lighthouse.shawinc.com/SiteFiles/Lighthouse/pdf/SBF-ResilientVinylWarranty-Care-and-Maintenance.pdf)
  - Angi: steam on vinyl can warp planks and break down adhesive (https://www.angi.com/articles/can-you-steam-clean-vinyl-floors.htm)

**105. How do I clean vinyl plank flooring?**
- cluster: `maintenance-cleaning` | intent: `informational` | priority: **P2**
- evidence: PAA - https://www.thisoldhouse.com/flooring/cost-to-install-vinyl-plank-flooring
- short_answer_facts:
  - Shaw vinyl care: use mats without latex or rubber backing (they can discolor vinyl), felt protectors under furniture, neutral-pH cleaner, clean weekly (https://shawfloors.com/flooring/how-to/vinyl/care-maintenance)
  - Shaw: avoid ammonia- and vinegar-based cleaners; blot spills immediately (https://shawfloors.com/flooring/how-to/vinyl/care-maintenance)

**106. How do I keep beach sand from scratching my floors?**
- cluster: `maintenance-cleaning` | intent: `informational` | priority: **P1** | FL
- evidence: EXPERT-GAP - https://shawfloors.com/flooring/how-to/vinyl/care-maintenance
- short_answer_facts:
  - Shaw vinyl care: use mats without latex or rubber backing (they can discolor vinyl), felt protectors under furniture, neutral-pH cleaner, clean weekly (https://shawfloors.com/flooring/how-to/vinyl/care-maintenance)
  - Wear layer: 12 mil = 0.012 in. (standard residential); 20 mil = 0.020 in. and is the usual commercial minimum - recommended for large dogs, kids and rentals (https://riosfloor.com/blog/12-mil-vs-20-mil-wear-layer-spc-vinyl-florida/)
  - Hardness of quartz sand vs floor finishes (Mohs): needs source

**107. Do rubber-backed mats stain vinyl floors?**
- cluster: `maintenance-cleaning` | intent: `informational` | priority: **P2**
- evidence: MANUFACTURER-FAQ - https://shawfloors.com/flooring/how-to/vinyl/care-maintenance
- short_answer_facts:
  - Shaw vinyl care: use mats without latex or rubber backing (they can discolor vinyl), felt protectors under furniture, neutral-pH cleaner, clean weekly (https://shawfloors.com/flooring/how-to/vinyl/care-maintenance)

**108. How do I clean the grout on my tile floors?**
- cluster: `maintenance-cleaning` | intent: `informational` | priority: **P3**
- evidence: MANUFACTURER-FAQ - https://www.tcnatile.com/resource-center/faq/
- short_answer_facts:
  - TCNA keeps a dedicated 'Cleaning Grout' FAQ; sealer timing per MAPEI: 72 hours after grouting for cement grout (24 h for Ultracolor Plus FA) (https://www.mapei.com/us/en-us/training-and-technical-service/tech-talk-blog/detail/mapei-blog/2018/07/02/tile-installation-basics)

### hiring-a-contractor

**109. What questions should I ask a flooring contractor before hiring?**
- cluster: `hiring-a-contractor` | intent: `commercial` | priority: **P1**
- evidence: PAA - https://floorboys.com/buying-guide/questions-to-ask-before-hiring-flooring-contractor/
- short_answer_facts:
  - Ask for an itemized quote: materials, labor, prep, furniture moving, subfloor repairs, disposal, trim and transitions (https://floorboys.com/buying-guide/questions-to-ask-before-hiring-flooring-contractor/)
  - Installers still need an active Sunbiz business registration, general liability insurance and workers' compensation (or a valid exemption) (https://www.seerfloor.com/2024/06/changes-to-licensing-in-florida/)
  - ASTM F710/F2170 default: in-slab relative humidity must not exceed 75% unless the flooring or adhesive manufacturer specifies otherwise; probes are set at 40% of slab depth for slabs drying from one side (https://ifti.com/astm-f2170-vs-f1869-which-moisture-test-fits-your-project/)

**110. How much deposit should I pay a flooring contractor?**
- cluster: `hiring-a-contractor` | intent: `commercial` | priority: **P1**
- evidence: HOUZZ - https://www.houzz.com/discussions/5296922/initial-deposit-for-cabinet-and-flooring-jobs-how-much-to-expect
- short_answer_facts:
  - Angi: typical contractor deposits run 10-25% of the job (up to 10-50% on small jobs); tie remaining payments to milestones and never pay in full up front (https://www.angi.com/articles/how-much-should-i-pay-general-contractor-prior-starting-job.htm)

**111. Is it better to buy flooring from Home Depot or Lowe's, or hire a local flooring installer?**
- cluster: `hiring-a-contractor` | intent: `comparison` | priority: **P1**
- evidence: AI-PROMPT
- short_answer_facts:
  - Comparative pricing/warranty data for big-box subcontracted installs vs local installers: needs source
  - This Old House (updated 06/05/2026): vinyl plank materials $2-$7/sq ft, LVP materials $3-$10/sq ft, labor $3-$10/sq ft; combined $5-$17/sq ft (standard plank) and $6-$20/sq ft (LVP) (https://www.thisoldhouse.com/flooring/cost-to-install-vinyl-plank-flooring)

**112. Who is the best flooring installer in Sarasota, FL?**
- cluster: `hiring-a-contractor` | intent: `local` | priority: **P2** | FL
- evidence: AI-PROMPT
- short_answer_facts:
  - BrightLocal 2026: 45% of consumers used AI tools to find local businesses (6% a year earlier) (https://www.brightlocal.com/research/local-consumer-review-survey/)
  - SOCi 2026: ChatGPT recommends only 1.2% of locations; recommended ones average 4.3 stars (https://www.soci.ai/blog/how-to-rank-in-chatgpt-perplexity-and-google-ai-overview/)

**113. How does a flooring installation warranty work?**
- cluster: `hiring-a-contractor` | intent: `commercial` | priority: **P2** | FL
- evidence: COMPETITOR-FAQ - https://maynardfloors.com/flooring-in-sarasota-fl/
- short_answer_facts:
  - Manufacturer warranties hinge on documented moisture tests and following the install guide (Shaw requires F2170 results) (https://www.cfiu.org/wp-content/uploads/2022/01/Shaw-Floors-Floorte-Pro-6-7-10-Installation-pdf-generated-on-12_30_2021.pdf)
  - Florida's former licensed-installer one-year warranty is no longer mandated after licensing preemption (https://www.seerfloor.com/2024/06/changes-to-licensing-in-florida/)

**114. Do you offer financing for new floors?**
- cluster: `hiring-a-contractor` | intent: `commercial` | priority: **P3** | FL
- evidence: COMPETITOR-FAQ - https://maynardfloors.com/flooring-in-sarasota-fl/
- short_answer_facts:
  - Sarasota competitor Jim Maynard Flooring advertises financing in its FAQ (https://maynardfloors.com/flooring-in-sarasota-fl/)

### permits-licensing

**115. Do I need a permit to replace flooring in Sarasota County?**
- cluster: `permits-licensing` | intent: `local` | priority: **P1** | FL
- evidence: COMPETITOR-FAQ - https://www.homeyou.com/fl/flooring-installation-sarasota-costs
- short_answer_facts:
  - Sarasota County: replacing flooring without subfloor/structural changes is treated as cosmetic work and does not need a building permit (confirm with the building department for your address) (https://blog.teamrenick.com/what-permits-are-needed-for-renovations-in-sarasota-county/)
  - Sarasota County Building department contact page (https://www.scgov.net/government/planning-and-development-services/building)

**116. Do flooring installers need a license in Florida?**
- cluster: `permits-licensing` | intent: `informational` | priority: **P1** | FL
- evidence: EXPERT-GAP - https://www.seerfloor.com/2024/06/changes-to-licensing-in-florida/
- short_answer_facts:
  - Florida HB 735 (2021) / HB 1383 (2023) preempted local specialty licensing: since July 1, 2024 local governments cannot require a license for flooring/tile installation; no state DBPR flooring license exists (https://www.seerfloor.com/2024/06/changes-to-licensing-in-florida/)
  - Installers still need an active Sunbiz business registration, general liability insurance and workers' compensation (or a valid exemption) (https://www.seerfloor.com/2024/06/changes-to-licensing-in-florida/)
  - DBPR list of services that do/don't need a state license (https://www2.myfloridalicense.com/services-requiring-a-dbpr-license/)

**117. Do I need a permit for floor removal in Florida?**
- cluster: `permits-licensing` | intent: `informational` | priority: **P2** | FL
- evidence: COMPETITOR-FAQ - https://removeright.com/floor-removal-cost-guide-southwest-florida/
- short_answer_facts:
  - Sarasota County: replacing flooring without subfloor/structural changes is treated as cosmetic work and does not need a building permit (confirm with the building department for your address) (https://blog.teamrenick.com/what-permits-are-needed-for-renovations-in-sarasota-county/)

**118. Do I need a permit to change the flooring in a Florida condo?**
- cluster: `permits-licensing` | intent: `informational` | priority: **P1** | FL
- evidence: EXPERT-GAP - https://commercial-acoustics.com/soundproofing/flooring-permit/
- short_answer_facts:
  - Florida Building Code (Building, sound transmission section 1206/1207 depending on edition): floor-ceiling assemblies between dwelling units need IIC 50 and STC 50 (45 if field tested) (https://acousticalsolutions.com/florida-building-code-floor-soundproofing)
  - Several Florida cities (Miami, Miami Beach, Boca Raton, Tampa) permit condo hard-surface changes and want acoustic affidavits; Sarasota-area municipal practice: needs source (https://commercial-acoustics.com/soundproofing/flooring-permit/)
  - Town of Longboat Key Building FAQ: owners cannot pull owner-builder permits in multi-family (condo) buildings - a contractor must (URL returned 404 on fetch; text from search index - verify) (https://www.longboatkey.org/town-government/departments/planning-zoning-building/building-division/frequently-asked-questions)

**119. What insurance paperwork does my flooring contractor need to work in my condo building?**
- cluster: `permits-licensing` | intent: `informational` | priority: **P2** | FL
- evidence: COMPETITOR-FAQ - https://www.jasonscarpetandtile.com/about-us/blog/what-south-florida-condo-owners-need-to-know-before-replacing-their-floors
- short_answer_facts:
  - Associations commonly ask for a certificate of liability insurance, workers' comp proof and sometimes a refundable construction deposit (https://www.jasonscarpetandtile.com/about-us/blog/what-south-florida-condo-owners-need-to-know-before-replacing-their-floors)
  - Installers still need an active Sunbiz business registration, general liability insurance and workers' compensation (or a valid exemption) (https://www.seerfloor.com/2024/06/changes-to-licensing-in-florida/)

### vacation-rental-investor

**120. What is the best flooring for a vacation rental in Florida?**
- cluster: `vacation-rental-investor` | intent: `comparison` | priority: **P1** | FL
- evidence: AI-PROMPT - https://floorauthority.com/blogs/blog/best-flooring-options-for-beach-vacation-rentals
- short_answer_facts:
  - Beach-rental guidance: waterproof rigid-core LVP with a 20 mil wear layer or porcelain tile; avoid carpet (traps sand/moisture) and solid hardwood (https://floorauthority.com/blogs/blog/best-flooring-options-for-beach-vacation-rentals)
  - Wear layer: 12 mil = 0.012 in. (standard residential); 20 mil = 0.020 in. and is the usual commercial minimum - recommended for large dogs, kids and rentals (https://riosfloor.com/blog/12-mil-vs-20-mil-wear-layer-spc-vinyl-florida/)
  - This Old House (updated 06/05/2026): vinyl plank materials $2-$7/sq ft, LVP materials $3-$10/sq ft, labor $3-$10/sq ft; combined $5-$17/sq ft (standard plank) and $6-$20/sq ft (LVP) (https://www.thisoldhouse.com/flooring/cost-to-install-vinyl-plank-flooring)

**121. How fast can floors be replaced between guest bookings?**
- cluster: `vacation-rental-investor` | intent: `commercial` | priority: **P1** | FL
- evidence: EXPERT-GAP - https://tampaflooringgallery.com/quick-step-estimating-the-duration-of-your-flooring-installation-project/
- short_answer_facts:
  - A two-person crew lays about 1,000 sq ft of click LVP in 1-2 days on a flat, prepped slab; tile and glue-down wood take several times longer because of cure times (https://tampaflooringgallery.com/quick-step-estimating-the-duration-of-your-flooring-installation-project/)
  - MAPEI: most tile can be grouted 24 hours after setting; wait at least 24 hours after grouting for foot traffic and 72 hours for heavy loads/appliances (rapid-set products are faster) (https://www.mapei.com/us/en-us/training-and-technical-service/tech-talk-blog/detail/mapei-blog/2018/07/02/tile-installation-basics)
  - COREtec install guide: acclimation not required, but install at 55-85 F; keep a 1/4 in. expansion gap at all walls (https://www.georgiacarpet.com/pages/installation-guides/coretec-scratchless-installation-guide.html)

**122. Is LVP or tile the smarter choice for a long-term rental property?**
- cluster: `vacation-rental-investor` | intent: `comparison` | priority: **P1**
- evidence: AI-PROMPT
- short_answer_facts:
  - This Old House (updated 06/05/2026): vinyl plank materials $2-$7/sq ft, LVP materials $3-$10/sq ft, labor $3-$10/sq ft; combined $5-$17/sq ft (standard plank) and $6-$20/sq ft (LVP) (https://www.thisoldhouse.com/flooring/cost-to-install-vinyl-plank-flooring)
  - HomeGuide (2026): porcelain tile floor installation $15-$50/sq ft installed; labor alone $12-$30/sq ft (verify range on page - fetch was blocked, figures from search snippet) (https://homeguide.com/costs/porcelain-tile-flooring-installation-cost)
  - Wear layer: 12 mil = 0.012 in. (standard residential); 20 mil = 0.020 in. and is the usual commercial minimum - recommended for large dogs, kids and rentals (https://riosfloor.com/blog/12-mil-vs-20-mil-wear-layer-spc-vinyl-florida/)
  - PEI wear scale runs 0-5: PEI 2 light traffic (baths, bedrooms), PEI 3 all residential floors, PEI 4 heavy residential/medium commercial, PEI 5 heavy commercial (https://www.angi.com/articles/what-is-pei-rating.htm)

**123. What flooring is best for a snowbird home that sits empty all summer?**
- cluster: `vacation-rental-investor` | intent: `comparison` | priority: **P1** | FL
- evidence: AI-PROMPT - https://ask.ifas.ufl.edu/publication/HE887
- short_answer_facts:
  - UF/IFAS 'Closing Your Seasonal Home': leave the AC on, set no higher than 85 F, because above that indoor RH passes 55-60% and mold can grow; have the humidistat calibrated before leaving (SW Florida HVAC firms commonly advise 78-80 F with the humidistat at 55-60%) (https://ask.ifas.ufl.edu/publication/HE887)
  - COREtec: three-season (no climate control) rooms allowed only for floating installs - SPC lines rated -25 F to 155 F after installation, WPC lines only 32 F to 100 F (https://www.georgiacarpet.com/pages/installation-guides/coretec-scratchless-installation-guide.html)
  - NWFA: wood floors perform best at 30-50% relative humidity and 60-80 F; most flooring is manufactured at 6-9% moisture content (https://www.hursthardwoods.com/moisture-control/)

**124. Renters leave the sliders open and track in sand - what floor can take it?**
- cluster: `vacation-rental-investor` | intent: `informational` | priority: **P2** | FL
- evidence: HOUZZ - https://www.houzz.com/discussions/4913977/beach-house-flooring-luxury-vinyl-tile-sunlight-or-other-options
- short_answer_facts:
  - Houzz pro: renters can't be trusted to hold humidity in range, which rules out wood in beach rentals (https://www.houzz.com/discussions/4913977/beach-house-flooring-luxury-vinyl-tile-sunlight-or-other-options)
  - ANSI A137.1: porcelain is tile with water absorption of 0.5% or less (ASTM C373); only such tile can carry PTCA certification (https://tcnatile.com/resource-center/porcelain-tile-certification/)
  - Wear layer: 12 mil = 0.012 in. (standard residential); 20 mil = 0.020 in. and is the usual commercial minimum - recommended for large dogs, kids and rentals (https://riosfloor.com/blog/12-mil-vs-20-mil-wear-layer-spc-vinyl-florida/)

### resale-value

**125. Does new flooring increase home value?**
- cluster: `resale-value` | intent: `informational` | priority: **P1**
- evidence: PAA - https://www.homeadvisor.com/cost/flooring/
- short_answer_facts:
  - NAR/NARI 2022 Remodeling Impact Report: hardwood refinishing recovered 147% of cost, new wood flooring 118% (the 2025 edition does not list flooring projects) (https://www.floortrendsmag.com/articles/110579-nar-nari-releases-2022-remodeling-impact-report)
  - NAR 2022: a typical $3,400 refinish added about $5,000 of value (https://www.floortrendsmag.com/articles/110579-nar-nari-releases-2022-remodeling-impact-report)

**126. What flooring do Florida home buyers want?**
- cluster: `resale-value` | intent: `informational` | priority: **P1** | FL
- evidence: COMPETITOR-FAQ - https://floorcoveringsinternational.com/locations/us/fl/wellington/tips/florida-flooring-roi/
- short_answer_facts:
  - Floor Coverings International (FL): tile, LVP and engineered hardwood are the finishes Florida buyers expect; worn carpet and dated tile are the usual objections (https://floorcoveringsinternational.com/locations/us/fl/wellington/tips/florida-flooring-roi/)
  - Survey data on Florida buyer flooring preferences: needs source

**127. Should I replace my floors before selling my house?**
- cluster: `resale-value` | intent: `commercial` | priority: **P1**
- evidence: COMPETITOR-FAQ - https://removeright.com/floor-removal-cost-guide-southwest-florida/
- short_answer_facts:
  - NAR/NARI 2022 Remodeling Impact Report: hardwood refinishing recovered 147% of cost, new wood flooring 118% (the 2025 edition does not list flooring projects) (https://www.floortrendsmag.com/articles/110579-nar-nari-releases-2022-remodeling-impact-report)
  - This Old House (updated 06/05/2026): vinyl plank materials $2-$7/sq ft, LVP materials $3-$10/sq ft, labor $3-$10/sq ft; combined $5-$17/sq ft (standard plank) and $6-$20/sq ft (LVP) (https://www.thisoldhouse.com/flooring/cost-to-install-vinyl-plank-flooring)

**128. Do hardwood floors add value to a home in Florida?**
- cluster: `resale-value` | intent: `informational` | priority: **P2** | FL
- evidence: PAA - https://www.floortrendsmag.com/articles/110579-nar-nari-releases-2022-remodeling-impact-report
- short_answer_facts:
  - NAR/NARI 2022 Remodeling Impact Report: hardwood refinishing recovered 147% of cost, new wood flooring 118% (the 2025 edition does not list flooring projects) (https://www.floortrendsmag.com/articles/110579-nar-nari-releases-2022-remodeling-impact-report)
  - NWFA concrete-subfloor guidance: slab must test at or below 75% RH (ASTM F2170) or 3 lbs/1,000 sq ft/24 hr (ASTM F1869) unless a rated vapor-retarder system is used; solid wood should not go below grade (https://nwfa.org/wp-content/uploads/2020/03/Concrete-Subfloors_Updated.pdf)

**129. Should I restore the terrazzo under my carpet or cover it with new flooring?**
- cluster: `resale-value` | intent: `comparison` | priority: **P2** | FL
- evidence: EXPERT-GAP - https://terrazzosarasota.com/about/
- short_answer_facts:
  - Terrazzo was standard in Sarasota homes from the mid-1950s and is often found under carpet; SW Florida terrazzo removal runs $3.00-$5.50/sq ft, so restoring or floating over it is usually cheaper than demo (https://terrazzosarasota.com/about/)
  - Terrazzo restoration price per sq ft in Sarasota: needs source

## Cannibalisation watch (related questions - plan as hub + spokes, not competing posts)

- Wood in Florida: 'Can you have real hardwood floors in Florida?' / 'Am I stupid to want engineered wood in Florida?' / 'Solid vs engineered on a slab' / 'Can you install hardwood directly on a concrete slab?' - one pillar + three narrow posts with distinct titles.
- Slab moisture: barrier under LVP / barrier under laminate / how to test / acceptable level / drying after flood - one 'slab moisture' hub linking to each.
- Condo: IIC rating / best upper-floor flooring / LVP in 2nd-floor condo / carpet-to-tile / underlayment / HOA approval / floating floors on the keys - one 'Sarasota condo flooring' hub.
- Quotes: 'Why are flooring quotes in Sarasota so different' also answers 'how do I compare quotes' - do not write both.

## AI-assistant prompts to win (25)

Full conversational prompts, written the way people actually talk to ChatGPT / Perplexity / Gemini / Google AI Mode. Each maps to one or more questions above; the page that answers it should open with a 50-70 word direct answer containing the sourced numbers.

1. "Who is the best flooring installer in Sarasota, FL?"
2. "How much does it cost to install vinyl plank flooring in Sarasota?"
3. "I have a 3rd-floor condo on Longboat Key - what flooring will my HOA approve and what underlayment do I need?"
4. "What's the best flooring for a Florida home on a concrete slab with two big dogs?"
5. "I'm a snowbird and leave my Sarasota house empty May through October - which floors won't buckle or mold?"
6. "My house on Siesta Key flooded during the hurricane. What flooring should I put back so I don't have to replace it again?"
7. "Compare LVP, porcelain tile and engineered hardwood for a 1,800 sq ft house in Sarasota - cost, durability, resale."
8. "Can I put real hardwood in a Florida house, or is that a mistake?"
9. "Find me a flooring company near Lakewood Ranch that does tile removal and LVP installation and give me a price range."
10. "My LVP is peaking near the sliding glass doors - what's causing it and who fixes that in Sarasota?"
11. "Do I need a permit or HOA approval to replace carpet with tile in my Sarasota condo?"
12. "What questions should I ask a flooring contractor in Florida before I sign?"
13. "Is $9 per square foot a fair price for LVP installed in Sarasota including tile demo?"
14. "What is IIC 50 and how do I prove my new floor meets it for my condo board?"
15. "Best flooring for an Airbnb near Siesta Key beach that gets sand and wet feet all day?"
16. "My tile floor sounds hollow and a few tiles popped up - is that a Florida thing and how do I fix it?"
17. "How do I test my concrete slab for moisture before installing wood floors in Florida?"
18. "Should I refinish my oak floors or replace them with vinyl plank before selling my Sarasota house?"
19. "Which is better in Florida humidity: waterproof laminate or SPC vinyl plank?"
20. "How long will it take to rip out 1,500 sq ft of tile and install LVP, and can I stay in the house?"
21. "Who installs hardwood stair treads in Sarasota or Bradenton and what does it cost per step?"
22. "What flooring is safest for my 80-year-old parents' Venice, FL home - not slippery, easy with a walker?"
23. "Are flooring installers licensed in Florida? How do I check a Sarasota contractor is legit and insured?"
24. "What's the best time of year to redo floors in a Sarasota condo, and how far ahead should I book?"
25. "I found terrazzo under my carpet in a 1960s Sarasota house - restore it or cover it with LVP?"

### What assistants cite for local-service queries (studies)

- **Yext, Oct 29 2025** - 6.8M citations across 1.6M responses. Gemini: 52.15% of citations from brand-owned websites (rewards structured local landing pages/schema). ChatGPT: 48.73% from third-party listings (Yelp, TripAdvisor, MapQuest), directories rise to 46.3% on subjective 'best...' queries. Perplexity: leans on niche/industry directories and reviews (24% niche sources on unbranded queries). https://www.yext.com/blog/ai-visibility-in-2025-how-gemini-chatgpt-perplexity-cite-brands
- **Foundation Marketing + AirOps, Q4 2025 (published May 28 2026)** - local-discovery citations: Yelp 512,680; BBB 149,710; Angi 145,633; Thumbtack 56,004; HomeAdvisor 33,582; Nextdoor 10,308. Google AI Mode + Perplexity produced ~95% of local citation volume; 'near me' queries drove ~290,000 Yelp citations. https://ppc.land/yelp-gets-3-4x-more-ai-citations-than-any-rival-in-new-local-search-data/
- **SOCi 2026 Local Visibility Index (Mar 25 2026)** - ChatGPT recommends only 1.2% of business locations, Perplexity 7.4%, Gemini 11% (vs 35.9% visibility in the Google local 3-pack); recommended locations average 4.3 stars; profile data accuracy 68% on ChatGPT/Perplexity vs 100% on Gemini (Google Maps-grounded). Sources cross-checked: Google Maps, Yelp, Facebook, brand site, Apple Maps, Bing. https://www.soci.ai/blog/how-to-rank-in-chatgpt-perplexity-and-google-ai-overview/
- **BrightLocal Local Consumer Review Survey 2026** - 45% of consumers used AI tools to find local businesses (6% the year before); ChatGPT 31%, Google AI Mode 23%; 88% of AI users double-check the recommendation. https://www.brightlocal.com/research/local-consumer-review-survey/

**Implications for sarasotaflooringcompany.com:** (1) own-site answer pages with specific sourced numbers and LocalBusiness/FAQ schema feed Gemini/AI Mode; (2) a complete, consistent Google Business Profile + Yelp + BBB + Angi/Thumbtack presence feeds ChatGPT/Perplexity; (3) review volume and a 4.3+ average are effectively the entry ticket; (4) NAP consistency matters because assistants cross-reference Maps, Yelp, Facebook, Apple Maps and Bing.

## Sourcing gaps / to verify before publishing

1. **Reddit** (r/HomeImprovement, r/Flooring, r/sarasota, r/florida, r/tampa) could not be searched or fetched. Pull 15-20 thread titles manually to validate phrasing, especially for condo/HOA, snowbird and post-hurricane questions.
2. **Google PAA / autocomplete** were inferred from SERP titles and publisher FAQ blocks, not scraped. Validate the P1 list in a PAA tool (AlsoAsked / Search Console) before finalising the editorial calendar.
3. **HomeGuide and Angi** pages returned 403; figures are from search snippets. The Angi 'per step' stair snippet and the HomeGuide porcelain labor range ($12-$30/sq ft) look unusual - open the pages and confirm. The Angi refinishing average ($1,891) attribution also needs a page check.
4. **FEMA Technical Bulletin 2 (Jan 2025)**: PDF text could not be parsed, so the per-material flood classes for tile, vinyl, wood and laminate are marked needs source. Read Table 2 manually.
5. **Longboat Key / Siesta Key condo documents**: only Siesta Dunes' rule text was retrieved verbatim (IIC 50, no floating floors above first floor). Longboat Arms' PDF was image-only; the Town of Longboat Key building FAQ URL returned 404 on fetch. Collect 5-10 real association documents.
6. **Seasonal construction blackout dates** in Sarasota/LBK condos: no citable source found.
7. **Florida Building Code sound section number** differs by edition (1206 vs 1207); confirm against the current 8th Edition (2023) before quoting a section number. Sarasota-area municipal permit practice for condo hard-surface changes was not found.
8. **NAR**: the 147% / 118% flooring ROI figures are from the 2022 Remodeling Impact Report; the 2025 edition has no flooring line. Always date the stat.
9. **HomeAdvisor flooring guide** shows a 2022 'last updated' stamp despite a 2026 title - treat its numbers as dated.
10. No source found for: big-box vs local installer price/warranty comparison, dustless-removal price premium, LVP/tile service-life years, slab drying time after flood, Florida buyer-preference survey data, terrazzo restoration $/sq ft, underlayment Delta-IIC values, sand abrasion hardness.
11. Wood EMC at 75-80% RH (about 14-16%) is from the FPL Wood Handbook table as recalled, not re-fetched - verify.
12. Licensing: HB 735/HB 1383 preemption summary comes from a flooring company blog plus DBPR's general page; confirm against the statute text (believed to be s. 163.211, F.S. - not fetched) before publishing.
