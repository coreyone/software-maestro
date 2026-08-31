# Growth Product Management, Growth Loops, & Retention

Growth product management focuses on **sustainable, compounding acquisition and retention**. While traditional marketing treats growth as a linear funnel (Acquire $\to$ Activate $\to$ Retain), modern growth architecture operates through **self-reinforcing loops**.

---

## 1. The Expert Methodology Roster

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                       GROWTH EXPERT METHODOLOGY ROSTER                      │
├──────────────────────────────────────┬──────────────────────────────────────┤
│ 1. BRIAN BALFOUR: Growth Loops & Fits│ 2. FAREED MOSAVAT: Retention-First   │
│ The 4 Growth Fits & closed-loop      │ Natural frequency of use &           │
│ flywheels (Loops > Funnels).         │ quantitative activation milestones.  │
├──────────────────────────────────────┼──────────────────────────────────────┤
│ 3. ELENA VERNA: Product-Led Growth   │ 4. NIR EYAL: The Hooked Model        │
│ Self-serve freemium/trial loops,     │ Trigger -> Action -> Variable Reward │
│ product-led sales (PLS) triggers.    │ -> Investment (stored value).        │
├──────────────────────────────────────┼──────────────────────────────────────┤
│ 5. JOSH ELMAN: The Core Action       │ 6. LENNY RACHITSKY: 7 Growth Channels│
│ The single value-creating metric:    │ The Racecar Growth Model (Engine,    │
│ "Users performing the core action."  │ Turbochargers, Lubricants, Fuel).    │
└──────────────────────────────────────┴──────────────────────────────────────┘
```

---

## 2. Brian Balfour: Growth Loops vs Linear Funnels

Linear funnels require constantly pouring more paid marketing dollars into the top. Growth loops reinvest user activity to acquire the next cohort:

```mermaid
flowchart TD
    subgraph ViralUserLoop ["The Viral Collaboration Loop (e.g. Figma / Slack / Notion)"]
        U1["1. New User Signs Up"] --> U2["2. Creates & Shares Collaborative Canvas"]
        U2 --> U3["3. Collaborator Receives Invite & Views Project"]
        U3 --> U4["4. Collaborator Signs Up to Edit"]
        U4 --> U1
    end
    
    subgraph ContentSEOLoop ["The User-Generated Content SEO Loop (e.g. Pinterest / Quora)"]
        C1["1. User Publishes Public Content"] --> C2["2. Search Engines Index New Page"]
        C2 --> C3["3. New Visitor Finds Page via Organic Search"]
        C3 --> C4["4. Visitor Signs Up & Creates Content"]
        C4 --> C1
    end
```

### The 4 Growth Fits Framework:
1. **Market-Product Fit**: Product solves a burning problem for a large, growing market.
2. **Product-Channel Fit**: Products are built for specific channels (e.g. SEO, Virality, Paid), not vice-versa.
3. **Channel-Model Fit**: Channel cost matches monetization model (e.g. Low ARPU requires virality/SEO; High ARPU supports outbound sales).
4. **Model-Market Fit**: Number of customers $	imes$ ARPU equals a $\$100M+$ business.

---

## 3. Fareed Mosavat & Josh Elman: Natural Frequency & Activation

Growth starts with retention, and retention is governed by the product's **Natural Frequency**:

| Natural Frequency | Example Products | Core Action | Healthy Activation Milestone |
| :--- | :--- | :--- | :--- |
| **Daily** | Slack, Instagram, Twitter | Send message / View feed | Send 10 messages in Day 1 |
| **Weekly** | Notion, Asana, Linear, Jira | Update task / Edit document | Complete 3 tasks in first 7 days |
| **Monthly** | Gusto, QuickBooks, Carta | Run payroll / Reconcile ledger | Execute 1st payroll within 14 days |
| **Seasonal / Annual** | Airbnb, TurboTax, Booking.com | Search & Book trip / File taxes | Save 1 wishlist & search within 3 days |

---

## 4. Nir Eyal: The Hooked Model

```mermaid
flowchart LR
    Trigger["<b>1. Trigger</b><br/>External (Push) -> Internal (Anxiety/FOMO)"] --> Action["<b>2. Action</b><br/>Simple behavior in anticipation of reward"]
    Action --> Reward["<b>3. Variable Reward</b><br/>Tribe (Social), Hunt (Data), Self (Mastery)"]
    Reward --> Investment["<b>4. Investment</b><br/>Data, content, reputation stored for next loop"]
    Investment --> Trigger
```
