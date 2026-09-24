# Research policy

## Standard of evidence

A linguistic feature may enter generated prose only if it has:

1. a named source,
2. a documented linguistic form,
3. a documented geographic distribution,
4. enough semantic detail to apply it without changing meaning.

Preferred evidence, in order:

1. peer-reviewed dialectology / sociolinguistics research;
2. academic books from established university/linguistics presses;
3. academic dissertations and university research projects;
4. the Harvard Dialect Survey itself for variables it directly elicited.

Popular articles, social posts, TV/film dialogue, Reddit, dictionaries without regional evidence, and model intuition are not evidence for adding a feature.

## Harvard Dialect Survey status

Vaux and Golder's Harvard Dialect Survey is an academic research project, not a conventional peer-reviewed journal paper. Later academic work describes it as an online 122-item survey covering phonological, grammatical, and lexical variation, completed by more than 47,000 informants in 2002–03. Its results were not formally published as a standalone article.

Therefore:

- treat HDS answer distributions as direct survey evidence;
- do not overstate sampling precision;
- remember the sample was self-selected;
- do not equate a state majority with a categorical rule;
- do not infer social traits the survey did not measure.

## Evidence classes

Each feature should be labeled:

- `direct-hds`: directly measured by an HDS question
- `peer-reviewed`: documented in a peer-reviewed study
- `academic-book`: documented in an academic monograph/atlas
- `academic-project`: documented in a university research project
- `dissertation`: documented in a graduate dissertation

A feature can have more than one evidence class.

## Engineering thresholds are not linguistic facts

If scripts use thresholds such as minimum regional share, lift, or margin, those thresholds are implementation heuristics. They are not claims from the underlying research.

Always distinguish:

- **observed data**: percentages, distributions, mapped regions
- **implementation choice**: when the agent decides a tendency is strong enough to use

## No stereotype completion

Never infer unmeasured traits from a region.

Examples of forbidden inference:

- Midwest → polite
- Minnesota → says `uff da`
- Chicago → drops every `th`
- Kansas → rural
- Great Lakes → blue-collar
- Midwest → politically moderate
- Upper Midwest → Scandinavian ancestry

Those may be cultural stereotypes, demographic associations, or context-dependent observations. They are outside this skill unless separately sourced for the exact linguistic feature being used.
