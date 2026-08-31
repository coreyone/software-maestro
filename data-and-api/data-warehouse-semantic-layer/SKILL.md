---
name: data-warehouse-semantic-layer
description: "Trigger: dbt, dimensional modeling, star schema, snowflake schema, data mart, semantic layer, metric layer, MetricFlow, Cube.js, data contracts, fct_ tables, dim_ tables, stg_ models, int_ models, surrogate keys, incremental strategy, dbt test, schema validation. Scope: Designing and maintaining production analytics engineering architecture: Kimball dimensional modeling (staging stg_, intermediate int_, dimensional dim_, fact fct_ layers), dbt models with incremental materialization (merge, delete+insert), strict data contracts (YAML schema enforcement, column types, nullability, uniqueness), and semantic metric definitions (entities, measures, dimensions, time grains). Boundary: Excludes client-side event tracking tag schemas (use analytics-event-tracking) or application transactional database indexing/caching (use data-persistence-caching)."
---

# Rule: Analytics Engineering, Dimensional Modeling, & Semantic Layers

## When to use

Use this skill when designing, building, or refactoring data warehouse models, dbt pipelines, or semantic metric layers:
- Structuring raw ingested tables into clean, tested Kimball dimensional marts (`fct_` and `dim_` tables).
- Defining strict Data Contracts on public data models to prevent breaking downstream BI dashboards or ML feature stores.
- Implementing dbt Semantic Layer / MetricFlow / Cube.js definitions (entities, measures, cumulative metrics, time grains).
- Optimizing high-volume data models with incremental materialization strategies (`merge`, `delete+insert`, partitioning).

## When not to use

Do not use this skill for:
- Client-side event tracking telemetry schemas (use `analytics-event-tracking`).
- Application transactional PostgreSQL/MySQL schema design and query indexing (use `data-persistence-caching`).
- Server telemetry and infrastructure log aggregation (use `observability-telemetry`).

## Trigger cues

- Request mentions: `dbt`, `dimensional modeling`, `star schema`, `data mart`, `fact table`, `dimension table`, `semantic layer`, `metric layer`, `MetricFlow`, `Cube.js`, `data contracts`, `fct_`, `dim_`, `stg_`, `int_`, `surrogate key`, `dbt test`.
- Requests to author dbt SQL models, define YAML data contracts, or structure metric aggregation layers.

## Routing boundary

- Route frontend/mobile event tracking specifications to `analytics-event-tracking`.
- Route relational application database models and Redis caching to `data-persistence-caching`.
- Route diagnostic KPI root-cause investigations to `product-data-metric-investigation-triage`.

## Inputs required

1. **Business Domain & Entities**: Core business concepts (e.g., Bookings, Listings, Users, Reviews).
2. **Grain Specification**: Precise declaration of what one row represents in each fact and dimension table.
3. **Data Sources & Upstream Schemas**: Raw source tables, CDC logs, or Kafka event streams.
4. **Downstream Consumption Requirements**: BI dashboard queries, ad-hoc analytics, or ML feature pipelines.
5. **Source of truth**: [references/source.md](references/source.md)

## Instructions

1. Read [references/source.md](references/source.md) first.
2. **Architect the 4-Layer dbt Pipeline**:
   - **Staging (`stg_`)**: 1-to-1 with raw sources, rename fields to standard conventions, cast data types, zero business logic joins.
   - **Intermediate (`int_`)**: Entity-specific joins, business rule transformations, window functions, and deduplication.
   - **Dimensions (`dim_`)**: Conformed dimensional entities with surrogate primary keys (`dim_<entity>.sql`).
   - **Facts (`fct_`)**: Clean event/transaction facts at explicit grain with foreign keys to conformed dimensions (`fct_<verb>.sql`).
3. **Define Strict Data Contracts**:
   - In YAML model configs, enforce `contract: {enforced: true}` with explicit column types, `not_null`, and `unique` constraints.
   - Specify breaking change protection for downstream consumers.
4. **Implement Semantic Layer / MetricFlow Definitions**:
   - Define **Entities** (primary/foreign keys: `user_id`, `listing_id`).
   - Define **Measures** with explicit aggregations (`sum`, `count_distinct`, `average`) and additive filters.
   - Define **Dimensions** (categorical attributes and time dimensions with standard time grains: day, week, month).
   - Define **Derived / Ratio Metrics** (e.g., Conversion Rate = Bookings / Searches).
5. **Agent Database & Warehouse Tooling**:
   - Connect downstream AI agents to analytical marts and semantic layers using [MCP Toolbox for Databases (`googleapis/mcp-toolbox`)](https://github.com/googleapis/mcp-toolbox) for schema-aware, parameterized SQL querying with OpenTelemetry tracing.
6. **Optimize Materialization & Performance**:
   - Use `materialized='incremental'` with `unique_key` and appropriate incremental strategy (`merge` for updates, `insert_overwrite` for partition replacements).
   - Generate surrogate keys using `dbt_utils.generate_surrogate_key`.
7. **Implement Comprehensive Test Suites**:
   - Enforce generic tests: `unique`, `not_null`, `relationships` (referential integrity), `accepted_values`.
   - Add singular tests for domain invariants (e.g., `checkout_date >= checkin_date`).

## Completion gate

Before reporting completion, verify against `evals/cases.json`:
- Clean 4-layer dbt naming conventions (`stg_`, `int_`, `dim_`, `fct_`).
- Strict YAML data contract with column types and nullability constraints.
- Explicit grain definition and surrogate key generation.
- Semantic Layer / MetricFlow definitions (measures, dimensions, metrics).

## Output format

- **Architectural Overview**: Grain declaration and Entity-Relationship / DAG flow.
- **dbt SQL Model Code**: Clean, modular SQL with Jinja macros and surrogate keys.
- **YAML Schema & Data Contract**: Enforced schema specification with testing invariants.
- **Semantic Layer Configuration**: Semantic model YAML with entities, measures, and metrics.
- **Materialization & Indexing Strategy**: Partitioning, clustering, and incremental update logic.
