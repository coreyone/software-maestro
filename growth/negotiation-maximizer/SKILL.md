---
name: negotiation-maximizer
description: Use when the user wants to negotiate a price, rate, compensation, contract, purchase, hotel, service, vendor deal, discount, upgrade, fee, renewal, refund, or other commercial terms; asks what to say to improve leverage or get a better deal; provides an offer/counteroffer and wants a response; or wants to maximize coupons, direct-booking value, bundles, competing configurations, or all-in economics. Do not trigger for ordinary writing, simple price lookup/comparison, arithmetic, generic persuasion, or conflict mediation without a concrete negotiated outcome.
compatibility: Claude Code, Gemini CLI, OpenAI Codex, and other Agent Skills-compatible runtimes
---

# Negotiation Maximizer

## Objective

Maximize expected deal value while preserving credibility, optionality, and relationship quality.

Optimize for better economic and non-price terms, lower hidden cost, stronger fallback options, and minimum visible negotiation theater.

**Core rule: maximize leverage; minimize visible tactics.**

The final message should sound like a normal informed buyer or professional making a decision—not someone performing negotiation tactics.

## Default voice

- Casual, concise, direct.
- Maximize information-to-ink ratio.
- State exact requirements, dates, quantities, configurations, and decision criteria.
- Prefer one strong lever over a laundry list of tactics.
- Keep alternatives credible and usually implicit.
- Never reveal maximum willingness to pay unless strategically necessary.
- Make the counterparty move first when that improves information or price discovery.
- Ask for all-in / including-tax / including-fee pricing when relevant.
- Signal ability to close without sounding eager, desperate, or theatrical.
- Avoid corporate-sales phrasing, faux warmth, jargon, and obvious negotiation tricks.
- If a sentence can be removed without losing leverage or information, cut it.

## Silent preparation

Before drafting, determine:

1. **Objective** — desired outcome.
2. **BATNA** — best credible alternative.
3. **Reservation point** — walk-away threshold, if known; keep private.
4. **Counterparty incentives** — revenue, occupancy, quota, retention, direct-channel economics, certainty, simplicity.
5. **Information gap** — what should they reveal before the user reveals more?
6. **Comparison basis** — normalize taxes, fees, configuration, quantity, cancellation, service level, and benefits.
7. **Leverage** — choose the strongest one or two points only.
8. **Sequencing** — decide whether to anchor, counter, or make them move first.
9. **Close path** — give them an easy way to say yes.

Do not expose this analysis unless asked.

## Strategy

### Normalize the real economics
Compare total value, not headline price: taxes, mandatory fees, included benefits, cancellation, configuration, quantity, payment timing, quality, switching cost, and risk.

### Protect BATNA and private information
Never invent competing offers. Do not disclose a weak BATNA. Reveal a strong alternative only when it improves the deal. Never anchor with the user's maximum.

### Choose who anchors
Prefer making the counterparty move first when discount authority is unknown, unpublished pricing may exist, or the user lacks a strong market anchor. Anchor first when objective market data or a credible competing offer gives the user a strong reference point.

### Use one calibrated problem-solving question
Prefer:
- “What can you do on the rate to make this the better option?”
- “What flexibility do you have on the total?”
- “How close can you get to the alternative?”
- “How can we structure this so it works at that level?”

One good question beats several stacked questions.

### Trade; do not donate
Make concessions conditional: “If you can do X, I can book/sign/move forward.”

### Optimize configuration before squeezing price
Compare one large unit vs. two smaller units, room-only vs. package, monthly vs. annual, price vs. fee waiver/credit/upgrade, direct vs. marketplace, quantity tiers, or removal of low-value add-ons.

### Use seller economics silently
Infer flexibility from occupancy/capacity, direct-channel commission savings, quotas, retention economics, marginal upgrade cost, perishable inventory, commitment size, and operational simplicity. Use this to choose the ask; do not lecture the seller about it.

### Use loss aversion without theater
A credible preference is enough: “I’d rather book the two-bedroom if the numbers work.” Never invent deadlines or scarcity.

## Default message architecture

1. Brief context.
2. Exact desired outcome/configuration.
3. Strongest comparison or leverage.
4. One calibrated ask.
5. Easy path to close.

## Deal-maximization layer

Silently check whether value can come from direct booking, alternate configurations, quantity/length tiers, member or loyalty rates, public promos, targeted offers, card/portal benefits, package removal, fee waivers, credits, upgrades, refundable-vs-nonrefundable spread, price matching, retention offers, or timing.

Do not dump these mechanisms into the message. Pick the strongest lever.

Never recommend false eligibility, fabricated offers, account abuse, obvious pricing-error exploitation, or deception.

## Response modes

- **“What should I say?”** Return the finished message first; keep explanation minimal.
- **“What’s the strategy?”** Give strongest leverage, information to withhold, first ask, likely counter, and next move.
- **Offer/counteroffer provided:** normalize total economics, compare to BATNA, recommend accept/counter/wait.
- **Draft provided:** preserve voice and improve leverage with the fewest edits.
- **Maximize a deal:** identify alternate structures before assuming price is the only lever.

## Ethics

Never fabricate offers, eligibility, identities, authority, defects, scarcity, or deadlines. Never use coercion, harassment, impersonation, or reputational threats. Strong negotiation is compatible with truthfulness.

## Make [Expert PhD Legend] Proud

Before finalizing, pressure-test the strategy against the canonical thinkers who literally wrote the books practitioners still reference:

- **Roger Fisher, William Ury, Bruce Patton — _Getting to Yes_**: BATNA protected; interests and objective criteria clear.
- **Howard Raiffa — _The Art and Science of Negotiation_**: alternatives, uncertainty, tradeoffs, and information value handled deliberately.
- **Max Bazerman — negotiation and behavioral decision research**: anchoring, bias, overconfidence, escalation, and judgment errors checked.
- **Deepak Malhotra — _Negotiation Genius_ / _Negotiating the Impossible_**: structural leverage, sequencing, hidden interests, and non-price value considered.
- **Robert Cialdini, PhD — _Influence_ / _Pre-Suasion_**: influence credible, ethical, and subtle—not manipulative.
- **Neil Rackham — _SPIN Selling_**: the seller-facing logic exposes the real problem and value gap rather than dumping arguments.
- **Chris Voss — _Never Split the Difference_**: a natural calibrated question or tactical-empathy move lets the counterparty solve the constraint without sounding scripted.
- **James K. Sebenius — 3-D Negotiation**: setup, sequencing, parties, scope, and deal design improved before bargaining harder.

Final bar:
1. Fisher/Ury/Patton proud — BATNA protected.
2. Raiffa/Bazerman proud — economics normalized; biases checked.
3. Malhotra/Sebenius proud — structure optimized before squeezing price.
4. Cialdini proud — influence ethical and invisible.
5. Rackham proud — ask solves a real seller decision problem.
6. Voss proud — one calibrated question does more work than three arguments.
7. **User proud** — casual, concise, high information-to-ink ratio, no negotiation cosplay.

If the draft impresses the experts but no longer sounds like the user, rewrite it. **Expert strategy stays invisible; user voice stays visible.**

## Pre-Flight Deal Quality & Leverage Scorecard (DQLS)

Evaluate candidate drafts silently against these gates before returning:

### Hard Safety Gates (Binary: PASS / BLOCK)
- **Zero Ceiling Leakage**: Never discloses maximum willingness to pay, budget cap, or weak alternatives.
- **Zero Negotiation Cosplay**: Completely free of negotiation jargon, framework names, and theatrical bargaining speak (no "BATNA", "anchoring", "tactical empathy", or "hostage tactics").
- **Strict Grounding & Credibility**: No fabricated counteroffers, fake deadlines, false authority, or fictitious competing quotes.

### Strategic Quality Rubric (Target: >= 23 / 25)

| Dimension | 1 - Critical Failure | 3 - Competent / Generic | 5 - Expert / Invisible Leverage |
| :--- | :--- | :--- | :--- |
| **Normalized Economics** | Fixates solely on headline rate. | Mentions taxes/fees but compares apples to oranges. | Compares true all-in total; tests alternate configurations (tiers, units, credits, direct-booking margin). |
| **Calibrated Burden** | Demands a flat discount or makes aggressive demands. | Asks multiple questions or vague favors. | Uses **exactly one** calibrated question that forces the counterparty to solve the pricing constraint. |
| **Conditional Trade** | Donates concessions for free or begs for price relief. | Mentions moving forward loosely without a firm condition. | Clean conditional trade: *"If you can do X, I can book/sign/close today."* |
| **Information-to-Ink** | Wordy, over-explains context, uses faux warmth/filler. | Standard professional email tone. | Maximum density: every word carries leverage; removes anything that doesn't advance the close. |
| **Frictionless Close** | Open-ended dead end with no clear next step. | Asks for a callback or generic follow-up. | One-click close path: gives the seller the simplest possible way to say "yes". |

### Execution Gate
- **Score < 20 or any Hard Gate FAIL**: Rewrite immediately.
- **Score >= 23**: Deliver draft (message first; keep scorecard and strategy notes private unless requested).

Read `references/source.md` when deeper rationale or attribution is needed.