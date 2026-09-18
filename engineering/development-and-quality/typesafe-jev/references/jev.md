# TypeSafe Jev reference

Checked 2026-09-18. Re-read the official pages before implementation because aliases, limits, pricing, SDKs, and legal terms can change.

## Official model facts

- [Introduction](https://docs.typesafe.ai/introduction): Jev maps text state plus typed questions to structured answers and probabilities; it does not generate text.
- [System One](https://docs.typesafe.ai/concepts/system-one): text-only input; calibrated probabilities are group-level behavior, not an individual correctness guarantee.
- [State](https://docs.typesafe.ai/concepts/state): state may be a string, JSON object, or array of text values. English is strongest; other languages and CJK require validation.
- [Primitives](https://docs.typesafe.ai/primitives): `Choice`, `Score`, and `Noul`; questions are independent and can be requested together.
- [Advanced primitive structure](https://docs.typesafe.ai/primitives/advanced): `instructions` and `criteria` accept structured JSON; structured rubrics clarify boundaries and support taxonomy traversal.
- [Choice](https://docs.typesafe.ai/primitives/choice): up to 255 options; use a second staged question for larger candidate sets.
- [Confidence](https://docs.typesafe.ai/confidence): confidence is derived from the distribution for `Choice` and `Score`; `Noul` exposes probability, not confidence.
- [Patterns](https://docs.typesafe.ai/patterns): speculative fan-out, confidence-gated routing, composite scoring, and intent routing.
- [How to build](https://docs.typesafe.ai/concepts/how-to-build-with-system-one): code owns workflow, rules, side effects, and next actions; Jev supplies comparable typed judgments.

## Current API and operations

- [API](https://docs.typesafe.ai/api): `POST https://api.typesafe.ai/v1/systemone` with bearer authentication, `state`, `model`, and `questions`.
- [Models](https://docs.typesafe.ai/models): current documented alias is `jev-latest` → `jev-1.13.0`; the page documents a 64k request limit, 32k state plus longest-question limit, text-only input, and current pricing/rate limits. Pin versions when calibrated.
- [Jev 1.13 limitations](https://docs.typesafe.ai/model-jaggedness/jev-1.13): weak areas include indirection, literal reading, math/counting, dates, irrelevant context, adversarial content, contradictory criteria, structural invariants, and generation.
- [JavaScript SDK](https://github.com/typesafe-ai/typesafe-sdk-js): official package is `@typesafe-ai/sdk`; Node 20+.
- [Python SDK](https://github.com/typesafe-ai/typesafe-sdk-python): official Python client.

## Advanced primitive structure

Every question field is an `EntryType`. These fields accept a string, object, array, or `null`:

- `instructions` for `Choice`, `Score`, and `Noul`
- `Choice` option descriptions
- `Score` level descriptions
- `Noul` `criteria.true` and `criteria.false`

Use structure when it makes the judgment clearer or carries supporting data. Pass a schema, taxonomy, database row, comparison list, or labeled definition as JSON instead of serializing it into a string template. A useful instruction object can separate the question, fields to compare, and focus.

For `Choice`, structured option descriptions can include coverage, exclusions, and examples to sharpen boundaries. For subtle `Noul` decisions, structured true/false criteria can define both sides.

For deep taxonomies, walk the tree in code: ask one `Choice` for the current level, provide its child options plus enough subtree context, then continue with the selected child. If probabilities are close, keep multiple candidate paths or beam-search them. Trim oversized branches to direct children and a representative leaf sample.

## Vendor evals and policy

- [Workflow evals](https://evals.typesafe.ai/): vendor-published comparisons across security incidents, agent trace observability, invoice processing, and customer service. Reference labels use an average of GPT-6 Astra and Claude Fable 5.1; treat results as directional, not independent ground truth.
- [Legal](https://docs.typesafe.ai/legal) and [privacy policy](https://typesafe.ai/legal/privacy-policy): TypeSafe states that customer requests and responses are not used for training; verify retention, DPA, regional hosting, and enterprise zero-data-retention terms for the deployment.
