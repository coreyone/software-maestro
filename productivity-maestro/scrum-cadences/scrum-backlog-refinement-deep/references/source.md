# Scrum Backlog Refinement: Deep Story Slicing & INVEST Mechanics

## 1. First Principles & Cybernetic Purpose
- **Large-Batch Neutralization**: Unrefined backlog items harbor hidden complexity. Breaking them into micro-increments surfaces integration risks days or weeks before sprint planning.
- **Cognitive Shared Model**: The Product Owner owns the *Value & Outcome*; the Developers own the *Technical Decomposition & Sizing*. Refinement is the collaborative forge where these perspectives align.
- **Continuous Flow**: Refinement is not a one-off event at sprint end; it is an ongoing 10% capacity investment ensuring the team never stalls waiting for ready work.

## 2. The 3 Cs Framework (Ron Jeffries)
1. **Card**: The physical or digital token representing intent (*"As a [role], I want [feature], so that [benefit]"*).
2. **Conversation**: The collaborative dialogue between PO, designers, and engineers to flesh out edge cases, UX behavior, and data boundaries.
3. **Confirmation**: The executable acceptance tests (BDD/Gherkin `Given / When / Then`) proving the story functions correctly.

## 3. Story Splitting Patterns
| Pattern | Monolithic Story | Sliced Stories |
| :--- | :--- | :--- |
| **Workflow Steps** | Complete checkout flow | 1. Cart summary & item lock<br>2. Address & shipping selection<br>3. Payment tokenization |
| **Business Rules** | Dynamic tax engine across 50 states | 1. Flat domestic tax calculation<br>2. Multi-jurisdiction dynamic lookup |
| **Data Variation** | Ingest all document types | 1. Ingest UTF-8 CSV only<br>2. Ingest PDF & binary parsing |
| **Happy vs. Unhappy** | OAuth 2.1 authentication | 1. Happy path Google SSO login<br>2. Expired session & network retry flow |
| **Simple vs. Complex** | Full-text search with faceted filtering | 1. Basic substring keyword query<br>2. Faceted category filters |

## 4. Definition of Ready (DoR) Checklist
- [ ] **Clear User Value**: Articulated from the perspective of the end user or consuming system.
- [ ] **Acceptance Criteria (BDD)**: Minimum 2 Gherkin scenarios covering happy path and boundary conditions.
- [ ] **Dependencies Resolved**: External API contracts, DB schema migrations, or third-party SDKs verified.
- [ ] **UI/UX Assets Ready**: Wireframes, design tokens, and copy provided when UI is involved.
- [ ] **Sized by Developers**: Relative estimate assigned ($\le 8$ story points / $\le 2$ days).
- [ ] **No Hidden Spikes**: Unknowns $>1$ day separated into exploratory research spikes.
